(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches,RTL=document.dir==='rtl';
const nav=$('.nav'),hero=$('.hero,.ahero');let ly=0;
const onS=()=>{const y=scrollY;document.body.classList.toggle('at-top',!!document.querySelector('.hero')&&y<innerHeight*.5);nav.classList.toggle('solid',y>40||!hero);nav.classList.toggle('hide',y>innerHeight&&y>ly+4&&!document.body.classList.contains('menu-open'));if(y<ly-4)nav.classList.remove('hide');ly=y};onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>document.body.classList.toggle('menu-open'));$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('menu-open')));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -6% 0px'});$$('.rv').forEach(el=>io.observe(el));
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,n=+el.dataset.count;if(RM)return;const t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/1600);el.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}),{threshold:.5});$$('[data-count]').forEach(el=>cio.observe(el));
/* hero slides */
const hs=$$('.hs'),hb=$$('.hb'),hcap=$('.hcap'),caps=JSON.parse($('.hcaps')?.textContent||'[]');let hi=0,ht;
const go=k=>{hs[hi].classList.remove('on');hb[hi].classList.remove('on');hb.forEach((b,j)=>b.classList.toggle('done',j<k));hi=(k+hs.length)%hs.length;hs[hi].classList.add('on');void hb[hi].offsetWidth;hb[hi].classList.add('on');if(hcap){hcap.style.opacity=0;setTimeout(()=>{hcap.textContent=caps[hi];hcap.style.opacity=1},300)}clearTimeout(ht);if(!RM)ht=setTimeout(()=>go(hi+1),6000)};
if(hs.length){hb.forEach((b,k)=>b.onclick=()=>go(k));if(!RM)ht=setTimeout(()=>go(1),6000);hs.slice(1).forEach(s=>{const i=s.querySelector('img');i.loading='eager'})}
/* scroll-linked */
const pars=$$('[data-par]'),hc=$('.hgrid'),hbg=$('.hbg'),prog=$('.prog');
const tick=()=>{const y=scrollY,H=innerHeight;
 if(!RM){if(hc&&y<H*1.2){hc.style.transform=`translate3d(0,${y*.18}px,0)`;hc.style.opacity=Math.max(0,1-y/(H*.8));hbg.style.transform=`scale(${1+y/H*.08})`}
 pars.forEach(el=>{const r=el.getBoundingClientRect();if(r.bottom<-100||r.top>H+100)return;const im=el.querySelector('img');if(im)im.style.transform=`translate3d(0,${(r.top+r.height/2-H/2)*-.07}px,0)`})}
 if(prog){const h=document.documentElement.scrollHeight-H;prog.style.transform=`scaleX(${h>0?y/h:0})`}
 requestAnimationFrame(tick)};requestAnimationFrame(tick);
/* tilt + magnetic */
if(FINE&&!RM){$$('[data-tilt]').forEach(c=>{c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(1100px) rotateY(${x*8}deg) rotateX(${-y*8}deg)`});c.addEventListener('pointerleave',()=>c.style.transform='')});
 $$('.mag').forEach(b=>{const s=b.querySelector('span');b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect(),x=e.clientX-r.left-r.width/2,y=e.clientY-r.top-r.height/2;b.style.transform=`translate(${x*.18}px,${y*.3}px)`;if(s)s.style.transform=`translate(${x*.08}px,${y*.12}px)`});b.addEventListener('pointerleave',()=>{b.style.transform='';if(s)s.style.transform=''})})}
/* tabs */
$$('.tabs').forEach(t=>{const sec=t.parentElement;$$('button',t).forEach(b=>b.onclick=()=>{$$('button',t).forEach(x=>x.classList.toggle('on',x===b));$$('.tp',sec).forEach(p=>p.classList.toggle('on',p.dataset.p===b.dataset.t));setup()})});
/* sliders */
const sls=$$('.sl');
function setup(){sls.forEach(sl=>{const trk=$('.trk',sl),cards=[...trk.children],dots=$('.dots',sl),bar=$('.bar i',sl),ap=$('.ap',sl),an=$('.an',sl);if(!trk.offsetParent)return;
 const visible=getComputedStyle(trk).display==='flex';if(!visible)return;
 const max=()=>trk.scrollWidth-trk.clientWidth;const pos=()=>Math.abs(trk.scrollLeft);
 if(!sl._init){sl._init=1;
  const upd=()=>{const m=max(),p=m>0?pos()/m:0;const step=cards[1]?Math.abs(cards[1].offsetLeft-cards[0].offsetLeft):1;let idx=Math.round(pos()/step);if(p>.98)idx=cards.length-1;
   bar&&bar.style.setProperty('--p',Math.max(8,(trk.clientWidth/trk.scrollWidth)*100+p*(100-(trk.clientWidth/trk.scrollWidth)*100))+'%');
   $$('button',dots).forEach((d,i)=>d.classList.toggle('on',i===idx));if(ap)ap.disabled=pos()<4;if(an)an.disabled=pos()>m-4};
  dots.innerHTML=cards.map((_,i)=>`<button aria-label="${i+1}"></button>`).join('');
  const to=i=>{const c=cards[i];if(!c)return;const off=RTL?-(cards[0].offsetLeft+cards[0].offsetWidth-c.offsetLeft-c.offsetWidth):c.offsetLeft-cards[0].offsetLeft;trk.scrollTo({left:off,behavior:'smooth'})};
  $$('button',dots).forEach((d,i)=>d.onclick=()=>to(i));
  const by=d=>{const step=(cards[0].offsetWidth+parseFloat(getComputedStyle(trk).columnGap||18))*d;trk.scrollBy({left:RTL?-step:step,behavior:'smooth'})};
  ap&&(ap.onclick=()=>by(-1));an&&(an.onclick=()=>by(1));
  trk.addEventListener('scroll',()=>requestAnimationFrame(upd),{passive:true});addEventListener('resize',upd);sl._upd=upd;
  // mouse drag
  let down=0,sx=0,sl0=0,moved=0;trk.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=1;moved=0;sx=e.clientX;sl0=trk.scrollLeft});
  addEventListener('pointermove',e=>{if(!down)return;const d=e.clientX-sx;if(Math.abs(d)>5){moved=1;trk.classList.add('drag')}if(moved)trk.scrollLeft=sl0-d});
  addEventListener('pointerup',()=>{if(!down)return;down=0;if(moved){const st=trk.scrollLeft;trk.classList.remove('drag');trk.scrollLeft=st;setTimeout(()=>{},0)}});
  trk.addEventListener('click',e=>{if(moved){e.preventDefault();e.stopPropagation();moved=0}},true);
  const hide=max()<4;sl.querySelector('.slc-ui').style.visibility=hide?'hidden':''}
 sl._upd&&sl._upd()})}
setup();addEventListener('load',setup);addEventListener('resize',()=>{clearTimeout(window._rs);window._rs=setTimeout(setup,200)});
/* cursor */
if(FINE&&!RM&&$('.cur')){document.body.classList.add('has-cur');const c=$('.cur'),dot=$('i',c),ring=$('b',c),H=$('.hero');const L={drag:H?.dataset.drag||(RTL?'גררו':'Drag'),view:H?.dataset.view||(RTL?'פתחו':'View')};
 let mx=-99,my=-99,rx=-99,ry=-99;addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;dot.style.transform=`translate(${mx}px,${my}px)`},{passive:true});
 const lp=()=>{rx+=(mx-rx)*.16;ry+=(my-ry)*.16;ring.style.transform=`translate(${rx}px,${ry}px)`;requestAnimationFrame(lp)};lp();
 document.addEventListener('pointerover',e=>{const t=e.target.closest('[data-cur]'),a=e.target.closest('a,button,label');const k=t?.dataset.cur;const lab=e.target.closest('[data-cur=view]')?'view':(k==='drag'&&!a?'drag':null);
  c.classList.toggle('lab',!!lab);ring.textContent=lab?L[lab]:'';c.classList.toggle('hov',!!a&&!lab)})}
/* lightbox */
const lb=$('.lb');if(lb){let g=[],i=0,z=1,tx=0,ty=0;const img=$('.lb-img',lb),cap=$('.lb-cap',lb),cnt=$('.lb-c',lb),th=$('.lb-th',lb),note=$('.lb-note',lb),stage=$('.lb-stage',lb);
 const apply=(anim=true)=>{img.style.transition=anim?'':'none';img.style.transform=`translate(${tx}px,${ty}px) scale(${z})`;lb.classList.toggle('zoom',z>1)};
 const show=(dir=0)=>{z=1;tx=ty=0;apply(false);if(dir){img.style.opacity=0;img.style.transform=`translateX(${dir*40}px)`}const nimg=new Image();nimg.src=g[i][0];const done=()=>{img.src=g[i][0];requestAnimationFrame(()=>{img.style.transition='';img.style.opacity=1;img.style.transform='none'})};nimg.decode?nimg.decode().then(done,done):done();
  cap.textContent=g[i][1];cnt.textContent=g.length>1?`${String(i+1).padStart(2,'0')} / ${String(g.length).padStart(2,'0')}`:'';$$('button',th).forEach((b,j)=>b.classList.toggle('on',j===i));$$('button',th)[i]?.scrollIntoView({inline:'center',block:'nearest'});
  [1,-1].forEach(d=>{const n=g[(i+d+g.length)%g.length];if(n){const p=new Image();p.src=n[0]}})};
 const open=(a,n,k=0)=>{g=a;i=k;lb.classList.toggle('note',!a.length);lb.classList.toggle('single',a.length===1);if(a.length){th.innerHTML=a.map((x,j)=>`<button aria-label="${j+1}"><img src="${x[2]||x[0]}" alt="" loading="lazy"></button>`).join('');$$('button',th).forEach((b,j)=>b.onclick=()=>{const d=j>i?1:-1;i=j;show(d)});show()}else note.textContent=n||'';lb.hidden=false;requestAnimationFrame(()=>lb.classList.add('vis'));document.documentElement.style.overflow='hidden'};
 const close=()=>{lb.classList.remove('vis');setTimeout(()=>{lb.hidden=true;img.removeAttribute('src')},350);document.documentElement.style.overflow=''};
 $$('[data-g]').forEach(b=>b.addEventListener('click',()=>open(JSON.parse(b.dataset.g),b.dataset.note,+(b.dataset.i||0))));$('.lb-x',lb).onclick=close;
 const nx=d=>{if(g.length>1){i=(i+d+g.length)%g.length;show(d)}};$('.lb-n',lb).onclick=()=>nx(RTL?-1:1);$('.lb-p',lb).onclick=()=>nx(RTL?1:-1);
 addEventListener('keydown',e=>{if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowRight')nx(RTL?-1:1);if(e.key==='ArrowLeft')nx(RTL?1:-1)});
 stage.addEventListener('click',e=>{if(e.target===stage)close()});
 const zoomAt=(cx,cy)=>{if(z>1){z=1;tx=ty=0}else{z=2.4;const r=img.getBoundingClientRect();tx=(r.left+r.width/2-cx)*1.4;ty=(r.top+r.height/2-cy)*1.4}apply()};
 img.addEventListener('dblclick',e=>zoomAt(e.clientX,e.clientY));
 let pts=new Map(),sx=0,sy=0,t0=0,lastTap=0,pd0=0,z0=1,tx0=0,ty0=0;
 stage.addEventListener('pointerdown',e=>{stage.setPointerCapture(e.pointerId);pts.set(e.pointerId,[e.clientX,e.clientY]);sx=e.clientX;sy=e.clientY;t0=Date.now();tx0=tx;ty0=ty;z0=z;if(pts.size===2){const [a,b]=[...pts.values()];pd0=Math.hypot(a[0]-b[0],a[1]-b[1])}});
 stage.addEventListener('pointermove',e=>{if(!pts.has(e.pointerId))return;pts.set(e.pointerId,[e.clientX,e.clientY]);
  if(pts.size===2){const [a,b]=[...pts.values()];z=Math.min(4,Math.max(1,z0*Math.hypot(a[0]-b[0],a[1]-b[1])/pd0));apply(false);return}
  const dx=e.clientX-sx,dy=e.clientY-sy;if(z>1){tx=tx0+dx;ty=ty0+dy;apply(false)}else{img.style.transition='none';img.style.transform=`translateX(${dx}px)`;img.style.opacity=1-Math.min(.5,Math.abs(dx)/600)}});
 stage.addEventListener('pointerup',e=>{const was=pts.size;pts.delete(e.pointerId);if(was===2){if(z<1.1){z=1;tx=ty=0;apply()}return}
  const dx=e.clientX-sx,dy=e.clientY-sy,dt=Date.now()-t0;
  if(z>1){return}
  if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy)){nx((dx<0)!==RTL?1:-1)}else if(dy>90){close()}else{img.style.transition='';img.style.transform='none';img.style.opacity=1;
   if(e.pointerType!=='mouse'&&dt<250&&Math.abs(dx)<10){const n=Date.now();if(n-lastTap<300){zoomAt(e.clientX,e.clientY);lastTap=0}else lastTap=n}}});
}
})();
(()=>{const form=document.querySelector('#lead');if(!form)return;form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button[type=submit]');const t=btn.innerHTML;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');form.querySelector('.ok').style.display='block'}
catch(_){btn.innerHTML=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj)}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});})();
