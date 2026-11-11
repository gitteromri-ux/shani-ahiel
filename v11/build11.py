import json,urllib.parse,os,html as H
src7=open('../v7/build7.py').read().split("\nFONTS=")[0]
ns={};exec(src7,ns)
for k in ['T3','BODY','ARTS','WA_SVG','D','VPH','VLOGO','PRESS','BLOGIMG','WAN','MAIL']: globals()[k]=ns[k]
ns2={};exec(open('../v8/build8.py').read().split('\nSVCIMG=')[0].replace("open('../v7/build7.py')","open('../v7/build7.py')"),ns2);X=ns2['X']
# Elevated F&B language, faithful to Shani's draft (no invented services)
D['he']['sv_h']='ארבעה מסלולים, <em>ושותפות אחת.</em>'
D['en']['sv_h']='Four engagements, <em>one partnership.</em>'
D['he']['svc']=[
 ('פיתוח קונספט והקמת מסעדה','מהרעיון ועד יום הפתיחה.','יזמים ובעלי מקום, לפני פתיחה',['תוכנית עסקית ותכנון','מיתוג וקונספט','בניית סטנדרטים תפעוליים'],'רוצה להקים עסק'),
 ('הבראה ושליטה בעלויות','כשהמספרים לא מסתדרים, מחזירים שליטה.','מסעדה מלאה שלא מרוויחה, או עסק שאיבד כיוון',['בקרת P&amp;L נכונה','שליטה בעלות עבודה','שליטה בעלות מזון'],'העסק שלי צריך סדר'),
 ('ניהול תפעול F&amp;B מקצה לקצה','לעסק שעובד ורוצה לצמוח ולהתעדכן.','מסעדות פעילות שרוצות לצמוח',['לוגיסטיקה ותפעול שוטף','פיתוח, סושיאל ואסטרטגיה','Hosting וחוויית אירוח','סדנאות לצוות ולבניית מחלקות חדשות'],'לליווי שוטף'),
 ('אירועים ומחלקת אירועים','הפקה והובלה של אירועים פרטיים ועסקיים, ובניית מחלקת אירועים בתוך עסק קיים.','מסעדות, מלונות וחברות',['הפקה ותפעול','בניית מחלקה והכשרת צוות'],'לתכנון אירוע'),
]
D['en']['svc']=[
 ('Concept development &amp; restaurant launch','From the idea to opening day.','Founders and owners before opening',['Business plan and planning','Branding and concept','Building operating standards'],'I want to open a business'),
 ('Turnaround and cost control','When the numbers don’t add up, we take back control.','A full room that isn’t profitable, or a business that lost its way',['Proper P&amp;L control','Labour cost control','Food cost control'],'My business needs order'),
 ('End-to-end F&amp;B operations','For a business that works and wants to grow and stay current.','Working restaurants ready to grow',['Logistics and day-to-day operations','Development, social media and strategy','Hosting and guest experience','Team workshops and new departments'],'Ongoing support'),
 ('Events and in-house events departments','Producing and leading private and corporate events, and building an events department inside an existing business.','Restaurants, hotels and companies',['Production and operations','Building a department and training the team'],'Plan an event'),
]
X['he']['sv_h']=D['he']['sv_h'];X['en']['sv_h']=D['en']['sv_h']

META=json.load(open('img/meta.json'))
BASE="https://gitteromri-ux.github.io/shani-ahiel/v11/";CV='11b'
VPH['shishi']=[n for n in VPH['shishi'] if not n.startswith('band')]
# dark venue marks for the light catalog
VLOGO={'yafo':'yafo.png','shishi':'shishi.png','selina':'selina.png'}
# Swappable hero reel. Change HERO to any keys from HERO_POOL (assets must exist).
HERO_POOL={
  'curtain':{'d':'hero-curtain','m':'hero-curtain-m',
    'cap':{'he':'שני אחיאל · ברלין','en':'Shani Ahiel · Berlin'},
    'alt':{'he':'שני אחיאל במסעדה עם וילון אדום ואורחים מאחוריה','en':'Shani Ahiel in the restaurant, red curtain and guests behind her'}},
  'stage':{'d':'hero-stage','m':'hero-stage-m',
    'cap':{'he':'Frauenforum Foodservice, ברלין','en':'Frauenforum Foodservice, Berlin'},
    'alt':{'he':'שני אחיאל על הבמה בשמלה אדומה מול קהל','en':'Shani Ahiel on stage in a red dress, speaking to an audience'}},
  'yafo':{'d':'hero-yafo','m':'hero-yafo-m',
    'cap':{'he':'Yafo · 200 מקומות ישיבה','en':'Yafo · 200 seats'},
    'alt':{'he':'חדר האוכל של Yafo מלא באורחים, מסגרות חלונות אדומות','en':'Yafo’s dining room full of guests, red window frames'}},
}
HERO=['curtain','stage','yafo']  # default reel; swap here
HCAP={'he':[HERO_POOL[k]['cap']['he'] for k in HERO],'en':[HERO_POOL[k]['cap']['en'] for k in HERO]}
# strongest, brighter photographs for the profile rail
RAIL=['yafo-toast','courtyard','longtable','bar-gold','tasting','street-crowd','challah','yafo-windows','candle-table','curtain-shani']
SVCIMG=['yafo-set','tasting','yafo-full','courtyard']
U={'he':dict(tab=['הגישה','הדרך'],drag='גררו',view='פתחו',next='הבא',prev='הקודם',scroll='גללו',gal='גלריה',swipe='החליקו'),
   'en':dict(tab=['Approach','The path'],drag='Drag',view='View',next='Next',prev='Previous',scroll='Scroll',gal='Gallery',swipe='Swipe')}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Frank+Ruhl+Libre:wght@400;500;700&family=Heebo:wght@300;400;500;600&family=Figtree:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'
def srcs(n,root):
    ws=META[n]['w'];return ', '.join(f'{root}img/{n}-{w}.webp {w}w' for w in ws),', '.join(f'{root}img/{n}-{w}.jpg {w}w' for w in ws)
def pic(n,root,sizes='100vw',alt='',eager=False,cls=''):
    ws=META[n]['w'];ar=META[n]['ar'];wv,jv=srcs(n,root);W=[w for w in ws if w<=1400][-1]
    att='fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture><source type="image/webp" srcset="{wv}" sizes="{sizes}"><img src="{root}img/{n}-{W}.jpg" srcset="{jv}" sizes="{sizes}" alt="{alt}" width="{W}" height="{round(W/ar)}" class="{cls}" {att}></picture>'
def heropic(key,root,eager=False):
    p=HERO_POOL[key]; d,m=p['d'],p['m']; alt=p['alt']
    def ss(n,ext):
        return ', '.join(f'{root}img/{n}-{w}.{ext} {w}w' for w in META[n]['w'])
    Wd=[w for w in META[d]['w'] if w<=1400][-1]; Wm=[w for w in META[m]['w'] if w<=1400][-1]
    att='fetchpriority="high" decoding="async"' if eager else 'decoding="async"'
    # art-direction: mobile crop first, then desktop; no lazy on hero (prevents blank frames)
    return (f'<picture>'
            f'<source type="image/webp" media="(max-width:900px)" srcset="{ss(m,"webp")}" sizes="100vw">'
            f'<source type="image/jpeg" media="(max-width:900px)" srcset="{ss(m,"jpg")}" sizes="100vw">'
            f'<source type="image/webp" srcset="{ss(d,"webp")}" sizes="100vw">'
            f'<img src="{root}img/{d}-{Wd}.jpg" srcset="{ss(d,"jpg")}" sizes="100vw" alt="{alt}" width="{Wd}" height="{round(Wd/META[d]["ar"])}" {att}>'
            f'</picture>')
def gl(names,root,cap): return H.escape(json.dumps([[f'{root}img/{n}-{max(META[n]["w"])}.webp',cap if isinstance(cap,str) else cap[i],f'{root}img/{n}-800.webp'] for i,n in enumerate(names)]))
def head(lang,title,desc,path,alt,root):
    he,en=(path,alt) if lang=='he' else (alt,path)
    og=f'{BASE}img/hero-curtain-1400.jpg'
    return f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#f3eee4"><title>{title}</title><meta name="description" content="{desc}"><link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:title" content="{title}"><meta property="og:image" content="{og}"><link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="{root}v11.css?v={CV}">'
NAV={'he':[('profile','הפרופיל'),('services','שירותים'),('process','תהליך'),('venues','המקומות'),('contact','צור קשר')],
     'en':[('profile','Profile'),('services','Services'),('process','Process'),('venues','Venues'),('contact','Contact')]}
def nav(lang,home,langhref):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return f'<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav class="links">{items}</nav><div class="r"><a class="lang" href="{langhref}">{L["lang"][0]}</a><a class="btn sm mag" href="{home}#contact"><span>{L["cta1"]}</span></a><button class="burger" aria-label="menu"><span></span><span></span></button></div></div></header><div class="mmenu">{items}<a class="lang" href="{langhref}">{L["lang"][0]}</a></div>'
STICK={'he':('בואו נדבר על העסק שלכם','בואו נדבר','זמינה בוואטסאפ'),
       'en':('Let’s talk about your business','Let’s talk','Available on WhatsApp')}
def wa(lang):
    lab=STICK[lang][2]
    return (f'<a class="fa-wa" href="https://wa.me/{WAN}?text={urllib.parse.quote(T3[lang]["wat"])}" target="_blank" rel="noopener" aria-label="{lab}">'
            f'{WA_SVG}<span class="label">{lab}</span></a>')
def stick(lang,home):
    t,cta,_=STICK[lang]
    return f'<aside class="stick" id="stick"><div class="w"><p>{t}</p><a class="btn sm mag" href="{home}#contact"><span>{cta}</span></a></div></aside>'

def foot(lang,home):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return f'<footer><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav>{items}</nav><p>© 2026 {L["brand"]} · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:+{WAN}" dir="ltr">054-6644489</a></p></div></footer>'
def LB(lang): return f'<div class="lb" hidden role="dialog" aria-modal="true"><div class="lb-top"><span class="lb-c"></span><button class="lb-x" aria-label="close">×</button></div><div class="lb-stage"><img class="lb-img" alt=""></div><button class="lb-p" aria-label="{U[lang]["prev"]}">‹</button><button class="lb-n" aria-label="{U[lang]["next"]}">›</button><div class="lb-cap"></div><div class="lb-th"></div><p class="lb-note"></p></div>'
def eb(t): return f'<span class="eb">{t}</span>'
def slider(cards,cls='',desk='',label=''):
    d=f' data-desk="{desk}"' if desk else ''
    return f'<div class="sl {cls}"{d}><div class="trk" tabindex="0" aria-label="{label}" data-cur="drag">{cards}</div><div class="slc-ui"><div class="dots"></div><div class="bar"><i></i></div><div class="arr"><button class="ap" aria-label="prev"></button><button class="an" aria-label="next"></button></div></div></div>'
def jcard(lang,s,root,href):
    t,h,p=T3[lang]['arts'][s];ar="←" if lang=="he" else "→"
    return f'<a class="jc c" href="{href}"><span class="ph">{pic(BLOGIMG[s],root,"(max-width:760px) 78vw, 400px")}</span><span class="t"><span class="k">{t}</span><b>{h}</b><span class="more">{D[lang]["jr_cta"]} {ar}</span></span></a>'
def scripts(root):
    return f'<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.7/dist/gsap.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.7/dist/ScrollTrigger.min.js" defer></script><script src="{root}v11.js?v={CV}" defer></script>'
def index(lang):
    L=D[lang];Y=X[lang];V=U[lang];root='' if lang=='he' else '../';path='' if lang=='he' else 'en/';alt='en/' if lang=='he' else '';ar='←' if lang=='he' else '→'
    slides=''.join(f'<div class="hs{" on" if k==0 else ""}" data-hero="{n}">{heropic(n,root,eager=True)}</div>' for k,n in enumerate(HERO))
    hbars=''.join(f'<button class="hd{" on" if k==0 else ""}" aria-label="{HCAP[lang][k]}"></button>' for k in range(len(HERO)))
    stats=''.join(f'<div class="st"><b dir="ltr">'+(f'<span class="pre">{p}</span>' if p else '')+f'<span data-count="{n}">{n}</span></b><span>{t}</span></div>' for n,p,t in L['stats'])
    pw,pj=srcs('portrait-c',root)
    cred=' · '.join(Y['cred'])
    # profile
    pcards=f'<figure class="c pimg">{pic("stage",root,"(max-width:900px) 78vw, 420px",Y["cap1"])}<figcaption>{Y["cap1"]}</figcaption></figure>'
    pcards+=''.join(f'<div class="c ptxt"><span class="pn">0{k+1}</span><p>{x}</p></div>' for k,x in enumerate(L['in_p']))
    pcards+=f'<blockquote class="c pq"><p>{L["quote"]}</p><cite>{L["quote_s"]}</cite></blockquote>'
    tcards=''.join(f'<div class="c tc{" ti" if im else ""}">'+(f'<span class="tim">{pic(im,root,"(max-width:900px) 70vw, 300px")}</span>' if im else '')+f'<span class="ty">{yr}</span><b>{t}</b><p>{d}</p></div>' for yr,t,d,im in L['story'])
    facts=''.join(f'<span>{f}</span>' for f in L['facts'])
    # photo rail
    mg=gl(RAIL,root,Y['mo_h'])
    mos=''.join(f'<button type="button" class="c mo m{k%3}" data-g="{mg}" data-i="{k}" aria-label="{Y["mo_h"]}">{pic(n,root,"(max-width:760px) 72vw, 28vw")}</button>' for k,n in enumerate(RAIL))
    # venues
    vc=''
    for key,yr,name,kind,line in L['venues']:
        ph=VPH[key];lg=f'<img class="vl" src="{root}logos/{VLOGO[key]}" alt="{name}">' if key in VLOGO else f'<span class="vwm">{name.split()[0]}</span>'
        if ph:
            thumbs=''.join(f'<span>{pic(n,root,"120px")}</span>' for n in ph[1:4])
            vc+=f'''<article class="c vf v-{key}"><button type="button" class="vbtn" data-g="{gl(ph,root,name)}" aria-label="{name} – {L['photos']}"><span class="vimg">{pic(ph[0],root,"(max-width:760px) 84vw, 560px",name)}<span class="vth">{thumbs}<em>+{max(0,len(ph)-4)}</em></span></span><span class="vb">{lg}<span class="vk">{kind}{' · '+yr if yr else ''}</span><b class="vn">{name}</b><span class="vp">{line}</span><span class="go">{Y['open_g']} · {len(ph)} {L['photos']} <i>{ar}</i></span></span></button></article>'''
        else:
            vc+=f'''<article class="c vs v-{key}"><button type="button" class="vbtn" data-g="[]" data-note="{L['soon']}"><span class="vsl">{lg}</span><span class="vk">{kind}{' · '+yr if yr else ''}</span><b class="vn">{name}</b><span class="vp">{line if key!='opera' else ''}</span><span class="soon">{L['soon']}</span></button></article>'''
    svc=''.join(f'''<article class="c tier"><span class="tph">{pic(SVCIMG[k],root,"(max-width:760px) 80vw, 320px")}<span class="no">0{k+1}</span></span><span class="tb"><h3>{h}</h3><p class="tg">{p}</p><p class="for"><span>{L['for_l']}</span>{fo}</p><ul>'''+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a class="go" href="#contact">{go} <i>{ar}</i></a></span></article>' for k,(h,p,fo,ul,go) in enumerate(L['svc']))
    ospts=''.join(f'<li>{x}</li>' for x in L['os_pts'])
    # compact press strip — ink logos, optional clipping lightbox, one real article link
    plogs=''
    for f,n,im,hl,yr,link in PRESS:
        g=gl([im],root,n)
        inner=f'<img class="s-{f.split(".")[0]}" src="{root}logos/ink/{f}" alt="{n}">'
        if link:
            plogs+=f'<a href="{link}" target="_blank" rel="noopener" aria-label="{n}">{inner}</a>'
        else:
            plogs+=f'<button type="button" data-g="{g}" aria-label="{n}">{inner}</button>'
    steps=''.join(f'<li class="c st2"><span class="n">0{k+1}</span><b>{a}</b><span>{b}</span></li>' for k,(a,b) in enumerate(L['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html') for s in ARTS)
    F=T3[lang]['fl'];P=L['ph'];chips=''.join(f'<label><input type="checkbox" name="service" value="{c[0]}"><span>{c[0]}</span></label>' for c in L['svc'])
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(lang,'./',L['lang'][1])}<main>
<header class="hero">
 <div class="hvis" aria-hidden="false"><div class="hstage">{slides}</div></div>
 <div class="hgrid w">
  <div class="hcopy glass">
   <p class="me ri">{Y['me']}</p>
   <h1 class="ri"><span>{Y['h1']}</span></h1>
   <p class="lead ri">{Y['lead']}</p>
   <p class="cred ri"><b>{Y['cred_l']}</b>{cred}</p>
   <div class="cta ri"><a class="btn mag" href="#contact"><span>{L['cta1']}</span></a><a class="btn ghost mag" href="#venues"><span>{L['cta2']}</span></a></div>
  </div>
  <div class="hfoot">
   <div class="hstats glass">{stats}</div>
   <div class="hnav"><span class="hcap">{HCAP[lang][0]}</span><div class="hdots">{hbars}</div></div>
  </div>
 </div>
 <div class="hcaps" hidden>{json.dumps(HCAP[lang],ensure_ascii=False)}</div>
</header>
<section class="sec paper profile" id="profile"><div class="w">
 <div class="phd">{eb(Y['pf_l'])}<h2 class="rv">{Y['pf_h']}</h2><p class="big rv">{Y['pf_lead']}</p><div class="facts rv">{facts}</div></div>
 <div class="tabs" role="tablist"><button class="on" data-t="0">{V['tab'][0]}</button><button data-t="1">{V['tab'][1]}</button></div>
 <div class="tp on" data-p="0">{slider(pcards,'s-prof','',V['tab'][0])}</div>
 <div class="tp" data-p="1">{slider(tcards,'s-tl','',V['tab'][1])}</div>
 <div class="rail"><div class="mhd">{eb(V['gal'])}<h2 class="rv">{Y['mo_h']}</h2><p class="rv">{Y['mo_p']}</p></div>{slider(mos,'s-mo','',Y['mo_h'])}</div>
</div></section>
<section class="sec ivory services" id="services"><div class="w"><div class="hd">{eb(Y['sv_l'])}<h2 class="rv">{Y['sv_h']}</h2><p class="sub rv">{L['sv_p']}</p></div>{slider(svc,'s-svc','grid4',Y['sv_l'])}</div></section>
<section class="erupt" aria-label="quote"><div class="eruph">{pic('yafo-full',root,"100vw")}</div><div class="w"><blockquote class="glass eq"><p>{L["quote"]}</p><cite>{L["quote_s"]}</cite></blockquote></div></section>
<section class="sec sand hotels"><div class="hrow w"><figure class="hv" data-par>{pic('tasting',root,"(max-width:900px) 100vw, 50vw")}</figure><div class="hti glass">{eb(L['os_l'])}<h2 class="rv">{L['os_h']}</h2><p class="rv">{L['os_p']}</p><ul class="rv">{ospts}</ul><a class="btn mag" href="#contact"><span>{L['cta1']}</span></a></div></div></section>
<section class="sec ivory process" id="process"><div class="w prc"><figure class="prv" data-par>{pic('bar-gold',root,"(max-width:900px) 92vw, 520px")}</figure><div class="prt glass">{eb(Y['hw_l'])}<h2 class="rv">{Y['hw_h']}</h2>{slider(steps,'s-st','list',Y['hw_l']).replace('<div class="trk"','<ol class="trk"').replace('</div><div class="slc-ui">','</ol><div class="slc-ui">',1)}<a class="btn mag" href="#contact"><span>{L['cta1']}</span></a></div></div></section>
<section id="press" class="sec paper press"><div class="w strip">{eb(L['strip'])}<div class="plogs">{plogs}</div></div></section>
<section class="sec sand venues" id="venues"><div class="w"><div class="hd">{eb(Y['vn_l'])}<h2 class="rv">{Y['vn_h']}</h2><p class="sub rv">{Y['vn_p']}</p></div></div>{slider(vc,'s-ven','',Y['vn_l'])}</section>
<section class="sec ivory journal" id="journal"><div class="w"><div class="hd">{eb(L['jr_l'])}<h2 class="rv">{L['jr_h']}</h2></div>{slider(jc,'s-jr','grid3',L['jr_h'])}</div></section>
<section id="contact" class="sec paper contact"><div class="crow w"><figure class="cv" data-par>{pic('courtyard',root,"(max-width:900px) 100vw, 45vw")}</figure><div class="cbox glass">{eb(L['ct_l'])}<h2 class="rv">{L['ct_h']}</h2><p class="sub">{L['ct_p']}</p><div class="cta2"><a class="btn ghost sm" href="mailto:{MAIL}">{MAIL}</a><a class="btn ghost sm" href="tel:+{WAN}" dir="ltr">054-6644489</a></div>
<div class="form"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{T3[lang]['sending']}" data-subj="{T3[lang]['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[4] if False else P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend><div>{chips}</div></fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" rows="2" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn full mag" type="submit"><span>{F[6]}</span></button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></div></section>
</main>{foot(lang,'./')}{stick(lang,'./')}{wa(lang)}{LB(lang)}{scripts(root)}</body></html>'''
def article(lang,s):
    L=D[lang];L3=T3[lang];root='../' if lang=='he' else '../../';t,h,p=L3['arts'][s];mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html';alt=('en/' if lang=='he' else '')+f'blog/{s}.html';langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,h+' · '+L['brand'],p,path,alt,root)}</head><body class="art"><div class="prog"></div>{nav(lang,'../',langhref)}<main>
<header class="ahero"><div class="w"><p class="me">{t}</p><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L3['mins']}</p></div><figure class="aimg w">{pic(BLOGIMG[s],root,'(max-width:900px) 100vw, 1100px',eager=True)}</figure></header>
<article class="prose">{body}<div class="byline">{pic('portrait-c',root,'56px')}<p>{L3['by']}</p></div><div class="actab"><h3>{L['ct_h']}</h3><p>{L['ct_p']}</p><a class="btn" href="../#contact"><span>{L['cta1']}</span></a></div></article>
<section class="sec ivory"><div class="w"><div class="hd"><h2>{L3['more']}</h2></div>{slider(others,'s-jr','grid2','')}<p class="back"><a href="../">{L3['back']}</a></p></div></section></main>{foot(lang,'../')}{stick(lang,'../')}{wa(lang)}{scripts(root)}</body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he'));open('en/index.html','w').write(index('en'))
for s in ARTS: open(f'blog/{s}.html','w').write(article('he',s));open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok',CV)
