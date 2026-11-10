const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.fu').forEach(el=>io.observe(el));
const wa=document.querySelector('.wa'),zones=[...document.querySelectorAll('.contact,footer')],vis=new Set();
if(wa&&zones.length){const z=new IntersectionObserver(es=>{es.forEach(e=>e.isIntersecting?vis.add(e.target):vis.delete(e.target));wa.classList.toggle('hide',vis.size>0)},{threshold:0});zones.forEach(x=>z.observe(x))}
const form=document.querySelector('#lead');
form?.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');const t=btn.textContent;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});
if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');const ok=form.querySelector('.ok');ok.style.display='block'}
catch(_){btn.textContent=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj+' – '+(data.name||''))}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});
