import json,urllib.parse,sys
sys.path.insert(0,'../v3')
BASE="https://gitteromri-ux.github.io/shani-ahiel/v4/"
WAN="972546644489"
WA_SVG='<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.5.7 4.8 1.9 6.8L3 29l6.8-2.1c1.9 1 4 1.6 6.2 1.6 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.1c-2 0-3.9-.6-5.5-1.6l-.4-.2-4 1.2 1.3-3.9-.3-.4c-1.1-1.7-1.7-3.6-1.7-5.6C5.4 9.8 10.2 5.1 16 5.1s10.6 4.7 10.6 10.5S21.8 26.1 16 26.1zm5.8-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.6 5.7 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'
# v3 content (facts, press, articles) reused verbatim
import importlib.util,os
src=open('../v3/build3.py').read().split("FONTS=")[0]
ns={};exec(src,ns)
PRESS,ARTS,T3,BODY=ns['PRESS'],ns['ARTS'],ns['T'],ns['BODY']
VID={'hotel-lobby-restaurant':'lobby','fnb-outsourcing-hotels':'bar','restaurant-turnaround':'kitchen'}
T={'he':dict(
 eyebrow='ייעוץ מזון ומשקאות למסעדות ולמלונות',h1=['עסק שעובד,','<em>וגם מרוויח.</em>'],
 sub='שני אחיאל מלווה מסעדות ומלונות בהקמה, בהבראה ובניהול שוטף של מערכי מזון ומשקאות, מתוך ניסיון של הקמה וניהול מסעדות בברלין.',
 cta='לתיאום שיחת היכרות',feat_b='The Infatuation · The Berliner',feat='ועוד כתבות על המסעדות בברלין',
 nav=[('services','שירותים'),('about','אודות'),('berlin','ברלין'),('journal','מגזין'),('contact','יצירת קשר')],brand_i='Hospitality &amp; F&amp;B',
 sv_tags=['הקמה','הבראה','ליווי','אירועים'],
 wd_l='התחומים',wd_h='מלונות, מסעדות <em>ואירועים</em>.',wd_p='שלושה עולמות שאני מכירה מבפנים, מהקבלה ועד המטבח.',
 worlds=[('lobby','מלונות','מזון ומשקאות במלון','מסעדה, בר ואירועים שמנוהלים כמו עסק עצמאי, לפי יעדים מדידים. מתוך העבודה עם Selina ברלין ו־Amano.'),
         ('kitchen','מסעדות','הקמה והבראה','מהקונספט ועד יום הפתיחה, ובחזרה לשליטה כשהמספרים לא מסתדרים.'),
         ('bar','אירועים','אירועים פרטיים ועסקיים','הפקה ותפעול, הקמת מחלקת אירועים והכשרת צוות.')],
 tag_b='שני אחיאל',tag='בעלים, מנהלת ויועצת אירוח ומסעדנות',
 facts=['תואר ראשון בתקשורת ובמנהל עסקים','אזרחות ישראלית וגרמנית','עברית · אנגלית · גרמנית'],
 stats=[('4','מסעדות ומלונות בברלין'),('8','כלי תקשורת כתבו על המסעדות'),('3','שפות עבודה')],
 bl_l='Yafo · Shishi',bl_h='ברלין, <em>אחרי החשכה</em>.',bl_p='בברלין הקמתי את Yafo, מסעדה ובר עם אירועים שבועיים, ואחריה את Shishi, מסעדת שף שעבדה ישירות מול חקלאים. שם למדתי, כבעלים וכמנהלת, את כל מה שאני מציעה היום ללקוחות.',
 gal_h='רגעים <em>מהדרך</em>.',gal_p='מהארכיון של שני: ערבים במסעדות, אירועים ובמות.',
 jr_cta='לקריאת המאמר',
 checks=['שיחה אישית עם שני, לא עם מוקד','תשובה תוך 24 שעות','בעברית, באנגלית או בגרמנית'],
 ft='בקשה לשיחת היכרות',fs='הפרטים נשארים אצל שני בלבד.',ph=['שם פרטי ומשפחה','למשל: מסעדה בתל אביב','050-000-0000','name@example.com','מה המצב היום, ומה הייתם רוצים לשנות?'],
 note='בשליחת הטופס אתם מאשרים ששני תחזור אליכם בטלפון או במייל.',wa_lbl='וואטסאפ',
 a_cta_h='רוצים לבדוק את זה אצלכם?',a_cta_p='שיחת היכרות קצרה מספיקה כדי להבין מאיפה מתחילים.',menu='תפריט',skip='דלגו לתוכן'),
'en':dict(
 eyebrow='Food &amp; beverage consulting for restaurants and hotels',h1=['A business that works,','<em>and makes money.</em>'],
 sub='Shani Ahiel advises restaurants and hotels on openings, turnarounds and ongoing food &amp; beverage operations, drawing on years of building and running restaurants in Berlin.',
 cta='Book an introductory call',feat_b='The Infatuation · The Berliner',feat='and more on her Berlin restaurants',
 nav=[('services','Services'),('about','About'),('berlin','Berlin'),('journal','Journal'),('contact','Contact')],brand_i='Hospitality &amp; F&amp;B',
 sv_tags=['Openings','Turnarounds','Support','Events'],
 wd_l='Where I work',wd_h='Hotels, restaurants <em>and events</em>.',wd_p='Three worlds I know from the inside, from the front desk to the kitchen.',
 worlds=[('lobby','Hotels','Hotel food &amp; beverage','Restaurant, bar and events run like an independent business, against measurable targets. Drawing on my work with Selina Berlin and Amano.'),
         ('kitchen','Restaurants','Openings and turnarounds','From concept to opening day, and back in control when the numbers don’t add up.'),
         ('bar','Events','Private and corporate events','Production and operations, building an events department and training the team.')],
 tag_b='Shani Ahiel',tag='Owner, operator and hospitality consultant',
 facts=['B.A. in Communications and Business Administration','Israeli and German citizen','Hebrew · English · German'],
 stats=[('4','Berlin restaurants and hotels'),('8','Publications featured'),('3','Working languages')],
 bl_l='Yafo · Shishi',bl_h='Berlin, <em>after dark</em>.',bl_p='In Berlin I founded Yafo, a restaurant and bar with weekly events, followed by Shishi, a chef-led restaurant that worked directly with farmers. That is where I learned, as an owner and operator, everything I offer clients today.',
 gal_h='Moments <em>along the way</em>.',gal_p='From Shani’s archive: evenings at the restaurants, events and stages.',
 jr_cta='Read the article',
 checks=['A personal conversation with Shani, not a call centre','A reply within 24 hours','In English, Hebrew or German'],
 ft='Introductory call request',fs='Your details stay with Shani only.',ph=['First and last name','e.g. a hotel in Berlin','+49 …','name@example.com','Where is the business today, and what would you like to change?'],
 note='By sending this form you agree that Shani may contact you by phone or email.',wa_lbl='WhatsApp',
 a_cta_h='Want to look at this in your business?',a_cta_p='A short introductory call is enough to see where to start.',menu='Menu',skip='Skip to content')}
GAL=['room','crowd','candles','tasting','longtable','bar','stage','night','feast','joy','crowd2','speaker','tables','garden','cover']
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@400;500;600&family=Frank+Ruhl+Libre:wght@400;500&family=Heebo:wght@400;500;600&display=swap" rel="stylesheet">'
def head(lang,title,desc,path,alt,root,preload=''):
    sch={"@context":"https://schema.org","@type":"ProfessionalService","name":"Shani Ahiel","url":BASE,"email":"Shanini.a@gmail.com","telephone":"+"+WAN,"areaServed":["Berlin","Germany","Israel"],"knowsLanguage":["he","en","de"],"founder":{"@type":"Person","name":"Shani Ahiel"}}
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#06061f"><title>{title}</title><meta name="description" content="{desc}">
<link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}media/hero-poster.webp">
<link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{preload}{FONTS}<script type="application/ld+json">{json.dumps(sch)}</script><link rel="stylesheet" href="{root}v4.css?v=2">'''
def nav(lang,home,langhref):
    L3,L=T3[lang],T[lang]
    items=''.join(f'<li><a href="{home}#{i}">{n}</a></li>' for i,n in L['nav'])
    mitems=''.join(f'<a class="m" href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'''<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L3['brand']}</b><i>{L['brand_i']}</i></a><nav aria-label="main"><ul>{items}</ul></nav><div class="r"><a class="lang" href="{langhref}">{L3['lang'][0]}</a><a class="btn" href="{home}#contact">{L['cta']}</a><button class="burger" aria-label="{L['menu']}" aria-expanded="false"><span></span><span></span><span></span></button></div></div></header>
<div class="mmenu">{mitems}<a class="btn" href="{home}#contact">{L['cta']}</a><a class="lang" href="{langhref}">{L3['lang'][0]}</a></div>'''
def wa(lang):
    L3,L=T3[lang],T[lang]
    return f'<div class="fa-wa"><a class="fa-wa-btn" href="https://wa.me/{WAN}?text={urllib.parse.quote(L3["wat"])}" target="_blank" rel="noopener" aria-label="{L3["wa"]}">{WA_SVG}<span class="lbl">{L["wa_lbl"]}</span></a></div>'
def foot(lang,home):
    L3,L=T3[lang],T[lang]
    links=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'<footer><div class="w"><div><a class="brand" href="{home}"><b>{L3["brand"]}</b><i>{L["brand_i"]}</i></a><div>{L3["foot"]}</div></div><nav>{links}<a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a></nav></div></footer>'
def vid(name,root,cls='',eager=False,alt=''):
    return f'<video data-v="{root}media/{name}" muted loop playsinline preload="none" {"data-eager" if eager else ""} aria-hidden="true" class="{cls}"></video>'
def img(name,root,alt='',cls='',lazy=True,sizes='(max-width:860px) 90vw, 40vw'):
    return f'<img src="{root}img/{name}-1400.webp" srcset="{root}img/{name}-720.webp 720w, {root}img/{name}-1400.webp 1400w" sizes="{sizes}" alt="{alt}" class="{cls}" {"loading=lazy decoding=async" if lazy else ""}>'
def jcard(lang,s,root,href,k=0):
    L3,L=T3[lang],T[lang]; t,h,p=L3['arts'][s]
    return f'<a class="jcard rv d{k}" href="{href}" data-tilt="6"><div class="ph"><img src="{root}media/{VID[s]}-poster.webp" alt="" loading="lazy" decoding="async"></div><div class="t"><span class="k">{t}</span><h3>{h}</h3><p>{p}</p><span class="more">{L["jr_cta"]} {"←" if lang=="he" else "→"}</span></div></a>'
def index(lang):
    L3,L=T3[lang],T[lang]; root='' if lang=='he' else '../'; path='' if lang=='he' else 'en/'; alt='en/' if lang=='he' else ''
    pre=f'<link rel="preload" as="image" href="{root}media/hero-poster-m.webp" media="(max-width:860px)" fetchpriority="high"><link rel="preload" as="image" href="{root}media/hero-poster.webp" media="(min-width:861px)" fetchpriority="high">'
    press=''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in PRESS)*2
    svc=''.join(f'<article class="pcard rv d{k}" data-tilt="8"><span class="glare"></span><div class="n">0{k+1}<span>{L["sv_tags"][k]}</span></div><h3>{h}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></article>' for k,(h,p,ul) in enumerate(L3['svc']))
    worlds=''.join(f'<article class="vcard rv d{k}" data-tilt="5">{vid(v,root)}<img class="pst" src="{root}media/{v}-poster-m.webp" alt="" loading="lazy" style="z-index:-1"><div class="in"><span class="k">{kk}</span><h3>{h}</h3><p>{p}</p></div></article>' for k,(v,kk,h,p) in enumerate(L['worlds']))
    facts=''.join(f'<span>{f}</span>' for f in L['facts'])
    stats=''.join(f'<div class="rv d{k}"><b data-count="{n}">{n}</b><span>{t}</span></div>' for k,(n,t) in enumerate(L['stats']))
    yafo,shishi=L3['rows'][0],L3['rows'][3]
    venues=''.join(f'<div class="venue rv d{k}" style="grid-template-columns:1fr"><div class="t"><span class="k">{t}</span><h3>{n}</h3><p>{d}</p></div></div>' for k,(n,t,d) in enumerate([yafo,shishi]))
    gal=''.join(f'<figure>{img(g,root,sizes="(max-width:860px) 72vw, 380px")}</figure>' for g in GAL)
    rows=''.join(f'<div class="row rv"><h3>{n}</h3><span class="k">{t}</span><p>{d}</p></div>' for n,t,d in L3['rows'])
    steps=''.join(f'<div class="step rv"><span class="n">0{k+1}</span><h3>{a}</h3><p>{b}</p></div>' for k,(a,b) in enumerate(L3['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html',k) for k,s in enumerate(ARTS))
    F=L3['fl'];P=L['ph']
    chips=''.join(f'<label><input type="checkbox" name="service" value="{c}"><span>{c}</span></label>' for c in L3['chips'])
    waurl=f'https://wa.me/{WAN}?text={urllib.parse.quote(L3["wat"])}'
    checks=''.join(f'<li>{c}</li>' for c in L['checks'])
    h1=''.join(f'<span class="ln"><span>{x}</span></span>' for x in L['h1'])
    return f'''<!doctype html><html lang="{lang}" dir="{L3['dir']}"><head>{head(lang,L3['title'],L3['desc'],path,alt,root,pre)}</head><body>
{nav(lang,'./',L3['lang'][1])}
<main>
<section class="hero"><div class="layer"><picture><source media="(max-width:860px)" srcset="{root}media/hero-poster-m.webp"><img src="{root}media/hero-poster.webp" alt="" fetchpriority="high" width="1600" height="900"></picture>{vid('hero',root,eager=True)}</div>
<div class="w"><div class="copy"><span class="eyebrow">{L['eyebrow']}</span><h1>{h1}</h1><p class="sub">{L['sub']}</p><div class="ctas"><a class="btn" href="#contact">{L['cta']}</a><span class="sep"></span><span class="feat"><b>{L['feat_b']}</b>{L['feat']}</span></div></div></div><span class="scrollcue"></span></section>
<section class="press" aria-label="{L3['press']}"><div class="lbl">{L3['press']}</div><div class="mq">{press}</div></section>
<section id="services" class="sec paths"><div class="w"><div class="head c rv"><span class="eyebrow">{L3['sv_l']}</span><h2>{L3['sv_h']}</h2><p class="lead">{L3['sv_p']}</p></div><div class="cards4" data-dots="#d1">{svc}</div><div class="dots" id="d1"></div></div></section>
<section class="sec dark worlds"><div class="w"><div class="head rv"><span class="eyebrow">{L['wd_l']}</span><h2>{L['wd_h']}</h2><p class="lead">{L['wd_p']}</p></div><div class="grid" data-dots="#d2">{worlds}</div><div class="dots" id="d2"></div></div></section>
<section id="about" class="sec about"><div class="w"><div class="grid"><div class="frame rv"><div class="ph clipin" data-tilt="5">{img('portrait',root,L3['brand'])}</div><div class="ph2">{img('speaker',root,'',sizes='200px')}</div><div class="tag"><b>{L['tag_b']}</b><span>{L['tag']}</span></div></div>
<div class="body"><span class="eyebrow rv">{L3['ab_l']}</span><h2 class="rv">{L3['ab_h']}</h2><div class="rv d1" style="margin-top:1.6rem">{''.join(f'<p>{x}</p>' for x in L3['ab'])}</div><div class="facts rv d2">{facts}</div></div></div>
<div class="stats">{stats}</div></div></section>
<section id="berlin" class="berlin"><div class="bg" data-par>{vid('berlin',root)}</div><div class="w"><div class="top"><span class="eyebrow rv">{L['bl_l']}</span><h2 class="rv">{L['bl_h']}</h2><p class="lead rv d1">{L['bl_p']}</p></div><div class="venues">{venues}</div></div>
<div class="gal"><div class="w lbl"><h2 class="rv" style="font-size:clamp(2rem,4vw,3rem)">{L['gal_h']}</h2><p class="rv d1">{L['gal_p']}</p></div><div class="track">{gal}</div></div></section>
<section id="record" class="sec exp"><div class="w"><div class="head rv"><span class="eyebrow">{L3['rc_l']}</span><h2>{L3['rc_h']}</h2><p class="lead">{L3['rc_p']}</p></div><div class="rows">{rows}</div></div></section>
<section id="method" class="sec dark proc"><div class="w"><div class="grid"><div class="vid clipin">{vid('plating',root)}<img src="{root}media/plating-poster-m.webp" alt="" loading="lazy" style="position:absolute;inset:0;z-index:-1"></div><div><div class="head rv"><span class="eyebrow">{L3['md_l']}</span><h2>{L3['md_h']}</h2></div><div class="steps"><span class="bar"></span>{steps}</div></div></div></div></section>
<section id="journal" class="sec paths"><div class="w"><div class="head c rv"><span class="eyebrow">{L3['jr_l']}</span><h2>{L3['jr_h']}</h2><p class="lead">{L3['jr_p']}</p></div><div class="jcards" data-dots="#d3">{jc}</div><div class="dots" id="d3"></div></div></section>
<section id="contact" class="sec dark contact"><div class="bg">{vid('table',root)}</div><div class="w"><div><span class="eyebrow rv">{L3['ct_l']}</span><h2 class="rv">{L3['ct_h']}</h2><p class="lead rv d1" style="margin-top:1.2rem">{L3['ct_p']}</p><ul class="checks rv d2">{checks}</ul>
<div class="direct rv d3"><a href="{waurl}" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a><a href="tel:+{WAN}" dir="ltr">054-664-4489</a></div></div>
<div class="fcard rv d1"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{L3['sending']}" data-subj="{L3['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" inputmode="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn" type="submit">{F[6]}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></section>
</main>
{foot(lang,'./')}
{wa(lang)}<script src="{root}v4.js?v=1" defer></script></body></html>'''
def article(lang,s):
    L3,L=T3[lang],T[lang]; root='../' if lang=='he' else '../../'; t,h,p=L3['arts'][s]; mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html'; alt=('en/' if lang=='he' else '')+f'blog/{s}.html'
    langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html',k) for k,o in enumerate([o for o in ARTS if o!=s]))
    v=VID[s]
    body=body.replace('<p>','<p class="rv">').replace('<h2>','<h2 class="rv">').replace('<blockquote>','<blockquote class="rv">').replace('<ul>','<ul class="rv">')
    pre=f'<link rel="preload" as="image" href="{root}media/{v}-poster-m.webp" media="(max-width:860px)"><link rel="preload" as="image" href="{root}media/{v}-poster.webp" media="(min-width:861px)">'
    return f'''<!doctype html><html lang="{lang}" dir="{L3['dir']}"><head>{head(lang,h+' · '+L3['brand'],p,path,alt,root,pre)}</head><body>
<div class="prog"></div>{nav(lang,'../',langhref)}
<main><section class="ahero"><div class="layer"><picture><source media="(max-width:860px)" srcset="{root}media/{v}-poster-m.webp"><img src="{root}media/{v}-poster.webp" alt="" fetchpriority="high"></picture>{vid(v,root,eager=True).replace('<video','<video style="position:absolute;inset:0"')}</div><div class="w"><span class="eyebrow" style="color:var(--gold)">{t}</span><h1>{h}</h1><p class="meta">{L3['brand']} · {mins} {L3['mins']}</p></div></section>
<article class="prose">{body}<div class="byline rv">{img('portrait',root,'',sizes='72px')}<p>{L3['by']}</p></div>
<div class="actab rv"><h3>{L['a_cta_h']}</h3><p>{L['a_cta_p']}</p><a class="btn" href="../#contact">{L['cta']}</a></div></article>
<section class="sec paths" style="padding-top:40px"><div class="w"><div class="head c"><span class="eyebrow">{L3['more']}</span></div><div class="jcards" style="grid-template-columns:repeat(2,1fr)" data-dots="#d4">{others}</div><div class="dots" id="d4"></div><p style="text-align:center;margin-top:3rem"><a class="link" href="../">{L3['back']}</a></p></div></section></main>
{foot(lang,'../')}
{wa(lang)}<script src="{root}v4.js?v=1" defer></script></body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he')); open('en/index.html','w').write(index('en'))
for s in ARTS:
    open(f'blog/{s}.html','w').write(article('he',s)); open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok')
