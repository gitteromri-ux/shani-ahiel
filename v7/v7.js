(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches;
const nav=$('.nav'),hero=$('.hero,.ahero');const onS=()=>nav.classList.toggle('solid',scrollY>30||!hero);onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>document.body.classList.toggle('menu-open'));$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('menu-open')));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});$$('.rv,.mask').forEach(el=>io.observe(el));
setTimeout(()=>$$('.rv,.mask').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')}),900);
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,n=+el.dataset.count;if(RM)return;const t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/1400);el.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}),{threshold:.5});$$('[data-count]').forEach(el=>cio.observe(el));
const prog=$('.prog');
const pars=$$('[data-par]'),hp=$('[data-hpar]'),tl=$('.tl'),tf=$('.tfill');
const tick=()=>{const y=scrollY,H=innerHeight;
 if(!RM){if(hp&&y<H*1.2)hp.style.transform=`translate3d(0,${y*.25}px,0)`;
 pars.forEach(el=>{const r=el.getBoundingClientRect();if(r.bottom<-100||r.top>H+100)return;const k=parseFloat(el.dataset.par)||.08;el.style.translate=`0 ${(r.top+r.height/2-H/2)*-k}px`})}
 if(tl&&tf){const r=tl.getBoundingClientRect();tf.style.height=Math.min(r.height,Math.max(0,H*.65-r.top))+'px'}
 if(prog){const h=document.documentElement.scrollHeight-H;prog.style.transform=`scaleX(${h>0?y/h:0})`}
 requestAnimationFrame(tick)};requestAnimationFrame(tick);
if(FINE&&!RM)$$('[data-tilt]').forEach(c=>{c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(1000px) rotateY(${x*5}deg) rotateX(${-y*5}deg) translateY(-4px)`});c.addEventListener('pointerleave',()=>c.style.transform='')});
const lb=$('.lb');if(lb){let g=[],i=0;const img=$('img',lb),cap=$('figcaption',lb),note=$('.lb-note',lb);
 const show=()=>{img.src=g[i][0];cap.textContent=g.length>1?`${g[i][1]} · ${i+1}/${g.length}`:g[i][1]};
 const open=(a,n)=>{g=a;i=0;lb.classList.toggle('note',!a.length);lb.classList.toggle('single',a.length===1);if(a.length)show();else note.textContent=n||'';lb.hidden=false;document.documentElement.style.overflow='hidden'};
 const close=()=>{lb.hidden=true;document.documentElement.style.overflow='';img.removeAttribute('src')};
 $$('[data-g]').forEach(b=>b.addEventListener('click',()=>open(JSON.parse(b.dataset.g),b.dataset.note)));$('.lb-x',lb).onclick=close;lb.addEventListener('click',e=>{if(e.target===lb)close()});
 const nx=d=>{if(g.length>1){i=(i+d+g.length)%g.length;show()}};$('.lb-n',lb).onclick=()=>nx(1);$('.lb-p',lb).onclick=()=>nx(-1);
 addEventListener('keydown',e=>{if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowRight')nx(1);if(e.key==='ArrowLeft')nx(-1)});
 let sx=0;lb.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-sx;if(Math.abs(d)>40)nx(d<0?1:-1)})}
})();
(()=>{const form=document.querySelector('#lead');if(!form)return;form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');const t=btn.textContent;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');form.querySelector('.ok').style.display='block'}
catch(_){btn.textContent=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj)}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});})();
