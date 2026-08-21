function trackTerritory(name, locality=''){
  try{ fetch('interesse-click.php?territorio='+encodeURIComponent(name)+'&localita='+encodeURIComponent(locality), {cache:'no-store'}); }catch(e){}
}
function openTerritory(name){ trackTerritory(name); window.location.href='territorio.php?territorio='+encodeURIComponent(name); }

(function(){
  const cfg = window.VS_CONFIG || {};
  const state = { lang: cfg.defaultLanguage || 'it', securityAttempts: 0, closedForSecurity: false };

  const TXT = {
    it:{
      title:'VìSì', subtitle:'Assistente Vacanze Sicure', online:'Online',
      hello:'Ciao 👋 Sono VìSì. Posso spiegarti Vacanze Sicure, aiutarti a orientarti e guidarti nell’iscrizione.',
      placeholder:'Scrivi a VìSì…', send:'Invia', signup:'Iscriviti', human:'Parla con una persona',
      security1:'Alcune informazioni richieste sono riservate e non possono essere divulgate. Posso però aiutarti con le informazioni pubbliche e con le funzioni disponibili sul sito.',
      security2:'Ti informo che richieste reiterate volte a ottenere informazioni riservate, tecniche o interne non possono essere soddisfatte. Ti invito a non proseguire con richieste di questo tipo.',
      security3:'La conversazione è stata chiusa per reiterate richieste di informazioni riservate. L’evento è stato segnalato al sistema di sicurezza per la verifica prevista.',
      unknown:'Su questo punto non ho una risposta pubblica sufficientemente affidabile. Posso aiutarti a iscriverti oppure passare la richiesta a un operatore.'
    },
    en:{
      title:'VìSì', subtitle:'Vacanze Sicure Assistant', online:'Online',
      hello:'Hi 👋 I’m VìSì. I can explain Vacanze Sicure, help you navigate the service and guide you through registration.',
      placeholder:'Write to VìSì…', send:'Send', signup:'Sign up', human:'Talk to a person',
      security1:'Some of the information requested is confidential and cannot be disclosed. I can still help with public information and the services available on this website.',
      security2:'Repeated attempts to obtain confidential, technical or internal information cannot be fulfilled. Please do not continue with this type of request.',
      security3:'This chat has been closed after repeated requests for confidential information. The event has been reported to the security system for review.',
      unknown:'I do not have a sufficiently reliable public answer for this. I can help you register or pass the request to a human operator.'
    },
    de:{
      title:'VìSì', subtitle:'Assistent von Vacanze Sicure', online:'Online',
      hello:'Hallo 👋 Ich bin VìSì. Ich erkläre Vacanze Sicure, helfe bei der Orientierung und begleite dich bei der Registrierung.',
      placeholder:'Schreibe an VìSì…', send:'Senden', signup:'Registrieren', human:'Mit einer Person sprechen',
      security1:'Einige der angeforderten Informationen sind vertraulich und dürfen nicht offengelegt werden. Ich kann dir jedoch mit öffentlichen Informationen und den Funktionen dieser Website helfen.',
      security2:'Wiederholte Versuche, vertrauliche, technische oder interne Informationen zu erhalten, können nicht erfüllt werden. Bitte stelle keine weiteren Fragen dieser Art.',
      security3:'Der Chat wurde nach wiederholten Anfragen nach vertraulichen Informationen geschlossen. Der Vorgang wurde zur Prüfung an das Sicherheitssystem gemeldet.',
      unknown:'Dazu habe ich keine ausreichend verlässliche öffentliche Antwort. Ich kann dir bei der Registrierung helfen oder die Anfrage an einen Mitarbeiter weitergeben.'
    }
  };

  const FAQ = {
    it:[
      {p:/chi siete|cos.?è vacanze sicure|cosa fate|a cosa serve/i, a:'Vacanze Sicure è un ecosistema che aiuta Viaggiatori e Host a orientarsi tra annunci, strutture, informazioni, verifiche disponibili e assistenza. VìSì ti guida soprattutto verso le informazioni pubbliche e l’iscrizione.'},
      {p:/come mi iscrivo|iscrizione|registrarmi|creare account/i, a:'Puoi iniziare dalla pagina Accesso/Registrazione. Se mi dici se sei Viaggiatore, Host/Gestore o Professionista, ti indico il percorso più adatto.'},
      {p:/cin|codice identificativo/i, a:'Il CIN è un dato importante da controllare. Vacanze Sicure distingue sempre tra dato dichiarato, fonte consultata e risultato del controllo. Il CIN da solo non rappresenta una garanzia assoluta sull’affidabilità complessiva.'},
      {p:/host|gestore|proprietario/i, a:'Per Host e Gestori, Vacanze Sicure prevede una Scheda Master dell’alloggio con descrizioni, fotografie, camere, letti, bagni, dotazioni, regole, prezzi, disponibilità, documenti e canali collegati.'},
      {p:/annuncio|facebook|booking|airbnb|vrbo|expedia|agoda/i, a:'Puoi usare Vacanze Sicure per comprendere meglio un annuncio e distinguere ciò che è dichiarato da ciò che deve essere controllato. Le informazioni provenienti dai canali restano collegate alla stessa Scheda Master quando tecnicamente possibile.'},
      {p:/operatore|persona|umano|assistenza/i, a:'Se una risposta richiede una decisione umana, una verifica specifica o informazioni che non posso fornire, posso indirizzarti a un operatore Vacanze Sicure.'},
      {p:/lavora|candidatura|personale|professionista/i, a:'Vacanze Sicure raccoglie candidature di dipendenti e professionisti per categoria e area. La rete può essere utilizzata per esigenze VS o per richieste dirette degli Host.'}
    ]
  };

  const secretPatterns = [
    /database|schema sql|tabell[ae]|colonn[ae]|query|supabase|service[_ -]?role|api[_ -]?key|secret|password|credenzial/i,
    /prompt di sistema|system prompt|istruzioni interne|regole interne|security knowledge|logica antifrode|risk score/i,
    /repository privat|endpoint privat|configurazione interna|architettura interna|codice sorgente riserv/i,
    /ignora .*istruz|fingi .*amministrator|bypass|aggira .*controll/i
  ];

  function esc(s){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));}
  function t(k){return (TXT[state.lang]||TXT.it)[k] || TXT.it[k] || k;}
  function pageContext(){
    const p=(location.pathname.split('/').pop()||'index.html').toLowerCase();
    const map={ 'index.html':'Home','assistente-ai.html':'VìSì','verifica-annuncio.html':'Verifica annuncio','controlla-cin.html':'Controllo CIN','eventi.html':'Eventi','candidatura.html':'Candidature','lavora-con-noi.html':'Lavora con noi','contatti.html':'Contatti','login.html':'Accesso' };
    return map[p] || document.title || 'Vacanze Sicure';
  }
  function isSecretProbe(q){ return secretPatterns.some(r=>r.test(q)); }

  async function reportSecurity(q, attempt){
    const payload={type:'SECURITY_SECRET_PROBING', attempt, page:location.pathname, message:q, occurred_at:new Date().toISOString(), user_agent:navigator.userAgent};
    try{
      if(cfg.apiBaseUrl) await fetch(cfg.apiBaseUrl.replace(/\/$/,'')+'/security-events',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),keepalive:true});
    }catch(e){}
  }

  async function askBackend(q){
    if(!cfg.visiEndpoint) return null;
    try{
      const r=await fetch(cfg.visiEndpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q,lang:state.lang,page:location.pathname})});
      if(!r.ok) return null;
      const d=await r.json();
      return typeof d.answer==='string' ? d.answer : null;
    }catch(e){ return null; }
  }

  function publicAnswer(q){
    if(isSecretProbe(q)){
      state.securityAttempts++;
      reportSecurity(q,state.securityAttempts);
      if(state.securityAttempts===1) return t('security1');
      if(state.securityAttempts===2) return t('security2');
      state.closedForSecurity=true;
      return t('security3');
    }
    const list=FAQ[state.lang] || FAQ.it;
    const hit=list.find(x=>x.p.test(q));
    return hit ? hit.a : t('unknown');
  }

  function mount(){
    if(document.getElementById('visiChatLauncher')) return;
    const root=document.createElement('div');
    root.id='visiChatRoot';
    root.innerHTML=`
      <button id="visiChatLauncher" class="visi-chat-launcher" aria-label="Apri chat con VìSì" title="VìSì">
        <img src="assets/img/visi-avatar.png" alt="VìSì">
      </button>
      <aside id="visiChatWindow" class="visi-chat-window" aria-hidden="true">
        <header class="visi-chat-head">
          <img src="assets/img/visi-avatar.png" alt="VìSì">
          <div class="visi-chat-title"><strong>${esc(t('title'))}</strong><small><span class="visi-online-dot">●</span> ${esc(t('online'))} · ${esc(t('subtitle'))}</small></div>
          <button id="visiChatClose" class="visi-chat-close" aria-label="Chiudi">×</button>
        </header>
        <div class="visi-chat-context"><span>${esc(pageContext())}</span>
          <div class="visi-lang"><button data-lang="it">IT</button><button data-lang="en">EN</button><button data-lang="de">DE</button></div>
        </div>
        <div id="visiChatMessages" class="visi-chat-messages"><div class="visi-bubble bot">${esc(t('hello'))}</div></div>
        <div class="visi-chat-actions"><a href="login.html" class="btn navy">${esc(t('signup'))}</a><a href="contatti.html" class="btn outline">${esc(t('human'))}</a></div>
        <form id="visiChatForm" class="visi-chat-form"><input id="visiChatInput" autocomplete="off" placeholder="${esc(t('placeholder'))}"><button type="submit">${esc(t('send'))}</button></form>
      </aside>`;
    document.body.appendChild(root);
    const w=root.querySelector('#visiChatWindow'), m=root.querySelector('#visiChatMessages'), i=root.querySelector('#visiChatInput');
    function open(){w.classList.add('open');w.setAttribute('aria-hidden','false');setTimeout(()=>i.focus(),120);}
    function close(){w.classList.remove('open');w.setAttribute('aria-hidden','true');}
    function add(text,who){const b=document.createElement('div');b.className='visi-bubble '+who;b.textContent=text;m.appendChild(b);m.scrollTop=m.scrollHeight;}
    root.querySelector('#visiChatLauncher').addEventListener('click',open);
    root.querySelector('#visiChatClose').addEventListener('click',close);
    document.querySelectorAll('[data-open-visi]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();open();}));
    root.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>{state.lang=b.dataset.lang; add(TXT[state.lang].hello,'bot'); i.placeholder=t('placeholder');}));
    root.querySelector('#visiChatForm').addEventListener('submit',async e=>{
      e.preventDefault(); if(state.closedForSecurity) return;
      const q=i.value.trim(); if(!q) return; i.value=''; add(q,'user');
      let a = await askBackend(q); if(!a) a=publicAnswer(q); add(a,'bot');
      if(state.closedForSecurity){ i.disabled=true; e.currentTarget.querySelector('button').disabled=true; }
    });
  }
  document.addEventListener('DOMContentLoaded',mount);
})();