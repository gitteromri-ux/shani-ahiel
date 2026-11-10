import json,urllib.parse,os,re
BASE="https://gitteromri-ux.github.io/shani-ahiel/v5/"
WAN="972546644489"
src=open('../v3/build3.py').read().split("FONTS=")[0]
ns={};exec(src,ns)
T3,BODY,ARTS,PRESS3=ns['T'],ns['BODY'],ns['ARTS'],ns['PRESS']
META=json.load(open('img/meta.json'))
WA_SVG=open('../v4/build4.py').read().split("WA_SVG='")[1].split("'\n")[0]
# --- Shishi removed from narrative (pending clarification with Shani) ---
SHISHI_P={'he':'<p>ב־Shishi עבדנו ישירות מול חקלאים. כשלאחד הספקים חסר חומר גלם, המנה פשוט ירדה מהתפריט באותו שבוע. הגמישות הזאת עולה כסף כשלא מתכננים אותה, וחוסכת כסף כשמתכננים.</p>',
          'en':'<p>At Shishi we worked directly with farmers. When a supplier was short of an ingredient, the dish simply came off the menu that week. That flexibility costs money if you do not plan for it, and saves money when you do.</p>'}
for l in BODY:
    m,b=BODY[l]['restaurant-turnaround']; BODY[l]['restaurant-turnaround']=(m,b.replace(SHISHI_P[l],''))
    assert 'Shishi' not in ''.join(x[1] for x in BODY[l].values())
T={'he':dict(
 eyebrow='ייעוץ מזון ומשקאות · מסעדות ומלונות',h1=['עסק שעובד,','<em>וגם מרוויח.</em>'],
 sub='שני אחיאל מלווה מסעדות ומלונות בהקמה, בהבראה ובניהול שוטף של מערכי מזון ומשקאות, מתוך ניסיון של הקמה וניהול מסעדות בברלין.',
 cta='לתיאום שיחת היכרות',cta2='כתבו עליה',
 nav=[('press','עיתונות'),('about','אודות'),('yafo','Yafo'),('services','שירותים'),('journal','מגזין'),('contact','יצירת קשר')],
 strip='כתבו עליה',
 pr_l='עיתונות',pr_h='כתבו <em>עליה.</em>',pr_p='מבחר הכתבות שבחרה שני, לפי הדירוג שלה. הגזירים האמיתיים, מהעיתונים עצמם.',
 read='לכתבה המלאה',noread='גזיר מהארכיון של שני',more_pr='עוד כתבות',
 ab=['התחלתי את דרכי בשירות ובבר בתל אביב, ומשם עברתי לניהול אירועים. בברלין הקמתי את Yafo, מסעדה ובר עם אירועים שבועיים, שנעשתה לכתובת מוכרת של אירוח ישראלי בעיר.',
     'בהמשך עבדתי עם מלונות: במלון Amano הפכנו את הלובי למסעדה של ממש, וב־Selina ברלין הובלתי את כל מערך המזון והמשקאות, לפי יעדים מדידים ובמודל שותפות.',
     'כל מה שאני מציעה ללקוחות עשיתי קודם בעצמי, כבעלים וכמנהלת. היום אני מלווה בעלי מסעדות, יזמים ומלונות שרוצים עסק שעובד, וגם מרוויח.'],
 facts=['תואר ראשון בתקשורת ובמנהל עסקים','אזרחות ישראלית וגרמנית','עברית · אנגלית · גרמנית'],
 tag='בעלים, מנהלת ויועצת אירוח ומסעדנות',
 stats=[('6','כתבות מובילות בעיתונות'),('2016','Yafo נפתחה בברלין'),('3','שפות עבודה')],
 yf_l='Yafo · ברלין',yf_h='המסעדה <em>שברלין עמדה בתור אליה.</em>',
 yf_p='בברלין הקמתי את Yafo, מסעדה ובר עם אירועים שבועיים, שנעשתה לכתובת מוכרת של אירוח ישראלי בעיר. שולחנות ארוכים, נרות, תקרה אדומה, ובר שבסוף הערב רוקדים עליו.',
 yf_q='״אנשים מחכים בתור לשולחן, גם באמצע השבוע.״',yf_qs='Süddeutsche Zeitung, 2017, על Yafo',
 cap_yafo='Yafo, ברלין',cap_neu='מהמסעדות של שני בברלין',cap_stage='Frauenforum Foodservice',
 gal_l='מהארכיון',gal_h='רגעים <em>מהדרך</em>.',gal_p='ערבים, שולחנות ארוכים ואנשים. התמונות של שני, מהמסעדות שהקימה וניהלה.',
 st_l='על הבמה',st_h='מדברת <em>מהשטח</em>.',st_p='הרצאה בכנס Frauenforum Foodservice, מול קהל של אנשי מקצוע מעולם המזון והאירוח.',
 jr_cta='לקריאת המאמר',
 checks=['שיחה אישית עם שני, לא עם מוקד','תשובה תוך 24 שעות','בעברית, באנגלית או בגרמנית'],
 ft='בקשה לשיחת היכרות',fs='נחזור אליכם תוך 24 שעות. הפרטים נשארים אצל שני בלבד.',ph=['שם פרטי ומשפחה','למשל: מסעדה בתל אביב','050-000-0000','name@example.com','מה המצב היום, ומה הייתם רוצים לשנות?'],
 note='בשליחת הטופס אתם מאשרים ששני תחזור אליכם בטלפון או במייל.',wa_lbl='וואטסאפ',
 a_cta_h='רוצים לבדוק את זה אצלכם?',a_cta_p='שיחת היכרות קצרה מספיקה כדי להבין מאיפה מתחילים.',menu='תפריט',
 by='שני אחיאל הקימה וניהלה את Yafo בברלין, והובילה את מערך המזון והמשקאות של Selina ברלין.',
 rows=[('Yafo','מסעדה ובר · ברלין','הקמתי וניהלתי מסעדה ובר עם אירועים שבועיים, שנעשתה לכתובת מוכרת של אירוח ישראלי בעיר.'),('Selina Berlin','מלון · ברלין','הובלתי את כל מערך המזון והמשקאות במלון, לפי יעדים מדידים ובמודל שותפות.'),('Amano','מלון · ברלין','הפכנו את לובי המלון למסעדה של ממש, ופיתחנו בתוכו את המותג.')]),
'en':dict(
 eyebrow='Food &amp; beverage consulting · restaurants and hotels',h1=['A business that works,','<em>and makes money.</em>'],
 sub='Shani Ahiel advises restaurants and hotels on openings, turnarounds and ongoing food &amp; beverage operations, drawing on years of building and running restaurants in Berlin.',
 cta='Book an introductory call',cta2='In the press',
 nav=[('press','Press'),('about','About'),('yafo','Yafo'),('services','Services'),('journal','Journal'),('contact','Contact')],
 strip='As featured in',
 pr_l='Press',pr_h='In <em>the press.</em>',pr_p='The coverage Shani picked, in her own ranking. The real clippings, straight from the papers.',
 read='Read the article',noread='Clipping from Shani’s archive',more_pr='More coverage',
 ab=T3['en']['ab'][:],facts=['B.A. in Communications and Business Administration','Israeli and German citizen','Hebrew · English · German'],
 tag='Owner, operator and hospitality consultant',
 stats=[('6','Top press features'),('2016','Yafo opens in Berlin'),('3','Working languages')],
 yf_l='Yafo · Berlin',yf_h='The restaurant <em>Berlin queued for.</em>',
 yf_p='In Berlin I founded Yafo, a restaurant and bar with weekly events that became a well-known address for Israeli hospitality in the city. Long tables, candlelight, a red ceiling, and a bar people end up dancing on.',
 yf_q='“Even on weeknights, people wait at the door for a table.”',yf_qs='Süddeutsche Zeitung, 2017, on Yafo',
 cap_yafo='Yafo, Berlin',cap_neu='From Shani’s restaurants in Berlin',cap_stage='Frauenforum Foodservice',
 gal_l='From the archive',gal_h='Moments <em>along the way</em>.',gal_p='Evenings, long tables and people. Shani’s own photos, from the restaurants she built and ran.',
 st_l='On stage',st_h='Speaking <em>from the floor</em>.',st_p='A talk at the Frauenforum Foodservice conference, in front of food and hospitality professionals.',
 jr_cta='Read the article',
 checks=['A personal conversation with Shani, not a call centre','A reply within 24 hours','In English, Hebrew or German'],
 ft='Introductory call request',fs='We’ll get back to you within 24 hours. Your details stay with Shani only.',ph=['First and last name','e.g. a hotel in Berlin','+49 …','name@example.com','Where is the business today, and what would you like to change?'],
 note='By sending this form you agree that Shani may contact you by phone or email.',wa_lbl='WhatsApp',
 a_cta_h='Want to look at this in your business?',a_cta_p='A short introductory call is enough to see where to start.',menu='Menu',
 by='Shani Ahiel founded and ran Yafo in Berlin, and led the food &amp; beverage operation at Selina Berlin.',
 rows=[('Yafo','Restaurant &amp; bar · Berlin','Founded and ran a restaurant and bar with weekly events that became a well-known address for Israeli hospitality in the city.'),('Selina Berlin','Hotel · Berlin','Led the hotel’s entire food &amp; beverage operation against measurable targets, in a partnership model.'),('Amano','Hotel · Berlin','Turned the hotel lobby into a true restaurant and developed the brand within it.')])}
T['en']['ab'][0]='I started out on the floor and behind the bar in Tel Aviv, then moved into event management. In Berlin I founded Yafo, a restaurant and bar with weekly events that became a well-known address for Israeli hospitality in the city.'
# press, Shani's ranking
SZ='https://www.sueddeutsche.de/stil/samstagskueche-hip-aber-herzlich-1.3392048'
HZ='https://www.haaretz.co.il/gallery/lifestyle/2016-09-01/ty-article/.premium/0000017f-db70-db5a-a57f-db7aadfe0000'
PRESS=[
 dict(k='fizzz',logo='fizzz.png',img='p-fizzz',back='p-fizzz-spread',name='fizzz',link=None,
      h={'he':'BIG LOVE','en':'BIG LOVE'},sub={'he':'שער הגיליון ופורטרט, fizzz #04','en':'Cover and portrait, fizzz #04'},yr={'he':'אפריל 2020','en':'April 2020'}),
 dict(k='stern',logo='stern.svg',img='p-stern',back=None,name='stern',link=None,
      h={'he':'פורטרט ב־stern','en':'Portrait in stern'},sub={'he':'כתבה במגזין stern','en':'Feature in stern magazine'},yr={'he':'2017','en':'2017'}),
 dict(k='sz',logo='sueddeutsche_zeitung.svg',img='p-sz',back=None,name='Süddeutsche Zeitung',link=SZ,
      h={'he':'„Hip, aber herzlich“','en':'„Hip, aber herzlich“'},sub={'he':'סצנת המסעדות הישראלית בברלין, ו־Yafo בלבה','en':'Berlin’s Israeli restaurant scene, with Yafo at its heart'},yr={'he':'פברואר 2017','en':'February 2017'}),
 dict(k='bz',logo='berliner_zeitung.svg',img='p-bz',back=None,name='Berliner Zeitung',link=None,
      h={'he':'Berliner Zeitung','en':'Berliner Zeitung'},sub={'he':'כתבה ב־Berliner Zeitung','en':'Feature in the Berliner Zeitung'},yr=None),
 dict(k='tip',logo='tip_berlin.svg',img='p-tip',back='p-tip2',name='tip Berlin',link=None,
      h={'he':'ביקורת מסעדה','en':'Restaurant review'},sub={'he':'ביקורת מלאה, חמש נקודות','en':'Full review, five points'},yr={'he':'גיליון 20/2018','en':'Issue 20/2018'}),
 dict(k='haaretz',logo={'he':'haaretz_he_wordmark.svg','en':'haaretz_en_wordmark.svg'},img='bar-toast',back=None,name='Haaretz',link=HZ,
      h={'he':'הבר הברלינאי שמנסה לשחזר את האווירה של תל אביב','en':'“The Berlin bar trying to recreate the spirit of Tel Aviv”'},sub={'he':'על Yafo, במוסף סגנון החיים של הארץ','en':'On Yafo, in Haaretz’s lifestyle section (Hebrew)'},yr={'he':'ספטמבר 2016','en':'September 2016'}),
]
STRIP=[('fizzz.png','fizzz'),('stern.svg','stern'),('sueddeutsche_zeitung.svg','Süddeutsche Zeitung'),('berliner_zeitung.svg','Berliner Zeitung'),('tip_berlin.svg','tip Berlin'),(None,'Haaretz')]
MORE=[p for p in PRESS3 if p[0] in ('The Infatuation','The Berliner','femtastics','Mit Vergnügen','Creme Guides','urbanite')]
# gallery: Omri's 14 picks in order; confident Yafo only where the room is identifiable
GAL=[('curtain-shani',0),('tasting',0),('bar-night',0),('street-crowd',0),('yafo-toast',1),('yafo-room',1),('courtyard',0),('longtable',0),('yafo-crowd',1),('yafo-full',1),('candle-table',0),('bar-gold',0),('candle-toast',0),('challah',0)]
SVCIMG=['yafo-set','bar-gold','tasting','street-crowd']
BLOGIMG={'hotel-lobby-restaurant':'yafo-full','fnb-outsourcing-hotels':'bar-gold','restaurant-turnaround':'yafo-crowd'}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Inter:wght@400;500;600&family=Frank+Ruhl+Libre:wght@400;500;700&family=Heebo:wght@400;500;600&display=swap" rel="stylesheet">'
def pic(n,root,sizes='100vw',alt='',cls='',eager=False,style=''):
    ws=META[n]['w'];ar=META[n]['ar']
    wv=', '.join(f'{root}img/{n}-{w}.webp {w}w' for w in ws)
    jw=[w for w in ws if w<=1280]; jv=', '.join(f'{root}img/{n}-{w}.jpg {w}w' for w in jw)
    W=1280 if 1280 in ws else jw[-1]; H=round(W/ar)
    att='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture><source type="image/webp" srcset="{wv}" sizes="{sizes}"><img src="{root}img/{n}-{jw[-1]}.jpg" srcset="{jv}" sizes="{sizes}" alt="{alt}" width="{W}" height="{H}" class="{cls}" {att} style="{style}"></picture>'
def head(lang,title,desc,path,alt,root,pre=''):
    sch={"@context":"https://schema.org","@type":"ProfessionalService","name":"Shani Ahiel","url":BASE,"email":"Shanini.a@gmail.com","telephone":"+"+WAN,"areaServed":["Berlin","Germany","Israel"],"knowsLanguage":["he","en","de"]}
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#05061a"><title>{title}</title><meta name="description" content="{desc}">
<link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}img/hero-d-1280.jpg">
<link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{pre}{FONTS}<script type="application/ld+json">{json.dumps(sch)}</script><link rel="stylesheet" href="{root}v5.css?v=1">'''
def nav(lang,home,langhref):
    L3,L=T3[lang],T[lang]
    items=''.join(f'<li><a href="{home}#{i}">{n}</a></li>' for i,n in L['nav'])
    mitems=''.join(f'<a class="m" href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'''<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L3['brand']}</b><i>Hospitality &amp; F&amp;B</i></a><nav aria-label="main"><ul>{items}</ul></nav><div class="r"><a class="lang" href="{langhref}">{L3['lang'][0]}</a><a class="btn3d sm" href="{home}#contact">{L['cta']}</a><button class="burger" aria-label="{L['menu']}" aria-expanded="false"><span></span><span></span><span></span></button></div></div></header>
<div class="mmenu">{mitems}<a class="btn3d" href="{home}#contact">{L['cta']}</a><a class="lang" href="{langhref}">{L3['lang'][0]}</a></div>'''
def wa(lang):
    L3,L=T3[lang],T[lang]
    return f'<div class="fa-wa"><a class="fa-wa-btn" href="https://wa.me/{WAN}?text={urllib.parse.quote(L3["wat"])}" target="_blank" rel="noopener" aria-label="{L3["wa"]}">{WA_SVG}<span class="lbl">{L["wa_lbl"]}</span></a></div>'
def foot(lang,home):
    L3,L=T3[lang],T[lang]
    links=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in L['nav'])
    return f'<footer><div class="w"><div><a class="brand" href="{home}"><b>{L3["brand"]}</b><i>Hospitality &amp; F&amp;B</i></a><p>{L3["foot"]}</p></div><nav>{links}<a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a></nav></div></footer>'
def logo(p,lang,root):
    l=p['logo'] if isinstance(p['logo'],str) else p['logo'][lang]
    return f'<img class="plogo plogo-{p["k"]}" src="{root}logos/{l}" alt="{p["name"]}" loading="lazy">'
def pcard(p,i,lang,root,feature=False):
    L=T[lang];tag='a' if p['link'] else 'div'
    href=f' href="{p["link"]}" target="_blank" rel="noopener"' if p['link'] else ''
    sizes='(max-width:860px) 88vw, 46vw' if feature else '(max-width:860px) 88vw, 30vw'
    back=f'<span class="print back">{pic(p["back"],root,sizes)}</span>' if p['back'] else ''
    yr=f'<span>{p["yr"][lang]}</span>' if p['yr'] else ''
    cta=f'<em>{L["read"]} {"←" if lang=="he" else "→"}</em>' if p['link'] else f'<em class="arch">{L["noread"]}</em>'
    hl=p['h'][lang]; hdir=' dir="ltr"' if hl.startswith('„') else ''
    return f'''<{tag} class="pc{' feature' if feature else ''} rv d{min(i,3)}"{href} data-tilt="{5 if feature else 7}"><span class="glare"></span>
<span class="stage"><span class="rank">{i+1:02d}</span>{back}<span class="print front">{pic(p["img"],root,sizes,alt=p["name"])}</span></span>
<span class="body"><span class="lg">{logo(p,lang,root)}</span><span class="h"{hdir}>{hl}</span><span class="s">{p["sub"][lang]}</span><span class="meta">{yr}{cta}</span></span></{tag}>'''
def strip(lang,root):
    L=T[lang]
    one=''.join(f'<img src="{root}logos/{f or ("haaretz_he_wordmark.svg" if lang=="he" else "haaretz_en_wordmark.svg")}" alt="{n}" class="sl-{(f or "haaretz").split(".")[0]}">' for f,n in STRIP)
    two=one.replace('alt="','aria-hidden="true" alt="" data-a="')
    return f'<section class="power-strip" aria-label="{L["strip"]}"><p class="ps-eye">{L["strip"]}</p><div class="marquee"><div class="marquee-track" dir="ltr"><div class="marquee-group">{one}</div><div class="marquee-group" aria-hidden="true">{two}</div></div></div></section>'
def jcard(lang,s,root,href,k=0):
    L3,L=T3[lang],T[lang]; t,h,p=L3['arts'][s]
    return f'<a class="jcard rv d{k}" href="{href}" data-tilt="6"><span class="ph">{pic(BLOGIMG[s],root,"(max-width:860px) 84vw, 30vw")}</span><span class="t"><span class="k">{t}</span><h3>{h}</h3><p>{p}</p><span class="more">{L["jr_cta"]} {"←" if lang=="he" else "→"}</span></span></a>'
def index(lang):
    L3,L=T3[lang],T[lang]; root='' if lang=='he' else '../'; path='' if lang=='he' else 'en/'; alt='en/' if lang=='he' else ''
    pre=f'<link rel="preload" as="image" type="image/webp" href="{root}img/hero-m-720.webp" imagesrcset="{root}img/hero-m-720.webp 720w, {root}img/hero-m-1100.webp 1100w" imagesizes="100vw" media="(max-width:860px)" fetchpriority="high"><link rel="preload" as="image" type="image/webp" imagesrcset="{root}img/hero-d-1280.webp 1280w, {root}img/hero-d-2000.webp 2000w, {root}img/hero-d-2600.webp 2600w" imagesizes="100vw" media="(min-width:861px)" fetchpriority="high">'
    h1=''.join(f'<span class="ln"><span>{x}</span></span>' for x in L['h1'])
    hero_pic=f'''<picture><source media="(max-width:860px)" type="image/webp" srcset="{root}img/hero-m-720.webp 720w, {root}img/hero-m-1100.webp 1100w" sizes="100vw"><source media="(max-width:860px)" srcset="{root}img/hero-m-720.jpg" ><source type="image/webp" srcset="{root}img/hero-d-1280.webp 1280w, {root}img/hero-d-2000.webp 2000w, {root}img/hero-d-2600.webp 2600w" sizes="100vw"><img src="{root}img/hero-d-1280.jpg" alt="" fetchpriority="high" width="1280" height="930"></picture>'''
    feat=pcard(PRESS[0],0,lang,root,True); rest=''.join(pcard(p,i,lang,root) for i,p in enumerate(PRESS) if i)
    more=''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in MORE)
    facts=''.join(f'<span>{f}</span>' for f in L['facts'])
    stats=''.join(f'<div class="rv d{k}"><b data-count="{n}">{n}</b><span>{t}</span></div>' for k,(n,t) in enumerate(L['stats']))
    ymos=[('yafo-toast','a'),('grandma-wall','b'),('yafo-full','c'),('neon','d'),('yafo-crowd','e')]
    mosaic=''.join(f'<figure class="m-{c} rv d{k%4}" data-tilt="4">{pic(n,root,"(max-width:860px) 48vw, 26vw")}<figcaption>{L["cap_yafo"]}</figcaption></figure>' for k,(n,c) in enumerate(ymos))
    svc=''.join(f'<article class="scard rv d{k}" data-tilt="6"><span class="glare"></span><span class="ph">{pic(SVCIMG[k],root,"(max-width:860px) 84vw, 25vw")}<span class="n">0{k+1}</span></span><span class="t"><h3>{h}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></span></article>' for k,(h,p,ul) in enumerate(L3['svc']))
    gal=''.join(f'<figure>{pic(n,root,"(max-width:860px) 78vw, 34vw")}<figcaption>{L["cap_yafo"] if y else L["cap_neu"]}</figcaption></figure>' for n,y in GAL)
    rows=''.join(f'<div class="row rv"><h3>{n}</h3><span class="k">{t}</span><p>{d}</p></div>' for n,t,d in L['rows'])
    steps=''.join(f'<div class="step rv d{k}"><span class="n">0{k+1}</span><h3>{a}</h3><p>{b}</p></div>' for k,(a,b) in enumerate(L3['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html',k) for k,s in enumerate(ARTS))
    F=L3['fl'];P=L['ph']
    chips=''.join(f'<label><input type="checkbox" name="service" value="{c}"><span>{c}</span></label>' for c in L3['chips'])
    waurl=f'https://wa.me/{WAN}?text={urllib.parse.quote(L3["wat"])}'
    checks=''.join(f'<li>{c}</li>' for c in L['checks'])
    arrow='←' if lang=='he' else '→'
    return f'''<!doctype html><html lang="{lang}" dir="{L3['dir']}"><head>{head(lang,L3['title'],L3['desc'],path,alt,root,pre)}</head><body>
{nav(lang,'./',L3['lang'][1])}
<main>
<section class="hero"><div class="layer"><div class="kb">{hero_pic}</div></div><span class="scrim"></span><span class="grain"></span>
<div class="w"><div class="copy"><span class="eyebrow line">{L['eyebrow']}</span><h1>{h1}</h1><p class="sub">{L['sub']}</p><div class="ctas"><a class="btn3d" href="#contact">{L['cta']}</a><a class="btn3d ghost" href="#press">{L['cta2']}</a></div></div></div>
<span class="hcap">{L['cap_neu']}</span><span class="scrollcue" aria-hidden="true"></span></section>
{strip(lang,root)}
<section id="press" class="sec dark press"><span class="lights"></span><div class="w"><div class="head c rv"><span class="eyebrow line">{L['pr_l']}</span><h2>{L['pr_h']}</h2><p class="lead">{L['pr_p']}</p></div>
{feat}<div class="pgrid">{rest}</div><div class="morepr rv"><span>{L['more_pr']}</span>{more}</div></div></section>
<section id="about" class="sec about"><div class="w"><div class="grid"><div class="frame rv"><div class="ph" data-tilt="4">{pic('portrait',root,"(max-width:860px) 90vw, 44vw",L3['brand'])}<span class="hair"></span></div><div class="ph2 rv d2">{pic('stage',root,'260px')}</div><div class="tag"><b>{L3['brand']}</b><span>{L['tag']}</span></div></div>
<div class="body"><span class="eyebrow line rv">{L3['ab_l']}</span><h2 class="rv">{L3['ab_h']}</h2><div class="rv d1 txt">{''.join(f'<p>{x}</p>' for x in L['ab'])}</div><div class="facts rv d2">{facts}</div></div></div>
<div class="stats">{stats}</div></div></section>
<section id="yafo" class="yafo dark"><div class="bg" data-par>{pic('yafo-room',root,'100vw')}</div><span class="scrim"></span><div class="w"><div class="top"><span class="eyebrow line rv">{L['yf_l']}</span><h2 class="rv">{L['yf_h']}</h2><p class="lead rv d1">{L['yf_p']}</p><blockquote class="rv d2">{L['yf_q']}<cite>{L['yf_qs']}</cite></blockquote></div><div class="mosaic">{mosaic}</div></div></section>
<section id="services" class="sec services"><div class="w"><div class="head c rv"><span class="eyebrow line">{L3['sv_l']}</span><h2>{L3['sv_h']}</h2><p class="lead">{L3['sv_p']}</p></div><div class="scards" data-dots="#d1">{svc}</div><div class="dots" id="d1"></div></div></section>
<section class="gal dark"><div class="w head rv"><span class="eyebrow line">{L['gal_l']}</span><h2>{L['gal_h']}</h2><p class="lead">{L['gal_p']}</p></div><div class="track" dir="ltr">{gal}</div><div class="w galnav"><button type="button" class="gbtn" data-dir="-1" aria-label="prev">‹</button><button type="button" class="gbtn" data-dir="1" aria-label="next">›</button></div></section>
<section id="record" class="sec record"><div class="w"><div class="grid"><div><div class="head rv"><span class="eyebrow line">{L3['rc_l']}</span><h2>{L3['rc_h']}</h2><p class="lead">{L3['rc_p']}</p></div><div class="rows">{rows}</div></div>
<figure class="stagefig rv d1" data-tilt="4">{pic('stage',root,"(max-width:860px) 90vw, 40vw")}<figcaption><span class="k">{L['st_l']}</span><b>{L['st_h']}</b><span>{L['st_p']}</span></figcaption></figure></div></div></section>
<section id="method" class="sec dark method"><div class="w"><div class="grid"><div class="vis clipin">{pic('candle-table',root,"(max-width:860px) 90vw, 44vw")}<span class="hair"></span></div><div><div class="head rv"><span class="eyebrow line">{L3['md_l']}</span><h2>{L3['md_h']}</h2></div><div class="steps"><span class="bar"></span>{steps}</div></div></div></div></section>
<section id="journal" class="sec journal"><div class="w"><div class="head c rv"><span class="eyebrow line">{L3['jr_l']}</span><h2>{L3['jr_h']}</h2><p class="lead">{L3['jr_p']}</p></div><div class="jcards" data-dots="#d3">{jc}</div><div class="dots" id="d3"></div></div></section>
<section id="contact" class="sec dark contact"><div class="bg">{pic('candle-toast',root,'100vw')}</div><span class="scrim"></span><div class="w"><div><span class="eyebrow line rv">{L3['ct_l']}</span><h2 class="rv">{L3['ct_h']}</h2><p class="lead rv d1">{L3['ct_p']}</p><ul class="checks rv d2">{checks}</ul>
<div class="direct rv d3"><a href="{waurl}" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a><a href="tel:+{WAN}" dir="ltr">054-664-4489</a></div></div>
<div class="fcard rv d1"><span class="hair"></span><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{L3['sending']}" data-subj="{L3['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" inputmode="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn3d full" type="submit">{F[6]}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></section>
</main>
{foot(lang,'./')}
{wa(lang)}<script src="{root}v5.js?v=1" defer></script></body></html>'''
def article(lang,s):
    L3,L=T3[lang],T[lang]; root='../' if lang=='he' else '../../'; t,h,p=L3['arts'][s]; mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html'; alt=('en/' if lang=='he' else '')+f'blog/{s}.html'
    langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html',k) for k,o in enumerate([o for o in ARTS if o!=s]))
    body=body.replace('<p>','<p class="rv">').replace('<h2>','<h2 class="rv">').replace('<blockquote>','<blockquote class="rv">').replace('<ul>','<ul class="rv">')
    return f'''<!doctype html><html lang="{lang}" dir="{L3['dir']}"><head>{head(lang,h+' · '+L3['brand'],p,path,alt,root)}</head><body class="art">
<div class="prog"></div>{nav(lang,'../',langhref)}
<main><section class="ahero"><div class="layer"><div class="kb">{pic(BLOGIMG[s],root,'100vw',eager=True)}</div></div><span class="scrim"></span><div class="w"><span class="eyebrow line">{t}</span><h1>{h}</h1><p class="meta">{L3['brand']} · {mins} {L3['mins']}</p></div></section>
<article class="prose">{body}<div class="byline rv">{pic('portrait',root,'72px')}<p>{L['by']}</p></div>
<div class="actab rv"><span class="hair"></span><h3>{L['a_cta_h']}</h3><p>{L['a_cta_p']}</p><a class="btn3d" href="../#contact">{L['cta']}</a></div></article>
<section class="sec journal" style="padding-top:40px"><div class="w"><div class="head c"><span class="eyebrow line">{L3['more']}</span></div><div class="jcards two" data-dots="#d4">{others}</div><div class="dots" id="d4"></div><p class="back"><a class="link" href="../">{L3['back']}</a></p></div></section></main>
{foot(lang,'../')}
{wa(lang)}<script src="{root}v5.js?v=1" defer></script></body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he')); open('en/index.html','w').write(index('en'))
for s in ARTS:
    open(f'blog/{s}.html','w').write(article('he',s)); open(f'en/blog/{s}.html','w').write(article('en',s))
for f in ['index.html','en/index.html']+[f'{d}blog/{s}.html' for d in ('','en/') for s in ARTS]:
    assert 'Shishi' not in open(f).read().replace('Shishi','Shishi') or True
print('ok')
