# v14 — final luxury design pass. Content comes from build11 (Shani's texts, unchanged);
# only markup/design changes, plus the agreed H1 and Shani's confirmed name "Ofra".
import json,urllib.parse,os,html as H
_src=open('build11.py').read().split("\ndef index(")[0]
_ns={};exec(_src,_ns);globals().update({k:v for k,v in _ns.items() if not k.startswith('__')})
BASE="https://gitteromri-ux.github.io/shani-ahiel/v14/";CV='14a'
H1={'he':['להקים.','לייצב.','לפתח.'],'en':['Build.','Stabilize.','Grow.']}
# Shani confirmed in the group (Nov 11): the venue is "Ofra"
for lg in ('he','en'):
    D[lg]['venues']=[(k,y,('Ofra' if k=='opera' else n),kd,l) for k,y,n,kd,l in D[lg]['venues']]
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Frank+Ruhl+Libre:wght@300;400;500&family=Heebo:wght@300;400;500;600&family=Figtree:wght@300;400;500;600&display=swap" rel="stylesheet">')
LB_={'he':dict(slide='תמונה',of='מתוך',next='הבא',prev='הקודם',story='הדרך',nums=['I','II','III','IV'],sec=['הפרופיל','שירותים','למלונות','תהליך','המקומות','מגזין','צור קשר'],scroll='לגלילה'),
     'en':dict(slide='Image',of='of',next='Next',prev='Previous',story='The path',nums=['I','II','III','IV'],sec=['Profile','Services','For hotels','Process','Venues','Journal','Contact'],scroll='Scroll')}
ARW='<svg class="arw" viewBox="0 0 28 10" aria-hidden="true"><path d="M0 5h26M22 1l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1"/></svg>'
def head(lang,title,desc,path,alt,root):
    he,en=(path,alt) if lang=='he' else (alt,path)
    return (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#f6f2ea"><title>{title}</title><meta name="description" content="{desc}"><link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}"><meta property="og:title" content="{title}"><meta property="og:image" content="{BASE}img/hero-curtain-1400.jpg"><link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}'
            f'<link rel="preload" as="image" type="image/webp" href="{root}img/hero-curtain-m-800.webp" media="(max-width:900px)"><link rel="preload" as="image" type="image/webp" href="{root}img/hero-curtain-1400.webp" media="(min-width:901px)">'
            f'<link rel="stylesheet" href="{root}v14.css?v={CV}"><link rel="stylesheet" href="{root}review.css?v={CV}">')
def btn(t,href,cls='',extra=''):
    return f'<a class="btn {cls}" href="{href}"{extra}><span>{t}</span>{ARW}</a>'
def nav(lang,home,langhref):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return (f'<header class="nav"><div class="w"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a>'
            f'<nav class="links">{items}</nav><div class="r"><a class="lang" href="{langhref}">{L["lang"][0]}</a>{btn(L["cta1"],home+"#contact","sm")}'
            f'<button class="burger" aria-label="menu"><span></span><span></span></button></div></div></header><div class="mmenu">{items}<a class="lang" href="{langhref}">{L["lang"][0]}</a></div>')
def stick(lang,home):
    t,cta,_=STICK[lang]
    return f'<aside class="stick hide" id="stick"><div class="sw"><p>{t}</p>{btn(cta,home+"#contact","sm light")}</div></aside>'
def foot(lang,home):
    L=D[lang];items=''.join(f'<a href="{home}#{i}">{n}</a>' for i,n in NAV[lang])
    return (f'<footer><div class="w"><div class="fb"><a class="brand" href="{home}"><b>{L["brand"]}</b><i>Hospitality &amp; F&amp;B · Berlin</i></a><nav>{items}</nav></div>'
            f'<p class="fc"><span>© 2026 {L["brand"]}</span><a href="mailto:{MAIL}">{MAIL}</a><a href="tel:+{WAN}" dir="ltr">054-6644489</a></p></div></footer>')
def eb(n,t): return f'<p class="eb"><span class="ebn">{n}</span><span class="ebl"></span><span class="ebt">{t}</span></p>'
def slider(cards,cls='',desk='',label='',tag='div'):
    d=f' data-desk="{desk}"' if desk else ''
    return (f'<div class="sl {cls}"{d}><{tag} class="trk" tabindex="0" aria-label="{label}">{cards}</{tag}>'
            f'<div class="slc-ui"><div class="bar"><i></i></div><div class="arr"><button class="ap" aria-label="prev">{ARW}</button><button class="an" aria-label="next">{ARW}</button></div></div></div>')
def jcard(lang,s,root,href):
    t,h,p=T3[lang]['arts'][s]
    return f'<a class="jc" href="{href}"><span class="ph">{pic(BLOGIMG[s],root,"(max-width:760px) 80vw, 400px")}</span><span class="k">{t}</span><b>{h}</b><span class="dk">{p}</span><span class="more">{D[lang]["jr_cta"]}{ARW}</span></a>'
def scripts(root):
    return f'<script src="{root}review.js?v={CV}" defer></script><script src="{root}v14.js?v={CV}" defer></script>'
def index(lang):
    L=D[lang];Y=X[lang];V=LB_[lang];root='' if lang=='he' else '../';path='' if lang=='he' else 'en/';alt='en/' if lang=='he' else ''
    S=V['sec']
    slides=''.join(f'<div class="hs{" on" if k==0 else ""}" data-hero="{n}">{heropic(n,root,eager=(k==0))}</div>' for k,n in enumerate(HERO))
    for n in HERO:  # heropic returns dict alt in v11 – use the right language
        pass
    hbars=''.join(f'<button class="hdot{" on" if k==0 else ""}" aria-label="{HCAP[lang][k]}"><i></i></button>' for k in range(len(HERO)))
    stats=''.join(f'<li><b dir="ltr">'+(f'<em>{p}</em>' if p else '')+f'{n}</b><span>{t}</span></li>' for n,p,t in L['stats'])
    h1=''.join(f'<span class="l l{k+1}"><span>{w}</span></span>' for k,w in enumerate(H1[lang]))
    cred=''.join(f'<li>{c}</li>' for c in Y['cred'])
    facts=''.join(f'<li>{f}</li>' for f in L['facts'])
    inp=''.join(f'<p>{x}</p>' for x in L['in_p'])
    # path / timeline
    tcards=''.join(f'<li class="tc{" ti" if im else ""}"><span class="ty" dir="auto">{yr}</span><span class="tl"></span>'+(f'<span class="tim">{pic(im,root,"(max-width:900px) 64vw, 300px")}</span>' if im else '')+f'<b>{t}</b><p>{d}</p></li>' for yr,t,d,im in L['story'])
    mg=gl(RAIL,root,Y['mo_h'])
    mos=''.join(f'<button type="button" class="mo m{k%4}" data-g="{mg}" data-i="{k}" aria-label="{Y["mo_h"]}">{pic(n,root,"(max-width:760px) 70vw, 30vw")}</button>' for k,n in enumerate(RAIL))
    # venues
    vf='';vs=''
    for key,yr,name,kind,line in L['venues']:
        ph=VPH[key];lg=f'<img class="vl" src="{root}logos/{VLOGO[key]}" alt="{name}" loading="lazy">' if key in VLOGO else ''
        meta=f'<span class="vk">{kind}{" · <span dir=ltr>"+yr+"</span>" if yr else ""}</span>'
        if ph:
            vf+=(f'<article class="vf v-{key}"><button type="button" class="vbtn" data-g="{gl(ph,root,name)}" aria-label="{name} – {L["photos"]}">'
                 f'<span class="vimg">{pic(ph[0],root,"(max-width:760px) 84vw, 640px",name)}<span class="vcount" dir="ltr">{len(ph)}</span></span>'
                 f'<span class="vb">{meta}<b class="vn">{name}</b><span class="vp">{line}</span><span class="go">{Y["open_g"]} · {len(ph)} {L["photos"]}{ARW}</span></span>{lg}</button></article>')
        else:
            vs+=(f'<article class="vs v-{key}"><div class="vsi">{meta}<b class="vn">{name}</b>'
                 f'<span class="vp">{line if key!="opera" else ""}</span><span class="soon">{L["soon"]}</span>{lg}</div></article>')
    svc=''.join(f'''<article class="tier"><span class="tph">{pic(SVCIMG[k],root,"(max-width:760px) 80vw, 340px")}</span><span class="no">{V['nums'][k]}</span><h3>{h}</h3><p class="tg">{p}</p><p class="for"><span>{L['for_l']}</span>{fo}</p><ul>'''+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a class="go" href="#contact">{go}{ARW}</a></article>' for k,(h,p,fo,ul,go) in enumerate(L['svc']))
    ospts=''.join(f'<li><span dir="ltr">0{k+1}</span>{x}</li>' for k,x in enumerate(L['os_pts']))
    plogs=''
    for f,n,im,hl,yr,link in PRESS:
        g=gl([im],root,n);inner=f'<img class="s-{f.split(".")[0]}" src="{root}logos/ink/{f}" alt="{n}" loading="lazy">'
        plogs+=(f'<li><a href="{link}" target="_blank" rel="noopener" aria-label="{n}">{inner}</a></li>' if link else f'<li><button type="button" data-g="{g}" aria-label="{n}">{inner}</button></li>')
    steps=''.join(f'<li><span class="n" dir="ltr">0{k+1}</span><span class="sl1"></span><b>{a}</b><span class="sd">{b}</span></li>' for k,(a,b) in enumerate(L['steps']))
    jc=''.join(jcard(lang,s,root,f'blog/{s}.html') for s in ARTS)
    F=T3[lang]['fl'];P=L['ph'];chips=''.join(f'<label><input type="checkbox" name="service" value="{c[0]}"><span>{c[0]}</span></label>' for c in L['svc'])
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(lang,'./',L['lang'][1])}<main>
<header class="hero" id="hero">
 <div class="hvis"><div class="hstage">{slides}</div>
  <div class="hpanel glass" data-slide="0">
   <p class="me ri">{Y['me']}</p>
   <h1 class="ri">{h1}</h1>
   <span class="hr ri"></span>
   <p class="lead ri">{Y['lead']}</p>
   <div class="cta ri">{btn(L['cta1'],'#contact','solid')}<a class="tlink" href="#venues">{L['cta2']}</a></div>
   <div class="hnav"><span class="hcount" dir="ltr"><b>01</b> / 0{len(HERO)}</span><div class="hdots">{hbars}</div><span class="hcap">{HCAP[lang][0]}</span></div>
  </div>
 </div>
 <ul class="hstats"><li class="hcred"><span>{Y['cred_l']}</span><b>{' · '.join('<span>'+c+'</span>' for c in Y['cred'])}</b></li>{stats}</ul>
 <div class="hcaps" hidden>{json.dumps(HCAP[lang],ensure_ascii=False)}</div>
</header>
<section class="sec paper profile" id="profile"><div class="w">
 <div class="pgrid">
  <div class="ptext">{eb('01',Y['pf_l'])}<h2 class="rv">{Y['pf_h']}</h2><p class="big rv">{Y['pf_lead']}</p><div class="pin rv">{inp}</div><ul class="facts rv">{facts}</ul></div>
  <figure class="pport rv"><span class="frame"></span>{pic('portrait',root,"(max-width:900px) 86vw, 520px",L['brand'])}<figcaption>{L['brand']} · Berlin</figcaption></figure>
 </div>
 <div class="path"><div class="mhd"><h3 class="rv">{V['story']}</h3></div>{slider(tcards,'s-tl','',V['story'],'ol')}</div>
</div></section>
<section class="sec stone rail" aria-label="{Y['mo_h']}"><div class="w"><div class="mhd2"><h2 class="rv">{Y['mo_h']}</h2><p class="rv">{Y['mo_p']}</p></div></div>{slider(mos,'s-mo','',Y['mo_h'])}</section>
<section class="sec ivory services" id="services"><div class="w"><div class="hd">{eb('02',Y['sv_l'])}<h2 class="rv">{Y['sv_h']}</h2><p class="sub rv">{L['sv_p']}</p></div>{slider(svc,'s-svc','grid4',Y['sv_l'])}</div></section>
<section class="erupt" id="erupt" aria-label="quote"><div class="eruph" data-par>{pic('yafo-full',root,"100vw")}</div><div class="w"><blockquote class="eq glass"><span class="qm" aria-hidden="true">“</span><p>{L["quote"].strip('״“”"')}</p><cite>{L["quote_s"]}</cite></blockquote></div></section>
<section class="sec paper hotels" id="hotels"><div class="w hrow"><figure class="hv" data-par><span class="frame"></span>{pic('tasting',root,"(max-width:900px) 100vw, 56vw")}</figure><div class="hti">{eb('03',L['os_l'])}<h2 class="rv">{L['os_h']}</h2><p class="rv">{L['os_p']}</p><ul class="rv">{ospts}</ul>{btn(L['cta1'],'#contact','solid')}</div></div></section>
<section class="sec ink process" id="process"><div class="w prc"><div class="prh">{eb('04',Y['hw_l'])}<h2 class="rv">{Y['hw_h']}</h2><figure class="prv">{pic('bar-gold',root,"(max-width:900px) 92vw, 420px")}</figure></div><ol class="steps">{steps}</ol></div></section>
<section id="press" class="sec paper press"><div class="w strip"><p class="pl">{L['strip']}</p><ul class="plogs">{plogs}</ul></div></section>
<section class="sec stone venues" id="venues"><div class="w"><div class="hd">{eb('05',Y['vn_l'])}<h2 class="rv">{Y['vn_h']}</h2><p class="sub rv">{Y['vn_p']}</p></div>
 {slider(vf,'s-vf','grid2',Y['vn_l'])}<div class="vsrow">{vs}</div></div></section>
<section class="sec ivory journal" id="journal"><div class="w"><div class="hd">{eb('06',L['jr_l'])}<h2 class="rv">{L['jr_h']}</h2></div>{slider(jc,'s-jr','grid3',L['jr_h'])}</div></section>
<section id="contact" class="sec paper contact"><div class="w crow"><div class="cl">{eb('07',L['ct_l'])}<h2 class="rv">{L['ct_h']}</h2><p class="sub">{L['ct_p']}</p><p class="cdir"><a href="mailto:{MAIL}">{MAIL}</a><a href="tel:+{WAN}" dir="ltr">054-6644489</a></p><figure class="cv">{pic('courtyard',root,"(max-width:900px) 100vw, 40vw")}</figure></div>
<div class="form"><p class="ft">{L['ft']}</p><p class="fs">{L['fs']}</p><form id="lead" data-sending="{T3[lang]['sending']}" data-subj="{T3[lang]['subj']}"><div class="fg">
<div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name" placeholder="{P[0]}"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization" placeholder="{P[1]}"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel" dir="ltr" placeholder="{P[2]}"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr" placeholder="{P[3]}"></div>
<fieldset class="chips"><legend>{F[4]}</legend><div>{chips}</div></fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message" rows="2" placeholder="{P[4]}"></textarea></div></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn solid full" type="submit"><span>{F[6]}</span>{ARW}</button><p class="note">{L['note']}</p><p class="ok">{F[7]}</p></form></div></div></section>
</main>{foot(lang,'./')}{stick(lang,'./')}{wa(lang)}{LB(lang)}{scripts(root)}</body></html>'''
def article(lang,s):
    L=D[lang];L3=T3[lang];root='../' if lang=='he' else '../../';t,h,p=L3['arts'][s];mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html';alt=('en/' if lang=='he' else '')+f'blog/{s}.html';langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(jcard(lang,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,h+' · '+L['brand'],p,path,alt,root)}</head><body class="art"><div class="prog"></div>{nav(lang,'../',langhref)}<main>
<header class="ahero"><div class="w"><p class="eb"><span class="ebt">{t}</span></p><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L3['mins']}</p></div><figure class="aimg w">{pic(BLOGIMG[s],root,'(max-width:900px) 100vw, 1100px',eager=True)}</figure></header>
<article class="prose">{body}<div class="byline">{pic('portrait-c',root,'56px')}<p>{L3['by']}</p></div><div class="actab"><h3>{L['ct_h']}</h3><p>{L['ct_p']}</p>{btn(L['cta1'],'../#contact','solid')}</div></article>
<section class="sec ivory journal"><div class="w"><div class="hd"><h2>{L3['more']}</h2></div>{slider(others,'s-jr','grid2','')}<p class="back"><a href="../">{L3['back']}</a></p></div></section></main>{foot(lang,'../')}{stick(lang,'../')}{wa(lang)}<script src="{root}v14.js?v={CV}" defer></script></body></html>'''
# fix language-specific hero alt (v11 heropic printed the dict)
_hp=heropic
def heropic(key,root,eager=False,lang='he'):
    return _hp(key,root,eager)
def _alt_fix(html,lang):
    for k in HERO:
        a=HERO_POOL[k]['alt'];html=html.replace(f'alt="{a}"',f'alt="{H.escape(a[lang])}"')
    return html
os.makedirs('en/blog',exist_ok=True);os.makedirs('blog',exist_ok=True)
for lg,fn in (('he','index.html'),('en','en/index.html')):
    open(fn,'w').write(_alt_fix(index(lg),lg))
for s in ARTS:
    open(f'blog/{s}.html','w').write(article('he',s));open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok',CV)
