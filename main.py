"""SmartStudy: Telegram Mini App для изучения английского.
Один процесс: FastAPI (API + страница) и бот aiogram 3 (polling)."""
import asyncio
import contextlib
import hashlib
import hmac
import json
import logging
import os
import sqlite3
import time
from contextlib import asynccontextmanager
from urllib.parse import parse_qsl

import uvicorn
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           LabeledPrice, Message, PreCheckoutQuery, WebAppInfo)
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBAPP_URL = os.environ["WEBAPP_URL"]
PRICE_STARS = int(os.getenv("PRICE_STARS", "100"))
FREE_WORDS = 12
DB_PATH = os.getenv("DB_PATH", "smartstudy.db")
DAY = 86400

# (English, Русский, пример)
WORDS = [
    ("hello", "привет", "Hello, how are you?"),
    ("thank you", "спасибо", "Thank you for your help."),
    ("please", "пожалуйста", "Please sit down."),
    ("water", "вода", "Can I have some water?"),
    ("friend", "друг", "She is my best friend."),
    ("house", "дом", "Their house is very big."),
    ("time", "время", "What time is it?"),
    ("work", "работа", "I go to work by bus."),
    ("eat", "есть, питаться", "We eat dinner at seven."),
    ("big", "большой", "That is a big dog."),
    ("small", "маленький", "I live in a small town."),
    ("today", "сегодня", "Today is a good day."),
    ("remember", "помнить", "I remember this song."),
    ("forget", "забывать", "Don't forget your keys."),
    ("choose", "выбирать", "You can choose any book."),
    ("travel", "путешествовать", "I love to travel by train."),
    ("improve", "улучшать", "I want to improve my English."),
    ("necessary", "необходимый", "Sleep is necessary for health."),
    ("environment", "окружающая среда", "We must protect the environment."),
    ("develop", "развивать", "She wants to develop her skills."),
    ("achieve", "достигать", "He worked hard to achieve his goal."),
    ("experience", "опыт", "I have no experience with this."),
    ("although", "хотя", "Although it rained, we went out."),
    ("suggest", "предлагать", "I suggest we leave early."),
    ("opportunity", "возможность", "This is a great opportunity."),
    ("reliable", "надёжный", "He is a reliable partner."),
    ("manage", "справляться, управлять", "Can you manage on your own?"),
    ("effort", "усилие", "It takes a lot of effort."),
    ("however", "однако", "It is late; however, I am not tired."),
    ("increase", "увеличиваться", "Prices increase every year."),
]


@contextlib.contextmanager
def db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def init_db():
    with db() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY, name TEXT, premium_until REAL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS progress(
            user_id INTEGER, word_id INTEGER, ease REAL, interval REAL,
            reps INTEGER, due REAL, PRIMARY KEY(user_id, word_id));
        CREATE TABLE IF NOT EXISTS payments(
            charge_id TEXT PRIMARY KEY, user_id INTEGER, stars INTEGER, ts REAL);
        """)


def is_premium(uid: int) -> bool:
    with db() as c:
        r = c.execute("SELECT premium_until FROM users WHERE id=?", (uid,)).fetchone()
    return bool(r and r["premium_until"] > time.time())


def sm2(ease, interval, reps, q):
    """Алгоритм SM-2. q: 1 не помню, 3 трудно, 4 хорошо, 5 легко."""
    if q < 3:
        return ease, 0, 0, time.time() + 600
    interval = 1 if reps == 0 else 6 if reps == 1 else round(interval * ease)
    ease = max(1.3, ease + 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    return ease, interval, reps + 1, time.time() + interval * DAY


def auth(init_data: str) -> dict:
    try:
        data = dict(parse_qsl(init_data, strict_parsing=True))
        got = data.pop("hash")
        check = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
        secret = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
        calc = hmac.new(secret, check.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(calc, got) or time.time() - int(data["auth_date"]) > DAY:
            raise ValueError
        user = json.loads(data["user"])
    except Exception:
        raise HTTPException(401, "Откройте приложение из Telegram")
    with db() as c:
        c.execute("INSERT OR IGNORE INTO users(id, name) VALUES(?,?)",
                  (user["id"], user.get("first_name", "")))
    return user


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="📚 Учить слова", web_app=WebAppInfo(url=WEBAPP_URL))]])
    await m.answer("Привет! Я SmartStudy. Учим английский карточками: "
                   "слова, которые вы забываете, я показываю чаще.", reply_markup=kb)


@dp.message(Command("paysupport"))
async def paysupport(m: Message):
    await m.answer("Проблемы с оплатой? Напишите сюда с номером платежа, поможем или вернём звёзды.")


@dp.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await q.answer(ok=q.invoice_payload == f"premium:{q.from_user.id}")


@dp.message(F.successful_payment)
async def paid(m: Message):
    p = m.successful_payment
    uid = m.from_user.id
    with db() as c:
        c.execute("INSERT OR IGNORE INTO users(id, name) VALUES(?,?)", (uid, m.from_user.first_name))
        c.execute("INSERT OR IGNORE INTO payments VALUES(?,?,?,?)",
                  (p.telegram_payment_charge_id, uid, p.total_amount, time.time()))
        c.execute("UPDATE users SET premium_until = MAX(premium_until, ?) + ? WHERE id=?",
                  (time.time(), 30 * DAY, uid))
    await m.answer("✅ Premium активен на 30 дней. Откройте приложение: слов стало больше!")


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    task = asyncio.create_task(dp.start_polling(bot, handle_signals=False))
    yield
    task.cancel()
    await bot.session.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "index.html"))


@app.get("/api/state")
def state(x_init_data: str = Header("")):
    uid = auth(x_init_data)["id"]
    prem = is_premium(uid)
    limit = len(WORDS) if prem else FREE_WORDS
    now = time.time()
    with db() as c:
        rows = {r["word_id"]: r for r in
                c.execute("SELECT * FROM progress WHERE user_id=?", (uid,))}
    due = sorted((i for i in range(limit) if i in rows and rows[i]["due"] <= now),
                 key=lambda i: rows[i]["due"])
    new = [i for i in range(limit) if i not in rows]
    ids = due[:15] + new[:max(5, 10 - len(due))]
    cards = [{"id": i, "en": WORDS[i][0], "ru": WORDS[i][1], "ex": WORDS[i][2]} for i in ids]
    learned = sum(1 for r in rows.values() if r["reps"] >= 3)
    return {"premium": prem, "cards": cards, "learned": learned,
            "total": limit, "locked": len(WORDS) - limit, "price": PRICE_STARS}


class Review(BaseModel):
    word_id: int
    quality: int


@app.post("/api/review")
def review(body: Review, x_init_data: str = Header("")):
    uid = auth(x_init_data)["id"]
    limit = len(WORDS) if is_premium(uid) else FREE_WORDS
    if not 0 <= body.word_id < limit or body.quality not in (1, 3, 4, 5):
        raise HTTPException(400, "Неверный запрос")
    with db() as c:
        r = c.execute("SELECT * FROM progress WHERE user_id=? AND word_id=?",
                      (uid, body.word_id)).fetchone()
        ease, interval, reps = (r["ease"], r["interval"], r["reps"]) if r else (2.5, 0, 0)
        ease, interval, reps, due = sm2(ease, interval, reps, body.quality)
        c.execute("INSERT OR REPLACE INTO progress VALUES(?,?,?,?,?,?)",
                  (uid, body.word_id, ease, interval, reps, due))
    return {"ok": True}


@app.post("/api/invoice")
async def invoice(x_init_data: str = Header("")):
    uid = auth(x_init_data)["id"]
    link = await bot.create_invoice_link(
        title="SmartStudy Premium",
        description="Все слова и уроки на 30 дней",
        payload=f"premium:{uid}",
        currency="XTR",
        prices=[LabeledPrice(label="Premium, 30 дней", amount=PRICE_STARS)],
    )
    return {"link": link}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
