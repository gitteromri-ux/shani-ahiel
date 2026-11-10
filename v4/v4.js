(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches, FINE=matchMedia('(pointer:fine)').matches, MOB=()=>innerWidth<861;
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
/* nav */
const nav=$('.nav'),hero=$('.hero,.ahero');
const onS=()=>{nav&&nav.classList.toggle('solid',scrollY>40||!hero)};onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>{const o=document.body.classList.toggle('menu-open');$('.burger').setAttribute('aria-expanded',o);document.documentElement.style.overflow=o?'hidden':''});
$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>{document.body.classList.remove('menu-open');document.documentElement.style.overflow=''}));
/* videos: lazy, mobile source, play only in view, poster only when reduced motion */
const vids=$$('video[data-v]');
const load=v=>{if(v.dataset.loaded)return;v.dataset.loaded=1;const b=v.dataset.v,m=MOB();
  v.poster=m?b+'-poster-m.webp':b+'-poster.webp';
  if(RM)return;
  if(!m){const s=document.createElement('source');s.src=b+'-1080.webm';s.type='video/webm';v.appendChild(s)}
  const s2=document.createElement('source');s2.src=m?b+'-m.mp4':b+'-1080.mp4';s2.type='video/mp4';v.appendChild(s2);v.load()};
const vio=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){load(v);if(!RM){const p=v.play();p&&p.catch(()=>{})}}else if(v.dataset.loaded){v.pause()}}),{rootMargin:'200px 0px'});
vids.forEach(v=>{v.muted=true;v.playsInline=true;if(v.hasAttribute('data-eager'))load(v);vio.observe(v)});
/* reveals */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.14,rootMargin:'0px 0px -6% 0px'});
$$('.rv,.clipin').forEach(el=>io.observe(el));
/* WhatsApp floater: in after hero, hidden over contact form */
const wa=$('.fa-wa');
if(wa){let over=false;const z=new IntersectionObserver(es=>{es.forEach(e=>over=e.isIntersecting);upd()},{threshold:.25});const c=$('#contact');c&&z.observe(c);
 const upd=()=>wa.classList.toggle('is-in',scrollY>innerHeight*.5&&!over);addEventListener('scroll',upd,{passive:true});setTimeout(upd,400)}
/* carousel dots (mobile) */
$$('[data-dots]').forEach(tr=>{const d=$(tr.dataset.dots);if(!d)return;const n=tr.children.length;d.innerHTML='<i></i>'.repeat(n);const ds=[...d.children];
 const f=()=>{const r=tr.getBoundingClientRect(),cx=r.left+r.width/2;let b=0,bd=1e9;[...tr.children].forEach((c,i)=>{const cr=c.getBoundingClientRect(),dd=Math.abs(cr.left+cr.width/2-cx);if(dd<bd){bd=dd;b=i}});ds.forEach((x,i)=>x.classList.toggle('on',i===b))};
 tr.addEventListener('scroll',()=>requestAnimationFrame(f),{passive:true});f()});
if(RM)return;
/* hero layered parallax + pointer depth */
const layer=$('.hero .layer,.ahero .layer'),copy=$('.hero .copy');let mx=0,my=0,tx=0,ty=0;
if(FINE&&$('.hero'))addEventListener('pointermove',e=>{mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5},{passive:true});
/* Berlin bg parallax */
const pbs=$$('[data-par]');
/* process progress */
const steps=$('.steps'),bar=$('.steps .bar'),stepEls=$$('.step');
/* gallery 3D */
const track=$('.track');
/* article progress */
const prog=$('.prog');
const tick=()=>{tx+=(mx-tx)*.06;ty+=(my-ty)*.06;const y=scrollY,H=innerHeight;
 if(layer&&y<H*1.2){layer.style.transform=`translate3d(${tx*-22}px,${y*.28+ty*-14}px,0) scale(${1.06+y/H*.06})`}
 if(copy&&y<H*1.2){copy.style.transform=`translate3d(${tx*14}px,${y*-.12+ty*8}px,0) rotateY(${tx*3}deg) rotateX(${ty*-2}deg)`;copy.style.opacity=Math.max(0,1-y/(H*.8))}
 pbs.forEach(el=>{const r=el.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>H)return;el.style.transform=`translate3d(0,${(r.top+r.height/2-H/2)*-.12}px,0)`});
 if(steps&&bar){const r=steps.getBoundingClientRect();const p=Math.min(1,Math.max(0,(H*.6-r.top)/r.height));bar.style.height=(p*(r.height-24))+'px';stepEls.forEach(s=>{s.classList.toggle('on',s.getBoundingClientRect().top<H*.6)})}
 if(track){const tr=track.getBoundingClientRect();if(tr.bottom>0&&tr.top<H){const cx=tr.left+tr.width/2;[...track.children].forEach(f=>{const r=f.getBoundingClientRect(),d=(r.left+r.width/2-cx)/tr.width;f.style.transform=`rotateY(${d*-28}deg) translateZ(${-Math.abs(d)*120}px)`})}}
 if(prog){const h=document.documentElement.scrollHeight-H;prog.style.transform=`scaleX(${h>0?y/h:0})`}
 requestAnimationFrame(tick)};requestAnimationFrame(tick);
/* drag-to-scroll gallery on desktop */
if(track&&FINE){let down=false,sx=0,sl=0;track.addEventListener('pointerdown',e=>{down=true;sx=e.clientX;sl=track.scrollLeft;track.style.scrollSnapType='none'});addEventListener('pointerup',()=>{down=false;track.style.scrollSnapType=''});track.addEventListener('pointermove',e=>{if(down)track.scrollLeft=sl-(e.clientX-sx)})}
/* tilt cards (desktop) */
if(FINE)$$('[data-tilt]').forEach(c=>{const m=+c.dataset.tilt||8;c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;c.style.transform=`perspective(1000px) rotateY(${(x-.5)*m}deg) rotateX(${(.5-y)*m}deg) translateZ(0)`;c.style.setProperty('--gx',x*100+'%');c.style.setProperty('--gy',y*100+'%')});c.addEventListener('pointerleave',()=>{c.style.transform=''})});
/* refined cursor */
if(FINE){const a=document.createElement('div'),b=document.createElement('div');a.className='cur';b.className='cur-dot';document.body.append(a,b);document.body.classList.add('has-cur');let x=-100,y=-100,ax=-100,ay=-100;
 addEventListener('pointermove',e=>{x=e.clientX;y=e.clientY;b.style.transform=`translate3d(${x}px,${y}px,0)`},{passive:true});
 const lp=()=>{ax+=(x-ax)*.16;ay+=(y-ay)*.16;a.style.transform=`translate3d(${ax}px,${ay}px,0)`;requestAnimationFrame(lp)};lp();
 document.addEventListener('pointerover',e=>{a.classList.toggle('big',!!e.target.closest('a,button,label,.vcard,figure'))})}
})();
/* FormSubmit lead form */
(()=>{const form=document.querySelector('#lead');if(!form)return;
form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');const t=btn.textContent;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});
if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');const ok=form.querySelector('.ok');ok.style.display='block'}
catch(_){btn.textContent=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj+' – '+(data.name||''))}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});})();
