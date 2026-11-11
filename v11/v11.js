(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches,RTL=document.dir==='rtl';
const nav=$('.nav'),hero=$('.hero,.ahero');let ly=0;
const onS=()=>{const y=scrollY;nav.classList.toggle('solid',y>32||!hero);nav.classList.toggle('hide',y>innerHeight&&y>ly+6&&!document.body.classList.contains('menu-open'));if(y<ly-4)nav.classList.remove('hide');ly=y};onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>document.body.classList.toggle('menu-open'));$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('menu-open')));
const reveal=()=>{
  const show=el=>el.classList.add('in');
  const visible=el=>{const r=el.getBoundingClientRect();return r.top<innerHeight*0.95 && r.bottom>0};
  $$('.rv').forEach(el=>{if(RM||visible(el))show(el)});
  if(RM)return;
  if(window.gsap&&window.ScrollTrigger){
    gsap.registerPlugin(ScrollTrigger);
    $$('.rv').forEach(el=>{
      if(el.classList.contains('in'))return;
      ScrollTrigger.create({trigger:el,start:'top 92%',once:true,onEnter:()=>show(el)});
    });
  }else{
    const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){show(e.target);io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
    $$('.rv').forEach(el=>{if(!el.classList.contains('in'))io.observe(el)});
  }
};
if(document.readyState==='complete')reveal();else addEventListener('load',reveal);
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,n=+el.dataset.count;if(RM)return;const t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/1400);el.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}),{threshold:.5});$$('[data-count]').forEach(el=>cio.observe(el));
/* hero slides — crossfade, preloaded, pause on hover/touch */
const hs=$$('.hs'),hd=$$('.hdot'),hcap=$('.hcap'),caps=JSON.parse($('.hcaps')?.textContent||'[]');
let hi=0,ht,hpaused=0;
const arm=()=>{clearTimeout(ht);if(!RM&&!hpaused&&hs.length>1)ht=setTimeout(()=>go(hi+1),5500)};
const go=k=>{if(!hs.length)return;const next=(k+hs.length)%hs.length;if(next===hi)return;
  hs[hi].classList.remove('on');hd[hi]?.classList.remove('on');
  hi=next;hs[hi].classList.add('on');hd[hi]?.classList.add('on');
  if(hcap){hcap.style.transition='opacity .3s';hcap.style.opacity=0;const t=caps[hi]||'';setTimeout(()=>{hcap.textContent=t;hcap.style.opacity=1},280)}
  arm()};
if(hs.length){
  // preload every hero frame so the crossfade never flashes empty
  hs.forEach(s=>{const i=s.querySelector('img');if(!i)return;i.loading='eager';i.decoding='async';if(i.decode)i.decode().catch(()=>{})});
  hd.forEach((b,k)=>b.onclick=()=>go(k));
  const stage=$('.hstage')||$('.hero');
  const pause=()=>{hpaused=1;clearTimeout(ht)};
  const resume=()=>{hpaused=0;arm()};
  if(stage){
    stage.addEventListener('pointerenter',pause);
    stage.addEventListener('pointerleave',resume);
    stage.addEventListener('touchstart',pause,{passive:true});
    stage.addEventListener('touchend',()=>setTimeout(resume,1200),{passive:true});
  }
  hd.forEach(b=>{b.addEventListener('pointerenter',pause);b.addEventListener('pointerleave',resume)});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pause();else resume()});
  arm();
}
/* sticky lead bar hides on the contact section and at the very top of the hero fold */
const stick=$('.stick');
if(stick){
  const contact=$('#contact');
  let inContact=0;
  const syncStick=()=>{
    const inHero=scrollY < innerHeight*0.55;
    stick.classList.toggle('hide', inHero || inContact);
  };
  if(contact){
    const io=new IntersectionObserver(es=>es.forEach(e=>{inContact=e.isIntersecting;syncStick()}),{threshold:.28});
    io.observe(contact);
  }
  addEventListener('scroll',syncStick,{passive:true});
  addEventListener('resize',syncStick);
  syncStick();
}
/* light parallax */
const pars=$$('[data-par]'),prog=$('.prog');
const tick=()=>{const y=scrollY,H=innerHeight;
 if(!RM){pars.forEach(el=>{const r=el.getBoundingClientRect();if(r.bottom<-80||r.top>H+80)return;const im=el.querySelector('img');if(im)im.style.transform=`translate3d(0,${(r.top+r.height/2-H/2)*-.05}px,0)`})}
 if(prog){const h=document.documentElement.scrollHeight-H;prog.style.transform=`scaleX(${h>0?y/h:0})`}
 requestAnimationFrame(tick)};requestAnimationFrame(tick);
/* magnetic */
if(FINE&&!RM){$$('.mag').forEach(b=>{const s=b.querySelector('span');b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect(),x=e.clientX-r.left-r.width/2,y=e.clientY-r.top-r.height/2;b.style.transform=`translate(${x*.14}px,${y*.22}px)`;if(s)s.style.transform=`translate(${x*.06}px,${y*.1}px)`});b.addEventListener('pointerleave',()=>{b.style.transform='';if(s)s.style.transform=''})})}
/* tabs */
$$('.tabs').forEach(t=>{const sec=t.parentElement;$$('button',t).forEach(b=>b.onclick=()=>{$$('button',t).forEach(x=>x.classList.toggle('on',x===b));$$('.tp',sec).forEach(p=>p.classList.toggle('on',p.dataset.p===b.dataset.t));setup()})});
/* sliders */
const sls=$$('.sl');
function setup(){sls.forEach(sl=>{const trk=$('.trk',sl),cards=trk?[...trk.children]:[],dots=$('.dots',sl),bar=$('.bar i',sl),ap=$('.ap',sl),an=$('.an',sl);if(!trk||!trk.offsetParent)return;
 const visible=getComputedStyle(trk).display==='flex';if(!visible)return;
 const max=()=>trk.scrollWidth-trk.clientWidth;const pos=()=>Math.abs(trk.scrollLeft);
 if(!sl._init){sl._init=1;
  const upd=()=>{const m=max(),p=m>0?pos()/m:0;const step=cards[1]?Math.abs(cards[1].offsetLeft-cards[0].offsetLeft):1;let idx=Math.round(pos()/step);if(p>.98)idx=cards.length-1;
   bar&&bar.style.setProperty('--p',Math.max(8,(trk.clientWidth/trk.scrollWidth)*100+p*(100-(trk.clientWidth/trk.scrollWidth)*100))+'%');
   $$('button',dots).forEach((d,i)=>d.classList.toggle('on',i===idx));if(ap)ap.disabled=pos()<4;if(an)an.disabled=pos()>m-4};
  if(dots)dots.innerHTML=cards.map((_,i)=>`<button aria-label="${i+1}"></button>`).join('');
  const to=i=>{const c=cards[i];if(!c)return;const off=RTL?-(cards[0].offsetLeft+cards[0].offsetWidth-c.offsetLeft-c.offsetWidth):c.offsetLeft-cards[0].offsetLeft;trk.scrollTo({left:off,behavior:'smooth'})};
  dots&&$$('button',dots).forEach((d,i)=>d.onclick=()=>to(i));
  const by=d=>{const step=(cards[0].offsetWidth+parseFloat(getComputedStyle(trk).columnGap||16))*d;trk.scrollBy({left:RTL?-step:step,behavior:'smooth'})};
  ap&&(ap.onclick=()=>by(-1));an&&(an.onclick=()=>by(1));
  trk.addEventListener('scroll',()=>requestAnimationFrame(upd),{passive:true});addEventListener('resize',upd);sl._upd=upd;
  let down=0,sx=0,sl0=0,moved=0;trk.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=1;moved=0;sx=e.clientX;sl0=trk.scrollLeft});
  addEventListener('pointermove',e=>{if(!down)return;const d=e.clientX-sx;if(Math.abs(d)>5){moved=1;trk.classList.add('drag')}if(moved)trk.scrollLeft=sl0-d});
  addEventListener('pointerup',()=>{if(!down)return;down=0;if(moved){const st=trk.scrollLeft;trk.classList.remove('drag');trk.scrollLeft=st}});
  trk.addEventListener('click',e=>{if(moved){e.preventDefault();e.stopPropagation();moved=0}},true);
  const hide=max()<4;const ui=sl.querySelector('.slc-ui');if(ui)ui.style.visibility=hide?'hidden':''}
 sl._upd&&sl._upd()})}
setup();addEventListener('load',setup);addEventListener('resize',()=>{clearTimeout(window._rs);window._rs=setTimeout(setup,200)});
/* warm up lazy images near viewport */
const warm=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const i=e.target;i.loading='eager';warm.unobserve(i)}),{rootMargin:'800px 400px'});
$$('img[loading=lazy]').forEach(i=>warm.observe(i));
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
