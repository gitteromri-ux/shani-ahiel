import json,urllib.parse,os,html as H
BASE="https://gitteromri-ux.github.io/shani-ahiel/v6/"
WAN="972546644489"
src=open('../v3/build3.py').read().split("FONTS=")[0]
ns={};exec(src,ns)
T3,BODY,ARTS=ns['T'],ns['BODY'],ns['ARTS']
META=json.load(open('img/meta.json'))
WA_SVG=open('../v4/build4.py').read().split("WA_SVG='")[1].split("'\n")[0]
MAIL='Shanini.a@gmail.com'
# ---- Shani's draft text, verbatim (HE); EN = faithful translation ----
D={'he':dict(dir='rtl',brand='שני אחיאל',lang=('English','en/'),
 title='שני אחיאל – שירותי אירוח ומסעדנות',desc='אני עוזרת לבעלי מסעדות ויזמים להקים, לייצב ולפתח עסקי אירוח, על בסיס למעלה מעשור של ניהול והקמה של מסעדות, מותגים ואירועים.',
 me='שני אחיאל · יזמית ומנהלת בתחום האירוח, ברלין',h1='מסעדה שעובדת, <em>וגם מרוויחה</em>',
 lead='אני עוזרת לבעלי מסעדות ויזמים להקים, לייצב ולפתח עסקי אירוח, על בסיס למעלה מעשור של ניהול והקמה של מסעדות, מותגים ואירועים.',
 cta1='בואו נדבר',cta2='במה אני יכולה לעזור',band_alt=['אורחים יושבים בחצר המסעדה בערב','אירוע עמוס במסעדה'],
 sv_h='במה אני יכולה לעזור',sv_p='ארבעה מסלולי עבודה, לפי השלב שבו העסק נמצא. אפשר לבחור אחד או לשלב.',
 svc=[('הקמת עסק חדש','מהרעיון ועד יום הפתיחה.',['תוכנית עסקית ותכנון','מיתוג וקונספט','בניית סטנדרטים תפעוליים'],'רוצה להקים עסק'),
      ('החייאה לעסק שלא מתפקד','כשהמספרים לא מסתדרים, מחזירים שליטה.',['בקרת P&amp;L נכונה','שליטה בעלות עבודה','שליטה בעלות מזון'],'העסק שלי צריך סדר'),
      ('ליווי מסעדה פעילה','לעסק שעובד ורוצה לצמוח ולהתעדכן.',['לוגיסטיקה ותפעול שוטף','פיתוח, סושיאל ואסטרטגיה','Hosting וחוויית אירוח','סדנאות לצוות ולבניית מחלקות חדשות'],'לליווי שוטף'),
      ('אירועים','הפקה והובלה של אירועים פרטיים ועסקיים, ובניית מחלקת אירועים בתוך עסק קיים.',['הפקה ותפעול','בניית מחלקה והכשרת צוות'],'לתכנון אירוע')],
 hw_h='איך זה עובד',hw_p='תהליך פשוט, בלי הפתעות.',
 steps=[('שיחת היכרות','מבינים איפה העסק נמצא ומה היעד.'),('אבחון','בוחנים תפעול, מספרים, צוות ומותג.'),('תוכנית','סדרי עדיפויות ברורים, עם יעדים ולוחות זמנים.'),('ליווי ביישום','עבודה צמודה בשטח עד שהשינוי מחזיק.')],
 why_h='למה לעבוד איתי',why_p='את כל מה שאני מציעה עשיתי בעצמי, בברלין, כבעלים וכמנהלת.',
 venues=[('yafo','2015 – היום','Yafo','הקמה וניהול של מסעדה בת 200 מקומות ישיבה, עם אירועים שבועיים.'),
         ('selina','2022 – 2023','Selina ברלין','הובלת כל מערך המזון והמשקאות במלון, לפי יעדי KPI ובמודל שותפות.'),
         ('amano','2019 – 2021','Amano','הפיכת לובי מלון למסעדה של ממש, ופיתוח המותג בתוכה.'),
         ('shishi','2018 – 2022','Shishi','מסעדת שף על עקרונות Farm to Table, בעבודה ישירה מול חקלאים.'),
         ('opera','','Opera','')],
 opera_line='לשני למלא – פרטים יתווספו',soon='לשני למלא – תמונות יתווספו',photos='תמונות',
 pr_l='עיתונות',pr_h='כתבו עליי',strip='כתבו עליי',
 ab_h='קצת עליי',ab=['התחלתי בשירות ובבר בתל אביב והתקדמתי לניהול אירועים. מאז הקמתי וניהלתי מסעדות בברלין, וליוויתי שיתופי פעולה עם רשתות מלונות.','בעלת תואר ראשון בתקשורת ומנהל עסקים, אזרחית ישראלית וגרמנית, דוברת עברית, אנגלית וגרמנית.'],
 jr_h='מהמגזין',jr_cta='לקריאה',
 ct_h='בואו נדבר על העסק שלכם',ct_p='ספרו לי בכמה משפטים איפה העסק נמצא, ואחזור אליכם.',
 ft='השאירו פרטים',fs='נחזור אליכם תוך 24 שעות.',ph=['שם פרטי ומשפחה','למשל: מסעדה בתל אביב','050-000-0000','name@example.com','איפה העסק נמצא היום?'],
 note='בשליחת הטופס אתם מאשרים ששני תחזור אליכם בטלפון או במייל.',close='סגירה',
 nav=[('services','שירותים'),('process','איך זה עובד'),('why','למה איתי'),('press','עיתונות'),('about','עליי'),('contact','צור קשר')]),
'en':dict(dir='ltr',brand='Shani Ahiel',lang=('עברית','../'),
 title='Shani Ahiel – Hospitality and Restaurant Services',desc='I help restaurant owners and entrepreneurs open, stabilise and grow hospitality businesses, drawing on more than a decade of building and running restaurants, brands and events.',
 me='Shani Ahiel · Hospitality entrepreneur and manager, Berlin',h1='A restaurant that works, <em>and makes money</em>',
 lead='I help restaurant owners and entrepreneurs open, stabilise and grow hospitality businesses, drawing on more than a decade of building and running restaurants, brands and events.',
 cta1='Let’s talk',cta2='How I can help',band_alt=['Guests seated in the restaurant courtyard in the evening','A busy event at the restaurant'],
 sv_h='How I can help',sv_p='Four ways to work together, depending on where the business is. Choose one or combine them.',
 svc=[('Opening a new business','From the idea to opening day.',['Business plan and planning','Branding and concept','Building operating standards'],'I want to open a business'),
      ('Reviving a business that isn’t working','When the numbers don’t add up, we take back control.',['Proper P&amp;L control','Labour cost control','Food cost control'],'My business needs order'),
      ('Supporting an active restaurant','For a business that works and wants to grow and stay current.',['Logistics and day-to-day operations','Development, social media and strategy','Hosting and guest experience','Team workshops and building new departments'],'Ongoing support'),
      ('Events','Producing and leading private and corporate events, and building an events department inside an existing business.',['Production and operations','Building a department and training the team'],'Plan an event')],
 hw_h='How it works',hw_p='A simple process, no surprises.',
 steps=[('Introductory call','We understand where the business is and what the goal is.'),('Diagnosis','We review operations, numbers, team and brand.'),('Plan','Clear priorities, with targets and timelines.'),('Hands-on implementation','Working closely on site until the change holds.')],
 why_h='Why work with me',why_p='Everything I offer, I have done myself, in Berlin, as an owner and manager.',
 venues=[('yafo','2015 – today','Yafo','Founded and ran a 200-seat restaurant with weekly events.'),
         ('selina','2022 – 2023','Selina Berlin','Led the hotel’s entire food &amp; beverage operation, against KPI targets and in a partnership model.'),
         ('amano','2019 – 2021','Amano','Turned a hotel lobby into a real restaurant, and developed the brand within it.'),
         ('shishi','2018 – 2022','Shishi','A chef’s restaurant built on farm-to-table principles, working directly with farmers.'),
         ('opera','','Opera','')],
 opera_line='Details coming soon',soon='Photos coming soon',photos='Photos',
 pr_l='Press',pr_h='In the press',strip='As featured in',
 ab_h='About me',ab=['I started out on the floor and behind the bar in Tel Aviv and moved up into event management. Since then I have founded and run restaurants in Berlin, and led partnerships with hotel chains.','I hold a B.A. in Communications and Business Administration, am an Israeli and German citizen, and speak Hebrew, English and German.'],
 jr_h='From the journal',jr_cta='Read',
 ct_h='Let’s talk about your business',ct_p='Tell me in a few sentences where the business is, and I will get back to you.',
 ft='Leave your details',fs='We’ll get back to you within 24 hours.',ph=['First and last name','e.g. a hotel in Berlin','+49 …','name@example.com','Where is the business today?'],
 note='By sending this form you agree that Shani may contact you by phone or email.',close='Close',
 nav=[('services','Services'),('process','Process'),('why','Why me'),('press','Press'),('about','About'),('contact','Contact')])}
# venue photos per Shani's tags (tags_nov10_evening.md)
VPH={'yafo':['yafo-room','yafo-toast','yafo-full','yafo-crowd','candle-table','bar-night','tasting','bar-gold','candle-toast','challah','neon'],
     'shishi':['longtable','curtain-shani','courtyard','street-crowd'],'selina':[],'amano':[],'opera':[]}
VLOGO={'yafo':'yafo.png','shishi':'shishi.png','selina':'selina.png'}
PRESS=[('fizzz.png','fizzz','p-fizzz',{'he':'BIG LOVE · שער ופורטרט','en':'BIG LOVE · cover and portrait'},{'he':'אפריל 2020','en':'April 2020'},None),
 ('stern.svg','stern','p-stern',{'he':'כתבת פורטרט','en':'Portrait feature'},{'he':'2017','en':'2017'},None),
 ('sueddeutsche_zeitung.svg','Süddeutsche Zeitung','p-sz',{'he':'„Hip, aber herzlich“','en':'„Hip, aber herzlich“'},{'he':'2017','en':'2017'},'https://www.sueddeutsche.de/stil/samstagskueche-hip-aber-herzlich-1.3392048'),
 ('berliner_zeitung.svg','Berliner Zeitung','p-bz',{'he':'„Shishi“ in Kreuzberg: Eine neue Oase','en':'„Shishi“ in Kreuzberg: Eine neue Oase'},None,None),
 ('tip_berlin.svg','tip Berlin','p-tip',{'he':'ביקורת על Shishi, חמש נקודות','en':'Review of Shishi, five points'},{'he':'20/2018','en':'20/2018'},None)]
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500;600&family=Frank+Ruhl+Libre:wght@400;500&family=Heebo:wght@300;400;500;600&display=swap" rel="stylesheet">'
def src(n,w): return f'img/{n}-{w}'
def pic(n,root,sizes='100vw',alt='',eager=False,cls=''):
    ws=META[n]['w'];ar=META[n]['ar'];jw=[w for w in ws if w<=1280]
    wv=', '.join(f'{root}img/{n}-{w}.webp {w}w' for w in ws);jv=', '.join(f'{root}img/{n}-{w}.jpg {w}w' for w in jw)
    W=jw[-1];att='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture><source type="image/webp" srcset="{wv}" sizes="{sizes}"><img src="{root}img/{n}-{W}.jpg" srcset="{jv}" sizes="{sizes}" alt="{alt}" width="{W}" height="{round(W/ar)}" class="{cls}" {att}></picture>'
def big(n,root):
    ws=META[n]['w'];w=1280 if 1280 in ws else max(ws);return f'{root}img/{n}-{w}.webp'
def head(lang,title,desc,path,alt,root):
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#000034"><title>{title}</title><meta name="description" content="{desc}"><link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:title" content="{title}"><meta property="og:image" content="{BASE}img/hero-d-1280.jpg"><link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="{root}v6.css?v=1">'''
def nav(lang,home,langhref):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'''<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L['brand']}</b><i>Hospitality &amp; F&amp;B</i></a><nav class="links" aria-label="main">{items}</nav><div class="r"><a class="lang" href="{langhref}">{L['lang'][0]}</a><a class="btn sm" href="{home}#contact">{L['cta1']}</a><button class="burger" aria-label="menu" aria-expanded="false"><span></span><span></span></button></div></div></header><div class="mmenu">{items}<a class="lang" href="{langhref}">{L['lang'][0]}</a></div>'''
def wa(lang):
    t=T3[lang]['wat'];return f'<a class="fa-wa" href="https://wa.me/{WAN}?text={urllib.parse.quote(t)}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>'
def foot(lang,home):
    L=D[lang];return f'<footer><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B</i></a><p>© 2026 {L["brand"]} · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:+{WAN}" dir="ltr">054-6644489</a></p></div></footer>'
LB='<div class="lb" hidden><button class="lb-x" aria-label="close">×</button><button class="lb-p" aria-label="prev">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="next">›</button><p class="lb-note"></p></div>'
def jcard(lang,s,root,href):
    t,h,p=T3[lang]['arts'][s];im={'hotel-lobby-restaurant':'yafo-full','fnb-outsourcing-hotels':'bar-gold','restaurant-turnaround':'yafo-crowd'}[s]
    return f'<a class="jc rv" href="{href}"><span class="ph">{pic(im,root,"(max-width:760px) 80vw, 340px")}</span><span class="t"><span class="k">{t}</span><b>{h}</b><span class="more">{D[lang]["jr_cta"]} {"←" if lang=="he" else "→"}</span></span></a>'
def index(lang):
    L=D[lang];root='' if lang=='he' else '../';path='' if lang=='he' else 'en/';alt='en/' if lang=='he' else ''
    svc=''.join(f'<article class="card rv"><span class="no">0{k+1}</span><h3>{h}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a class="go" href="#contact">{go} <span>{"←" if lang=="he" else "→"}</span></a></article>' for k,(h,p,ul,go) in enumerate(L['svc']))
    steps=''.join(f'<li class="rv"><span class="n">{k+1}</span><b>{a}</b><span>{b}</span></li>' for k,(a,b) in enumerate(L['steps']))
    vc=''
    VO=['yafo','shishi','selina','amano','opera']
    for key,yr,name,line in sorted(L['venues'],key=lambda v:VO.index(v[0])):
        ph=VPH[key];g=json.dumps([[big(n,root),name] for n in ph]);lg=f'<img class="vl" src="{root}logos/{VLOGO[key]}" alt="" aria-hidden="true">' if key in VLOGO else ''
        ln=line or L['opera_line'];yrs=f'<span class="y">{yr}</span>' if yr else ''
        if ph:
            vc+=f'''<button type="button" class="venue has rv" data-g='{H.escape(g)}'><span class="vph">{pic(ph[0],root,"(max-width:760px) 86vw, 380px",name)}</span><span class="vt">{yrs}<b>{name}</b><span class="vd">{ln}</span><span class="cnt">{L['photos']} · {len(ph)}</span></span></button>'''
        else:
            vc+=f'''<button type="button" class="venue plain rv" data-g="[]" data-note="{L['soon']}">{lg}<span class="vt">{yrs}<b>{name}</b><span class="vd">{ln}</span></span></button>'''
    logos=''.join(f'<img src="{root}logos/{f}" alt="{n}">' for f,n in [('yafo.png','Yafo'),('shishi.png','Shishi'),('selina.png','Selina')])
    strip=''.join(f'<img src="{root}logos/{f}" alt="{n}" class="s-{f.split(".")[0]}">' for f,n,*_ in PRESS)
    pcards=''
    for f,n,im,hl,yr,link in PRESS:
        g=json.dumps([[big(im,root),n]]);y=f'<span class="py">{yr[lang]}</span>' if yr else ''
        lk=f'<a class="pl" href="{link}" target="_blank" rel="noopener">{ "לכתבה" if lang=="he" else "Article"} ↗</a>' if link else ''
        pcards+=f'''<div class="pc rv"><button type="button" class="pth" data-g='{H.escape(g)}' aria-label="{n}">{pic(im,root,"160px",n)}</button><span class="pt"><img class="plg plg-{f.split('.')[0]}" src="{root}logos/{f}" alt="{n}"><span class="ph"{' dir="ltr"' if hl[lang].startswith('„') else ''}>{hl[lang]}</span><span class="pm">{y}{lk}</span></span></div>'''
    F=T3[lang]['fl'];P=L['ph'];chips=''.join(f'<label><input type="checkbox" name="service" value="{c[0]}"><span>{c[0]}</span></label>' for c in L['svc'])
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html') for s in ARTS)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(lang,'./',L['lang'][1])}
<main>
<header class="hero"><div class="bg"><div class="kb"><picture><source media="(max-width:760px)" type="image/webp" srcset="{root}img/hero-m-720.webp 720w, {root}img/hero-m-1100.webp 1100w" sizes="100vw"><source type="image/webp" srcset="{root}img/hero-d-1280.webp 1280w, {root}img/hero-d-2000.webp 2000w" sizes="100vw"><img src="{root}img/hero-d-1280.jpg" alt="" fetchpriority="high"></picture></div></div><span class="scrim"></span>
<div class="w"><p class="me">{L['me']}</p><h1>{L['h1']}</h1><p class="lead">{L['lead']}</p><div class="cta"><a class="btn" href="#contact">{L['cta1']}</a><a class="btn ghost" href="#services">{L['cta2']}</a></div></div></header>
<div class="band"><figure>{pic('band-courtyard',root,"(max-width:760px) 100vw, 50vw",L['band_alt'][0])}</figure><figure>{pic('band-event',root,"(max-width:760px) 100vw, 50vw",L['band_alt'][1])}</figure></div>
<section id="services" class="sec"><div class="w"><div class="hd rv"><h2>{L['sv_h']}</h2><p class="sub">{L['sv_p']}</p></div><div class="grid4">{svc}</div></div></section>
<section id="process" class="sec dark"><div class="w two"><div><div class="hd rv"><h2>{L['hw_h']}</h2><p class="sub">{L['hw_p']}</p></div><ol class="steps">{steps}</ol></div><figure class="side rv">{pic('candle-table',root,"(max-width:760px) 90vw, 420px")}</figure></div></section>
<section id="why" class="sec"><div class="w"><div class="hd rv"><h2>{L['why_h']}</h2><p class="sub">{L['why_p']}</p></div><div class="venues">{vc}</div><div class="logos rv">{logos}</div></div></section>
<section id="press" class="press"><div class="strip" aria-label="{L['strip']}"><p>{L['strip']}</p><div class="mq"><div class="mt" dir="ltr"><div class="mg">{strip}</div><div class="mg" aria-hidden="true">{strip}</div></div></div></div>
<div class="sec dark tight"><div class="w"><div class="hd rv"><h2>{L['pr_h']}</h2></div><div class="pgrid">{pcards}</div></div></div></section>
<section id="about" class="sec"><div class="w two about"><figure class="por rv">{pic('portrait',root,"(max-width:760px) 90vw, 400px",L['brand'])}</figure><div class="rv"><h2>{L['ab_h']}</h2>{''.join(f'<p>{x}</p>' for x in L['ab'])}</div></div></section>
<section id="journal" class="sec soft"><div class="w"><div class="hd rv"><h2>{L['jr_h']}</h2></div><div class="jgrid">{jc}</div></div></section>
<section id="contact" class="sec dark"><div class="w two"><div class="rv"><h2>{L['ct_h']}</h2><p class="sub">{L['ct_p']}</p><div class="cta"><a class="btn" href="mailto:{MAIL}">{MAIL}</a><a class="btn ghost" href="tel:+{WAN}" dir="ltr">054-6644489</a></div></div>
<div class="form rv"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{T3[lang]['sending']}" data-subj="{T3[lang]['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn full" type="submit">{F[6]}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></section>
</main>{foot(lang,'./')}{wa(lang)}{LB}<script src="{root}v6.js?v=1" defer></script></body></html>'''
def article(lang,s):
    L=D[lang];L3=T3[lang];root='../' if lang=='he' else '../../';t,h,p=L3['arts'][s];mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html';alt=('en/' if lang=='he' else '')+f'blog/{s}.html'
    langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    im={'hotel-lobby-restaurant':'yafo-full','fnb-outsourcing-hotels':'bar-gold','restaurant-turnaround':'yafo-crowd'}[s]
    others=''.join(jcard(lang,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,h+' · '+L['brand'],p,path,alt,root)}</head><body class="art">
<div class="prog"></div>{nav(lang,'../',langhref)}<main><header class="ahero"><div class="bg">{pic(im,root,'100vw',eager=True)}</div><span class="scrim"></span><div class="w"><p class="me">{t}</p><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L3['mins']}</p></div></header>
<article class="prose">{body}<div class="byline">{pic('portrait',root,'56px')}<p>{L3['by']}</p></div><div class="actab"><h3>{L['ct_h']}</h3><p>{L['ct_p']}</p><a class="btn" href="../#contact">{L['cta1']}</a></div></article>
<section class="sec soft"><div class="w"><div class="hd"><h2>{L3['more']}</h2></div><div class="jgrid two">{others}</div><p class="back"><a href="../">{L3['back']}</a></p></div></section></main>{foot(lang,'../')}{wa(lang)}<script src="{root}v6.js?v=1" defer></script></body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he'));open('en/index.html','w').write(index('en'))
for s in ARTS: open(f'blog/{s}.html','w').write(article('he',s));open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok')
