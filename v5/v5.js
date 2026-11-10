(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches;
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const nav=$('.nav'),hero=$('.hero,.ahero');const onS=()=>nav&&nav.classList.toggle('solid',scrollY>40||!hero);onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>{const o=document.body.classList.toggle('menu-open');$('.burger').setAttribute('aria-expanded',o);document.documentElement.style.overflow=o?'hidden':''});
$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>{document.body.classList.remove('menu-open');document.documentElement.style.overflow=''}));
/* reveals with sweep + failsafe (fa.js) */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:0,rootMargin:'0px 0px -8% 0px'});
$$('.rv,.clipin').forEach(el=>io.observe(el));
setTimeout(()=>$$('.rv,.clipin').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')}),1100);
/* counters */
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,n=+el.dataset.count;if(RM||n>999)return;const t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/1400);el.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}),{threshold:.4});
$$('[data-count]').forEach(el=>cio.observe(el));
/* marquee pause off-screen */
$$('.marquee').forEach(m=>{const tr=m.querySelector('.marquee-track');new IntersectionObserver(es=>es.forEach(e=>tr.style.animationPlayState=e.isIntersecting?'':'paused')).observe(m)});
/* WhatsApp */
const wa=$('.fa-wa');if(wa){let over=false;const upd=()=>wa.classList.toggle('is-in',scrollY>innerHeight*.5&&!over);const c=$('#contact');c&&new IntersectionObserver(es=>{es.forEach(e=>over=e.isIntersecting);upd()},{threshold:.25}).observe(c);addEventListener('scroll',upd,{passive:true});setTimeout(upd,400)}
/* dots */
$$('[data-dots]').forEach(tr=>{const d=$(tr.dataset.dots);if(!d)return;d.innerHTML='<i></i>'.repeat(tr.children.length);const ds=[...d.children];const f=()=>{const r=tr.getBoundingClientRect(),cx=r.left+r.width/2;let b=0,bd=1e9;[...tr.children].forEach((c,i)=>{const cr=c.getBoundingClientRect(),dd=Math.abs(cr.left+cr.width/2-cx);if(dd<bd){bd=dd;b=i}});ds.forEach((x,i)=>x.classList.toggle('on',i===b))};tr.addEventListener('scroll',()=>requestAnimationFrame(f),{passive:true});f()});
/* gallery buttons */
const track=$('.track');$$('.gbtn').forEach(b=>b.addEventListener('click',()=>{const c=track.querySelector('figure');track.scrollBy({left:(c.getBoundingClientRect().width+22)*+b.dataset.dir,behavior:'smooth'})}));
if(track){const mid=track.children[Math.floor(track.children.length/2)]; }
if(RM)return;
const layer=$('.hero .layer,.ahero .layer'),copy=$('.hero .copy'),pbs=$$('[data-par]'),steps=$('.steps'),bar=$('.steps .bar'),stepEls=$$('.step'),prog=$('.prog'),prints=$$('.pc .print.front');
const tick=()=>{const y=scrollY,H=innerHeight;
 if(layer&&y<H*1.3)layer.style.transform=`translate3d(0,${y*.3}px,0)`;
 if(copy&&y<H){copy.style.transform=`translate3d(0,${y*-.1}px,0)`;copy.style.opacity=Math.max(0,1-y/(H*.85))}
 pbs.forEach(el=>{const r=el.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>H)return;el.style.transform=`translate3d(0,${(r.top+r.height/2-H/2)*-.12}px,0)`});
 prints.forEach(p=>{const r=p.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>H)return;const d=(r.top+r.height/2-H/2)/H;p.style.marginTop=(d*-26)+'px'});
 if(steps&&bar){const r=steps.getBoundingClientRect();const p=Math.min(1,Math.max(0,(H*.6-r.top)/r.height));bar.style.height=(p*(r.height-16))+'px';stepEls.forEach(s=>s.classList.toggle('on',s.getBoundingClientRect().top<H*.6))}
 if(track){const tr=track.getBoundingClientRect();if(tr.bottom>0&&tr.top<H){const cx=tr.left+tr.width/2;[...track.children].forEach(f=>{const r=f.getBoundingClientRect(),d=(r.left+r.width/2-cx)/tr.width;f.style.transform=`rotateY(${Math.max(-1,Math.min(1,d))*-24}deg) translateZ(${-Math.min(1,Math.abs(d))*140}px)`})}}
 if(prog){const h=document.documentElement.scrollHeight-H;prog.style.transform=`scaleX(${h>0?y/h:0})`}
 requestAnimationFrame(tick)};requestAnimationFrame(tick);
if(track&&FINE){let down=false,sx=0,sl=0;track.addEventListener('pointerdown',e=>{down=true;sx=e.clientX;sl=track.scrollLeft;track.style.scrollSnapType='none'});addEventListener('pointerup',()=>{if(down){down=false;track.style.scrollSnapType=''}});track.addEventListener('pointermove',e=>{if(down)track.scrollLeft=sl-(e.clientX-sx)})}
if(FINE)$$('[data-tilt]').forEach(c=>{const m=+c.dataset.tilt||6;c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;c.style.transform=`perspective(1100px) rotateY(${(x-.5)*m}deg) rotateX(${(.5-y)*m}deg) translateY(-6px)`;c.style.setProperty('--gx',x*100+'%');c.style.setProperty('--gy',y*100+'%')});c.addEventListener('pointerleave',()=>{c.style.transform=''})});
})();
(()=>{const form=document.querySelector('#lead');if(!form)return;
form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');const t=btn.textContent;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});
if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');form.querySelector('.ok').style.display='block'}
catch(_){btn.textContent=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj)}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});})();
