(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const nav=$('.nav'),hero=$('.hero,.ahero');const onS=()=>nav.classList.toggle('solid',scrollY>30||!hero);onS();addEventListener('scroll',onS,{passive:true});
$('.burger')?.addEventListener('click',()=>{const o=document.body.classList.toggle('menu-open');$('.burger').setAttribute('aria-expanded',o)});
$$('.mmenu a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('menu-open')));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -6% 0px'});$$('.rv').forEach(el=>io.observe(el));
setTimeout(()=>$$('.rv').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')}),1000);
const prog=$('.prog');if(prog)addEventListener('scroll',()=>{const h=document.documentElement.scrollHeight-innerHeight;prog.style.transform=`scaleX(${h>0?scrollY/h:0})`},{passive:true});
/* lightbox */
const lb=$('.lb');if(lb){let g=[],i=0;const img=$('img',lb),cap=$('figcaption',lb),note=$('.lb-note',lb);
 const show=()=>{img.src=g[i][0];cap.textContent=g.length>1?`${g[i][1]} · ${i+1}/${g.length}`:g[i][1]};
 const open=(arr,n)=>{g=arr;i=0;lb.classList.toggle('note',!arr.length);lb.classList.toggle('single',arr.length===1);if(arr.length)show();else note.textContent=n||'';lb.hidden=false;document.documentElement.style.overflow='hidden'};
 const close=()=>{lb.hidden=true;document.documentElement.style.overflow='';img.removeAttribute('src')};
 $$('[data-g]').forEach(b=>b.addEventListener('click',()=>open(JSON.parse(b.dataset.g),b.dataset.note)));
 $('.lb-x',lb).onclick=close;lb.addEventListener('click',e=>{if(e.target===lb)close()});
 $('.lb-n',lb).onclick=()=>{i=(i+1)%g.length;show()};$('.lb-p',lb).onclick=()=>{i=(i-1+g.length)%g.length;show()};
 addEventListener('keydown',e=>{if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowRight'&&g.length>1){i=(i+1)%g.length;show()}if(e.key==='ArrowLeft'&&g.length>1){i=(i-1+g.length)%g.length;show()}});
 let sx=0;lb.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-sx;if(Math.abs(d)>40&&g.length>1){i=(i+(d<0?1:-1)+g.length)%g.length;show()}})}
})();
(()=>{const form=document.querySelector('#lead');if(!form)return;
form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button');const t=btn.textContent;btn.textContent=form.dataset.sending;btn.disabled=true;
const fd=new FormData(form),data=Object.fromEntries(fd.entries());data.services=fd.getAll('service').join(', ');delete data.service;
try{const r=await fetch('https://formsubmit.co/ajax/Shanini.a@gmail.com',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({...data,_subject:form.dataset.subj+' – '+(data.name||''),_template:'table'})});
if(!r.ok)throw 0;[...form.children].forEach(x=>x.style.display='none');form.querySelector('.ok').style.display='block'}
catch(_){btn.textContent=t;btn.disabled=false;location.href=`mailto:Shanini.a@gmail.com?subject=${encodeURIComponent(form.dataset.subj)}&body=${encodeURIComponent(Object.entries(data).map(([k,v])=>k+': '+v).join('\n'))}`}});})();
