const nav=document.querySelector('.nav'),bar=document.querySelector('.progress');
addEventListener('scroll',()=>{const y=scrollY;nav&&nav.classList.toggle('scrolled',y>40);if(bar)bar.style.width=(y/(document.body.scrollHeight-innerHeight)*100)+'%';
document.querySelectorAll('[data-par]').forEach(el=>{const r=el.parentElement.getBoundingClientRect();const v=Math.max(-50,Math.min(50,(r.top+r.height/2-innerHeight/2)*-0.08));el.style.transform=`translateY(${v}px)`})},{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.15});
document.querySelectorAll('.r,.step').forEach(el=>io.observe(el));
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target,to=+el.dataset.count,suf=el.dataset.suf||'',pre=el.dataset.pre||'';let t0=null;
const f=t=>{t0??=t;const p=Math.min((t-t0)/1600,1),v=Math.round(to*(1-Math.pow(1-p,3)));el.textContent=pre+v+suf;if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f);cio.unobserve(el)}),{threshold:.6});
document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));
document.querySelector('.burger')?.addEventListener('click',()=>nav.classList.toggle('open'));
document.querySelectorAll('.nav ul a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
const form=document.querySelector('#lead');
form?.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');btn.textContent=form.dataset.sending||'…';
const fd=new FormData(form);const data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:(form.dataset.subj||'Website enquiry')+' – '+(data.name||''),_template:'table'})});
if(!r.ok)throw 0;form.querySelectorAll('.f,.chips,button,.promise').forEach(x=>x.style.display='none');form.querySelector('.ok').style.display='block'}
catch(_){location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent((form.dataset.subj||'Website enquiry')+' – '+(data.name||''))}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});
