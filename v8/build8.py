import json,urllib.parse,os,html as H
src7=open('../v7/build7.py').read().split("\nFONTS=")[0].replace('img/meta.json','img/meta.json')
ns={};exec(src7,ns)
for k in ['T3','BODY','ARTS','META','WA_SVG','D','VPH','VLOGO','PRESS','BLOGIMG','WAN','MAIL']: globals()[k]=ns[k]
BASE="https://gitteromri-ux.github.io/shani-ahiel/v8/";CV='8b'
# draft wording (her own) for hero + profile
X={'he':dict(me='שני אחיאל · יזמית ומנהלת בתחום האירוח, ברלין',h1='מסעדה שעובדת,<br><em>וגם מרוויחה.</em>',
  lead='אני עוזרת לבעלי מסעדות ויזמים להקים, לייצב ולפתח עסקי אירוח, על בסיס למעלה מעשור של ניהול והקמה של מסעדות, מותגים ואירועים.',
  cred=['Yafo','Shishi','Amano','Selina ברלין'],cred_l='הקימה וניהלה בברלין',
  pf_l='הפרופיל',pf_h='כל מה שאני מציעה, <em>עשיתי קודם בעצמי.</em>',
  pf_lead='התחלתי בשירות ובבר בתל אביב והתקדמתי לניהול אירועים. מאז הקמתי ונהלתי מסעדות בברלין, וליוויתי שיתופי פעולה עם רשתות מלונות.',
  cap1='על הבמה · הרצאה',cap2='שני אחיאל · ברלין',
  mo_h='לילות של Yafo ו־Shishi',mo_p='מאות אורחים בערב, אירועים שבועיים, חתונות ומסיבות בחצר.',
  vn_l='למה לעבוד איתי',vn_h='מקומות שהקמתי <em>וניהלתי.</em>',vn_p='את כל מה שאני מציעה עשיתי בעצמי, בברלין, כבעלים וכמנהלת. לחצו על מקום כדי לראות את התמונות.',
  sv_l='במה אני יכולה לעזור',sv_h='ארבעה מסלולים, <em>ושותפות אחת.</em>',open_g='לגלריה',
  hw_l='איך זה עובד',hw_h='תהליך פשוט, <em>בלי הפתעות.</em>'),
 'en':dict(me='Shani Ahiel · Hospitality entrepreneur and operator, Berlin',h1='A restaurant that works,<br><em>and makes money.</em>',
  lead='I help restaurant owners and founders open, stabilise and grow hospitality businesses, drawing on more than a decade of building and running restaurants, brands and events.',
  cred=['Yafo','Shishi','Amano','Selina Berlin'],cred_l='Built and ran in Berlin',
  pf_l='Profile',pf_h='Everything I offer, <em>I have done myself first.</em>',
  pf_lead='I started on the floor and behind the bar in Tel Aviv and moved up into event management. Since then I have opened and run restaurants in Berlin and led partnerships with hotel groups.',
  cap1='On stage · keynote',cap2='Shani Ahiel · Berlin',
  mo_h='Nights at Yafo and Shishi',mo_p='Hundreds of guests a night, weekly events, weddings and courtyard parties.',
  vn_l='Why work with me',vn_h='Places I built <em>and ran.</em>',vn_p='Everything I offer, I did myself, in Berlin, as an owner and operator. Tap a venue to see the photos.',
  sv_l='How I can help',sv_h='Four engagements, <em>one partnership.</em>',open_g='Open gallery',
  hw_l='How it works',hw_h='A simple process, <em>no surprises.</em>')}
SVCIMG=['yafo-room','tasting','yafo-full','courtyard']
MOSAIC=['yafo-crowd','courtyard','candle-table','bar-gold','street-crowd','yafo-toast','challah','longtable']
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500;600&family=Frank+Ruhl+Libre:wght@400;500;700&family=Heebo:wght@300;400;500;600&display=swap" rel="stylesheet">'
def pic(n,root,sizes='100vw',alt='',eager=False,cls=''):
    ws=META[n]['w'];ar=META[n]['ar'];jw=[w for w in ws if w<=1400]
    wv=', '.join(f'{root}img/{n}-{w}.webp {w}w' for w in ws);jv=', '.join(f'{root}img/{n}-{w}.jpg {w}w' for w in jw);W=jw[-1]
    att='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture><source type="image/webp" srcset="{wv}" sizes="{sizes}"><img src="{root}img/{n}-{W}.jpg" srcset="{jv}" sizes="{sizes}" alt="{alt}" width="{W}" height="{round(W/ar)}" class="{cls}" {att}></picture>'
def big(n,root): ws=META[n]['w'];return f'{root}img/{n}-{max(ws)}.webp'
def head(lang,title,desc,path,alt,root):
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0b0f2a"><title>{title}</title><meta name="description" content="{desc}"><link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:title" content="{title}"><meta property="og:image" content="{BASE}img/portrait-1400.jpg"><link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="{root}v8.css?v={CV}">'
NAV={'he':[('profile','הפרופיל'),('venues','המקומות'),('services','שירותים'),('press','עיתונות'),('process','תהליך'),('contact','צור קשר')],
     'en':[('profile','Profile'),('venues','Venues'),('services','Services'),('press','Press'),('process','Process'),('contact','Contact')]}
def nav(lang,home,langhref):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return f'<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav class="links">{items}</nav><div class="r"><a class="lang" href="{langhref}">{L["lang"][0]}</a><a class="btn sm" href="{home}#contact">{L["cta1"]}</a><button class="burger" aria-label="menu"><span></span><span></span></button></div></div></header><div class="mmenu">{items}<a class="lang" href="{langhref}">{L["lang"][0]}</a></div>'
def wa(lang): return f'<a class="fa-wa" href="https://wa.me/{WAN}?text={urllib.parse.quote(T3[lang]["wat"])}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>'
def foot(lang,home):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return f'<footer><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav>{items}</nav><p>© 2026 {L["brand"]} · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:+{WAN}" dir="ltr">054-6644489</a></p></div></footer>'
LB='<div class="lb" hidden><button class="lb-x" aria-label="close">×</button><button class="lb-p" aria-label="prev">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="next">›</button><p class="lb-note"></p></div>'
def eb(t): return f'<span class="eb">{t}</span>'
def jcard(lang,s,root,href):
    t,h,p=T3[lang]['arts'][s];return f'<a class="jc rv" href="{href}"><span class="ph">{pic(BLOGIMG[s],root,"(max-width:760px) 92vw, 380px")}</span><span class="t"><span class="k">{t}</span><b>{h}</b><span class="more">{D[lang]["jr_cta"]} {"←" if lang=="he" else "→"}</span></span></a>'
def index(lang):
    L=D[lang];Y=X[lang];root='' if lang=='he' else '../';path='' if lang=='he' else 'en/';alt='en/' if lang=='he' else '';ar='←' if lang=='he' else '→'
    stats=''.join(f'<div class="st rv"><b dir="ltr">'+(f'<span class="pre">{p}</span>' if p else '')+f'<span class="num" data-count="{n}">{n}</span></b><span class="sl">{t}</span></div>' for n,p,t in L['stats'])
    cred=''.join(f'<span>{c}</span>' for c in Y['cred'])
    tl=''.join(f'<li><span class="ty">{yr}</span><b>{t}</b></li>' for yr,t,d,im in L['story'])
    facts=''.join(f'<span>{f}</span>' for f in L['facts'])
    mosaic=''.join(f'<figure class="m{k} rv">{pic(n,root,"(max-width:760px) 50vw, 25vw")}</figure>' for k,n in enumerate(MOSAIC))
    # venues
    feat='';small=''
    for key,yr,name,kind,line in L['venues']:
        ph=VPH[key];lg=f'<img class="vl" src="{root}logos/{VLOGO[key].replace("-w","")}" alt="{name}">' if key in VLOGO else f'<span class="vwm">{name.split()[0]}</span>'
        y=f'<span class="y">{yr}</span>' if yr else ''
        if ph:
            g=json.dumps([[big(n,root),name] for n in ph])
            th=''.join(f'<span>{pic(n,root,"(max-width:760px) 30vw, 200px")}</span>' for n in ph[1:4])
            feat+=f'''<article class="vf2 v-{key} rv"><button type="button" class="vimg" data-g='{H.escape(g)}' aria-label="{name} – {L['photos']}">{pic(ph[0],root,"(max-width:900px) 100vw, 62vw",name)}<span class="vcount">{L['photos']} · {len(ph)}</span></button><div class="vbody">{lg}<span class="vk">{kind}</span>{y}<h3>{name}</h3><p>{line}</p><div class="vth">{th}</div><button type="button" class="go" data-g='{H.escape(g)}'>{Y['open_g']} <span>{ar}</span></button></div></article>'''
        else:
            small+=f'''<button type="button" class="vs v-{key} rv" data-g="[]" data-note="{L['soon']}"><span class="vsl">{lg}</span><span class="soon">{L['soon']}</span><span class="vk">{kind}</span>{y}<b>{name}</b></button>'''
    svc=''.join(f'''<article class="tier rv"><span class="tph">{pic(SVCIMG[k],root,"(max-width:760px) 92vw, 300px")}</span><span class="tb"><span class="no">0{k+1}</span><h3>{h}</h3><p class="tg">{p}</p><p class="for"><span>{L['for_l']}</span>{fo}</p><ul>'''+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a class="go" href="#contact">{go} <span>{ar}</span></a></span></article>' for k,(h,p,fo,ul,go) in enumerate(L['svc']))
    ospts=''.join(f'<li>{x}</li>' for x in L['os_pts'])
    strip=''.join(f'<img src="{root}logos/{f}" alt="{n}" class="s-{f.split(".")[0]}">' for f,n,*_ in PRESS)
    pcards=''
    for f,n,im,hl,yr,link in PRESS:
        g=json.dumps([[big(im,root),n]]);y=f'<span>{yr[lang]}</span>' if yr else ''
        lk=f'<a class="pl" href="{link}" target="_blank" rel="noopener">{"לכתבה" if lang=="he" else "Article"} ↗</a>' if link else ''
        pcards+=f'''<div class="pc rv"><button type="button" class="pth" data-g='{H.escape(g)}' aria-label="{n}">{pic(im,root,"(max-width:760px) 40vw, 220px",n)}</button><span class="pt"><img class="plg plg-{f.split('.')[0]}" src="{root}logos/{f}" alt="{n}"><span class="ph"{' dir="ltr"' if hl[lang].startswith('„') else ''}>{hl[lang]}</span><span class="pm">{y}{lk}</span></span></div>'''
    steps=''.join(f'<li class="rv"><span class="n">0{k+1}</span><div><b>{a}</b><span>{b}</span></div></li>' for k,(a,b) in enumerate(L['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html') for s in ARTS)
    F=T3[lang]['fl'];P=L['ph'];chips=''.join(f'<label><input type="checkbox" name="service" value="{c[0]}"><span>{c[0]}</span></label>' for c in L['svc'])
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(lang,'./',L['lang'][1])}<main>
<header class="hero"><div class="hcopy"><div class="hin"><p class="me">{Y['me']}</p><h1>{Y['h1']}</h1><p class="lead">{Y['lead']}</p><div class="cta"><a class="btn" href="#contact">{L['cta1']}</a><a class="btn ghost" href="#venues">{L['cta2']}</a></div><div class="cred"><span class="cl">{Y['cred_l']}</span><div>{cred}</div></div></div></div>
<figure class="hph"><picture><source type="image/webp" srcset="{root}img/portrait-800.webp 800w, {root}img/portrait-1400.webp 1400w, {root}img/portrait-2200.webp 2200w" sizes="(max-width:900px) 100vw, 56vw"><img src="{root}img/portrait-1400.jpg" alt="{L['brand']}" fetchpriority="high"></picture><figcaption>{Y['cap2']}</figcaption></figure></header>
<section class="sec paper profile" id="profile"><div class="w pg"><div class="pv"><figure class="p1 rv">{pic('stage',root,"(max-width:900px) 92vw, 560px",Y['cap1'])}<figcaption>{Y['cap1']}</figcaption></figure><figure class="p2 rv">{pic('bench',root,"(max-width:900px) 40vw, 220px",L['brand'])}</figure></div>
<div class="pt2">{eb(Y['pf_l'])}<h2 class="rv">{Y['pf_h']}</h2><p class="big rv">{Y['pf_lead']}</p>{''.join(f'<p class="rv">{x}</p>' for x in L['in_p'])}<blockquote class="rv">{L['quote']}<cite>{L['quote_s']}</cite></blockquote><div class="facts rv">{facts}</div></div></div>
<div class="w"><ol class="tline rv">{tl}</ol><div class="stats">{stats}</div></div></section>
<section class="moment" aria-label="{Y['mo_h']}"><div class="mhd w"><h2 class="rv">{Y['mo_h']}</h2><p class="rv">{Y['mo_p']}</p></div><div class="mosaic">{mosaic}</div></section>
<section class="sec sand venues-s" id="venues"><div class="w"><div class="hd">{eb(Y['vn_l'])}<h2 class="rv">{Y['vn_h']}</h2><p class="sub rv">{Y['vn_p']}</p></div><div class="feat">{feat}</div><div class="smalls">{small}</div></div></section>
<section class="sec paper services" id="services"><div class="w"><div class="hd">{eb(Y['sv_l'])}<h2 class="rv">{Y['sv_h']}</h2><p class="sub rv">{L['sv_p']}</p></div><div class="tiers">{svc}</div></div></section>
<section class="hotels"><div class="hv">{pic('candle-table',root,"(max-width:900px) 100vw, 50vw")}</div><div class="ht"><div class="hti">{eb(L['os_l'])}<h2 class="rv">{L['os_h']}</h2><p class="rv">{L['os_p']}</p><ul class="rv">{ospts}</ul><a class="btn" href="#contact">{L['cta1']}</a></div></div></section>
<section id="press" class="press"><div class="strip"><p>{L['strip']}</p><div class="mq"><div class="mt" dir="ltr"><div class="mg">{strip}</div><div class="mg" aria-hidden="true">{strip}</div></div></div></div><div class="pwrap"><div class="w"><div class="pgrid">{pcards}</div></div></div></section>
<section class="sec ivory process" id="process"><div class="w prc"><figure class="prv rv">{pic('bar-gold',root,"(max-width:900px) 92vw, 520px")}</figure><div>{eb(Y['hw_l'])}<h2 class="rv">{Y['hw_h']}</h2><ol class="steps">{steps}</ol><a class="btn" href="#contact">{L['cta1']}</a></div></div></section>
<section class="sec paper" id="journal"><div class="w"><div class="hd">{eb(L['jr_l'])}<h2 class="rv">{L['jr_h']}</h2></div><div class="jgrid">{jc}</div></div></section>
<section id="contact" class="contact"><div class="cv">{pic('yafo-full',root,"(max-width:900px) 100vw, 45vw")}</div><div class="cbox"><div class="cin rv">{eb(L['ct_l'])}<h2>{L['ct_h']}</h2><p class="sub">{L['ct_p']}</p><div class="cta"><a class="btn ghost" href="mailto:{MAIL}">{MAIL}</a><a class="btn ghost" href="tel:+{WAN}" dir="ltr">054-6644489</a></div>
<div class="form"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{T3[lang]['sending']}" data-subj="{T3[lang]['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn full" type="submit">{F[6]}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></div></section>
</main>{foot(lang,'./')}{wa(lang)}{LB}<script src="{root}v8.js?v={CV}" defer></script></body></html>'''
def article(lang,s):
    L=D[lang];L3=T3[lang];root='../' if lang=='he' else '../../';t,h,p=L3['arts'][s];mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html';alt=('en/' if lang=='he' else '')+f'blog/{s}.html';langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,h+' · '+L['brand'],p,path,alt,root)}</head><body class="art"><div class="prog"></div>{nav(lang,'../',langhref)}<main>
<header class="ahero"><div class="w"><p class="me">{t}</p><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L3['mins']}</p></div><figure class="aimg w">{pic(BLOGIMG[s],root,'(max-width:900px) 100vw, 1100px',eager=True)}</figure></header>
<article class="prose">{body}<div class="byline">{pic('portrait',root,'56px')}<p>{L3['by']}</p></div><div class="actab"><h3>{L['ct_h']}</h3><p>{L['ct_p']}</p><a class="btn" href="../#contact">{L['cta1']}</a></div></article>
<section class="sec ivory"><div class="w"><div class="hd"><h2>{L3['more']}</h2></div><div class="jgrid two">{others}</div><p class="back"><a href="../">{L3['back']}</a></p></div></section></main>{foot(lang,'../')}{wa(lang)}<script src="{root}v8.js?v={CV}" defer></script></body></html>'''
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
open('index.html','w').write(index('he'));open('en/index.html','w').write(index('en'))
for s in ARTS: open(f'blog/{s}.html','w').write(article('he',s));open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok')
