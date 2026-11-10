import json,urllib.parse,os,html as H
BASE="https://gitteromri-ux.github.io/shani-ahiel/v7/";WAN="972546644489";MAIL='Shanini.a@gmail.com'
src=open('../v3/build3.py').read().split("FONTS=")[0];ns={};exec(src,ns);T3,BODY,ARTS=ns['T'],ns['BODY'],ns['ARTS']
META=json.load(open('img/meta.json'));WA_SVG=open('../v4/build4.py').read().split("WA_SVG='")[1].split("'\n")[0]
D={'he':dict(dir='rtl',brand='שני אחיאל',lang=('English','en/'),title='שני אחיאל – שירותי אירוח ומסעדנות · ברלין',
 desc='יותר מעשור של הקמה וניהול מסעדות, מותגים ואירועים בברלין. הקמה, הבראה, ליווי ומיקור חוץ של מערכי מזון ומשקאות למסעדות ולמלונות.',
 me='שני אחיאל · יזמית ומנהלת אירוח · ברלין',h1='מסעדה שעובדת,<br><em>וגם מרוויחה.</em>',
 lead='יותר מעשור של הקמה וניהול מסעדות, מותגים ואירועים בברלין, מ־Yafo ו־Shishi ועד מערך המזון והמשקאות של Selina. היום אני מביאה את הניסיון הזה לבעלי מסעדות, ליזמים ולמלונות.',
 cta1='בואו נדבר',cta2='המקומות שהקמתי',
 nav=[('venues','המקומות'),('services','שירותים'),('press','עיתונות'),('story','הדרך'),('process','תהליך'),('contact','צור קשר')],
 in_l='הגישה',in_h='כל מה שאני מציעה, <em>עשיתי קודם בעצמי.</em>',
 in_p=['את Yafo התחלתי במקום בלי מטבח ובלי בר, ובניתי הכל מאפס. ניקיתי את הרצפה אחרי סגירה, עבדתי מול ספקים, תיקנתי בעצמי מה שצריך, וגייסתי עובד אחרי עובד.','מכאן צמחו מסעדה בת 200 מקומות ישיבה, מסעדת שף, שיתופי פעולה עם מלונות וצוות של כמעט 60 עובדים. את הניסיון הזה, כבעלים וכמנהלת, אני מביאה היום לכל עסק שאני מלווה.'],
 quote='״אם אתם לא אוהבים אנשים, אתם לא עובדים באירוח.״',quote_s='שני אחיאל, בראיון ל־nomyblog',
 stats=[('10','+','שנים של הקמה וניהול בברלין'),('200','','מקומות ישיבה ב־Yafo'),('60','~','עובדים בשתי המסעדות'),('3','','שפות עבודה')],
 reel='לילות של Yafo ו־Shishi',soonk='גלריה בקרוב',
 vn_l='המקומות',vn_h='מקומות שהקמתי <em>וניהלתי.</em>',vn_p='מסעדות, מסעדת שף ומלונות בברלין. לחצו על מקום כדי לראות את התמונות.',
 venues=[('yafo','2015 – היום','Yafo','מסעדה ובר','מסעדה בת 200 מקומות ישיבה, עם אירועים שבועיים, חתונות ומסיבות. נבנתה מאפס, והפכה לכתובת מוכרת של אירוח ישראלי בברלין.'),
  ('shishi','2018 – 2022','Shishi','מסעדת שף','מסעדת שף שהקמתי, על עקרונות Farm to Table ובעבודה ישירה מול חקלאים בברנדנבורג. עיצוב פנים: Idan Gilony.'),
  ('amano','2019 – 2021','Amano','מלון · ברלין','Yafo התארחה במלון, והפכנו את הלובי למסעדה של ממש, עם מותג שפותח בתוכה.'),
  ('selina','2022 – 2023','Selina ברלין','מלון · מזון ומשקאות','הובלתי את כל מערך המזון והמשקאות במלון, לפי יעדי KPI ובמודל שותפות.'),
  ('opera','','Opera','מסעדה','לשני למלא – פרטים יתווספו')],
 soon='לשני למלא – תמונות יתווספו',photos='תמונות',
 sv_l='שירותים',sv_h='ארבעה מסלולים, <em>ושותפות אחת.</em>',sv_p='ארבעה מסלולי עבודה, לפי השלב שבו העסק נמצא. אפשר לבחור אחד או לשלב.',
 for_l='למי',
 svc=[('הקמת עסק חדש','מהרעיון ועד יום הפתיחה.','יזמים ובעלי מקום, לפני פתיחה',['תוכנית עסקית ותכנון','מיתוג וקונספט','בניית סטנדרטים תפעוליים'],'רוצה להקים עסק'),
      ('החייאה לעסק שלא מתפקד','כשהמספרים לא מסתדרים, מחזירים שליטה.','מסעדה מלאה שלא מרוויחה, או עסק שאיבד כיוון',['בקרת P&amp;L נכונה','שליטה בעלות עבודה','שליטה בעלות מזון'],'העסק שלי צריך סדר'),
      ('ליווי מסעדה פעילה','לעסק שעובד ורוצה לצמוח ולהתעדכן.','מסעדות פעילות שרוצות לצמוח',['לוגיסטיקה ותפעול שוטף','פיתוח, סושיאל ואסטרטגיה','Hosting וחוויית אירוח','סדנאות לצוות ולבניית מחלקות חדשות'],'לליווי שוטף'),
      ('אירועים','הפקה והובלה של אירועים פרטיים ועסקיים, ובניית מחלקת אירועים בתוך עסק קיים.','מסעדות, מלונות וחברות',['הפקה ותפעול','בניית מחלקה והכשרת צוות'],'לתכנון אירוע')],
 os_l='למלונות',os_h='מיקור חוץ של מערך <em>המזון והמשקאות.</em>',os_p='מסעדה, בר ואירועים שמנוהלים כמו עסק עצמאי בתוך המלון: אחריות על התפעול, יעדי KPI מדידים ומודל שותפות, כמו שהובלתי ב־Selina ברלין.',os_pts=['אחריות מלאה על התפעול','יעדי KPI מדידים','מודל שותפות'],
 pr_h='כתבו עליי',strip='כתבו עליי',
 st_l='הדרך',st_h='מתל אביב <em>לברלין.</em>',
 story=[('תל אביב','שירות, בר ואירועים','התחלתי בשירות ובבר בתל אביב, והתקדמתי לניהול אירועים.',None),
  ('2015','Yafo','מקום בלי מטבח ובלי בר הופך למסעדה ובר עם אירועים שבועיים, ולכתובת של אירוח ישראלי בברלין.','yafo-room'),
  ('2018','Shishi','מסעדת שף בחצר לבנים גדולה בקרויצברג, עם תפריט שנבנה מחומרי גלם של חקלאים מברנדנבורג.','courtyard'),
  ('2019 – 2021','Amano','Yafo מתארחת במלון Amano, והלובי הופך למסעדה של ממש.',None),
  ('2022 – 2023','Selina ברלין','הובלת כל מערך המזון והמשקאות במלון, לפי יעדי KPI ובמודל שותפות.',None),
  ('היום','ייעוץ והקמה','ליווי בעלי מסעדות, יזמים ומלונות: הקמה, הבראה, ליווי שוטף ומיקור חוץ, וגם הרצאות על הבמה.','stage')],
 facts=['תואר ראשון בתקשורת ומנהל עסקים','אזרחות ישראלית וגרמנית','עברית · אנגלית · גרמנית'],
 hw_l='תהליך',hw_h='איך זה <em>עובד.</em>',hw_p='תהליך פשוט, בלי הפתעות.',
 steps=[('שיחת היכרות','מבינים איפה העסק נמצא ומה היעד.'),('אבחון','בוחנים תפעול, מספרים, צוות ומותג.'),('תוכנית','סדרי עדיפויות ברורים, עם יעדים ולוחות זמנים.'),('ליווי ביישום','עבודה צמודה בשטח עד שהשינוי מחזיק.')],
 jr_l='מגזין',jr_h='מהמגזין',jr_cta='לקריאה',
 ct_l='צור קשר',ct_h='בואו נדבר על <em>העסק שלכם.</em>',ct_p='ספרו לי בכמה משפטים איפה העסק נמצא, ואחזור אליכם.',
 ft='השאירו פרטים',fs='נחזור אליכם תוך 24 שעות.',ph=['שם פרטי ומשפחה','למשל: מסעדה בתל אביב','050-000-0000','name@example.com','איפה העסק נמצא היום?'],
 note='בשליחת הטופס אתם מאשרים ששני תחזור אליכם בטלפון או במייל.'),
'en':dict(dir='ltr',brand='Shani Ahiel',lang=('עברית','../'),title='Shani Ahiel – Hospitality &amp; Restaurant Services · Berlin',
 desc='More than a decade of building and running restaurants, brands and events in Berlin. Openings, turnarounds, ongoing support and outsourced F&amp;B for restaurants and hotels.',
 me='Shani Ahiel · Hospitality entrepreneur · Berlin',h1='A restaurant that works,<br><em>and makes money.</em>',
 lead='More than a decade of building and running restaurants, brands and events in Berlin, from Yafo and Shishi to the food &amp; beverage operation at Selina. Today I bring that experience to restaurant owners, founders and hotels.',
 cta1='Let’s talk',cta2='The places I built',
 nav=[('venues','Venues'),('services','Services'),('press','Press'),('story','Story'),('process','Process'),('contact','Contact')],
 in_l='The approach',in_h='Everything I offer, <em>I have done myself first.</em>',
 in_p=['I started Yafo in a space with no kitchen and no bar, and built everything from scratch. I mopped the floor after closing, dealt with suppliers, fixed what needed fixing myself, and hired one person after another.','That grew into a 200-seat restaurant, a chef’s restaurant, hotel partnerships and a team of almost 60. I bring that experience, as an owner and operator, to every business I work with.'],
 quote='“If you don’t love people, you don’t work in hospitality.”',quote_s='Shani Ahiel, interviewed by nomyblog',
 stats=[('10','+','years building and running venues in Berlin'),('200','','seats at Yafo'),('60','~','people across two restaurants'),('3','','working languages')],
 reel='Nights at Yafo and Shishi',soonk='Gallery soon',
 vn_l='Venues',vn_h='Places I built <em>and ran.</em>',vn_p='Restaurants, a chef’s restaurant and hotels in Berlin. Tap a venue to see the photos.',
 venues=[('yafo','2015 – today','Yafo','Restaurant &amp; bar','A 200-seat restaurant with weekly events, weddings and parties. Built from scratch into a well-known address for Israeli hospitality in Berlin.'),
  ('shishi','2018 – 2022','Shishi','Chef’s restaurant','The chef’s restaurant I founded, built on farm-to-table principles and working directly with Brandenburg farmers. Interior by Idan Gilony.'),
  ('amano','2019 – 2021','Amano','Hotel · Berlin','Yafo was hosted at the hotel, and we turned the lobby into a real restaurant with its own brand.'),
  ('selina','2022 – 2023','Selina Berlin','Hotel · F&amp;B','Led the hotel’s entire food &amp; beverage operation against KPI targets, in a partnership model.'),
  ('opera','','Opera','Restaurant','For Shani to fill')],
 soon='For Shani to fill – photos to be added',photos='Photos',
 sv_l='Services',sv_h='Four engagements, <em>one partnership.</em>',sv_p='Four ways to work together, depending on where the business is. Choose one or combine them.',
 for_l='For',
 svc=[('Opening a new business','From the idea to opening day.','Founders and owners before opening',['Business plan and planning','Branding and concept','Building operating standards'],'I want to open a business'),
      ('Reviving a business that isn’t working','When the numbers don’t add up, we take back control.','A full room that isn’t profitable, or a business that lost its way',['Proper P&amp;L control','Labour cost control','Food cost control'],'My business needs order'),
      ('Supporting an active restaurant','For a business that works and wants to grow and stay current.','Working restaurants ready to grow',['Logistics and day-to-day operations','Development, social media and strategy','Hosting and guest experience','Team workshops and new departments'],'Ongoing support'),
      ('Events','Producing and leading private and corporate events, and building an events department inside an existing business.','Restaurants, hotels and companies',['Production and operations','Building a department and training the team'],'Plan an event')],
 os_l='For hotels',os_h='Outsourced <em>food &amp; beverage.</em>',os_p='A restaurant, bar and events run like an independent business inside the hotel: ownership of operations, measurable KPI targets and a partnership model, as I led at Selina Berlin.',os_pts=['Full ownership of operations','Measurable KPI targets','Partnership model'],
 pr_h='In the press',strip='As featured in',
 st_l='The story',st_h='From Tel Aviv <em>to Berlin.</em>',
 story=[('Tel Aviv','Floor, bar and events','I started on the floor and behind the bar in Tel Aviv, and moved up into event management.',None),
  ('2015','Yafo','A space with no kitchen and no bar becomes a restaurant and bar with weekly events, and an address for Israeli hospitality in Berlin.','yafo-room'),
  ('2018','Shishi','A chef’s restaurant in a large brick courtyard in Kreuzberg, with a menu built on produce from Brandenburg farmers.','courtyard'),
  ('2019 – 2021','Amano','Yafo is hosted at the Amano hotel, and the lobby becomes a real restaurant.',None),
  ('2022 – 2023','Selina Berlin','Leading the hotel’s entire food &amp; beverage operation, against KPI targets and in a partnership model.',None),
  ('Today','Advisory and openings','Working with restaurant owners, founders and hotels: openings, turnarounds, ongoing support and outsourcing, and talks on stage.','stage')],
 facts=['B.A. in Communications and Business Administration','Israeli and German citizen','Hebrew · English · German'],
 hw_l='Process',hw_h='How it <em>works.</em>',hw_p='A simple process, no surprises.',
 steps=[('Introductory call','We understand where the business is and what the goal is.'),('Diagnosis','We review operations, numbers, team and brand.'),('Plan','Clear priorities, with targets and timelines.'),('Hands-on implementation','Working closely on site until the change holds.')],
 jr_l='Journal',jr_h='From the journal',jr_cta='Read',
 ct_l='Contact',ct_h='Let’s talk about <em>your business.</em>',ct_p='Tell me in a few sentences where the business is, and I will get back to you.',
 ft='Leave your details',fs='We’ll get back to you within 24 hours.',ph=['First and last name','e.g. a hotel in Berlin','+49 …','name@example.com','Where is the business today?'],
 note='By sending this form you agree that Shani may contact you by phone or email.')}
VPH={'yafo':['yafo-room','yafo-toast','yafo-full','yafo-crowd','candle-table','bar-night','tasting','bar-gold','candle-toast','challah','bar-toast','neon'],'shishi':['longtable','curtain-shani','courtyard','street-crowd','courtyard-party','curtain-party','band-courtyard'],'amano':[],'selina':[],'opera':[]}
VLOGO={'yafo':'yafo-w.png','shishi':'shishi-w.png','selina':'selina-w.png'}
REEL1=['yafo-toast','courtyard','bar-gold','curtain-shani','yafo-full','candle-toast','street-crowd']
REEL2=['longtable','tasting','yafo-crowd','bar-night','challah','candle-table','yafo-room']
SVCIMG=['yafo-set','bar-gold','tasting','street-crowd']
PRESS=[('fizzz.png','fizzz','p-fizzz',{'he':'BIG LOVE · שער ופורטרט','en':'BIG LOVE · cover and portrait'},{'he':'אפריל 2020','en':'April 2020'},None),
 ('stern.svg','stern','p-stern',{'he':'כתבת פורטרט','en':'Portrait feature'},{'he':'2017','en':'2017'},None),
 ('sueddeutsche_zeitung.svg','Süddeutsche Zeitung','p-sz',{'he':'„Hip, aber herzlich“','en':'„Hip, aber herzlich“'},{'he':'2017','en':'2017'},'https://www.sueddeutsche.de/stil/samstagskueche-hip-aber-herzlich-1.3392048'),
 ('berliner_zeitung.svg','Berliner Zeitung','p-bz',{'he':'„Shishi“ in Kreuzberg: Eine neue Oase','en':'„Shishi“ in Kreuzberg: Eine neue Oase'},None,None),
 ('tip_berlin.svg','tip Berlin','p-tip',{'he':'ביקורת על Shishi, חמש נקודות','en':'Review of Shishi, five points'},{'he':'20/2018','en':'20/2018'},None)]
BLOGIMG={'hotel-lobby-restaurant':'yafo-full','fnb-outsourcing-hotels':'bar-gold','restaurant-turnaround':'yafo-crowd'}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500;600&family=Frank+Ruhl+Libre:wght@400;500&family=Heebo:wght@300;400;500;600&display=swap" rel="stylesheet">'
def pic(n,root,sizes='100vw',alt='',eager=False,cls=''):
    ws=META[n]['w'];ar=META[n]['ar'];jw=[w for w in ws if w<=1280]
    wv=', '.join(f'{root}img/{n}-{w}.webp {w}w' for w in ws);jv=', '.join(f'{root}img/{n}-{w}.jpg {w}w' for w in jw);W=jw[-1]
    att='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture><source type="image/webp" srcset="{wv}" sizes="{sizes}"><img src="{root}img/{n}-{W}.jpg" srcset="{jv}" sizes="{sizes}" alt="{alt}" width="{W}" height="{round(W/ar)}" class="{cls}" {att}></picture>'
def big(n,root): ws=META[n]['w'];return f'{root}img/{n}-{1280 if 1280 in ws else max(ws)}.webp'
def head(lang,title,desc,path,alt,root):
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0a0d26"><title>{title}</title><meta name="description" content="{desc}"><link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:title" content="{title}"><meta property="og:image" content="{BASE}img/hero-d-1280.jpg"><link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="{root}v7.css?v=5">'
def nav(lang,home,langhref):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav class="links">{items}</nav><div class="r"><a class="lang" href="{langhref}">{L["lang"][0]}</a><a class="btn sm" href="{home}#contact">{L["cta1"]}</a><button class="burger" aria-label="menu"><span></span><span></span></button></div></div></header><div class="mmenu">{items}<a class="lang" href="{langhref}">{L["lang"][0]}</a></div>'
def wa(lang): return f'<a class="fa-wa" href="https://wa.me/{WAN}?text={urllib.parse.quote(T3[lang]["wat"])}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>'
def foot(lang,home):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'<footer><div class="w"><div><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a></div><nav>{items}</nav><p>© 2026 {L["brand"]} · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:+{WAN}" dir="ltr">054-6644489</a></p></div></footer>'
LB='<div class="lb" hidden><button class="lb-x" aria-label="close">×</button><button class="lb-p" aria-label="prev">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="next">›</button><p class="lb-note"></p></div><div class="grain" aria-hidden="true"></div>'
def eyebrow(t): return f'<span class="eb">{t}</span>'
def jcard(lang,s,root,href):
    t,h,p=T3[lang]['arts'][s];return f'<a class="jc rv" href="{href}"><span class="ph">{pic(BLOGIMG[s],root,"(max-width:760px) 30vw, 340px")}</span><span class="t"><span class="k">{t}</span><b>{h}</b><span class="more">{D[lang]["jr_cta"]} {"←" if lang=="he" else "→"}</span></span></a>'
def index(lang):
    L=D[lang];root='' if lang=='he' else '../';path='' if lang=='he' else 'en/';alt='en/' if lang=='he' else '';ar='←' if lang=='he' else '→'
    ticker=' <i>·</i> '.join(['Yafo','Shishi','Amano','Selina Berlin','Opera'])
    stats=''.join(f'<div class="st rv"><b dir="ltr">'+ (f'<span class="pre">{p}</span>' if p else '') + f'<span class="num" data-count="{n}">{n}</span></b><span class="sl">{t}</span></div>' for n,p,t in L['stats'])
    reel=lambda arr:''.join(f'<figure>{pic(n,root,"260px")}</figure>'.replace('loading="lazy"','loading="eager"') for n in arr)
    vc=''
    for key,yr,name,kind,line in L['venues']:
        ph=VPH[key];lg=f'<img class="vl" src="{root}logos/{VLOGO[key]}" alt="" aria-hidden="true">' if key in VLOGO else ''
        y=f'<span class="y">{yr}</span>' if yr else ''
        if ph:
            g=json.dumps([[big(n,root),name] for n in ph])
            thumbs=''.join(f'<span>{pic(n,root,"60px")}</span>' for n in ph[1:4])
            vc+=f'''<button type="button" class="venue has v-{key} rv" data-g='{H.escape(g)}' data-tilt><span class="vph" data-par>{pic(ph[0],root,"(max-width:760px) 92vw, 560px",name,eager=True)}</span>{lg}<span class="vt"><span class="vk">{kind}</span>{y}<b>{name}</b><span class="vd">{line}</span><span class="vf"><span class="thumbs">{thumbs}</span><span class="cnt">{L['photos']} · {len(ph)} {ar}</span></span></span></button>'''
        else:
            vc+=f'''<button type="button" class="venue plain v-{key} rv" data-g="[]" data-note="{L['soon']}" data-tilt>{lg}<span class="wm" aria-hidden="true">{name.split()[0]}</span><span class="soon">{L['soonk']}</span><span class="vt"><span class="vk">{kind}</span>{y}<b>{name}</b><span class="vd">{line}</span></span></button>'''
    svc=''.join(f'''<article class="tier rv" data-tilt><span class="tph">{pic(SVCIMG[k],root,"(max-width:760px) 92vw, 280px")}<span class="no">0{k+1}</span></span><span class="tb"><h3>{h}</h3><p class="tg">{p}</p><p class="for"><span>{L['for_l']}</span>{fo}</p><ul>'''+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a class="go" href="#contact">{go} <span>{ar}</span></a></span></article>' for k,(h,p,fo,ul,go) in enumerate(L['svc']))
    ospts=''.join(f'<li>{x}</li>' for x in L['os_pts'])
    strip=''.join(f'<img src="{root}logos/{f}" alt="{n}" class="s-{f.split(".")[0]}">' for f,n,*_ in PRESS)
    pcards=''
    for f,n,im,hl,yr,link in PRESS:
        g=json.dumps([[big(im,root),n]]);y=f'<span>{yr[lang]}</span>' if yr else ''
        lk=f'<a class="pl" href="{link}" target="_blank" rel="noopener">{"לכתבה" if lang=="he" else "Article"} ↗</a>' if link else ''
        pcards+=f'''<div class="pc rv"><button type="button" class="pth" data-g='{H.escape(g)}' aria-label="{n}">{pic(im,root,"160px",n)}</button><span class="pt"><img class="plg plg-{f.split('.')[0]}" src="{root}logos/{f}" alt="{n}"><span class="ph"{' dir="ltr"' if hl[lang].startswith('„') else ''}>{hl[lang]}</span><span class="pm">{y}{lk}</span></span></div>'''
    story=''
    for k,(yr,t,d,im) in enumerate(L['story']):
        media=f'<figure class="sm mask">{pic(im,root,"(max-width:760px) 88vw, 420px")}</figure>' if im else ''
        story+=f'<li class="sn rv{" wimg" if im else ""}"><span class="dot"></span><span class="sy">{yr}</span><div class="sc"><h3>{t}</h3><p>{d}</p>{media}</div></li>'
    facts=''.join(f'<span>{f}</span>' for f in L['facts'])
    steps=''.join(f'<li class="rv"><span class="n">0{k+1}</span><b>{a}</b><span>{b}</span></li>' for k,(a,b) in enumerate(L['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html') for s in ARTS)
    F=T3[lang]['fl'];P=L['ph'];chips=''.join(f'<label><input type="checkbox" name="service" value="{c[0]}"><span>{c[0]}</span></label>' for c in L['svc'])
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(lang,'./',L['lang'][1])}<main>
<header class="hero"><div class="bg" data-hpar><div class="kb"><picture><source media="(max-width:760px)" type="image/webp" srcset="{root}img/hero-m-720.webp 720w, {root}img/hero-m-1100.webp 1100w" sizes="100vw"><source type="image/webp" srcset="{root}img/hero-d-1280.webp 1280w, {root}img/hero-d-2000.webp 2000w" sizes="100vw"><img src="{root}img/hero-d-1280.jpg" alt="" fetchpriority="high"></picture></div></div><span class="scrim"></span><span class="glow"></span>
<div class="w hw"><div class="copy"><p class="me">{L['me']}</p><h1>{L['h1']}</h1><p class="lead">{L['lead']}</p><div class="cta"><a class="btn" href="#contact">{L['cta1']}</a><a class="btn ghost" href="#venues">{L['cta2']}</a></div></div>
<figure class="hcard mask"><span class="hc-in">{pic('yafo-room',root,'260px')}</span><figcaption>Yafo · Berlin</figcaption></figure></div>
<div class="ticker"><div class="w">{ticker}</div></div></header>
<section class="sec intro" id="intro"><div class="w ig"><div class="it">{eyebrow(L['in_l'])}<h2 class="rv">{L['in_h']}</h2>{''.join(f'<p class="rv">{x}</p>' for x in L['in_p'])}<blockquote class="rv">{L['quote']}<cite>{L['quote_s']}</cite></blockquote></div>
<div class="ivis"><figure class="i1 mask" data-par>{pic('neon',root,"(max-width:760px) 56vw, 300px","Yafo")}</figure><figure class="i2 mask" data-par="-.06">{pic('bar-gold',root,"(max-width:760px) 44vw, 240px")}</figure><span class="ring"></span></div></div>
<div class="w"><div class="stats">{stats}</div></div></section>
<section class="reel dark" aria-label="{L['reel']}"><div class="rr"><div class="rt">{reel(REEL1)}{reel(REEL1)}</div></div><div class="rr rev"><div class="rt">{reel(REEL2)}{reel(REEL2)}</div></div><p class="rcap">{L['reel']}</p></section>
<section class="sec venues-s" id="venues"><div class="w"><div class="hd">{eyebrow(L['vn_l'])}<h2 class="rv">{L['vn_h']}</h2><p class="sub rv">{L['vn_p']}</p></div><div class="vgrid">{vc}</div></div></section>
<section class="sec dark services" id="services"><span class="lights"></span><div class="w"><div class="hd">{eyebrow(L['sv_l'])}<h2 class="rv">{L['sv_h']}</h2><p class="sub rv">{L['sv_p']}</p></div><div class="tiers">{svc}</div>
<div class="os rv"><div class="osv">{pic('candle-table',root,"(max-width:760px) 92vw, 460px")}</div><div class="ost">{eyebrow(L['os_l'])}<h3>{L['os_h']}</h3><p>{L['os_p']}</p><ul>{ospts}</ul><a class="btn" href="#contact">{L['cta1']}</a></div></div></div></section>
<section id="press" class="press"><div class="strip"><p>{L['strip']}</p><div class="mq"><div class="mt" dir="ltr"><div class="mg">{strip}</div><div class="mg" aria-hidden="true">{strip}</div></div></div></div><div class="sec tight dark2"><div class="w"><div class="hd"><h2 class="rv">{L['pr_h']}</h2></div><div class="pgrid">{pcards}</div></div></div></section>
<section class="sec story" id="story"><div class="w"><div class="hd">{eyebrow(L['st_l'])}<h2 class="rv">{L['st_h']}</h2></div><ol class="tl"><span class="tline"><span class="tfill"></span></span>{story}</ol><div class="facts rv">{facts}</div></div></section>
<section class="sec dark process" id="process"><div class="w"><div class="hd">{eyebrow(L['hw_l'])}<h2 class="rv">{L['hw_h']}</h2><p class="sub rv">{L['hw_p']}</p></div><ol class="steps">{steps}</ol></div></section>
<section class="sec soft" id="journal"><div class="w"><div class="hd">{eyebrow(L['jr_l'])}<h2 class="rv">{L['jr_h']}</h2></div><div class="jgrid">{jc}</div></div></section>
<section id="contact" class="sec dark contact"><div class="cbg" data-par>{pic('candle-toast',root,'100vw')}</div><span class="cscrim"></span><div class="w two"><div class="rv">{eyebrow(L['ct_l'])}<h2>{L['ct_h']}</h2><p class="sub">{L['ct_p']}</p><div class="cta"><a class="btn" href="mailto:{MAIL}">{MAIL}</a><a class="btn ghost" href="tel:+{WAN}" dir="ltr">054-6644489</a></div></div>
<div class="form rv"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{T3[lang]['sending']}" data-subj="{T3[lang]['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn full" type="submit">{F[6]}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></section>
</main>{foot(lang,'./')}{wa(lang)}{LB}<script src="{root}v7.js?v=3" defer></script></body></html>'''
def article(lang,s):
    L=D[lang];L3=T3[lang];root='../' if lang=='he' else '../../';t,h,p=L3['arts'][s];mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html';alt=('en/' if lang=='he' else '')+f'blog/{s}.html';langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,h+' · '+L['brand'],p,path,alt,root)}</head><body class="art"><div class="prog"></div>{nav(lang,'../',langhref)}<main>
<header class="ahero"><div class="bg" data-hpar>{pic(BLOGIMG[s],root,'100vw',eager=True)}</div><span class="scrim"></span><div class="w"><p class="me">{t}</p><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L3['mins']}</p></div></header>
<article class="prose">{body}<div class="byline">{pic('portrait',root,'56px')}<p>{L3['by']}</p></div><div class="actab"><h3>{L['ct_h']}</h3><p>{L['ct_p']}</p><a class="btn" href="../#contact">{L['cta1']}</a></div></article>
<section class="sec soft"><div class="w"><div class="hd"><h2>{L3['more']}</h2></div><div class="jgrid two">{others}</div><p class="back"><a href="../">{L3['back']}</a></p></div></section></main>{foot(lang,'../')}{wa(lang)}<div class="grain" aria-hidden="true"></div><script src="{root}v7.js?v=3" defer></script></body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he'));open('en/index.html','w').write(index('en'))
for s in ARTS: open(f'blog/{s}.html','w').write(article('he',s));open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok')
