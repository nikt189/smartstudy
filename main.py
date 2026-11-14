<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
<title>SmartStudy</title>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ar:200,255,0;--bg:#09090D;--surface:#13131A;--surface-elevated:#1B1B24;--border:rgba(255,255,255,.08);--border-highlight:rgba(255,255,255,.15);--accent:#C8FF00;--accent-text:#09090D;--accent-dim:rgba(var(--ar),.14);--accent-glow:rgba(var(--ar),.35);--text:#F8FAFC;--text-muted:#8A8F9E;--danger:#FF4D6D;--warning:#FFB703;--success:#00E676;--safe-bottom:env(safe-area-inset-bottom,16px);--fox:#FF8A3D;--fox-light:#FFC9A3;--fox-dark:#C75C1B}
body.light-theme{--bg:#F4F5F8;--surface:#FFFFFF;--surface-elevated:#EAECEF;--border:rgba(15,23,42,.08);--border-highlight:rgba(255,255,255,.9);--accent:#65A30D;--accent-text:#FFFFFF;--accent-dim:rgba(101,163,13,.12);--accent-glow:rgba(101,163,13,.25);--text:#0F172A;--text-muted:#64748B}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent;user-select:none}
body{font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,sans-serif;background-color:var(--bg);background-image:radial-gradient(circle at 50% 0%,rgba(var(--ar),.07) 0%,transparent 45%),radial-gradient(rgba(255,255,255,.03) 1px,transparent 0);background-size:100% 100%,24px 24px;color:var(--text);min-height:100vh;overflow-x:hidden;padding-bottom:calc(84px + var(--safe-bottom));transition:background-color .3s ease,color .3s ease}
body.light-theme{background-image:radial-gradient(circle at 50% 0%,rgba(101,163,13,.08) 0%,transparent 45%),radial-gradient(rgba(15,23,42,.04) 1px,transparent 0)}
.ic{display:block;flex:none}
#confettiCanvas{position:fixed;inset:0;pointer-events:none;z-index:200}
.header{display:flex;align-items:center;justify-content:space-between;padding:14px 18px 10px;position:sticky;top:0;z-index:40;background:rgba(9,9,13,.82);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
body.light-theme .header{background:rgba(244,245,248,.85)}
.logo{font-size:20px;font-weight:800;letter-spacing:-.5px;display:flex;align-items:center;gap:2px}.logo span{color:var(--accent)}
.header-actions{display:flex;align-items:center;gap:10px}
.streak-pill{display:flex;align-items:center;gap:5px;font-size:14px;font-weight:800;color:#FF9F1C;padding:6px 8px}
.pro-badge{display:flex;align-items:center;gap:6px;background:linear-gradient(135deg,rgba(var(--ar),.2),rgba(var(--ar),.05));border:1px solid rgba(var(--ar),.45);color:var(--accent);font-family:inherit;font-size:12px;font-weight:800;padding:7px 14px;border-radius:999px;box-shadow:0 0 20px rgba(var(--ar),.15);cursor:pointer;transition:transform .15s cubic-bezier(.34,1.56,.64,1)}
.pro-badge.is-pro{background:var(--accent);color:var(--accent-text)}.pro-badge:active{transform:scale(.93)}
.lang-scroll{display:flex;gap:10px;overflow-x:auto;padding:6px 18px 14px;scrollbar-width:none}.lang-scroll::-webkit-scrollbar{display:none}
.lang-chip{display:flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--border);padding:8px 14px;border-radius:999px;font-family:inherit;font-size:13px;font-weight:600;color:var(--text-muted);white-space:nowrap;cursor:pointer;transition:all .2s ease;box-shadow:inset 0 1px 0 var(--border-highlight)}
.lang-chip.active{background:var(--surface-elevated);border-color:var(--accent);color:var(--text);box-shadow:0 0 16px rgba(var(--ar),.12),inset 0 1px 0 var(--border-highlight)}
.lang-code{font-size:10px;font-weight:800;background:rgba(255,255,255,.08);color:var(--text);padding:2px 6px;border-radius:6px;letter-spacing:.5px}
body.light-theme .lang-code{background:rgba(15,23,42,.07)}.lang-chip.active .lang-code{background:var(--accent);color:var(--accent-text)}
.view{display:none;padding:0 18px;animation:fadeIn .25s ease}.view.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.foxy-card{background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:12px 14px;display:flex;align-items:center;gap:14px;margin-bottom:14px;box-shadow:inset 0 1px 0 var(--border-highlight),0 10px 25px rgba(0,0,0,.25);cursor:pointer}
body.light-theme .foxy-card{box-shadow:inset 0 1px 0 var(--border-highlight),0 8px 20px rgba(15,23,42,.06)}
.foxy-avatar{width:66px;height:66px;flex-shrink:0;animation:floatFoxy 3.5s ease-in-out infinite}.foxy-avatar svg,.char-item .art svg{width:100%;height:100%;display:block;overflow:visible}
@keyframes floatFoxy{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
.foxy-eye,.eye{transform-origin:center;transform-box:fill-box;animation:blink 4.5s infinite}
@keyframes blink{0%,94%,100%{transform:scaleY(1)}97%{transform:scaleY(.1)}}
.foxy-info{flex:1;min-width:0}
.foxy-bubble{background:rgba(255,255,255,.05);border:1px solid var(--border);border-radius:12px;padding:7px 11px;font-size:13px;font-weight:600;line-height:1.35;color:var(--text);margin-bottom:8px}
body.light-theme .foxy-bubble{background:#F1F5F9}
.xp-row{display:flex;align-items:center;justify-content:space-between;font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:5px}.xp-row span:first-child{color:var(--text)}
.xp-bar{height:5px;background:rgba(255,255,255,.08);border-radius:999px;overflow:hidden}body.light-theme .xp-bar{background:rgba(15,23,42,.08)}
.xp-fill{height:100%;background:var(--accent);border-radius:999px;box-shadow:0 0 10px var(--accent-glow);transition:width .4s cubic-bezier(.34,1.56,.64,1)}
.session-meta{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;padding:0 2px}
.session-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted)}
.session-dots{display:flex;gap:4px}
.s-dot{width:14px;height:4px;border-radius:4px;background:rgba(255,255,255,.1);transition:all .3s ease}body.light-theme .s-dot{background:rgba(15,23,42,.12)}
.s-dot.done{background:var(--accent);box-shadow:0 0 8px var(--accent-glow)}.s-dot.current{background:rgba(var(--ar),.55);width:22px}
.deck-wrapper{position:relative;height:260px;margin-bottom:24px;perspective:1200px}
.deck-ghost{position:absolute;inset:0;background:var(--surface);border:1px solid var(--border);border-radius:26px;pointer-events:none}
.deck-ghost-1{transform:translateY(10px) scale(.95);opacity:.65;z-index:1}.deck-ghost-2{transform:translateY(19px) scale(.9);opacity:.35;z-index:0}
.flashcard{position:relative;width:100%;height:100%;z-index:10;transform-style:preserve-3d;transform:translate3d(var(--tx,0px),var(--ty,0px),0) rotate(var(--rot,0deg)) rotateY(var(--flip,0deg));transition:transform .55s cubic-bezier(.23,1,.32,1);cursor:pointer;touch-action:pan-y;will-change:transform}
.flashcard.flipped{--flip:180deg}.flashcard.swiping{transition:none}.flashcard.flying{transition:transform .32s ease,opacity .32s ease}
.card-face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;background:radial-gradient(circle at 50% 0%,rgba(var(--ar),.1) 0%,var(--surface) 65%);border:1px solid rgba(var(--ar),.35);border-radius:26px;padding:18px 20px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:inset 0 1px 0 var(--border-highlight),0 18px 38px rgba(0,0,0,.45)}
body.light-theme .card-face{box-shadow:0 14px 30px rgba(15,23,42,.08)}
.card-back{transform:rotateY(180deg);background:radial-gradient(circle at 50% 0%,rgba(56,189,248,.12) 0%,var(--surface) 65%);border-color:rgba(56,189,248,.38)}
.card-top{display:flex;align-items:center;justify-content:space-between}.tag-group{display:flex;gap:6px}
.card-tag{font-size:11px;font-weight:700;padding:4px 10px;border-radius:8px;background:rgba(255,255,255,.06);color:var(--text-muted);letter-spacing:.3px}body.light-theme .card-tag{background:rgba(15,23,42,.06)}
.card-tag.level{color:var(--accent);background:var(--accent-dim)}
.icon-btn{width:36px;height:36px;border-radius:12px;background:rgba(255,255,255,.06);border:1px solid var(--border);color:var(--text);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:transform .15s ease;flex-shrink:0}
body.light-theme .icon-btn{background:rgba(15,23,42,.05)}.icon-btn:active{transform:scale(.9)}
.card-center{text-align:center;margin:auto 0}
.word-main{font-size:36px;font-weight:800;letter-spacing:-.8px;color:var(--accent);text-shadow:0 0 28px rgba(var(--ar),.22);margin-bottom:6px;word-break:break-word}
body.light-theme .word-main{text-shadow:none}.card-back .word-main{color:var(--text);font-size:30px;text-shadow:none}
.example-box{background:rgba(0,0,0,.25);border:1px solid var(--border);border-radius:14px;padding:10px 14px;margin-top:12px;text-align:left}body.light-theme .example-box{background:#F8FAFC}
.example-orig{font-size:13px;font-weight:600;color:var(--text);line-height:1.35}.example-orig b{color:var(--accent)}
.card-hint{text-align:center;font-size:11px;font-weight:600;color:var(--text-muted);opacity:.75}
.swipe-badge{position:absolute;top:18px;padding:6px 14px;border-radius:10px;font-size:14px;font-weight:800;letter-spacing:1px;text-transform:uppercase;opacity:0;pointer-events:none;z-index:20;backface-visibility:hidden;-webkit-backface-visibility:hidden;transition:opacity .15s ease}
.swipe-badge.know{left:18px;border:2px solid var(--success);color:var(--success);background:rgba(0,230,118,.14);transform:rotate(-10deg)}
.swipe-badge.again{right:18px;border:2px solid var(--danger);color:var(--danger);background:rgba(255,77,109,.14);transform:rotate(10deg)}
.session-done{display:none;position:absolute;inset:0;flex-direction:column;align-items:center;justify-content:center;gap:6px;background:var(--surface);border:1px solid rgba(var(--ar),.4);border-radius:26px;z-index:30;text-align:center;padding:24px;box-shadow:0 18px 38px rgba(0,0,0,.45);animation:fadeIn .3s ease}
.deck-wrapper.done .session-done{display:flex}.deck-wrapper.done .flashcard,.deck-wrapper.done .deck-ghost{display:none}
.done-ic{width:56px;height:56px;border-radius:50%;background:var(--accent);color:var(--accent-text);display:grid;place-items:center;box-shadow:0 0 28px var(--accent-glow);margin-bottom:4px}
.done-title{font-size:20px;font-weight:800;letter-spacing:-.4px}.done-sub{font-size:13px;font-weight:600;color:var(--text-muted);margin-bottom:10px}
.rating-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:24px;transition:opacity .25s}
.rate-btn{background:var(--surface-elevated);border:1px solid var(--border);border-bottom:4px solid #0B0B10;border-radius:16px;padding:10px 4px 9px;display:flex;flex-direction:column;align-items:center;gap:4px;cursor:pointer;font-family:inherit;color:var(--text);transition:transform .1s ease,border-bottom-width .1s ease}
body.light-theme .rate-btn{border-bottom-color:rgba(15,23,42,.18)}.rate-btn:active{transform:translateY(3px);border-bottom-width:1px}
.rate-btn[data-type=again]{border-bottom-color:rgba(255,77,109,.55)}.rate-btn[data-type=hard]{border-bottom-color:rgba(255,183,3,.55)}.rate-btn[data-type=good]{border-bottom-color:rgba(0,230,118,.55)}.rate-btn[data-type=easy]{border-bottom-color:rgba(var(--ar),.65)}
.rate-title{font-size:12px;font-weight:700}.rate-time{font-size:10px;font-weight:600;color:var(--text-muted)}
.section-title{font-size:12px;font-weight:800;letter-spacing:.9px;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px}
.decks-list{display:flex;flex-direction:column;gap:12px}
.deck-item{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:16px;position:relative;overflow:hidden;cursor:pointer;box-shadow:inset 0 1px 0 var(--border-highlight);transition:transform .15s ease}.deck-item:active{transform:scale(.985)}
.deck-item.active-deck{border-color:rgba(var(--ar),.45);background:linear-gradient(145deg,rgba(var(--ar),.06),var(--surface))}
.deck-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;gap:8px}
.deck-name{display:flex;align-items:center;gap:8px;font-size:16px;font-weight:700}
.deck-badge{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:800;padding:3px 8px;border-radius:6px;background:var(--accent-dim);color:var(--accent);white-space:nowrap}.deck-badge.pro{background:var(--accent);color:var(--accent-text)}
.deck-words{font-size:13px;color:var(--text-muted);margin-bottom:8px;line-height:1.4}.deck-words.blurred{filter:blur(4px);opacity:.7}
.deck-meta{font-size:11px;font-weight:700;color:var(--text-muted);letter-spacing:.4px}
.bento-card{background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:20px;margin-bottom:14px;box-shadow:inset 0 1px 0 var(--border-highlight)}
.ring-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px 0;position:relative}
.ring-center{position:absolute;text-align:center;top:50%;left:50%;transform:translate(-50%,-50%)}
.ring-num{font-size:28px;font-weight:800;line-height:1}.ring-sub{font-size:11px;font-weight:700;color:var(--text-muted);letter-spacing:.8px;margin-top:4px}
.learned-line{text-align:center;font-size:12px;font-weight:700;color:var(--text-muted);margin-top:6px}
.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.stat-box{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:14px 10px;text-align:center;box-shadow:inset 0 1px 0 var(--border-highlight)}
.stat-val{font-size:20px;font-weight:800;margin-bottom:4px;display:flex;align-items:center;justify-content:center;gap:4px}.stat-lbl{font-size:11px;color:var(--text-muted);font-weight:600}
.achievements-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.ach-item{display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px}
.ach-icon{width:54px;height:54px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;color:var(--text-muted)}body.light-theme .ach-icon{background:rgba(15,23,42,.03)}
.ach-item.unlocked .ach-icon{background:var(--accent);color:var(--accent-text);border-color:var(--accent);box-shadow:0 0 22px var(--accent-glow)}
.ach-name{font-size:11px;font-weight:700;color:var(--text-muted);line-height:1.25}.ach-item.unlocked .ach-name{color:var(--text)}
.setting-group{margin-bottom:18px}.setting-label{font-size:13px;font-weight:700;margin-bottom:10px;display:block}
.segmented{display:flex;background:rgba(0,0,0,.25);padding:4px;border-radius:14px;border:1px solid var(--border);gap:2px}body.light-theme .segmented{background:#F1F5F9}
.seg-btn{flex:1;padding:9px 6px;border-radius:10px;border:none;background:transparent;color:var(--text-muted);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;transition:all .2s ease}
.seg-btn.active{background:var(--accent);color:var(--accent-text);box-shadow:0 2px 12px var(--accent-glow)}
.skins-row{display:flex;gap:12px;flex-wrap:wrap}
.skin-circle{width:44px;height:44px;border-radius:50%;border:2px solid transparent;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff;transition:transform .15s ease,border-color .15s ease;box-shadow:inset 0 -3px 0 rgba(0,0,0,.18)}
.skin-circle.selected{border-color:var(--text);transform:scale(1.08)}
.toggle-row{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-top:1px solid var(--border);gap:12px}
.switch{width:48px;height:28px;background:#23232F;border-radius:999px;position:relative;cursor:pointer;transition:background .25s ease;flex-shrink:0}body.light-theme .switch{background:#CBD5E1}.switch.on{background:var(--accent)}
.switch::after{content:'';position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:transform .25s cubic-bezier(.34,1.56,.64,1)}.switch.on::after{background:var(--accent-text);transform:translateX(20px)}
.tabbar{position:fixed;bottom:0;left:0;right:0;height:calc(68px + var(--safe-bottom));padding-bottom:var(--safe-bottom);background:rgba(13,13,18,.88);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border-top:1px solid var(--border);display:flex;justify-content:space-around;align-items:center;z-index:50}
body.light-theme .tabbar{background:rgba(255,255,255,.9)}
.tab-btn{display:flex;flex-direction:column;align-items:center;gap:4px;background:none;border:none;color:var(--text-muted);font-family:inherit;font-size:11px;font-weight:700;cursor:pointer;padding:6px 2px;flex:1;font-size:10px;transition:color .2s ease}.tab-btn.active{color:var(--accent)}
.modal-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.72);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);z-index:100;display:none;align-items:flex-end;justify-content:center}
.modal-backdrop.open{display:flex;animation:fadeOverlay .2s ease}@keyframes fadeOverlay{from{opacity:0}to{opacity:1}}
.bottom-sheet{width:100%;max-width:480px;background:var(--surface);border-top:1px solid rgba(var(--ar),.4);border-radius:28px 28px 0 0;padding:14px 22px calc(24px + var(--safe-bottom));box-shadow:0 -12px 40px rgba(0,0,0,.6);animation:slideUp .3s cubic-bezier(.22,1,.36,1)}
@keyframes slideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}
.sheet-handle{width:40px;height:4px;border-radius:4px;background:rgba(255,255,255,.2);margin:0 auto 18px}body.light-theme .sheet-handle{background:rgba(15,23,42,.15)}
.pro-hero{text-align:center;margin-bottom:20px}.pro-hero h2{font-size:24px;font-weight:800;margin-bottom:6px;letter-spacing:-.5px}.pro-hero h2 span{color:var(--accent)}.pro-hero p{font-size:13px;color:var(--text-muted);line-height:1.4}
.perks-list{display:flex;flex-direction:column;gap:12px;margin-bottom:22px}
.perk-item{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.03);border:1px solid var(--border);padding:12px 14px;border-radius:16px;font-size:13px;font-weight:600;line-height:1.35}body.light-theme .perk-item{background:rgba(15,23,42,.03)}
.perk-icon{width:32px;height:32px;border-radius:10px;background:var(--accent-dim);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cta-pay{width:100%;background:var(--accent);color:var(--accent-text);border:none;border-bottom:4px solid rgba(0,0,0,.28);border-radius:18px;padding:16px;font-family:inherit;font-size:16px;font-weight:800;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 8px 25px var(--accent-glow);transition:transform .1s ease,border-bottom-width .1s ease}
.cta-pay:active{transform:translateY(3px);border-bottom-width:1px}
.sheet-close{width:100%;margin-top:10px;background:transparent;border:none;color:var(--text-muted);font-family:inherit;font-size:13px;font-weight:700;padding:12px;cursor:pointer}
.toast{position:fixed;left:50%;bottom:calc(96px + var(--safe-bottom));transform:translate(-50%,20px);background:var(--surface-elevated);border:1px solid var(--border);color:var(--text);font-size:13px;font-weight:700;padding:11px 18px;border-radius:14px;z-index:300;opacity:0;pointer-events:none;transition:opacity .25s ease,transform .25s ease;box-shadow:0 12px 30px rgba(0,0,0,.4);max-width:90vw;text-align:center}
.toast.show{opacity:1;transform:translate(-50%,0)}
.chars-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.char-item{position:relative;background:var(--surface-elevated);border:1px solid var(--border);border-radius:20px;padding:14px 10px 12px;text-align:center;cursor:pointer;transition:transform .15s ease,border-color .2s,box-shadow .2s}
.char-item:active{transform:scale(.96)}
.char-item.selected{border-color:var(--accent);box-shadow:0 0 20px var(--accent-glow),inset 0 1px 0 var(--border-highlight)}
.char-item .art{width:68px;height:68px;margin:0 auto 8px}
.char-item b{display:block;font-size:13px;font-weight:800}
.char-item span{display:block;font-size:11px;color:var(--text-muted);line-height:1.3;margin-top:2px}
.char-item .lk{position:absolute;top:10px;right:10px;color:var(--accent)}
.card-tag.slang{color:#FF9F1C;background:rgba(255,159,28,.16)}.slang-note{display:block;font-size:11px;font-weight:800;letter-spacing:.4px;color:#FF9F1C;margin-bottom:4px}
.deck-badge.sl{background:rgba(255,159,28,.16);color:#FF9F1C}
.plan-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}.plan-top h2{font-size:20px;font-weight:800;letter-spacing:-.4px}
.day{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:14px;margin-bottom:10px;cursor:pointer;box-shadow:inset 0 1px 0 var(--border-highlight);transition:transform .15s}
.day:active{transform:scale(.985)}.day.now{border-color:var(--accent);box-shadow:0 0 20px var(--accent-glow),inset 0 1px 0 var(--border-highlight)}.day.lockd{opacity:.5}
.day-ic{width:44px;height:44px;border-radius:14px;background:var(--surface-elevated);display:grid;place-items:center;color:var(--accent);flex:none}.day.done .day-ic{background:var(--accent);color:var(--accent-text)}
.day b{display:block;font-size:15px}.day span{font-size:12px;color:var(--text-muted)}.day small{margin-left:auto;font-size:10px;font-weight:800;color:var(--accent);letter-spacing:.6px}
.rule-item{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:14px 16px;margin-bottom:10px;box-shadow:inset 0 1px 0 var(--border-highlight)}
.rule-item b{display:flex;align-items:center;gap:6px;font-size:15px}.rule-item b em{font-style:normal;font-size:10px;font-weight:800;color:var(--accent-text);background:var(--accent);padding:2px 7px;border-radius:6px;letter-spacing:.4px}
.rule-item p{font-size:13px;color:var(--text-muted);margin-top:4px;line-height:1.45}.rule-item.lockd{opacity:.55}
.rule-ex{display:flex;align-items:center;gap:8px;margin-top:8px;background:rgba(0,0,0,.25);border:1px solid var(--border);border-radius:12px;padding:8px 12px;font-size:13px;font-weight:600;cursor:pointer;text-align:left}body.light-theme .rule-ex{background:#F8FAFC}.rule-ex .ic{color:var(--accent)}
.lesson{position:fixed;inset:0;z-index:150;background:var(--bg);display:none;flex-direction:column;padding:calc(14px + env(safe-area-inset-top)) 18px calc(18px + var(--safe-bottom))}.lesson.open{display:flex}
.lq-head{display:flex;align-items:center;gap:12px;margin-bottom:18px}.lq-head .xp-bar,.lq-head .prog{flex:1}
.lq-body{flex:1;overflow:auto;display:flex;flex-direction:column;align-items:center;gap:12px;padding-top:6px;text-align:center}.lq-body.center{justify-content:center}
.lq-prompt{font-size:20px;font-weight:800;letter-spacing:-.4px}.lq-big{font-size:34px;font-weight:800;color:var(--accent);word-break:break-word}.lq-sub{font-size:15px;font-weight:600}.lq-hint{font-size:13px;color:var(--text-muted)}
.lq-play{width:64px;height:64px;border-radius:50%;border:1px solid var(--border);background:var(--surface-elevated);color:var(--accent);display:grid;place-items:center;box-shadow:0 0 20px var(--accent-glow);transition:transform .15s}.lq-play:active{transform:scale(.92)}
.opts{display:flex;flex-direction:column;gap:10px;width:100%;margin-top:6px}
.opt{width:100%;padding:15px;border-radius:16px;border:1px solid var(--border);border-bottom:4px solid #0B0B10;background:var(--surface-elevated);color:var(--text);font-family:inherit;font-size:15px;font-weight:700;transition:transform .1s}
.opt:active{transform:translateY(3px);border-bottom-width:1px}.opt.ok{background:rgba(0,230,118,.16);border-color:var(--success);color:var(--success)}.opt.bad{background:rgba(255,77,109,.16);border-color:var(--danger);color:var(--danger)}
.slots,.bank{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;width:100%;min-height:52px}.slots{border-bottom:2px dashed var(--border);padding-bottom:12px}
.tok{padding:10px 14px;border-radius:12px;border:1px solid var(--border);border-bottom:3px solid #0B0B10;background:var(--surface-elevated);color:var(--text);font-family:inherit;font-size:15px;font-weight:700}
.cta-pay:disabled{opacity:.4}
.lq-foot{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.fb{display:flex;flex-direction:column;gap:2px;padding:12px 14px;border-radius:14px;font-size:13px;text-align:left}.fb b{font-size:15px}.fb span{color:var(--text-muted)}.fb.good{background:rgba(0,230,118,.12);color:var(--success)}.fb.miss{background:rgba(255,77,109,.12);color:var(--danger)}
.rule-body{font-size:15px;line-height:1.5;text-align:left;width:100%}
.chat{position:fixed;inset:0;z-index:160;background:var(--bg);display:none;flex-direction:column}.chat.open{display:flex}
.ch-head{display:flex;align-items:center;gap:12px;padding:calc(12px + env(safe-area-inset-top)) 16px 12px;border-bottom:1px solid var(--border)}
.ch-art{width:48px;height:48px;flex:none}.ch-art svg{width:100%;height:100%}.ch-t{flex:1}.ch-t b{display:block;font-size:16px}.ch-t span{font-size:12px;color:var(--text-muted)}
.ch-msgs{flex:1;overflow:auto;padding:14px 16px;display:flex;flex-direction:column;gap:10px}
.msg{max-width:84%;padding:10px 14px;border-radius:16px;font-size:14px;line-height:1.45;white-space:pre-wrap;user-select:text}.msg.a{align-self:flex-start;background:var(--surface-elevated);border:1px solid var(--border)}.msg.u{align-self:flex-end;background:var(--accent);color:var(--accent-text)}
.ch-chips{display:flex;gap:8px;overflow-x:auto;padding:0 16px 8px;scrollbar-width:none}.chip{flex:none;padding:8px 12px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--text);font-family:inherit;font-size:12px;font-weight:700}
.ch-in{display:flex;gap:8px;padding:8px 16px calc(12px + var(--safe-bottom))}.ch-in input{flex:1;height:44px;border-radius:14px;border:1px solid var(--border);background:var(--surface);color:var(--text);padding:0 14px;font-family:inherit;font-size:15px;user-select:text;outline:none}.ch-in input:focus{border-color:var(--accent)}.ch-in .icon-btn{width:44px;height:44px;background:var(--accent);color:var(--accent-text);border:0}
.rw{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid var(--border)}
.rw-i{width:40px;height:40px;border-radius:12px;background:var(--accent-dim);color:var(--accent);display:grid;place-items:center;flex:none}.rw-t{flex:1;min-width:0}.rw-t b{display:block;font-size:14px}.rw-t span{font-size:12px;color:var(--text-muted)}
.rw-b{padding:8px 11px;border-radius:10px;border:1px solid var(--border);background:var(--surface-elevated);color:var(--text);font-family:inherit;font-size:12px;font-weight:800}.rw-b.pri{background:var(--accent);color:var(--accent-text);border-color:var(--accent)}.rw-ok{color:var(--accent)}
</style>
</head>
<body>
<canvas id="confettiCanvas"></canvas>

<header class="header">
  <div class="logo">Smart<span>Study</span></div>
  <div class="header-actions">
    <div class="streak-pill" id="streakPill"></div>
    <button class="pro-badge" id="proBadge"></button>
  </div>
</header>

<div class="lang-scroll" id="langScroll"></div>

<main>
<section class="view active" id="view-learn">
  <div class="foxy-card" id="foxyCard">
    <div class="foxy-avatar" id="foxyArt"></div>
    <div class="foxy-info">
      <div class="foxy-bubble" id="foxyText"></div>
      <div class="xp-row"><span id="foxyLevel"></span><span id="foxyXp"></span></div>
      <div class="xp-bar"><div class="xp-fill" id="xpFill" style="width:4%"></div></div>
    </div>
  </div>

  <div class="session-meta">
    <span class="session-label" id="sessionLabel"></span>
    <div class="session-dots" id="sessionDots"></div>
  </div>

  <div class="deck-wrapper" id="deckWrapper">
    <div class="deck-ghost deck-ghost-2"></div>
    <div class="deck-ghost deck-ghost-1"></div>
    <div class="flashcard" id="flashcard">
      <div class="card-face card-front">
        <div class="card-top">
          <div class="tag-group"><span class="card-tag level" id="frontLevel">EN</span><span class="card-tag" id="frontTag"></span></div>
          <button class="icon-btn" id="speakBtn" aria-label="Audio"><svg class="ic" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg></button>
        </div>
        <div class="card-center"><div class="word-main" id="frontWord"></div></div>
        <div class="card-hint" data-en="Tap to flip or swipe">Нажми для перевода или свайпни</div>
      </div>
      <div class="card-face card-back">
        <div class="card-top">
          <div class="tag-group"><span class="card-tag level" id="backLevel">EN</span><span class="card-tag" data-en="translation">перевод</span></div>
          <button class="icon-btn" id="speakBtnBack" aria-label="Audio"><svg class="ic" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg></button>
        </div>
        <div class="card-center">
          <div class="word-main" id="backWord"></div>
          <div class="example-box"><div class="example-orig" id="backExample"></div></div>
        </div>
        <div class="card-hint" data-en="Rate how easily you recalled it">Оцени, насколько легко вспомнил</div>
      </div>
      <div class="swipe-badge know" id="badgeKnow" data-en="Know it">Знаю</div>
      <div class="swipe-badge again" id="badgeAgain" data-en="Again">Повтор</div>
    </div>
    <div class="session-done" id="sessionDone">
      <div class="done-ic"><svg class="ic" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>
      <div class="done-title" id="doneTitle"></div>
      <div class="done-sub" id="doneSub"></div>
      <button class="cta-pay" id="restartBtn" style="max-width:220px" data-en="Next round">Ещё раунд</button>
    </div>
  </div>

  <div class="rating-grid" id="ratingGrid">
    <button class="rate-btn" data-type="again"><span class="rate-title" data-en="Forgot">Не помню</span><span class="rate-time">+0 XP</span></button>
    <button class="rate-btn" data-type="hard"><span class="rate-title" data-en="Hard">Трудно</span><span class="rate-time">+1 XP</span></button>
    <button class="rate-btn" data-type="good"><span class="rate-title" data-en="Good">Хорошо</span><span class="rate-time">+2 XP</span></button>
    <button class="rate-btn" data-type="easy"><span class="rate-title" data-en="Easy">Легко</span><span class="rate-time">+3 XP</span></button>
  </div>

  <div class="section-title" data-en="Word sets">Наборы слов</div>
  <div class="decks-list" id="decksList"></div>
</section>

<section class="view" id="view-plan"></section>
<section class="view" id="view-rules"></section>
<section class="view" id="view-progress">
  <div class="bento-card">
    <div class="ring-wrap">
      <svg width="150" height="150" viewBox="0 0 130 130">
        <circle cx="65" cy="65" r="52" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="11"/>
        <circle id="ringProgress" cx="65" cy="65" r="52" fill="none" stroke="var(--accent)" stroke-width="11" stroke-linecap="round" transform="rotate(-90 65 65)" stroke-dasharray="326.7" stroke-dashoffset="326.7" style="transition:stroke-dashoffset .6s cubic-bezier(.34,1.56,.64,1);filter:drop-shadow(0 0 8px var(--accent-glow))"/>
      </svg>
      <div class="ring-center"><div class="ring-num" id="ringNum">0%</div><div class="ring-sub" data-en="DAILY GOAL">ЦЕЛЬ ДНЯ</div></div>
    </div>
    <div class="learned-line" id="learnedLine"></div>
  </div>
  <div class="stats-row">
    <div class="stat-box"><div class="stat-val" id="statStreak">0</div><div class="stat-lbl" data-en="day streak">дней подряд</div></div>
    <div class="stat-box"><div class="stat-val" id="statToday">0</div><div class="stat-lbl" data-en="today">сегодня</div></div>
    <div class="stat-box"><div class="stat-val" id="statTotal">0</div><div class="stat-lbl" data-en="total reviews">всего повторов</div></div>
  </div>
  <div class="bento-card">
    <div class="section-title" style="margin-bottom:0" data-en="Achievements">Достижения</div>
    <div class="achievements-grid" id="achGrid"></div>
  </div>
</section>

<section class="view" id="view-settings">
  <div class="bento-card">
    <div class="setting-group">
      <span class="setting-label" data-en="Interface language">Язык интерфейса</span>
      <div class="segmented" data-seg="ui"><button class="seg-btn" data-val="ru">Русский</button><button class="seg-btn" data-val="en">English</button></div>
    </div>
    <div class="setting-group">
      <span class="setting-label" data-en="Daily goal, words">Цель на день, слов</span>
      <div class="segmented" data-seg="goal"><button class="seg-btn" data-val="5">5</button><button class="seg-btn" data-val="10">10</button><button class="seg-btn" data-val="20">20</button><button class="seg-btn" data-val="30">30</button></div>
    </div>
    <div class="setting-group" style="margin-bottom:0">
      <span class="setting-label" data-en="Theme">Тема оформления</span>
      <div class="segmented" data-seg="theme"><button class="seg-btn" data-val="dark" data-en="Dark">Тёмная</button><button class="seg-btn" data-val="light" data-en="Light">Светлая</button></div>
    </div>
  </div>
  <div class="bento-card"><span class="setting-label" data-en="Companion">Персонаж-компаньон</span><div class="chars-grid" id="charsGrid"></div></div>
  <div class="bento-card">
    <div class="toggle-row" style="border-top:none;padding-top:0"><span class="setting-label" style="margin:0" data-en="Pronunciation audio">Озвучка произношения</span><div class="switch" id="switchSound"></div></div>
    <div class="toggle-row"><span class="setting-label" style="margin:0" data-en="Haptic feedback">Тактильная вибрация</span><div class="switch" id="switchHaptics"></div></div>
  </div>
  <div class="bento-card">
    <div class="setting-group"><span class="setting-label" data-en="Word audio">Озвучка слов</span>
      <div class="segmented" data-seg="wv"><button class="seg-btn" data-val="word" data-en="Word">Слово</button><button class="seg-btn" data-val="both" data-en="Word + translation">Слово + перевод</button></div></div>
    <div class="toggle-row" style="border-top:none;padding:0"><span class="setting-label" style="margin:0" data-en="Companion voice">Голос компаньона</span><div class="switch" id="switchCv"></div></div>
  </div>
  <div class="bento-card" id="settingsProCard"><button class="cta-pay" id="settingsProBtn"></button></div>
</section>
</main>

<nav class="tabbar">
  <button class="tab-btn active" data-view="learn"><i class="ti" data-ic="book"></i><span data-en="Learn">Учить</span></button>
  <button class="tab-btn" data-view="plan"><i class="ti" data-ic="cal"></i><span data-en="Plan">План</span></button>
  <button class="tab-btn" data-view="rules"><i class="ti" data-ic="bookmark"></i><span data-en="Rules">Правила</span></button>
  <button class="tab-btn" data-view="progress"><i class="ti" data-ic="bars"></i><span data-en="Progress">Прогресс</span></button>
  <button class="tab-btn" data-view="settings"><i class="ti" data-ic="sliders"></i><span data-en="Settings">Настройки</span></button>
</nav>

<div class="modal-backdrop" id="proModal">
  <div class="bottom-sheet">
    <div class="sheet-handle"></div>
    <div class="pro-hero">
      <h2>SmartStudy <span>PRO</span></h2>
      <p data-en="Learn without limits">Учи язык без ограничений</p>
    </div>
    <div class="perks-list" id="perksList"></div>
    <button class="cta-pay" id="payBtn"></button>
    <button class="sheet-close" id="closeProModal" data-en="Later">Позже</button>
  </div>
</div>

<div class="lesson" id="lesson"></div>
<div class="chat" id="chat"></div>
<div class="toast" id="toast"></div>

<script>
const tg = (window.Telegram && window.Telegram.WebApp) || null;
if (tg) { try { tg.ready(); tg.expand(); if (tg.disableVerticalSwipes) tg.disableVerticalSwipes(); } catch (e) {} }
const DEMO = !tg || !tg.initData;

const LS = {
  get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
};
const cfg = Object.assign({ ui: 'ru', goal: 10, theme: 'dark', char: 'fox', sound: true, haptics: true, learn: 'en', cv: true, wv: 'both' }, LS.get('ss_cfg3', {}));
const prog = Object.assign({ xp: 0, streak: 0, last: '', day: '', today: 0, total: 0 }, LS.get('ss_st3', {}));
const saveCfg = () => LS.set('ss_cfg3', cfg), saveProg = () => LS.set('ss_st3', prog);

let S = { premium: false, cards: [], learned: 0, total: 12, locked: 8, price: 100 };
let queue = [], total0 = 0, answered = 0, done = false, busy = false, flipped = false, gain = 0, current = 'learn';

const $ = (id) => document.getElementById(id);
const L = (r, e) => cfg.ui === 'en' ? e : r;
const pro = () => !!S.premium;
const day = (ms) => new Date(ms || Date.now()).toLocaleDateString('sv');
const todayN = () => prog.day === day() ? prog.today : 0;
const streakNow = () => { const gap = pro() ? 2 : 1; for (let i = 0; i <= gap; i++) if (prog.last === day(Date.now() - i * 864e5)) return prog.streak; return 0; };
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function hl(text, word) {
  const i = text.toLowerCase().indexOf(String(word).toLowerCase().replace(/^(der|die|das|le|la|l')\s?/i, ''));
  const w = String(word).replace(/^(der|die|das|le|la|l')\s?/i, '');
  return i < 0 || !w ? esc(text) : esc(text.slice(0, i)) + '<b>' + esc(text.slice(i, i + w.length)) + '</b>' + esc(text.slice(i + w.length));
}

const IC = {
  flame: '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
  zap: '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
  lock: '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
  check: '<path d="M20 6 9 17l-5-5"/>',
  flag: '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/>',
  target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
  award: '<circle cx="12" cy="8" r="6"/><path d="M15.5 12.9 17 22l-5-3-5 3 1.5-9.1"/>',
  crown: '<path d="m2 4 3 12h14l3-12-6 7-4-7-4 7z"/><path d="M5 20h14"/>',
  book: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
  swatch: '<circle cx="13.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="10.5" r="2.5"/><circle cx="8.5" cy="7.5" r="2.5"/><circle cx="6.5" cy="12.5" r="2.5"/><path d="M12 22a10 10 0 1 1 10-10c0 3-2 4-4 4h-2a2 2 0 0 0-1.5 3.3A2 2 0 0 1 12 22z"/>'
};
Object.assign(IC, {
  x: '<path d="M18 6 6 18M6 6l12 12"/>', vol: '<path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>',
  mic: '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>',
  headphones: '<path d="M3 14v-2a9 9 0 0 1 18 0v2"/><rect x="2" y="14" width="5" height="7" rx="2"/><rect x="17" y="14" width="5" height="7" rx="2"/>',
  bookmark: '<path d="M19 21l-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>', chat: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
  cal: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>', layers: '<path d="M12 2 2 7l10 5 10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>',
  send: '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>', gift: '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
  users: '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
  bars: '<path d="M18 20V10M12 20V4M6 20v-6"/>', sliders: '<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3M14 2v4M8 10v4M16 18v4"/>'
});
const ic = (n, s = 18, w = 2) => '<svg class="ic" width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="' + w + '" stroke-linecap="round" stroke-linejoin="round">' + IC[n] + '</svg>';

document.querySelectorAll('.ti').forEach((e) => { e.outerHTML = ic(e.dataset.ic, 22); });
function haptic(type) {
  if (!cfg.haptics) return;
  try {
    if (tg && tg.HapticFeedback) {
      if (type === 'success' || type === 'warning' || type === 'error') tg.HapticFeedback.notificationOccurred(type);
      else tg.HapticFeedback.impactOccurred(type || 'light');
    } else if (navigator.vibrate) navigator.vibrate(8);
  } catch (e) {}
}
const SPEECH = { en: 'en-US', es: 'es-ES', de: 'de-DE', fr: 'fr-FR', it: 'it-IT', pt: 'pt-BR', tr: 'tr-TR', zh: 'zh-CN', ja: 'ja-JP' };
let VOICES = [], spkId = 0;
const loadVoices = () => { try { VOICES = speechSynthesis.getVoices() || []; } catch (e) {} };
try { loadVoices(); speechSynthesis.onvoiceschanged = loadVoices; } catch (e) {}
const base = (w) => String(w).split(' (')[0];
function voiceFor(lang, g) {
  const b = lang.slice(0, 2).toLowerCase(), list = VOICES.filter((v) => String(v.lang).toLowerCase().replace('_', '-').startsWith(b));
  if (!list.length) return null;
  const fem = /female|woman|milena|alena|katya|anna|zira|samantha|karen|tessa|elsa|paulina|google.*(русск|russian)/i, mal = /\bmale\b|yuri|pavel|ivan|daniel|david|alex|thomas|jorge|diego/i;
  return list.find((v) => (g === 'f' ? fem : mal).test(v.name)) || list[0];
}
function sayText(text, lang, o) {
  return new Promise((res) => {
    try {
      const u = new SpeechSynthesisUtterance(text); u.lang = lang; u.rate = o.r || .92; u.pitch = o.p || 1;
      const v = voiceFor(lang, o.g); if (v) u.voice = v;
      u.onend = u.onerror = () => res(); speechSynthesis.speak(u);
    } catch (e) { res(); }
  });
}
async function speakSeq(parts) {
  if (!('speechSynthesis' in window)) return;
  const my = ++spkId; try { speechSynthesis.cancel(); } catch (e) {}
  for (const p of parts) { if (my !== spkId) return; await sayText(p.t, p.l, p); }
}
function speakWord(c) {
  if (!cfg.sound || !c) return;
  const parts = [{ t: base(c.en), l: SPEECH[cfg.learn] || 'en-US', r: .85 }];
  if (cfg.wv === 'both' && c.ru) parts.push({ t: c.ru, l: 'ru-RU', r: .95 });
  speakSeq(parts);
}
const speak = (t) => { if (cfg.sound) speakSeq([{ t: base(t), l: SPEECH[cfg.learn] || 'en-US', r: .85 }]); };
const VP = { fox: { p: 1.2, r: 1, g: 'f' }, cat: { p: .95, r: .92, g: 'm' }, capy: { p: .75, r: .78, g: 'm' }, shiba: { p: 1.35, r: 1.12, g: 'm' }, hamster: { p: 1.4, r: 1.18, g: 'm' }, ai: { p: .85, r: .95, g: 'm' }, robot: { p: .55, r: .82, g: 'm' }, detective: { p: .8, r: .88, g: 'm' }, scientist: { p: 1.25, r: 1.22, g: 'm' }, raven: { p: .65, r: .78, g: 'm' }, ninja: { p: 1, r: 1.15, g: 'm' }, astro: { p: 1.1, r: 1, g: 'f' } };
function talk(text) { if (!cfg.cv || !text) return; const v = VP[cur().id] || {}; speakSeq([{ t: String(text).replace(/[\[\]]/g, ''), l: cfg.ui === 'en' ? 'en-US' : 'ru-RU', p: v.p, r: v.r, g: v.g }]); }
let toastTimer;
function toast(msg) { const el = $('toast'); el.textContent = msg; el.classList.add('show'); clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('show'), 2000); }

async function api(path, body) {
  const r = await fetch('/api/' + path, {
    method: body ? 'POST' : 'GET',
    headers: { 'X-Init-Data': tg ? tg.initData : '', 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined
  });
  if (!r.ok) throw new Error(r.status);
  return r.json();
}

/* ---------- data ---------- */
const LANGS = [['en', 'Английский', 'English'], ['es', 'Испанский', 'Spanish'], ['de', 'Немецкий', 'German'], ['fr', 'Французский', 'French'], ['it', 'Итальянский', 'Italian'], ['pt', 'Португальский', 'Portuguese'], ['tr', 'Турецкий', 'Turkish'], ['zh', 'Китайский', 'Chinese'], ['ja', 'Японский', 'Japanese']];
const CH = [
  { id: 'fox', free: 1, n: ['Фокси', 'Foxy'], t: ['Классический друг', 'Classic buddy'], a: '#C8FF00', al: '#65A30D', on: '#09090D', bg: '#09090D', s: '#13131A', e: '#1B1B24',
    ru: ['Привет! Нажми на карточку, чтобы увидеть перевод.', 'Отлично! Так держать.', 'Да ты талант.', 'Ничего, повторим ещё раз.', 'Бывает. Это слово вернётся.', 'Новый уровень! Я горжусь тобой.'],
    en: ['Hi! Tap the card to see the translation.', 'Awesome! Keep it up.', 'You are a natural.', 'No worries, we will repeat it.', 'It happens. This word will come back.', 'Level up! I am proud of you.'] },
  { id: 'cat', free: 1, n: ['Мурз', 'Murz'], t: ['Ироничный кот', 'Ironic cat'], a: '#4C9BFF', al: '#2563EB', on: '#06101F', bg: '#080B14', s: '#101624', e: '#18203A',
    ru: ['Мяу. Ну что, поучим слова? Только не засыпай.', 'Надо же. Правильно. Почти не удивлён.', 'Мурр. Это было красиво.', 'Эх, человек. Ладно, вернём слово позже.', 'Ошибся? Я тоже иногда роняю вещи со стола.', 'Новый уровень. Приношу рыбу в награду.'],
    en: ['Meow. Shall we learn words? Just do not fall asleep.', 'Well, well. Correct. Barely surprised.', 'Purr. That was beautiful.', 'Oh, human. Fine, the word will return.', 'Wrong? I also knock things off tables sometimes.', 'Level up. Here, have a fish.'] },
  { id: 'capy', n: ['Капи', 'Capy'], t: ['Чилл без стресса', 'Stress-free chill'], a: '#9BD17A', al: '#4D7C0F', on: '#14210E', bg: '#14110C', s: '#1E1A13', e: '#2A241A',
    ru: ['Привет. Никуда не спеши, слова подождут.', 'Ты молодец. Выдохни и продолжай.', 'Вот это спокойное мастерство.', 'Не страшно. Слово зайдёт в другой раз.', 'Ошибка тоже часть пути. Дыши.', 'Новый уровень. Заслужил тёплую ванну.'],
    en: ['Hi. No rush, the words can wait.', 'Well done. Breathe out and carry on.', 'Such calm mastery.', 'No worries. The word will come back later.', 'A mistake is part of the path. Breathe.', 'Level up. You earned a warm bath.'] },
  { id: 'shiba', n: ['Шиби', 'Shiba'], t: ['Много монетки', 'Much coins'], a: '#F5C451', al: '#B45309', on: '#1A1405', bg: '#0F0F11', s: '#1A1A1E', e: '#25252B',
    ru: ['Вау. Много слов. Такой запас. Давай учить.', 'Вау. Правильно. Плюс монетка.', 'Очень знание. Много XP.', 'Так мало. Но ничего. Повторим.', 'Не угадал. Монетки не пропали.', 'Новый уровень! Много богатство.'],
    en: ['Wow. Many words. Much stock. Let us learn.', 'Wow. Correct. Plus one coin.', 'Very knowledge. Much XP.', 'So close. But okay. We repeat.', 'Not guessed. Coins are safe.', 'Level up! Much wealth.'] },
  { id: 'hamster', n: ['Хомяк', 'Hamster'], t: ['Комбо и прокачка', 'Combos & levels'], a: '#FFC933', al: '#B7791F', on: '#1A1200', bg: '#0B0B0B', s: '#17140D', e: '#221D10',
    ru: ['Добро пожаловать. Сегодня качаем слова и собираем комбо.', 'Комбо! Прокачка идёт.', 'Плюс к профиту знаний.', 'Комбо сбито. Соберём заново.', 'Промах. Слово вернётся в колоду.', 'Новый уровень прокачки. Карточки дорожают, ты тоже.'],
    en: ['Welcome. Today we level up words and build combos.', 'Combo! Level-up in progress.', 'Plus to your knowledge profit.', 'Combo broken. We will rebuild it.', 'Miss. The word returns to the deck.', 'New upgrade level. Cards get pricier, and so do you.'] },
  { id: 'ai', n: ['ОРИОН', 'ORION'], t: ['Системные отчёты', 'System reports'], a: '#38E1FF', al: '#0E7490', on: '#031318', bg: '#040A12', s: '#0A1622', e: '#10243A',
    ru: ['[СИСТЕМА] Онлайн. Готов к обучению. Выберите карточку.', '[ОТЧЁТ] Ответ верен. Эффективность растёт.', '[АНАЛИЗ] Отличный результат. Продолжаем.', '[ОТЧЁТ] Обнаружена ошибка. Слово вернётся в очередь.', '[АНАЛИЗ] Неточность зафиксирована. Рекомендую повторить.', '[СИСТЕМА] Уровень повышен. Доступ к новым данным.'],
    en: ['[SYSTEM] Online. Ready to teach. Select a card.', '[REPORT] Answer correct. Efficiency rising.', '[ANALYSIS] Excellent result. Proceeding.', '[REPORT] Error detected. Word returns to the queue.', '[ANALYSIS] Inaccuracy logged. Repetition recommended.', '[SYSTEM] Level increased. New data unlocked.'] },
  { id: 'robot', n: ['КУБ-7', 'CUB-7'], t: ['Ретрофутуризм СССР', 'Soviet retro-future'], a: '#FF3B3B', al: '#B91C1C', on: '#FFFFFF', bg: '#0E0E0F', s: '#1A1A1C', e: '#26262A',
    ru: ['Товарищ, добро пожаловать. Приступаем к занятию.', 'Верно. План по знаниям выполняется.', 'Отличная работа. Норма перевыполнена.', 'Ошибка. Исправим, товарищ.', 'Неточность. Слово вернётся в очередь.', 'Новый разряд присвоен. Так держать, товарищ.'],
    en: ['Comrade, welcome. Let us begin the lesson.', 'Correct. The knowledge plan is on track.', 'Excellent work. Quota exceeded.', 'Error. We will correct it, comrade.', 'Inaccuracy. The word returns to the queue.', 'New rank awarded. Keep it up, comrade.'] },
  { id: 'detective', n: ['Инспектор', 'Inspector'], t: ['Дедукция', 'Deduction'], a: '#A9C7FF', al: '#1D4ED8', on: '#0A1226', bg: '#070B16', s: '#0F1730', e: '#172248',
    ru: ['Добрый день. Дело простое: выучить слова. Приступим.', 'Элементарно. Ответ верен.', 'Блестящая дедукция.', 'Любопытно. Улика не сходится, повторим.', 'Ошибка, но это тоже зацепка.', 'Новый ранг. Расследуем дальше.'],
    en: ['Good day. A simple case: learn the words. Shall we?', 'Elementary. The answer is correct.', 'Brilliant deduction.', 'Curious. The clue does not fit, we repeat.', 'A mistake, but also a lead.', 'New rank. Onward with the case.'] },
  { id: 'scientist', n: ['Профессор', 'Professor'], t: ['Безумные примеры', 'Wild examples'], a: '#7CFF3E', al: '#15803D', on: '#0A1A02', bg: '#0C0716', s: '#170F29', e: '#221740',
    ru: ['Ха! Эксперимент начинается. Слова ждут, ассистент!', 'Гениально! Колбы не взорвались.', 'Эврика! Мозг работает на максимум.', 'Бах! Ошибка. Но наука любит ошибки.', 'Эксперимент не удался. Повторим реакцию.', 'Новый уровень. Лаборатория гудит.'],
    en: ['Ha! The experiment begins. Words await, assistant!', 'Genius! The flasks did not explode.', 'Eureka! Brain at maximum.', 'Boom! A mistake. But science loves mistakes.', 'Experiment failed. We repeat the reaction.', 'Level up. The lab is humming.'] },
  { id: 'raven', n: ['Эдгар', 'Edgar'], t: ['Готика', 'Gothic'], a: '#A78BFA', al: '#6D28D9', on: '#0E0820', bg: '#050505', s: '#0F0F10', e: '#19191C',
    ru: ['Добро пожаловать в тишину. Слова ждут.', 'Верно. Тьма одобряет.', 'Изящно. Почти зловеще.', 'Ошибка. Что ж, такова ночь.', 'Неверно. Слово вернётся из тени.', 'Новая ступень. Ночь становится глубже.'],
    en: ['Welcome to the silence. The words await.', 'Correct. The dark approves.', 'Elegant. Almost ominous.', 'A mistake. Such is the night.', 'Wrong. The word returns from the shadows.', 'A new step. The night grows deeper.'] },
  { id: 'ninja', n: ['Ниндзя', 'Ninja'], t: ['Живой сленг', 'Street slang'], a: '#FF3D4D', al: '#B91C1C', on: '#FFFFFF', bg: '#0B0A0A', s: '#171212', e: '#241A1A',
    ru: ['Йо. Сегодня учим живую речь. Без зевоты.', 'Чётко. Как по маслу.', 'Огонь. Это уже сленг.', 'Мимо. Ниндзя падают и встают.', 'Облом. Слово вернётся.', 'Новый пояс. Респект.'],
    en: ['Yo. Today we learn real talk. No yawning.', 'Clean. Smooth as butter.', 'Fire. That is slang already.', 'Missed. Ninjas fall and get back up.', 'Bummer. The word will return.', 'New belt. Respect.'] },
  { id: 'astro', n: ['Астро', 'Astro'], t: ['Миссия на орбите', 'Mission to orbit'], a: '#FF8A3D', al: '#C2410C', on: '#1A0B02', bg: '#0A0B12', s: '#14161F', e: '#1E2130',
    ru: ['Приём! Миссия: выучить слова. Поехали.', 'Цель поражена. Курс верный.', 'Отличный выход в открытый космос.', 'Отклонение от курса. Скорректируем.', 'Сбой. Слово вернётся на орбиту.', 'Новая орбита. Миссия идёт по плану.'],
    en: ['Houston! Mission: learn the words. Lift off.', 'Target hit. Course is true.', 'Great spacewalk.', 'Course deviation. We will correct it.', 'Glitch. The word returns to orbit.', 'New orbit. The mission is on plan.'] }
];
const E = (cx, cy, rx, ry, f) => '<ellipse class="eye" cx="' + cx + '" cy="' + cy + '" rx="' + rx + '" ry="' + ry + '" fill="' + f + '"/>';
const ART = {
  fox: '<polygon points="12,46 18,8 44,28" fill="#C75C1B"/><polygon points="88,46 82,8 56,28" fill="#C75C1B"/><polygon points="19,36 21,19 35,28" fill="#FFC9A3"/><polygon points="81,36 79,19 65,28" fill="#FFC9A3"/><path d="M50 24C74 24 90 38 90 58C90 78 72 91 50 91C28 91 10 78 10 58C10 38 26 24 50 24Z" fill="#FF8A3D"/><path d="M10 58C22 68 36 72 50 72C64 72 78 68 90 58C90 78 72 91 50 91C28 91 10 78 10 58Z" fill="#FFF1E6"/>' + E(35, 54, 5, 6, '#14141C') + E(65, 54, 5, 6, '#14141C') + '<circle cx="36.6" cy="52" r="1.6" fill="#fff"/><circle cx="66.6" cy="52" r="1.6" fill="#fff"/><path d="M45 68h10l-5 6z" fill="#14141C"/><path d="M50 74v3M50 77q-4 4-8 1M50 77q4 4 8 1" stroke="#14141C" stroke-width="2" stroke-linecap="round"/>',
  cat: '<polygon points="14,44 16,10 42,26" fill="#8FA3C0"/><polygon points="86,44 84,10 58,26" fill="#8FA3C0"/><polygon points="20,36 21,19 34,27" fill="#F4A6B8"/><polygon points="80,36 79,19 66,27" fill="#F4A6B8"/><ellipse cx="50" cy="58" rx="38" ry="33" fill="#9FB2CE"/><path d="M44 36v8M50 34v9M56 36v8" stroke="#7D91B0" stroke-width="3" stroke-linecap="round"/><ellipse cx="50" cy="72" rx="16" ry="11" fill="#EAF0FA"/>' + E(33, 56, 6, 7, '#101624') + E(67, 56, 6, 7, '#101624') + '<circle cx="35" cy="53.5" r="2" fill="#fff"/><circle cx="69" cy="53.5" r="2" fill="#fff"/><polygon points="46,66 54,66 50,71" fill="#F4A6B8"/><path d="M50 71q-5 6-9 2M50 71q5 6 9 2" stroke="#101624" stroke-width="2" stroke-linecap="round"/><path d="M10 64L30 66M10 72L30 70M90 64L70 66M90 72L70 70" stroke="#EAF0FA" stroke-width="1.6" stroke-linecap="round"/>',
  capy: '<circle cx="24" cy="32" r="8" fill="#9B7248"/><circle cx="76" cy="32" r="8" fill="#9B7248"/><rect x="12" y="30" width="76" height="60" rx="30" fill="#B98B5E"/><ellipse cx="50" cy="70" rx="22" ry="16" fill="#CBA07A"/><ellipse cx="42" cy="65" rx="2.5" ry="3.5" fill="#6B4A2B"/><ellipse cx="58" cy="65" rx="2.5" ry="3.5" fill="#6B4A2B"/><path d="M44 77q6 4 12 0" stroke="#6B4A2B" stroke-width="2.4" stroke-linecap="round"/><path class="eye" d="M26 50q6 5 12 0M62 50q6 5 12 0" stroke="#2A1B0E" stroke-width="3" stroke-linecap="round"/><ellipse cx="24" cy="62" rx="5" ry="3" fill="#E7A58A" opacity=".6"/><ellipse cx="76" cy="62" rx="5" ry="3" fill="#E7A58A" opacity=".6"/><circle cx="50" cy="26" r="8" fill="#F59E0B"/><path d="M52 19q6-6 11-2q-4 6-11 2z" fill="#6FAE4C"/>',
  shiba: '<polygon points="14,46 20,10 44,28" fill="#E2A25A"/><polygon points="86,46 80,10 56,28" fill="#E2A25A"/><path d="M50 24C74 24 90 38 90 58C90 78 72 90 50 90C28 90 10 78 10 58C10 38 26 24 50 24Z" fill="#EFB36B"/><path d="M50 58C62 58 88 58 88 66C84 82 68 90 50 90C32 90 16 82 12 66C12 58 38 58 50 58Z" fill="#FFF3DF"/><circle cx="36" cy="40" r="2.2" fill="#FFF3DF"/><circle cx="64" cy="40" r="2.2" fill="#FFF3DF"/>' + E(36, 52, 4.4, 5.2, '#1E1A16') + E(64, 52, 4.4, 5.2, '#1E1A16') + '<ellipse cx="50" cy="66" rx="6" ry="4.4" fill="#1E1A16"/><path d="M50 70q-6 6-11 1M50 70q6 6 11 1" stroke="#1E1A16" stroke-width="2" stroke-linecap="round"/><circle cx="85" cy="18" r="10" fill="#F5C451" stroke="#B8861B" stroke-width="2"/><circle cx="85" cy="18" r="5" stroke="#B8861B" stroke-width="2"/>',
  hamster: '<circle cx="24" cy="28" r="10" fill="#D9A066"/><circle cx="76" cy="28" r="10" fill="#D9A066"/><circle cx="24" cy="28" r="5" fill="#F4B6B0"/><circle cx="76" cy="28" r="5" fill="#F4B6B0"/><ellipse cx="50" cy="58" rx="40" ry="34" fill="#F0C48A"/><ellipse cx="50" cy="68" rx="28" ry="22" fill="#FFF1DC"/><circle cx="22" cy="68" r="9" fill="#F7B6A3" opacity=".6"/><circle cx="78" cy="68" r="9" fill="#F7B6A3" opacity=".6"/>' + E(36, 54, 5.5, 6.5, '#1B1208') + E(64, 54, 5.5, 6.5, '#1B1208') + '<circle cx="37.6" cy="52" r="1.8" fill="#fff"/><circle cx="65.6" cy="52" r="1.8" fill="#fff"/><ellipse cx="50" cy="64" rx="4" ry="3" fill="#E58C8C"/><rect x="46" y="68" width="8" height="8" rx="2" fill="#fff" stroke="#E5D3B5"/><polygon points="38,24 42,12 50,19 58,12 62,24" fill="#FFC933" stroke="#B7791F" stroke-width="1.5" stroke-linejoin="round"/>',
  ai: '<circle cx="50" cy="50" r="42" stroke="var(--accent)" stroke-width="2" stroke-dasharray="6 5" opacity=".8"/><circle cx="50" cy="50" r="33" stroke="#E7B94A" stroke-width="3" stroke-dasharray="40 20 10 20"/><circle cx="50" cy="50" r="22" fill="#0A1622" stroke="var(--accent)" stroke-width="2"/>' + E(50, 50, 13, 5, 'var(--accent)') + '<circle cx="50" cy="50" r="2.6" fill="#031318"/><path d="M50 3v7M50 90v7M3 50h7M90 50h7" stroke="#E7B94A" stroke-width="2.5" stroke-linecap="round"/>',
  robot: '<defs><linearGradient id="rbS" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D5DBE2"/><stop offset="1" stop-color="#8E98A3"/></linearGradient></defs><line x1="50" y1="7" x2="50" y2="19" stroke="#9AA3AD" stroke-width="3" stroke-linecap="round"/><circle cx="50" cy="6" r="5" fill="#E5262B"/><circle cx="48.5" cy="4.5" r="1.5" fill="#fff" opacity=".7"/><rect x="5" y="40" width="11" height="28" rx="5" fill="#5F6872"/><rect x="84" y="40" width="11" height="28" rx="5" fill="#5F6872"/><circle cx="10.5" cy="48" r="2.5" fill="#E5262B"/><circle cx="89.5" cy="48" r="2.5" fill="#E5262B"/><rect x="40" y="76" width="20" height="12" rx="3" fill="#5F6872"/><path d="M14 100C14 91 26 87 50 87S86 91 86 100Z" fill="#E8EBEF"/><rect x="24" y="94" width="52" height="4" rx="2" fill="#E5262B"/><rect x="16" y="18" width="68" height="60" rx="14" fill="url(#rbS)"/><rect x="21" y="22" width="58" height="5" rx="2.5" fill="#E5262B"/><rect x="22" y="32" width="56" height="42" rx="10" fill="#1B1D21"/><circle cx="50" cy="50" r="14" fill="#101215" stroke="#E5262B" stroke-width="3"/><circle class="eye" cx="50" cy="50" r="8" fill="#E5262B"/><circle cx="54" cy="46" r="2.5" fill="#fff"/><path d="M36 67h28M39 70h22" stroke="#F2F2F2" stroke-width="1.6" stroke-linecap="round" opacity=".7"/><circle cx="26" cy="27" r="1.8" fill="#6B747E"/><circle cx="74" cy="27" r="1.8" fill="#6B747E"/>',
  detective: '<circle cx="50" cy="60" r="28" fill="#F2C9A5"/><path d="M22 46C22 26 36 16 50 16C64 16 78 26 78 46Z" fill="#2B3A67"/><ellipse cx="50" cy="46" rx="34" ry="6" fill="#1B2547"/><rect x="23" y="38" width="54" height="5" fill="#C8D3E6"/><path d="M33 52l11-3M67 52l-11-3" stroke="#1B2547" stroke-width="2.5" stroke-linecap="round"/>' + E(40, 58, 3.6, 4.6, '#1B2547') + E(60, 58, 3.6, 4.6, '#1B2547') + '<path d="M50 60v8h-3" stroke="#D99F78" stroke-width="2.5" stroke-linecap="round"/><path d="M38 72q6-4 12 0q6-4 12 0q-6 8-12 4q-6 4-12-4z" fill="#3A2A1F"/><circle cx="76" cy="76" r="12" fill="#C8D3E6" fill-opacity=".25" stroke="#C8D3E6" stroke-width="4"/><line x1="85" y1="85" x2="95" y2="95" stroke="#C8D3E6" stroke-width="5" stroke-linecap="round"/>',
  scientist: '<path d="M18 48L8 30L24 34L22 14L38 28L50 8L62 28L78 14L76 34L92 30L82 48Z" fill="#E8F7FF"/><circle cx="50" cy="60" r="28" fill="#F5CFA8"/><path d="M14 54L28 56M86 54L72 56" stroke="#2A2A35" stroke-width="4" stroke-linecap="round"/><circle cx="37" cy="56" r="10" fill="#7CFF3E" fill-opacity=".85" stroke="#2A2A35" stroke-width="4"/><circle cx="63" cy="56" r="10" fill="#7CFF3E" fill-opacity=".85" stroke="#2A2A35" stroke-width="4"/><path d="M47 56h6" stroke="#2A2A35" stroke-width="4"/>' + '<circle class="eye" cx="37" cy="56" r="3.4" fill="#10200A"/><circle class="eye" cx="63" cy="56" r="3.4" fill="#10200A"/><path d="M34 72q16 16 32 0z" fill="#3A1A1A"/><path d="M36 72h28" stroke="#fff" stroke-width="3"/>',
  raven: '<path d="M32 26L28 8L44 20ZM48 20L50 3L56 20ZM66 26L72 10L62 22Z" fill="#16161A"/><circle cx="50" cy="52" r="32" fill="#16161A"/><polygon points="50,56 36,66 50,88 64,66" fill="#3B3B46"/><polygon points="50,56 44,64 50,72" fill="#55556A"/><circle cx="34" cy="46" r="8" fill="#0B0B0E" stroke="#A78BFA" stroke-width="3"/><circle cx="66" cy="46" r="8" fill="#0B0B0E" stroke="#A78BFA" stroke-width="3"/><circle class="eye" cx="34" cy="46" r="3.5" fill="#A78BFA"/><circle class="eye" cx="66" cy="46" r="3.5" fill="#A78BFA"/><path d="M84 12a10 10 0 1 0 6 16a8 8 0 0 1-6-16z" fill="#E9E1FF"/>',
  ninja: '<circle cx="50" cy="52" r="34" fill="#1F1717"/><rect x="22" y="42" width="56" height="22" rx="11" fill="#F2C9A5"/><rect x="16" y="30" width="68" height="9" rx="4" fill="#FF3D4D"/><polygon points="84,32 98,26 94,37 100,46 86,40" fill="#FF3D4D"/>' + E(38, 53, 4.6, 5.6, '#1F1717') + E(62, 53, 4.6, 5.6, '#1F1717') + '<circle cx="39.6" cy="51" r="1.5" fill="#fff"/><circle cx="63.6" cy="51" r="1.5" fill="#fff"/><path d="M29 46l14 4M71 46l-14 4" stroke="#1F1717" stroke-width="3" stroke-linecap="round"/>',
  astro: '<line x1="50" y1="16" x2="50" y2="7" stroke="#C9CCD6" stroke-width="3"/><circle cx="50" cy="5" r="4" fill="#FF8A3D"/><circle cx="50" cy="52" r="36" fill="#F3F4F8" stroke="#C9CCD6" stroke-width="3"/><rect x="22" y="36" width="56" height="34" rx="17" fill="#141A33"/><path d="M30 44q8-6 18-6" stroke="#fff" stroke-opacity=".5" stroke-width="3" stroke-linecap="round"/>' + E(40, 54, 4, 5, '#7DD3FC') + E(60, 54, 4, 5, '#7DD3FC') + '<path d="M43 62q7 6 14 0" stroke="#7DD3FC" stroke-width="2.5" stroke-linecap="round"/><path d="M26 84q24 12 48 0" stroke="#FF8A3D" stroke-width="7" stroke-linecap="round"/>'
};
const art = (id) => '<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">' + (ART[id] || ART.fox) + '</svg>';
const cur = () => { const c = CH.find((x) => x.id === cfg.char) || CH[0]; return c.free || pro() ? c : CH[0]; };
const rgbStr = (h) => parseInt(h.slice(1, 3), 16) + ',' + parseInt(h.slice(3, 5), 16) + ',' + parseInt(h.slice(5, 7), 16);
function applyChar() {
  const c = cur(), b = document.body.style, light = cfg.theme === 'light', a = light ? c.al : c.a;
  b.setProperty('--accent', a); b.setProperty('--accent-text', light ? '#fff' : c.on); b.setProperty('--ar', rgbStr(a));
  b.setProperty('--accent-dim', 'rgba(' + rgbStr(a) + ',.14)'); b.setProperty('--accent-glow', 'rgba(' + rgbStr(a) + ',' + (light ? .25 : .35) + ')');
  ['--bg', '--surface', '--surface-elevated'].forEach((v, i) => { if (light) b.removeProperty(v); else b.setProperty(v, [c.bg, c.s, c.e][i]); });
  $('foxyArt').innerHTML = art(c.id);
}
function renderChars() {
  const g = $('charsGrid'); g.innerHTML = '';
  CH.forEach((c) => {
    const lk = !c.free && !pro(), e = document.createElement('div');
    e.className = 'char-item' + (cur().id === c.id ? ' selected' : '');
    e.innerHTML = '<div class="art">' + art(c.id) + '</div><b>' + L(c.n[0], c.n[1]) + '</b><span>' + L(c.t[0], c.t[1]) + '</span>' + (lk ? '<i class="lk">' + ic('lock', 14, 2.6) + '</i>' : '');
    e.onclick = () => { haptic('light'); if (lk) return openModal(); cfg.char = c.id; saveCfg(); applyChar(); renderChars(); renderFoxy(); say('hi'); };
    g.appendChild(e);
  });
}
function say(kind, voice) {
  const p = cur()[cfg.ui === 'en' ? 'en' : 'ru'], idx = { hi: [0], ok: [1, 2], bad: [3, 4], up: [5] }[kind];
  const t = p[idx[Math.floor(Math.random() * idx.length)]]; $('foxyText').textContent = t; if (voice) talk(t);
}
const IDLE = {
  fox: [['Как дела? Давай ещё одну карточку.', 'Я тут, если что, спрашивай.'], ['How is it going? One more card?', 'I am here if you need me.']],
  cat: [['Мур. Я не просто так сижу на твоём экране.', 'У меня лапки, но я всё равно умный.'], ['Purr. I am not sitting on your screen for nothing.', 'I have paws, but I am still smart.']],
  capy: [['Всё хорошо. Просто будь здесь.', 'Слова как вода: не торопи их.'], ['All is well. Just be here.', 'Words are like water: do not rush them.']],
  shiba: [['Так учиться. Очень прогресс.', 'Много карточки. Мало страха.'], ['So learning. Very progress.', 'Many cards. Little fear.']],
  hamster: [['Тапай карточки, собирай комбо.', 'Ежедневное комбо само себя не соберёт.'], ['Tap cards, build combos.', 'The daily combo will not build itself.']],
  ai: [['[СТАТУС] Все системы в норме. Жду команды.', '[СОВЕТ] Регулярность важнее скорости.'], ['[STATUS] All systems nominal. Awaiting input.', '[TIP] Consistency beats speed.']],
  robot: [['Товарищ, график обучения не ждёт.', 'Знание — лучший инструмент.'], ['Comrade, the study schedule waits for no one.', 'Knowledge is the best tool.']],
  detective: [['Любое слово — улика. Собирай их.', 'Наблюдательность — половина успеха.'], ['Every word is a clue. Collect them.', 'Observation is half the success.']],
  scientist: [['Гипотеза: ты выучишь ещё пять слов!', 'Тише, мозг в процессе реакции.'], ['Hypothesis: you will learn five more words!', 'Quiet, the brain is mid-reaction.']],
  raven: [['Тишина. И только слова.', 'Каждое слово — перо в ночи.'], ['Silence. And only words.', 'Every word is a feather in the night.']],
  ninja: [['Тренировка — путь. Ещё карточку?', 'Быстро, чётко, без лишнего.'], ['Practice is the way. One more card?', 'Quick, clean, no extra.']],
  astro: [['Центр, у меня всё стабильно. Дальше?', 'Орбита зависит от ежедневных манёвров.'], ['Control, all stable here. Next?', 'Orbit depends on daily maneuvers.']]
};
function idleTalk() { const a = (IDLE[cur().id] || IDLE.fox)[cfg.ui === 'en' ? 1 : 0], t = a[Math.floor(Math.random() * a.length)]; $('foxyText').textContent = t; talk(t); haptic('light'); }
const DEMO_CARDS = {
  en: [['hello', 'привет', 'Hello, how are you?'], ['remember', 'помнить', 'I remember this song.'], ['travel', 'путешествовать', 'I love to travel by train.']],
  es: [['hola', 'привет', 'Hola, ¿cómo estás?'], ['gracias', 'спасибо', 'Muchas gracias.'], ['agua', 'вода', 'Quiero un vaso de agua.']],
  de: [['hallo', 'привет', "Hallo, wie geht's?"], ['danke', 'спасибо', 'Danke für deine Hilfe.'], ['das Wasser', 'вода', 'Ich möchte Wasser.']],
  fr: [['bonjour', 'здравствуйте', 'Bonjour, ça va ?'], ['merci', 'спасибо', 'Merci pour ton aide.'], ["l'eau", 'вода', "Je voudrais de l'eau."]],
  it: [['ciao', 'привет', 'Ciao, come stai?'], ['grazie', 'спасибо', 'Grazie mille.'], ['acqua', 'вода', "Vorrei un bicchiere d'acqua."]],
  pt: [['olá', 'привет', 'Olá, como você está?'], ['obrigado', 'спасибо', 'Muito obrigado.'], ['água', 'вода', 'Quero um copo de água.']],
  tr: [['merhaba', 'привет', 'Merhaba, nasılsın?'], ['teşekkürler', 'спасибо', 'Çok teşekkürler.'], ['su', 'вода', 'Bir bardak su istiyorum.']],
  zh: [['你好 (nǐ hǎo)', 'привет', '你好，你好吗？'], ['谢谢 (xièxie)', 'спасибо', '谢谢你的帮助。'], ['水 (shuǐ)', 'вода', '我想喝水。']],
  ja: [['こんにちは (konnichiwa)', 'здравствуйте', 'こんにちは、お元気ですか？'], ['ありがとう (arigatou)', 'спасибо', 'ありがとう。'], ['水 (mizu)', 'вода', '水をください。']]
};

/* ---------- i18n for static text ---------- */
document.querySelectorAll('[data-en]').forEach((el) => { el.dataset.ru = el.textContent; });
function applyStatic() {
  document.documentElement.lang = cfg.ui;
  document.querySelectorAll('[data-en]').forEach((el) => { el.textContent = cfg.ui === 'en' ? el.dataset.en : el.dataset.ru; });
}

/* ---------- renders ---------- */
function renderHeader() {
  $('streakPill').innerHTML = ic('flame', 16) + '<span>' + streakNow() + '</span>';
  const b = $('proBadge'); b.innerHTML = ic('zap', 14) + 'PRO'; b.classList.toggle('is-pro', pro());
}
function renderLangChips() {
  const w = $('langScroll'); w.innerHTML = '';
  LANGS.forEach(([code, ru, en]) => {
    const b = document.createElement('button');
    b.className = 'lang-chip' + (cfg.learn === code ? ' active' : '');
    b.innerHTML = '<span class="lang-code">' + code.toUpperCase() + '</span>' + L(ru, en);
    b.onclick = () => { if (cfg.learn === code) return; cfg.learn = code; saveCfg(); haptic('light'); renderLangChips(); loadState(); };
    w.appendChild(b);
  });
}
function renderFoxy() {
  const level = Math.floor(prog.xp / 60) + 1, titles = [['Новичок', 'Newbie'], ['Ученик', 'Student'], ['Знаток', 'Pro'], ['Мастер', 'Master'], ['Гуру', 'Guru']];
  const t = titles[Math.min(titles.length - 1, level - 1)];
  $('foxyLevel').textContent = L(cur().n[0], cur().n[1]) + ' · ' + L('Ур. ', 'Lv. ') + level;
  $('foxyXp').textContent = prog.xp + ' XP';
  $('xpFill').style.width = Math.max(4, (prog.xp % 60) / 60 * 100) + '%';
}
function renderDots() {
  const w = $('sessionDots'); w.innerHTML = '';
  const n = Math.min(total0, 12), d = total0 ? Math.round(answered / total0 * n) : 0;
  for (let i = 0; i < n; i++) { const x = document.createElement('div'); x.className = 's-dot' + (i < d ? ' done' : i === d && !done ? ' current' : ''); w.appendChild(x); }
  $('sessionLabel').textContent = total0 ? L('Сессия · ', 'Session · ') + Math.min(answered + 1, total0) + ' / ' + total0 : L('Сессия', 'Session');
}
function renderCard() {
  const c = queue[0]; if (!c) return;
  $('frontWord').textContent = c.en; $('backWord').textContent = c.ru;
  $('frontLevel').textContent = $('backLevel').textContent = cfg.learn.toUpperCase();
  const base = c.en.split(' (')[0], tg_ = $('frontTag');
  tg_.className = 'card-tag' + (c.tag === 'slang' ? ' slang' : ''); tg_.textContent = c.tag === 'slang' ? L('СЛЕНГ', 'SLANG') : c.tag === 'phrase' ? L('фраза', 'phrase') : L('слово', 'word');
  const note = c.tag === 'slang' ? '<span class="slang-note">' + L('Неформально, в разговоре с друзьями', 'Informal, among friends') + '</span>' : '';
  $('backExample').innerHTML = note + (c.ex ? hl(c.ex, base) : '');
  $('backExample').parentNode.style.display = c.ex || note ? '' : 'none';
}
const PACK_N = { base: ['Базовый старт', 'Basics'], mind: ['Ум и память', 'Mind & memory'], career: ['Карьера и цели', 'Career & goals'], food: ['Еда и кафе', 'Food & cafe'], travel: ['Путешествия', 'Travel'], people: ['Люди и чувства', 'People & feelings'], phrases: ['Фразы', 'Phrases'], slang: ['Сленг', 'Slang'] };
function renderDecks() {
  const w = $('decksList'); w.innerHTML = '';
  (S.packs || []).forEach((p, i) => {
    const locked = p.locked && !pro(), nm = PACK_N[p.k] || [p.k, p.k];
    const badge = locked ? '<span class="deck-badge pro">' + ic('lock', 11, 2.6) + 'PRO</span>' : '<span class="deck-badge' + (p.k === 'slang' ? ' sl' : '') + '">' + (p.k === 'slang' ? L('СЛЕНГ', 'SLANG') : L('ОТКРЫТ', 'OPEN')) + '</span>';
    const el = document.createElement('div'); el.className = 'deck-item' + (i === 0 ? ' active-deck' : '');
    el.innerHTML = '<div class="deck-head"><div class="deck-name">' + L(nm[0], nm[1]) + badge + '</div></div><div class="deck-words' + (locked ? ' blurred' : '') + '">' + esc(p.sample) + '</div><div class="deck-meta">' + (locked ? L('НАЖМИ, ЧТОБЫ ОТКРЫТЬ', 'TAP TO UNLOCK') : p.n + L(' СЛОВ', ' WORDS')) + '</div>';
    el.onclick = () => { if (locked) openModal(); else haptic('light'); };
    w.appendChild(el);
  });
}
function renderProgress() {
  const pct = Math.min(1, todayN() / cfg.goal), c = 2 * Math.PI * 52, ring = $('ringProgress');
  ring.setAttribute('stroke-dasharray', c.toFixed(1)); ring.setAttribute('stroke-dashoffset', (c * (1 - pct)).toFixed(1));
  $('ringNum').textContent = Math.round(pct * 100) + '%';
  $('statStreak').textContent = streakNow(); $('statToday').textContent = todayN(); $('statTotal').textContent = prog.total;
  $('learnedLine').textContent = L('Выучено слов: ', 'Words learned: ') + S.learned + ' / ' + S.total;
  const list = [['flag', 'Первый шаг', 'First step', prog.total > 0], ['flame', '3 дня подряд', '3-day streak', streakNow() >= 3], ['target', 'Цель дня', 'Daily goal', todayN() >= cfg.goal], ['zap', '50 повторов', '50 reviews', prog.total >= 50], ['award', '100 повторов', '100 reviews', prog.total >= 100], ['crown', 'Клуб PRO', 'PRO club', pro()]];
  const g = $('achGrid'); g.innerHTML = '';
  list.forEach(([i, ru, en, ok]) => { const e = document.createElement('div'); e.className = 'ach-item' + (ok ? ' unlocked' : ''); e.innerHTML = '<div class="ach-icon">' + ic(ok ? i : 'lock', 24) + '</div><div class="ach-name">' + L(ru, en) + '</div>'; g.appendChild(e); });
}
function renderProButtons() {
  const price = (S.price || 100) + ' Stars';
  $('payBtn').innerHTML = ic('zap', 18) + L('Открыть за ', 'Get for ') + price;
  $('settingsProBtn').innerHTML = ic('zap', 18) + L('Открыть PRO за ', 'Get PRO for ') + price;
  $('settingsProCard').style.display = pro() ? 'none' : 'block';
  const perks = [['book', 'Все наборы слов и новые уроки', 'All word sets and new lessons'], ['flame', 'Заморозка серии: пропусти день без потерь', 'Streak freeze: skip a day, keep your streak'], ['swatch', 'Все персонажи-компаньоны', 'All companion characters']];
  $('perksList').innerHTML = perks.map(([i, ru, en]) => '<div class="perk-item"><div class="perk-icon">' + ic(i, 16) + '</div>' + L(ru, en) + '</div>').join('');
}
function syncSegs() {
  document.querySelectorAll('.segmented').forEach((seg) => { const k = seg.dataset.seg; seg.querySelectorAll('.seg-btn').forEach((b) => b.classList.toggle('active', String(cfg[k]) === b.dataset.val)); });
  $('switchSound').classList.toggle('on', cfg.sound); $('switchHaptics').classList.toggle('on', cfg.haptics); $('switchCv').classList.toggle('on', cfg.cv);
}
function renderAll() { applyStatic(); renderHeader(); renderLangChips(); renderFoxy(); renderDots(); renderDecks(); renderProgress(); renderPlan(); renderRules(); renderRewards(); renderChars(); applyChar(); renderProButtons(); syncSegs(); if (queue[0]) renderCard(); if (done) showDone(); }

/* ---------- session ---------- */
async function loadState() {
  try {
    if (DEMO) S = { premium: false, learned: 4, total: 12, locked: 8, price: 100, cards: (DEMO_CARDS[cfg.learn] || []).map((w, id) => ({ id, en: w[0], ru: w[1], ex: w[2] })) };
    else S = await api('state?lang=' + cfg.learn);
    if (DEMO) demoExtra();
  } catch (e) { toast(L('Не удалось загрузить данные', 'Could not load data')); S.cards = []; }
  $('proBadge').classList.toggle('is-pro', pro());
  loadRewards();
  startSession();
}
function startSession() {
  queue = S.cards.slice(); total0 = queue.length; answered = 0; gain = 0; done = false; busy = false;
  $('deckWrapper').classList.remove('done'); $('ratingGrid').style.opacity = 1;
  resetCard(); renderAll(); say('hi');
  if (!queue.length) { done = true; showDone(); }
}
function showDone() {
  $('deckWrapper').classList.add('done'); $('ratingGrid').style.opacity = .35;
  $('doneTitle').textContent = total0 ? L('Сессия завершена!', 'Session complete!') : L('На сегодня всё', 'All done for today');
  $('doneSub').textContent = total0 ? '+' + gain + ' XP · ' + total0 + L(' карточек', ' cards') : L('Новые карточки появятся позже', 'New cards will appear later');
}
function resetCard() {
  const c = $('flashcard');
  c.classList.add('swiping'); c.classList.remove('flipped', 'flying'); c.style.opacity = '1';
  ['--tx', '--ty'].forEach((p) => c.style.setProperty(p, '0px')); c.style.setProperty('--rot', '0deg');
  flipped = false; void c.offsetWidth; c.classList.remove('swiping'); updateBadges(0);
}
function toggleFlip() {
  flipped = !flipped; $('flashcard').classList.toggle('flipped', flipped); haptic('light');
  if (flipped && queue[0]) setTimeout(() => speakWord(queue[0]), 220);
}
function updateBadges(dx) {
  $('badgeKnow').style.opacity = dx > 45 ? Math.min(1, (dx - 45) / 60) : 0;
  $('badgeAgain').style.opacity = dx < -45 ? Math.min(1, (-dx - 45) / 60) : 0;
}
function flyOut(dir) {
  const c = $('flashcard'); busy = true; c.classList.add('flying');
  c.style.setProperty('--tx', dir * 460 + 'px'); c.style.setProperty('--rot', dir * 20 + 'deg'); c.style.opacity = '0';
  setTimeout(() => { busy = false; rate(dir > 0 ? 'good' : 'again'); }, 290);
}
function bump(g) {
  const T = day(), Y = day(Date.now() - 864e5);
  if (prog.day !== T) { prog.day = T; prog.today = 0; }
  if (prog.last !== T) { prog.streak = (prog.last === Y || (pro() && prog.last === day(Date.now() - 2 * 864e5))) ? prog.streak + 1 : 1; prog.last = T; }
  prog.today++; prog.total++; prog.xp += g; saveProg();
}
function rate(type) {
  if (done || busy || !queue[0]) return;
  const w = queue.shift(), q = { again: 1, hard: 3, good: 4, easy: 5 }[type], g = { again: 0, hard: 1, good: 2, easy: 3 }[type];
  const lv0 = Math.floor(prog.xp / 60);
  haptic(q >= 4 ? 'success' : q === 1 ? 'warning' : 'medium');
  if (!DEMO) api('review', { word_id: w.id, quality: q, lang: cfg.learn }).catch(() => {});
  bump(g); gain += g;
  if (q === 1) queue.push(w); else answered++;
  const up = Math.floor(prog.xp / 60) > lv0;
  renderFoxy(); renderHeader(); renderProgress(); say(up ? 'up' : q >= 3 ? 'ok' : 'bad', up);
  if (planPending !== null && (answered >= 5 || !queue.length)) { completeDay(planPending); planPending = null; }
  if (up || todayN() === cfg.goal) { confetti(); haptic('success'); }
  if (!queue.length) { done = true; resetCard(); renderDots(); showDone(); confetti(); say('ok', true); return; }
  resetCard(); renderCard(); renderDots();
}

/* ---------- views, modal, pay ---------- */
function setView(v) {
  current = v; document.querySelectorAll('.view').forEach((x) => x.classList.remove('active')); $('view-' + v).classList.add('active');
  document.querySelectorAll('.tab-btn').forEach((b) => b.classList.toggle('active', b.dataset.view === v));
  $('langScroll').style.display = ['learn', 'plan', 'rules'].includes(v) ? 'flex' : 'none';
  if (v === 'progress') { renderProgress(); renderRewards(); }
  if (v === 'plan') renderPlan();
  if (v === 'rules') renderRules();
  haptic('light'); window.scrollTo({ top: 0, behavior: 'smooth' });
}
function openModal() { renderProButtons(); $('proModal').classList.add('open'); haptic('medium'); }
function closeModal() { $('proModal').classList.remove('open'); }
async function pay() {
  if (DEMO) { toast(L('Оплата работает только внутри Telegram', 'Payment works inside Telegram only')); return; }
  try {
    const r = await api('invoice', {});
    tg.openInvoice(r.link, (st) => { if (st === 'paid') { closeModal(); toast(L('PRO активируется...', 'Activating PRO...')); setTimeout(loadState, 1500); } });
  } catch (e) { toast(L('Не удалось создать счёт', 'Could not create the invoice')); }
}
function confetti() {
  const cv = $('confettiCanvas'), ctx = cv.getContext('2d'); cv.width = innerWidth; cv.height = innerHeight;
  const cols = ['#C8FF00', '#00E676', '#38BDF8', '#FFB703', '#FF4D6D', '#A78BFA'], ps = [];
  for (let i = 0; i < 130; i++) ps.push({ x: Math.random() * cv.width, y: -20 - Math.random() * cv.height * .4, vx: (Math.random() - .5) * 3.5, vy: 2 + Math.random() * 4.5, s: 3 + Math.random() * 6, c: cols[i % cols.length], a: Math.random() * Math.PI, sp: (Math.random() - .5) * .22 });
  let f = 0;
  (function loop() {
    f++; ctx.clearRect(0, 0, cv.width, cv.height);
    ps.forEach((p) => { p.x += p.vx; p.y += p.vy; p.vy += .055; p.a += p.sp; ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.a); ctx.globalAlpha = Math.max(0, 1 - f / 170); ctx.fillStyle = p.c; ctx.fillRect(-p.s / 2, -p.s / 2, p.s, p.s * 1.7); ctx.restore(); });
    if (f < 175) requestAnimationFrame(loop); else ctx.clearRect(0, 0, cv.width, cv.height);
  })();
}

/* ---------- card gestures ---------- */
(function () {
  const card = $('flashcard'); let drag = null;
  card.addEventListener('pointerdown', (e) => { if (busy || done || e.target.closest('.icon-btn')) return; drag = { x: e.clientX, y: e.clientY, moved: false }; card.classList.add('swiping'); try { card.setPointerCapture(e.pointerId); } catch (x) {} });
  card.addEventListener('pointermove', (e) => {
    if (!drag) return; const dx = e.clientX - drag.x, dy = e.clientY - drag.y; if (Math.abs(dx) > 6) drag.moved = true;
    card.style.setProperty('--tx', dx + 'px'); card.style.setProperty('--ty', dy * .22 + 'px'); card.style.setProperty('--rot', dx * .06 + 'deg'); updateBadges(dx);
  });
  card.addEventListener('pointerup', (e) => {
    if (!drag) return; const dx = e.clientX - drag.x, moved = drag.moved; drag = null; card.classList.remove('swiping');
    if (Math.abs(dx) > 90) flyOut(Math.sign(dx));
    else { card.style.setProperty('--tx', '0px'); card.style.setProperty('--ty', '0px'); card.style.setProperty('--rot', '0deg'); updateBadges(0); if (!moved) toggleFlip(); }
  });
  card.addEventListener('pointercancel', () => { if (!drag) return; drag = null; card.classList.remove('swiping'); card.style.setProperty('--tx', '0px'); card.style.setProperty('--ty', '0px'); card.style.setProperty('--rot', '0deg'); updateBadges(0); });
  const sp = (e) => { e.stopPropagation(); if (queue[0]) speakWord(queue[0]); haptic('light'); };
  $('speakBtn').addEventListener('click', sp); $('speakBtnBack').addEventListener('click', sp);
})();

/* ---------- study path, lessons, rules, rewards, teacher ---------- */
const norm = (s) => String(s).toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const sample = (a, n) => shuffle(a).slice(0, n);
const esc2 = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const lev = (a, b) => { const m = a.length, n = b.length, d = Array.from({ length: m + 1 }, (_, i) => [i]); for (let j = 1; j <= n; j++) d[0][j] = j; for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); return d[m][n]; };
const near = (a, b) => { a = norm(a); b = norm(b); return a === b || a.includes(b) || lev(a, b) <= Math.floor(b.length / 4); };
const pool = () => S.pool || [];
const seenPool = () => { const p = pool().filter((w) => w.seen && w.tag !== 'slang'); return p.length >= 4 ? p : pool(); };
const distract = (w, key, n) => sample(pool().filter((x) => x.id !== w.id && x[key] !== w[key]), n).map((x) => key === 'ru' ? x.ru : base(x.en));
function bumpXP(n) { prog.xp += n; saveProg(); renderFoxy(); }
function saveSentence(w) { const k = 'ss_book_' + cfg.learn, a = LS.get(k, []); if (!a.some((x) => x.s === w.ex)) { a.unshift({ s: w.ex, ru: w.ru }); LS.set(k, a.slice(0, 50)); } }
function listenOnce(lang, cb) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  try { const r = new SR(); r.lang = lang; r.interimResults = false; r.maxAlternatives = 3; r.onresult = (e) => cb(Array.from(e.results[0]).map((x) => x.transcript)); r.onerror = () => cb(null); r.onnomatch = () => cb(null); r.start(); } catch (e) { cb(null); }
}

function mkListen(n) { return sample(seenPool(), n).map((w) => { const opts = shuffle([w.ru].concat(distract(w, 'ru', 3))); return { t: 'choice', prompt: L('Что ты слышишь?', 'What do you hear?'), audio: { t: base(w.en), l: SPEECH[cfg.learn] }, opts, a: opts.indexOf(w.ru), show: base(w.en) }; }); }
function mkGap(n) {
  const re = (w) => new RegExp(esc2(base(w.en)), 'i');
  return sample(seenPool().filter((w) => w.ex && base(w.en).length > 1 && re(w).test(w.ex)), n).map((w) => { const b = base(w.en), opts = shuffle([b].concat(distract(w, 'en', 3))); return { t: 'choice', prompt: L('Вставь пропущенное слово', 'Fill in the missing word'), sub: w.ex.replace(re(w), '____'), hint: w.ru, opts, a: opts.indexOf(b) }; });
}
function mkSlang(n) { return sample(pool().filter((w) => w.tag === 'slang'), n).map((w) => { const opts = shuffle([w.ru].concat(distract(w, 'ru', 3))); return { t: 'choice', prompt: L('Что значит это слово?', 'What does this word mean?'), big: base(w.en), sub: w.ex, audio: { t: base(w.en), l: SPEECH[cfg.learn] }, opts, a: opts.indexOf(w.ru), note: L('Сленг: неформально, в разговоре с друзьями', 'Slang: informal, among friends') }; }); }
function mkBuild(n) {
  if (/^(zh|ja)$/.test(cfg.learn)) return mkGap(n);
  return sample(seenPool().filter((w) => w.ex && w.ex.split(' ').length >= 3), n).map((w) => ({ t: 'build', w, tokens: shuffle(w.ex.split(' ').map((x, i) => ({ x, i }))) }));
}
function mkSpeak(n) { return sample(seenPool(), n).map((w) => ({ t: 'speak', w })); }
function mkRule() { const rl = (S.rules || []).filter((r) => r.unlocked), read = LS.get('ss_read_' + cfg.learn, []), r = rl.find((x) => !read.includes(x.id)) || rl[rl.length - 1]; return r ? [{ t: 'rule', r }].concat(mkGap(3)) : []; }
function makeItems(k) {
  if (k === 'build') return mkBuild(5); if (k === 'speak') return mkSpeak(5); if (k === 'listen') return mkListen(6);
  if (k === 'rule') return mkRule(); if (k === 'slang') return mkSlang(5);
  if (k === 'test') return mkListen(3).concat(mkGap(3), mkSlang(2));
  return [];
}

const PLAN = [
  { k: 'cards', i: 'book', t: ['Карточки', 'Cards'], d: ['Новые слова и повторение', 'New words and review'] },
  { k: 'build', i: 'layers', t: ['Предложения', 'Sentences'], d: ['Собери предложения из изученных слов', 'Build sentences from learned words'] },
  { k: 'speak', i: 'mic', t: ['Произношение', 'Speaking'], d: ['Произнеси слова вслух', 'Say the words aloud'] },
  { k: 'listen', i: 'headphones', t: ['Аудирование', 'Listening'], d: ['Слушай и выбирай перевод', 'Listen and pick the translation'] },
  { k: 'rule', i: 'bookmark', t: ['Правило дня', 'Rule of the day'], d: ['Новое правило и закрепление', 'A new rule and practice'] },
  { k: 'slang', i: 'chat', t: ['Сленг', 'Slang'], d: ['Живая разговорная речь', 'Everyday spoken language'] },
  { k: 'test', i: 'award', t: ['Итоговый тест', 'Final test'], d: ['Смешанный тест недели', 'Mixed weekly test'] }
];
let planPending = null;
const planKey = () => 'ss_plan_' + cfg.learn;
const planState = () => Object.assign({ week: 1, done: [0, 0, 0, 0, 0, 0, 0] }, LS.get(planKey(), {}));
function completeDay(i) {
  const p = planState(); if (!p.done[i]) { p.done[i] = 1; LS.set(planKey(), p); bumpXP(20); }
  renderPlan(); confetti(); haptic('success'); toast(L('День плана выполнен! +20 XP', 'Plan day complete! +20 XP'));
}
function renderPlan() {
  const v = $('view-plan'); if (!v) return;
  const p = planState(), next = p.done.indexOf(0), cnt = p.done.filter(Boolean).length;
  let h = '<div class="plan-top"><h2>' + L('План на неделю', 'Weekly plan') + '</h2><span class="cap">' + L('Неделя ', 'Week ') + p.week + ' · ' + cnt + '/7</span></div><div class="xp-bar" style="margin-bottom:14px"><div class="xp-fill" style="width:' + cnt / 7 * 100 + '%"></div></div>';
  PLAN.forEach((d, i) => {
    const done = p.done[i], lk = !done && next >= 0 && i > next;
    h += '<div class="day ' + (done ? 'done ' : '') + (i === next ? 'now ' : '') + (lk ? 'lockd' : '') + '" data-d="' + i + '"><div class="day-ic">' + ic(done ? 'check' : lk ? 'lock' : d.i, 22, 2.4) + '</div><div><b>' + L('День ', 'Day ') + (i + 1) + ' · ' + L(d.t[0], d.t[1]) + '</b><span>' + L(d.d[0], d.d[1]) + '</span></div><small>' + (done ? L('ГОТОВО', 'DONE') : i === next ? L('СЕГОДНЯ', 'TODAY') : '') + '</small></div>';
  });
  if (next < 0) h += '<button class="cta-pay" id="newWeek" style="margin-top:6px">' + L('Начать новую неделю', 'Start a new week') + '</button>';
  v.innerHTML = h;
  v.querySelectorAll('.day').forEach((e) => e.onclick = () => { if (e.classList.contains('lockd')) return toast(L('Сначала заверши предыдущий день', 'Finish the previous day first')); startDay(+e.dataset.d); });
  const nw = $('newWeek'); if (nw) nw.onclick = () => { LS.set(planKey(), { week: p.week + 1, done: [0, 0, 0, 0, 0, 0, 0] }); renderPlan(); haptic('medium'); };
}
function startDay(i) {
  const k = PLAN[i].k; haptic('light');
  if (k === 'cards') { planPending = i; setView('learn'); toast(L('Пройди сессию карточек, и день засчитается', 'Finish a card session to complete the day')); return; }
  const items = makeItems(k);
  if (!items.length) return toast(L('Пока мало слов. Сначала пройди карточки', 'Not enough words yet. Do cards first'));
  openLesson(k, items, () => completeDay(i));
}

let LQ = null;
function openLesson(kind, items, onDone) { LQ = { kind, items, i: 0, ok: 0, onDone, sel: [], st: 0 }; $('lesson').classList.add('open'); renderLesson(); }
function closeLesson() { $('lesson').classList.remove('open'); LQ = null; spkId++; try { speechSynthesis.cancel(); } catch (e) {} }
function lqFoot(ok, msg) {
  LQ.st = 1;
  $('lqFoot').innerHTML = '<div class="fb ' + (ok ? 'good' : 'miss') + '"><b>' + (ok ? L('Верно!', 'Correct!') : L('Не совсем', 'Not quite')) + '</b>' + (msg ? '<span>' + esc(msg) + '</span>' : '') + '</div><button class="cta-pay" id="lqNext">' + L('Дальше', 'Continue') + '</button>';
  $('lqNext').onclick = () => { LQ.i++; LQ.st = 0; LQ.sel = []; renderLesson(); };
}
function renderLesson() {
  const el = $('lesson'), q = LQ.items[LQ.i], n = LQ.items.length;
  const head = '<div class="lq-head"><button class="icon-btn" id="lqClose" aria-label="Close">' + ic('x', 18) + '</button><div class="xp-bar"><div class="xp-fill" style="width:' + Math.round(LQ.i / n * 100) + '%"></div></div></div>';
  if (!q) {
    const pass = LQ.ok >= Math.ceil(n / 2);
    el.innerHTML = head + '<div class="lq-body center"><div class="done-ic">' + ic(pass ? 'check' : 'flag', 28, 3) + '</div><div class="lq-prompt">' + (pass ? L('Отлично!', 'Great job!') : L('Почти получилось', 'Almost there')) + '</div><div class="lq-sub">' + LQ.ok + ' / ' + n + '</div></div><div class="lq-foot"><button class="cta-pay" id="lqDone">' + (pass ? L('Готово', 'Done') : L('Попробовать ещё раз', 'Try again')) + '</button></div>';
    $('lqClose').onclick = closeLesson;
    $('lqDone').onclick = () => { const k = LQ.kind, cb = LQ.onDone, ok = LQ.ok; if (pass) { bumpXP(ok * 2 + 5); closeLesson(); if (cb) cb(); } else openLesson(k, makeItems(k), cb); };
    if (pass) { confetti(); talk(L('Отличная работа!', 'Great job!')); }
    return;
  }
  if (q.t === 'choice') {
    el.innerHTML = head + '<div class="lq-body"><div class="lq-prompt">' + q.prompt + '</div>' + (q.big ? '<div class="lq-big">' + esc(q.big) + '</div>' : '') + (q.audio ? '<button class="lq-play" id="lqPlay">' + ic('vol', 26) + '</button>' : '') + (q.sub ? '<div class="lq-sub">' + esc(q.sub) + '</div>' : '') + (q.hint ? '<div class="lq-hint">' + esc(q.hint) + '</div>' : '') + '<div class="opts">' + q.opts.map((o, i) => '<button class="opt" data-i="' + i + '">' + esc(o) + '</button>').join('') + '</div></div><div class="lq-foot" id="lqFoot"></div>';
    if (q.audio) { const play = () => speakSeq([{ t: q.audio.t, l: q.audio.l, r: .85 }]); $('lqPlay').onclick = play; play(); }
    el.querySelectorAll('.opt').forEach((b) => b.onclick = () => {
      if (LQ.st) return; const i = +b.dataset.i, ok = i === q.a; b.classList.add(ok ? 'ok' : 'bad');
      if (!ok) el.querySelectorAll('.opt')[q.a].classList.add('ok'); if (ok) LQ.ok++;
      haptic(ok ? 'success' : 'warning'); lqFoot(ok, q.note || (q.show ? q.show + ' = ' + q.opts[q.a] : ''));
    });
  } else if (q.t === 'build') {
    const sel = LQ.sel, used = new Set(sel.map((t) => t.i));
    el.innerHTML = head + '<div class="lq-body"><div class="lq-prompt">' + L('Составь предложение', 'Build the sentence') + '</div><div class="lq-hint">' + esc(q.w.ru) + '</div><div class="slots">' + sel.map((t) => '<button class="tok" data-r="' + t.i + '">' + esc(t.x) + '</button>').join('') + '</div><div class="bank">' + q.tokens.filter((t) => !used.has(t.i)).map((t) => '<button class="tok" data-a="' + t.i + '">' + esc(t.x) + '</button>').join('') + '</div></div><div class="lq-foot" id="lqFoot"><button class="cta-pay" id="lqCheck"' + (sel.length === q.tokens.length ? '' : ' disabled') + '>' + L('Проверить', 'Check') + '</button></div>';
    el.querySelectorAll('[data-a]').forEach((b) => b.onclick = () => { if (LQ.st) return; LQ.sel.push(q.tokens.find((t) => t.i === +b.dataset.a)); haptic('light'); renderLesson(); });
    el.querySelectorAll('[data-r]').forEach((b) => b.onclick = () => { if (LQ.st) return; LQ.sel = LQ.sel.filter((t) => t.i !== +b.dataset.r); renderLesson(); });
    $('lqCheck').onclick = () => { if (LQ.st || sel.length !== q.tokens.length) return; const ok = sel.map((t) => t.x).join(' ') === q.w.ex; if (ok) { LQ.ok++; saveSentence(q.w); } haptic(ok ? 'success' : 'warning'); lqFoot(ok, ok ? L('Предложение сохранено в твоих правилах', 'Sentence saved to your rulebook') : q.w.ex); };
  } else if (q.t === 'speak') {
    const can = !!(window.SpeechRecognition || window.webkitSpeechRecognition), b = base(q.w.en);
    el.innerHTML = head + '<div class="lq-body"><div class="lq-prompt">' + L('Произнеси вслух', 'Say it aloud') + '</div><div class="lq-big">' + esc(b) + '</div><div class="lq-sub">' + esc(q.w.ru) + '</div><button class="lq-play" id="lqPlay">' + ic('vol', 26) + '</button>' + (can ? '' : '<div class="lq-hint">' + L('Распознавание речи недоступно: послушай и повтори вслух', 'Speech recognition is unavailable: listen and repeat aloud') + '</div>') + '</div><div class="lq-foot" id="lqFoot"><button class="cta-pay" id="lqGo">' + (can ? ic('mic', 18) + L('Нажми и скажи', 'Tap and speak') : L('Я повторил(а)', 'I repeated it')) + '</button></div>';
    const play = () => speakSeq([{ t: b, l: SPEECH[cfg.learn], r: .8 }]); $('lqPlay').onclick = play; play();
    $('lqGo').onclick = () => {
      if (LQ.st) return;
      if (!can) { LQ.ok++; haptic('success'); return lqFoot(true, ''); }
      $('lqGo').textContent = L('Слушаю...', 'Listening...');
      listenOnce(SPEECH[cfg.learn], (alts) => { if (LQ.st) return; const ok = !!alts && alts.some((a) => near(a, b)); if (ok) LQ.ok++; haptic(ok ? 'success' : 'warning'); lqFoot(ok, ok ? '' : (alts && alts[0] ? L('Я услышал: ', 'I heard: ') + alts[0] : L('Не расслышал, попробуй ещё раз', 'Did not catch that'))); });
    };
  } else if (q.t === 'rule') {
    el.innerHTML = head + '<div class="lq-body"><div class="cap">' + L('Правило', 'Rule') + '</div><div class="lq-prompt">' + esc(q.r.title) + '</div><div class="rule-body">' + esc(q.r.body) + '</div><div class="rule-ex" id="lqEx">' + ic('vol', 14) + esc(q.r.ex) + '</div></div><div class="lq-foot"><button class="cta-pay" id="lqOk">' + L('Понятно', 'Got it') + '</button></div>';
    $('lqEx').onclick = () => speakSeq([{ t: q.r.ex, l: SPEECH[cfg.learn], r: .85 }]);
    $('lqOk').onclick = () => { const k = 'ss_read_' + cfg.learn, a = LS.get(k, []); if (!a.includes(q.r.id)) { a.push(q.r.id); LS.set(k, a); } LQ.ok++; LQ.i++; renderLesson(); };
  }
  $('lqClose').onclick = closeLesson;
}

function renderRules() {
  const v = $('view-rules'); if (!v) return;
  const rl = S.rules || [], read = LS.get('ss_read_' + cfg.learn, []), seen = S.seen || 0, book = LS.get('ss_book_' + cfg.learn, []);
  const slang = pool().filter((w) => w.tag === 'slang' && w.seen), allSl = pool().filter((w) => w.tag === 'slang').length;
  let h = '<div class="plan-top"><h2>' + L('Сборник правил', 'Rulebook') + '</h2><span class="cap">' + rl.filter((r) => r.unlocked).length + '/' + rl.length + '</span></div>';
  rl.forEach((r) => { h += r.unlocked ? '<div class="rule-item"><b>' + esc(r.title) + (read.includes(r.id) ? '' : '<em>' + L('новое', 'new') + '</em>') + '</b><p>' + esc(r.body) + '</p><div class="rule-ex" data-say="' + esc(r.ex) + '">' + ic('vol', 14) + esc(r.ex) + '</div></div>' : '<div class="rule-item lockd"><b>' + ic('lock', 14, 2.4) + esc(r.title) + '</b><p>' + L('Откроется после ', 'Unlocks after ') + r.need + L(' изученных слов (сейчас ', ' learned words (now ') + seen + ')</p></div>'; });
  h += '<div class="section-title" style="margin-top:18px">' + L('Сленг, который ты встретил', 'Slang you have met') + '</div>';
  h += slang.length ? slang.map((w) => '<div class="rule-item"><b>' + esc(base(w.en)) + '<em>' + L('сленг', 'slang') + '</em></b><p>' + esc(w.ru) + '</p>' + (w.ex ? '<div class="rule-ex" data-say="' + esc(w.ex) + '">' + ic('vol', 14) + esc(w.ex) + '</div>' : '') + '</div>').join('') : '<div class="rule-item lockd"><p>' + L('Сленг появится в карточках с пометкой «сленг». Слов в наборе: ', 'Slang appears in cards marked “slang”. Words available: ') + allSl + '</p></div>';
  h += '<div class="section-title" style="margin-top:18px">' + L('Мои предложения', 'My sentences') + '</div>';
  h += book.length ? book.map((x) => '<div class="rule-item"><div class="rule-ex" data-say="' + esc(x.s) + '">' + ic('vol', 14) + esc(x.s) + '</div><p>' + esc(x.ru) + '</p></div>').join('') : '<div class="rule-item lockd"><p>' + L('Предложения, которые ты соберёшь в плане, сохранятся здесь.', 'Sentences you build in the plan are saved here.') + '</p></div>';
  v.innerHTML = h;
  v.querySelectorAll('[data-say]').forEach((e) => e.onclick = () => speakSeq([{ t: e.dataset.say, l: SPEECH[cfg.learn], r: .85 }]));
}

let RW = null;
const openLink = (u) => { try { if (tg && tg.openTelegramLink && u.indexOf('https://t.me/') === 0) tg.openTelegramLink(u); else window.open(u, '_blank'); } catch (e) { window.open(u, '_blank'); } };
async function loadRewards() {
  if (DEMO) RW = { channels: [{ key: 'ch:@demo', handle: '@demo', days: 3, claimed: false }], invite: { link: 'https://t.me/demo_bot?start=ref_1', count: 0, days: 3, cap: 20 } };
  else { try { RW = await api('rewards'); } catch (e) { RW = null; } }
  renderRewards();
}
function renderRewards() {
  const c = $('rewardsCard'); if (!c) return;
  if (!RW) { c.style.display = 'none'; return; }
  c.style.display = '';
  let h = '<div class="section-title" style="margin-bottom:6px">' + L('Бонусные дни PRO', 'Free PRO days') + '</div>';
  RW.channels.forEach((ch) => { h += '<div class="rw"><div class="rw-i">' + ic('gift', 20) + '</div><div class="rw-t"><b>' + L('Подпишись на ', 'Subscribe to ') + esc(ch.handle) + '</b><span>+' + ch.days + L(' дн. PRO', ' PRO days') + '</span></div>' + (ch.claimed ? '<span class="rw-ok">' + ic('check', 18, 3) + '</span>' : '<button class="rw-b" data-open="' + esc(ch.handle) + '">' + L('Открыть', 'Open') + '</button><button class="rw-b pri" data-claim="' + esc(ch.key) + '">' + L('Проверить', 'Check') + '</button>') + '</div>'; });
  const iv = RW.invite;
  h += '<div class="rw"><div class="rw-i">' + ic('users', 20) + '</div><div class="rw-t"><b>' + L('Пригласи друга', 'Invite a friend') + '</b><span>+' + iv.days + L(' дн. за каждого · приглашено ', ' days each · invited ') + iv.count + '/' + iv.cap + '</span></div><button class="rw-b pri" id="rwShare">' + L('Пригласить', 'Invite') + '</button></div>';
  c.innerHTML = h;
  c.querySelectorAll('[data-open]').forEach((b) => b.onclick = () => openLink('https://t.me/' + b.dataset.open.replace('@', '')));
  c.querySelectorAll('[data-claim]').forEach((b) => b.onclick = () => claimReward(b.dataset.claim));
  $('rwShare').onclick = () => { const t = L('Учу языки в SmartStudy, присоединяйся!', 'I am learning languages in SmartStudy, join me!'); openLink('https://t.me/share/url?url=' + encodeURIComponent(iv.link) + '&text=' + encodeURIComponent(t)); try { navigator.clipboard.writeText(iv.link); } catch (e) {} };
}
async function claimReward(key) {
  if (DEMO) return toast(L('Работает только внутри Telegram', 'Works inside Telegram only'));
  try { const r = await api('rewards/claim', { key }); toast(L('Готово! +', 'Done! +') + r.days + L(' дн. PRO', ' PRO days')); haptic('success'); confetti(); loadState(); }
  catch (e) { toast({ 412: L('Подписка не найдена. Подпишись и нажми ещё раз', 'Subscription not found. Subscribe and try again'), 400: L('Не удалось проверить подписку', 'Could not verify the subscription'), 409: L('Награда уже получена', 'Already claimed') }[e.message] || L('Ошибка. Попробуй позже', 'Error. Try again later')); }
}

let CHAT = [], chatBusy = false;
function renderMsgs() { const m = $('chMsgs'); if (!m) return; m.innerHTML = CHAT.map((x) => '<div class="msg ' + x.r + '">' + esc(x.t) + '</div>').join(''); m.scrollTop = m.scrollHeight; }
function openChat() {
  const c = cur(), el = $('chat');
  if (!CHAT.length) CHAT.push({ r: 'a', t: c[cfg.ui === 'en' ? 'en' : 'ru'][0] });
  el.innerHTML = '<div class="ch-head"><div class="ch-art">' + art(c.id) + '</div><div class="ch-t"><b>' + L(c.n[0], c.n[1]) + '</b><span>' + L('Задай мне вопрос по языку', 'Ask me about the language') + '</span></div
