(function(){
  var params=new URLSearchParams(location.search);
  if(params.get('review')!=='1')return;

  var API='https://shani-review.gitter-omri.workers.dev';
  var DECK='shani-v12';
  var ACCESS=params.get('k')||'';
  var LS='shani-v12-review';
  var lang=document.documentElement.lang==='en'?'en':'he';

  var TITLES={
    hero:{he:'הירו — עמוד הפתיחה',en:'Hero'},
    profile:{he:'הסיפור',en:'The story'},
    services:{he:'השירותים',en:'Services'},
    erupt:{he:'ציטוט',en:'Quote'},
    hotels:{he:'מיקור חוץ למלונות',en:'Hotel F&B outsourcing'},
    process:{he:'התהליך',en:'Process'},
    press:{he:'עיתונות',en:'Press'},
    venues:{he:'מקומות',en:'Venues'},
    journal:{he:'המגזין',en:'Journal'},
    contact:{he:'יצירת קשר',en:'Contact'},
    stick:{he:'סרגל לידים',en:'Lead-capture bar'},
    wa:{he:'כפתור וואטסאפ',en:'WhatsApp button'}
  };

  var MAIN_IDS=['hero','profile','services','erupt','hotels','process','press','venues','journal','contact'];
  var CHROME_IDS=['stick','wa'];
  var DEFAULT_ORDER=MAIN_IDS.concat(CHROME_IDS);

  function titleOf(id){
    var t=TITLES[id];
    return t?(t.he):id;
  }

  document.documentElement.classList.add('review-on');

  function loadLocal(){
    try{return JSON.parse(localStorage.getItem(LS)||'')}catch(e){return null}
  }
  function saveLocal(state){
    try{localStorage.setItem(LS,JSON.stringify(state))}catch(e){}
  }

  function emptyState(){
    var folds={};
    DEFAULT_ORDER.forEach(function(id){
      folds[id]={title:titleOf(id),comment:'',status:''};
    });
    return {deck:DECK,updated:'',folds:folds,order:DEFAULT_ORDER.slice()};
  }

  function mergeState(base,incoming){
    if(!incoming||typeof incoming!=='object')return base;
    var out=emptyState();
    if(Array.isArray(incoming.order)&&incoming.order.length){
      var seen={};
      out.order=[];
      incoming.order.forEach(function(id){
        if(TITLES[id]&&!seen[id]){out.order.push(id);seen[id]=1}
      });
      DEFAULT_ORDER.forEach(function(id){if(!seen[id])out.order.push(id)});
    }
    var src=Object.assign({},base&&base.folds,incoming.folds);
    Object.keys(out.folds).forEach(function(id){
      var f=src[id]||{};
      out.folds[id]={
        title:titleOf(id),
        comment:typeof f.comment==='string'?f.comment:'',
        status:f.status==='in'||f.status==='out'||f.status==='fix'?f.status:''
      };
    });
    out.updated=incoming.updated||base&&base.updated||'';
    return out;
  }

  var state=mergeState(emptyState(),loadLocal());

  function headers(){
    var h={'content-type':'application/json'};
    if(ACCESS)h['x-review-key']=ACCESS;
    return h;
  }

  var els={};

  function foldEl(id){
    if(id==='stick')return document.querySelector('aside.stick, .stick');
    if(id==='wa')return document.querySelector('a.fa-wa, .fa-wa');
    return document.getElementById(id);
  }

  function wrapMains(){
    MAIN_IDS.forEach(function(id){
      var el=foldEl(id);
      if(!el||el.closest('.rv-slot'))return;
      var slot=document.createElement('div');
      slot.className='rv-slot';
      slot.dataset.fold=id;
      el.parentNode.insertBefore(slot,el);
      var hold=document.createElement('div');
      hold.className='rv-fold';
      var badge=document.createElement('div');
      badge.className='rv-badge';
      badge.setAttribute('aria-hidden','true');
      hold.appendChild(badge);
      hold.appendChild(el);
      slot.appendChild(hold);
      slot.appendChild(makeCard(id));
    });

    var contactSlot=document.querySelector('.rv-slot[data-fold="contact"]');
    var host=contactSlot&&contactSlot.parentNode;
    CHROME_IDS.forEach(function(id){
      if(document.querySelector('.rv-slot[data-fold="'+id+'"]'))return;
      var slot=document.createElement('div');
      slot.className='rv-slot rv-chrome';
      slot.dataset.fold=id;
      var hold=document.createElement('div');
      hold.className='rv-fold';
      var badge=document.createElement('div');
      badge.className='rv-badge';
      badge.setAttribute('aria-hidden','true');
      hold.appendChild(badge);
      var lab=document.createElement('div');
      lab.style.cssText='padding:48px 28px;font:400 22px/1.4 Heebo,system-ui,sans-serif;color:#1a1a1a;background:#faf7f0';
      lab.textContent=titleOf(id)+' — רכיב קבוע באתר (לא מקטע). ההערה כאן מתייחסת אליו.';
      hold.appendChild(lab);
      slot.appendChild(hold);
      slot.appendChild(makeCard(id));
      if(host){
        var after=host.querySelector('.rv-slot.rv-chrome:last-of-type')||contactSlot;
        if(after&&after.nextSibling)host.insertBefore(slot,after.nextSibling);
        else host.appendChild(slot);
      } else document.body.appendChild(slot);
    });
  }

  function makeCard(id){
    var card=document.createElement('aside');
    card.className='rv-card';
    card.dataset.fold=id;
    var f=state.folds[id]||{comment:'',status:''};
    var n=DEFAULT_ORDER.indexOf(id)+1;
    card.innerHTML=
      '<h3></h3>'+
      '<label class="rv-k"></label>'+
      '<textarea placeholder="הקלידי כאן. נשמר תוך כדי הקלדה."></textarea>'+
      '<div class="rv-status" role="group" aria-label="סטטוס המקטע">'+
        '<button type="button" data-s="in">בפנים</button>'+
        '<button type="button" data-s="out">בחוץ</button>'+
        '<button type="button" data-s="fix">תיקון</button>'+
      '</div>'+
      '<div class="rv-saved"></div>';
    card.querySelector('h3').textContent=n+'. '+titleOf(id);
    card.querySelector('label').textContent='הערה על מקטע '+n;
    card.querySelector('label').setAttribute('for','rv-c-'+id);
    var ta=card.querySelector('textarea');
    ta.id='rv-c-'+id;
    ta.value=f.comment||'';
    ta.addEventListener('input',function(){
      state.folds[id].comment=ta.value;
      card.querySelector('.rv-saved').textContent='שומר…';
      queueSave();
    });
    card.querySelectorAll('.rv-status button').forEach(function(btn){
      btn.setAttribute('aria-pressed', (f.status===btn.dataset.s)?'true':'false');
      btn.addEventListener('click',function(){
        var next=state.folds[id].status===btn.dataset.s?'':btn.dataset.s;
        state.folds[id].status=next;
        syncStatusUI(id);
        renderList();
        card.querySelector('.rv-saved').textContent='שומר…';
        queueSave();
      });
    });
    els[id]=card;
    return card;
  }

  function syncStatusUI(id){
    var card=els[id];
    if(!card)return;
    var st=state.folds[id]&&state.folds[id].status||'';
    card.querySelectorAll('.rv-status button').forEach(function(btn){
      btn.setAttribute('aria-pressed', st===btn.dataset.s?'true':'false');
    });
  }

  function siteNumbers(){
    var map={};
    DEFAULT_ORDER.forEach(function(id,i){map[id]=i+1});
    return map;
  }

  function refreshBadges(){
    var nums=siteNumbers();
    document.querySelectorAll('.rv-slot').forEach(function(slot){
      var id=slot.dataset.fold;
      var b=slot.querySelector('.rv-badge');
      if(b)b.textContent=String(nums[id]||'');
      var card=els[id];
      if(card){
        var n=nums[id];
        card.querySelector('h3').textContent=n+'. '+titleOf(id);
        card.querySelector('label').textContent='הערה על מקטע '+n;
      }
    });
  }

  function renderList(){
    var box=document.getElementById('rv-list-body');
    if(!box)return;
    var finals=state.order.filter(function(id){return state.folds[id]&&state.folds[id].status==='in'});
    box.innerHTML='';
    var nums=siteNumbers();
    if(!finals.length){
      var p=document.createElement('p');
      p.className='rv-empty';
      p.textContent='עוד אין מקטעים בפנים. סמני «בפנים» ליד מקטע כדי להוסיף אותו לרשימת הסופיים. אפשר לשנות את הסדר כאן.';
      box.appendChild(p);
      return;
    }
    finals.forEach(function(id,i){
      var row=document.createElement('div');
      row.className='rv-li';
      row.draggable=true;
      row.dataset.id=id;
      row.innerHTML='<span class="n"></span><span class="t"></span><span class="mv"><button type="button" data-d="-1" aria-label="למעלה">▲</button><button type="button" data-d="1" aria-label="למטה">▼</button></span>';
      row.querySelector('.n').textContent=(i+1)+' · '+nums[id];
      row.querySelector('.t').textContent=titleOf(id);
      row.querySelectorAll('.mv button').forEach(function(btn){
        btn.addEventListener('click',function(){moveFinal(id,parseInt(btn.dataset.d,10))});
      });
      row.addEventListener('dragstart',function(e){
        e.dataTransfer.setData('text/plain',id);
        row.classList.add('dragging');
      });
      row.addEventListener('dragend',function(){row.classList.remove('dragging')});
      row.addEventListener('dragover',function(e){e.preventDefault()});
      row.addEventListener('drop',function(e){
        e.preventDefault();
        var from=e.dataTransfer.getData('text/plain');
        dropFinal(from,id);
      });
      box.appendChild(row);
    });
  }

  function reorderFinals(nextFinals){
    var rest=state.order.filter(function(id){return state.folds[id].status!=='in'});
    state.order=nextFinals.concat(rest);
    renderList();
    queueSave();
  }

  function currentFinals(){
    return state.order.filter(function(id){return state.folds[id]&&state.folds[id].status==='in'});
  }

  function moveFinal(id,dir){
    var arr=currentFinals();
    var i=arr.indexOf(id);
    var j=i+dir;
    if(i<0||j<0||j>=arr.length)return;
    arr.splice(j,0,arr.splice(i,1)[0]);
    reorderFinals(arr);
  }

  function dropFinal(from,to){
    if(!from||from===to)return;
    var arr=currentFinals();
    var i=arr.indexOf(from),j=arr.indexOf(to);
    if(i<0||j<0)return;
    arr.splice(j,0,arr.splice(i,1)[0]);
    reorderFinals(arr);
  }

  function makeChrome(){
    var top=document.createElement('div');
    top.id='rv-top';
    top.innerHTML=
      '<span class="rv-brand">סקירת האתר, מקטע־מקטע</span>'+
      '<span class="rv-sync" id="rv-sync"></span>'+
      '<button type="button" class="rv-btn" id="rv-toggle-ui">הסתר סקירה</button>'+
      '<button type="button" class="rv-btn" id="rv-toggle-list">רשימת הסופיים</button>'+
      '<button type="button" class="rv-btn p" id="rv-send-top">שלחי את ההערות</button>';
    document.body.insertBefore(top,document.body.firstChild);

    var list=document.createElement('div');
    list.id='rv-list';
    list.innerHTML='<h2>רשימת הסופיים</h2><p class="rv-empty" style="margin:0 0 10px">מקטעים שסומנו «בפנים», לפי הסדר שבחרת. אפשר לגרור או להזיז עם החיצים. הרשימה נשמרת אוטומטית.</p><div id="rv-list-body"></div>';
    document.body.appendChild(list);

    var send=document.createElement('button');
    send.id='rv-send';
    send.className='rv-btn p';
    send.textContent='שלחי את ההערות';
    send.style.cssText='font:400 16px Heebo,system-ui,sans-serif;padding:14px 20px;border-radius:12px;border:1px solid #006EFF;background:#006EFF;color:#fff;cursor:pointer;box-shadow:0 0 30px rgba(0,110,255,.5)';
    send.addEventListener('click',sendAll);
    document.body.appendChild(send);

    document.getElementById('rv-send-top').addEventListener('click',sendAll);
    document.getElementById('rv-toggle-list').addEventListener('click',function(){
      list.classList.toggle('open');
    });
    document.getElementById('rv-toggle-ui').addEventListener('click',function(){
      var hide=document.documentElement.classList.toggle('review-hide');
      this.textContent=hide?'הצג סקירה':'הסתר סקירה';
    });
  }

  var saveTimer=null;
  var saving=false;

  function queueSave(){
    state.updated=new Date().toISOString();
    saveLocal(state);
    clearTimeout(saveTimer);
    saveTimer=setTimeout(pushState,800);
  }

  function setSync(msg,ok){
    var n=document.getElementById('rv-sync');
    if(n){n.textContent=msg;n.style.color=ok===false?'#ff8a9a':'#8AD2FF'}
  }

  function pushState(){
    saving=true;
    setSync('שומר…');
    var body=JSON.stringify({
      deck:DECK,
      client:localStorage.getItem('shani-v12-cid')||'',
      folds:state.folds,
      order:state.order,
      updated:state.updated
    });
    return fetch(API+'/state',{method:'POST',headers:headers(),body:body})
      .then(function(r){
        if(!r.ok)throw new Error('http '+r.status);
        return r.json();
      })
      .then(function(d){
        Object.keys(els).forEach(function(id){
          var s=els[id].querySelector('.rv-saved');
          if(s)s.textContent=d.github?'נשמר (וגם ב-GitHub)':'נשמר';
        });
        setSync(d.github?'נשמר · GitHub':'נשמר',true);
        return d;
      })
      .catch(function(){
        Object.keys(els).forEach(function(id){
          var s=els[id].querySelector('.rv-saved');
          if(s)s.textContent='נשמר במכשיר זה';
        });
        setSync(ACCESS?'לא נשמר בשרת — נשמר במכשיר':'נשמר במכשיר (אין מפתח סקירה בכתובת)',false);
      })
      .finally(function(){saving=false});
  }

  function pullState(){
    var url=API+'/state?deck='+encodeURIComponent(DECK);
    return fetch(url,{headers:headers()})
      .then(function(r){
        if(!r.ok)throw new Error('http '+r.status);
        return r.json();
      })
      .then(function(d){
        if(!d||!d.ok||!d.state)return;
        var remote=d.state;
        var local=loadLocal();
        if(!local||!local.updated||(remote.updated&&remote.updated>=local.updated)){
          state=mergeState(state,remote);
          applyStateToUI();
          saveLocal(state);
          setSync('נטען מהשמירה',true);
        }
      })
      .catch(function(){
        setSync(ACCESS?'עובד מקומית':'עובד מקומית (אין מפתח בכתובת)');
      });
  }

  function applyStateToUI(){
    Object.keys(els).forEach(function(id){
      var f=state.folds[id]||{comment:'',status:''};
      var ta=els[id].querySelector('textarea');
      if(ta&&ta.value!==(f.comment||''))ta.value=f.comment||'';
      syncStatusUI(id);
    });
    refreshBadges();
    renderList();
  }

  function sendBody(){
    var nums=siteNumbers();
    var lines=[];
    state.order.forEach(function(id){
      var f=state.folds[id];
      if(!f)return;
      var st=f.status==='in'?'בפנים':f.status==='out'?'בחוץ':f.status==='fix'?'תיקון':'לא סומן';
      if(!((f.comment||'').trim())&&!f.status)return;
      lines.push('מקטע '+nums[id]+', '+titleOf(id)+' ['+st+']:\n'+(f.comment||'').trim());
    });
    var finals=currentFinals().map(function(id,i){return (i+1)+'. ('+nums[id]+') '+titleOf(id)}).join('\n');
    var body=(lines.join('\n\n')||'אין הערות.')+'\n\nרשימת הסופיים:\n'+(finals||'(ריקה)')+'\n\n'+location.href;
    return {lines:lines,body:body,finals:currentFinals()};
  }

  function sendAll(){
    var payload=sendBody();
    var btns=[document.getElementById('rv-send'),document.getElementById('rv-send-top')];
    btns.forEach(function(b){if(b){b.disabled=true;b.textContent='שולחת…'}});
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(payload.body).catch(function(){});
    }
    var items=state.order.map(function(id){
      var f=state.folds[id]||{};
      return {id:id,title:titleOf(id),comment:f.comment||'',status:f.status||''};
    });
    fetch(API+'/send',{method:'POST',headers:headers(),body:JSON.stringify({
      deck:DECK,
      client:localStorage.getItem('shani-v12-cid')||'',
      subject:'Shani v12 review comments',
      url:location.href,
      items:items,
      order:state.order,
      folds:state.folds
    })})
      .then(function(r){if(!r.ok)throw new Error('http '+r.status);return r.json()})
      .then(function(){
        btns.forEach(function(b){if(b){b.disabled=false;b.textContent='נשלח'}});
        setSync('נשלח',true);
      })
      .catch(function(){
        location.href='mailto:gitter.omri@gita-agency.com?subject='+encodeURIComponent('הערות לסקירת האתר של שני, v12')+'&body='+encodeURIComponent(payload.body);
        btns.forEach(function(b){if(b){b.disabled=false;b.textContent='שלחי את ההערות'}});
      });
  }

  if(!localStorage.getItem('shani-v12-cid')){
    localStorage.setItem('shani-v12-cid',Math.random().toString(36).slice(2,12));
  }

  makeChrome();
  wrapMains();
  refreshBadges();
  renderList();
  setSync(ACCESS?'מתחבר לשמירה…':'נשמר במכשיר (הוסיפי מפתח לכתובת לסינכרון)');
  pullState();
})();
