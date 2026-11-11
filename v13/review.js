(function(){
  var params=new URLSearchParams(location.search);
  if(params.get('review')!=='1')return;

  var API='https://shani-review.gitter-omri.workers.dev';
  var DECK='shani-v13';
  var ACCESS=params.get('k')||'';
  var LS='shani-v13-review';
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

  var I18N={
    he:{
      brand:'סקירת האתר, מקטע־מקטע',
      hide:'הסתר סקירה',
      show:'הצג סקירה',
      finals:'רשימת הסופיים',
      send:'שלחי את ההערות',
      sending:'שולחת…',
      sent:'נשלח',
      label:function(n){return 'הערה על מקטע '+n},
      placeholder:'הקלידי כאן. נשמר תוך כדי הקלדה.',
      inn:'בפנים', out:'בחוץ', fix:'תיקון',
      saved:'נשמר',
      savedGh:'נשמר ב-GitHub הציבורי',
      savedLocal:'נשמר במכשיר זה',
      saving:'שומר…',
      listTitle:'רשימת הסופיים',
      listLead:'מקטעים שסומנו «בפנים», לפי הסדר שבחרת. אפשר לגרור או להזיז עם החיצים. הרשימה נשמרת אוטומטית.',
      listEmpty:'עוד אין מקטעים בפנים. סמני «בפנים» ליד מקטע כדי להוסיף אותו לרשימת הסופיים. אפשר לשנות את הסדר כאן.',
      chromeNote:function(title){return title+' — רכיב קבוע באתר (לא מקטע). ההערה כאן מתייחסת אליו.';},
      statusAria:'סטטוס המקטע',
      up:'למעלה', down:'למטה',
      connecting:'מתחבר לשמירה…',
      noKey:'נשמר במכשיר (הוסיפי מפתח לכתובת לסינכרון)',
      loaded:'נטען מהשמירה',
      local:'עובד מקומית',
      localNoKey:'עובד מקומית (אין מפתח בכתובת)',
      notServer:'לא נשמר בשרת — נשמר במכשיר',
      notServerNoKey:'נשמר במכשיר (אין מפתח סקירה בכתובת)',
      mailSubject:'הערות לסקירת האתר של שני, v13',
      lead:'ליד כל מקטע יש תיבת הערה שנשמרת תוך כדי הקלדה. אפשר לסמן בפנים, בחוץ או תיקון. כשסיימת, לחצי על «שלחי את ההערות».'
    },
    en:{
      brand:'Site review, section by section',
      hide:'Hide review',
      show:'Show review',
      finals:'Final list',
      send:'Send my comments',
      sending:'Sending…',
      sent:'Sent',
      label:function(n){return 'Your comment on section '+n},
      placeholder:'Type here. It saves as you type.',
      inn:'In', out:'Out', fix:'Fix',
      saved:'Saved',
      savedGh:'Saved to the public GitHub repo',
      savedLocal:'Saved on this device',
      saving:'Saving…',
      listTitle:'Final list',
      listLead:'Sections marked In, in the order you chose. Drag or use the arrows. The list saves automatically.',
      listEmpty:'No sections in the final list yet. Mark a section In to add it. You can change the order here.',
      chromeNote:function(title){return title+' — a fixed site control (not a section). The note here is about that control.';},
      statusAria:'Section status',
      up:'Move up', down:'Move down',
      connecting:'Connecting to save…',
      noKey:'Saved on this device (add the review key to the URL to sync)',
      loaded:'Loaded from saved review',
      local:'Working locally',
      localNoKey:'Working locally (no key in the URL)',
      notServer:'Not saved on the server — saved on this device',
      notServerNoKey:'Saved on this device (no review key in the URL)',
      mailSubject:'Comments on Shani\'s site review, v13',
      lead:'Next to every section there is a box for your comments; it saves as you type. You can mark a section In, Out or Fix. When you are done, press Send my comments.'
    }
  };
  var tx=I18N[lang]||I18N.he;

  var MAIN_IDS=['hero','profile','services','erupt','hotels','process','press','venues','journal','contact'];
  var CHROME_IDS=['stick','wa'];
  var DEFAULT_ORDER=MAIN_IDS.concat(CHROME_IDS);

  function titleOf(id){
    var t=TITLES[id];
    return t?(t[lang]||t.he):id;
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

  function makeHead(id){
    var head=document.createElement('div');
    head.className='rv-head';
    var num=document.createElement('div');
    num.className='rv-num';
    var title=document.createElement('h2');
    title.className='rv-title';
    title.textContent=titleOf(id);
    head.appendChild(num);
    head.appendChild(title);
    return head;
  }

  function wrapMains(){
    MAIN_IDS.forEach(function(id){
      var el=foldEl(id);
      if(!el||el.closest('.rv-slot'))return;
      var slot=document.createElement('div');
      slot.className='rv-slot';
      slot.dataset.fold=id;
      el.parentNode.insertBefore(slot,el);
      var left=document.createElement('div');
      left.className='rv-left';
      left.appendChild(makeHead(id));
      var hold=document.createElement('div');
      hold.className='rv-fold';
      hold.appendChild(el);
      left.appendChild(hold);
      slot.appendChild(left);
      slot.appendChild(makeCard(id));
    });

    var contactSlot=document.querySelector('.rv-slot[data-fold="contact"]');
    var host=contactSlot&&contactSlot.parentNode;
    CHROME_IDS.forEach(function(id){
      if(document.querySelector('.rv-slot[data-fold="'+id+'"]'))return;
      var slot=document.createElement('div');
      slot.className='rv-slot rv-chrome';
      slot.dataset.fold=id;
      var left=document.createElement('div');
      left.className='rv-left';
      left.appendChild(makeHead(id));
      var hold=document.createElement('div');
      hold.className='rv-fold';
      var lab=document.createElement('div');
      lab.style.cssText='padding:48px 28px;font:400 22px/1.4 Heebo,system-ui,sans-serif;color:#1a1a1a;background:#faf7f0';
      lab.textContent=tx.chromeNote(titleOf(id));
      hold.appendChild(lab);
      left.appendChild(hold);
      slot.appendChild(left);
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
      '<label class="rv-k"></label>'+
      '<textarea></textarea>'+
      '<div class="rv-status" role="group"></div>'+
      '<div class="rv-saved"></div>';
    var lab=card.querySelector('label');
    lab.textContent=tx.label(n);
    lab.setAttribute('for','rv-c-'+id);
    var ta=card.querySelector('textarea');
    ta.id='rv-c-'+id;
    ta.placeholder=tx.placeholder;
    ta.value=f.comment||'';
    ta.addEventListener('input',function(){
      state.folds[id].comment=ta.value;
      card.querySelector('.rv-saved').textContent=tx.saving;
      queueSave();
    });
    var group=card.querySelector('.rv-status');
    group.setAttribute('aria-label',tx.statusAria);
    [['in',tx.inn],['out',tx.out],['fix',tx.fix]].forEach(function(pair){
      var btn=document.createElement('button');
      btn.type='button';
      btn.dataset.s=pair[0];
      btn.textContent=pair[1];
      btn.setAttribute('aria-pressed',(f.status===pair[0])?'true':'false');
      btn.addEventListener('click',function(){
        var next=state.folds[id].status===btn.dataset.s?'':btn.dataset.s;
        state.folds[id].status=next;
        syncStatusUI(id);
        renderList();
        card.querySelector('.rv-saved').textContent=tx.saving;
        queueSave();
      });
      group.appendChild(btn);
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

  function refreshHeads(){
    var nums=siteNumbers();
    document.querySelectorAll('.rv-slot').forEach(function(slot){
      var id=slot.dataset.fold;
      var n=nums[id]||'';
      var num=slot.querySelector('.rv-num');
      if(num)num.textContent=String(n);
      var title=slot.querySelector('.rv-title');
      if(title)title.textContent=titleOf(id);
      var card=els[id];
      if(card){
        var lab=card.querySelector('label');
        if(lab)lab.textContent=tx.label(n);
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
      p.textContent=tx.listEmpty;
      box.appendChild(p);
      return;
    }
    finals.forEach(function(id,i){
      var row=document.createElement('div');
      row.className='rv-li';
      row.draggable=true;
      row.dataset.id=id;
      row.innerHTML='<span class="n"></span><span class="t"></span><span class="mv"><button type="button" data-d="-1"></button><button type="button" data-d="1"></button></span>';
      row.querySelector('.n').textContent=(i+1)+' · '+nums[id];
      row.querySelector('.t').textContent=titleOf(id);
      var btns=row.querySelectorAll('.mv button');
      btns[0].setAttribute('aria-label',tx.up);
      btns[0].textContent='▲';
      btns[1].setAttribute('aria-label',tx.down);
      btns[1].textContent='▼';
      btns.forEach(function(btn){
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
      '<span class="rv-brand"></span>'+
      '<span class="rv-sync" id="rv-sync"></span>'+
      '<button type="button" class="rv-btn" id="rv-toggle-ui"></button>'+
      '<button type="button" class="rv-btn" id="rv-toggle-list"></button>'+
      '<button type="button" class="rv-btn p" id="rv-send-top"></button>';
    top.querySelector('.rv-brand').textContent=tx.brand;
    top.querySelector('#rv-toggle-ui').textContent=tx.hide;
    top.querySelector('#rv-toggle-list').textContent=tx.finals;
    top.querySelector('#rv-send-top').textContent=tx.send;
    document.body.insertBefore(top,document.body.firstChild);

    var lead=document.createElement('p');
    lead.id='rv-lead';
    lead.textContent=tx.lead;
    top.insertAdjacentElement('afterend',lead);

    var list=document.createElement('div');
    list.id='rv-list';
    list.innerHTML='<h2></h2><p class="rv-empty" style="margin:0 0 10px"></p><div id="rv-list-body"></div>';
    list.querySelector('h2').textContent=tx.listTitle;
    list.querySelector('p').textContent=tx.listLead;
    document.body.appendChild(list);

    var send=document.createElement('button');
    send.id='rv-send';
    send.type='button';
    send.textContent=tx.send;
    send.addEventListener('click',sendAll);
    document.body.appendChild(send);

    document.getElementById('rv-send-top').addEventListener('click',sendAll);
    document.getElementById('rv-toggle-list').addEventListener('click',function(){
      list.classList.toggle('open');
    });
    document.getElementById('rv-toggle-ui').addEventListener('click',function(){
      var hide=document.documentElement.classList.toggle('review-hide');
      this.textContent=hide?tx.show:tx.hide;
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

  function markCards(text){
    Object.keys(els).forEach(function(id){
      var s=els[id].querySelector('.rv-saved');
      if(s)s.textContent=text;
    });
  }

  function pushState(){
    saving=true;
    setSync(tx.saving);
    var body=JSON.stringify({
      deck:DECK,
      client:localStorage.getItem('shani-v13-cid')||'',
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
        var msg=d.repo||d.github?tx.savedGh:tx.saved;
        markCards(msg);
        setSync(msg,true);
        return d;
      })
      .catch(function(){
        markCards(tx.savedLocal);
        setSync(ACCESS?tx.notServer:tx.notServerNoKey,false);
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
          setSync(tx.loaded,true);
        }
      })
      .catch(function(){
        setSync(ACCESS?tx.local:tx.localNoKey);
      });
  }

  function applyStateToUI(){
    Object.keys(els).forEach(function(id){
      var f=state.folds[id]||{comment:'',status:''};
      var ta=els[id].querySelector('textarea');
      if(ta&&ta.value!==(f.comment||''))ta.value=f.comment||'';
      syncStatusUI(id);
    });
    refreshHeads();
    renderList();
  }

  function sendBody(){
    var nums=siteNumbers();
    var lines=[];
    state.order.forEach(function(id){
      var f=state.folds[id];
      if(!f)return;
      var st=f.status==='in'?tx.inn:f.status==='out'?tx.out:f.status==='fix'?tx.fix:'';
      if(!((f.comment||'').trim())&&!f.status)return;
      lines.push((lang==='he'?'מקטע ':'Section ')+nums[id]+', '+titleOf(id)+(st?' ['+st+']':'')+':\n'+(f.comment||'').trim());
    });
    var finals=currentFinals().map(function(id,i){return (i+1)+'. ('+nums[id]+') '+titleOf(id)}).join('\n');
    var body=(lines.join('\n\n')||(lang==='he'?'אין הערות.':'No comments yet.'))+'\n\n'+(lang==='he'?'רשימת הסופיים:':'Final list:')+'\n'+(finals||(lang==='he'?'(ריקה)':'(empty)'))+'\n\n'+location.href;
    return {lines:lines,body:body,finals:currentFinals()};
  }

  function sendAll(){
    var payload=sendBody();
    var btns=[document.getElementById('rv-send'),document.getElementById('rv-send-top')];
    btns.forEach(function(b){if(b){b.disabled=true;b.textContent=tx.sending}});
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(payload.body).catch(function(){});
    }
    var items=state.order.map(function(id){
      var f=state.folds[id]||{};
      return {id:id,title:titleOf(id),comment:f.comment||'',status:f.status||''};
    });
    fetch(API+'/send',{method:'POST',headers:headers(),body:JSON.stringify({
      deck:DECK,
      client:localStorage.getItem('shani-v13-cid')||'',
      subject:'Shani v13 review comments',
      url:location.href,
      items:items,
      order:state.order,
      folds:state.folds
    })})
      .then(function(r){if(!r.ok)throw new Error('http '+r.status);return r.json()})
      .then(function(){
        btns.forEach(function(b){if(b){b.disabled=false;b.textContent=tx.sent}});
        setSync(tx.sent,true);
      })
      .catch(function(){
        location.href='mailto:gitter.omri@gita-agency.com?subject='+encodeURIComponent(tx.mailSubject)+'&body='+encodeURIComponent(payload.body);
        btns.forEach(function(b){if(b){b.disabled=false;b.textContent=tx.send}});
      });
  }

  if(!localStorage.getItem('shani-v13-cid')){
    localStorage.setItem('shani-v13-cid',Math.random().toString(36).slice(2,12));
  }

  makeChrome();
  wrapMains();
  refreshHeads();
  renderList();
  setSync(ACCESS?tx.connecting:tx.noKey);
  pullState();
})();
