function trackTerritory(name, locality=''){
  try{ fetch('interesse-click.php?territorio='+encodeURIComponent(name)+'&localita='+encodeURIComponent(locality), {cache:'no-store'}); }catch(e){}
}
function openTerritory(name){ trackTerritory(name); window.location.href='territorio.php?territorio='+encodeURIComponent(name); }

(function(){
  const cfg = window.VS_CONFIG || {};
  const state = { lang: cfg.defaultLanguage || 'it', securityAttempts: 0, closedForSecurity: false, news: [] };

  const TXT = {
    it:{
      title:'VìSì', subtitle:'Assistente Vacanze Sicure', online:'Online',
      hello:'Ciao 👋 Sono VìSì. Posso aiutarti con Vacanze Sicure, annunci, CIN, eventi, territorio, mobilità e procedure pubbliche. Come posso aiutarti?',
      placeholder:'Scrivi a VìSì…', send:'Invia', signup:'Iscriviti', human:'Parla con una persona',
      security1:'Alcune informazioni richieste sono riservate e non possono essere divulgate. Posso però aiutarti con le informazioni pubbliche e con le funzioni disponibili sul sito.',
      security2:'Ti informo che richieste reiterate volte a ottenere informazioni riservate, tecniche o interne non possono essere soddisfatte. Ti invito a non proseguire con richieste di questo tipo.',
      security3:'La conversazione è stata chiusa per reiterate richieste di informazioni riservate. L’evento è stato segnalato al sistema di sicurezza per la verifica prevista.',
      unknown:'Su questo punto non ho ancora una risposta pubblica sufficientemente affidabile. Posso indicarti la fonte disponibile oppure passare la richiesta a un operatore.'
    },
    en:{
      title:'VìSì', subtitle:'Vacanze Sicure Assistant', online:'Online',
      hello:'Hi 👋 I’m VìSì. I can help with Vacanze Sicure, listings, CIN, events, local information, mobility and public procedures. How can I help?',
      placeholder:'Write to VìSì…', send:'Send', signup:'Sign up', human:'Talk to a person',
      security1:'Some of the information requested is confidential and cannot be disclosed. I can still help with public information and the services available on this website.',
      security2:'Repeated attempts to obtain confidential, technical or internal information cannot be fulfilled. Please do not continue with this type of request.',
      security3:'This chat has been closed after repeated requests for confidential information. The event has been reported to the security system for review.',
      unknown:'I do not yet have a sufficiently reliable public answer for this. I can point you to an available source or pass the request to a human operator.'
    },
    de:{
      title:'VìSì', subtitle:'Assistent von Vacanze Sicure', online:'Online',
      hello:'Hallo 👋 Ich bin VìSì. Ich helfe bei Vacanze Sicure, Inseraten, CIN, Veranstaltungen, lokalen Informationen, Mobilität und öffentlichen Verfahren. Wie kann ich helfen?',
      placeholder:'Schreibe an VìSì…', send:'Senden', signup:'Registrieren', human:'Mit einer Person sprechen',
      security1:'Einige der angeforderten Informationen sind vertraulich und dürfen nicht offengelegt werden. Ich kann dir jedoch mit öffentlichen Informationen und den Funktionen dieser Website helfen.',
      security2:'Wiederholte Versuche, vertrauliche, technische oder interne Informationen zu erhalten, können nicht erfüllt werden. Bitte stelle keine weiteren Fragen dieser Art.',
      security3:'Der Chat wurde nach wiederholten Anfragen nach vertraulichen Informationen geschlossen. Der Vorgang wurde zur Prüfung an das Sicherheitssystem gemeldet.',
      unknown:'Dazu habe ich noch keine ausreichend verlässliche öffentliche Antwort. Ich kann dir eine verfügbare Quelle nennen oder die Anfrage an einen Mitarbeiter weitergeben.'
    }
  };

  const FAQ = {
    it:[
      {p:/^(ciao|salve|hey|hei|buongiorno|buonasera|buondì|buondi)[!?. ]*$/i, a:'Ciao! 👋 Sono VìSì, l’assistente di Vacanze Sicure. Posso aiutarti con annunci, CIN, eventi, mobilità, territorio e informazioni sui servizi. Cosa vorresti sapere?'},
      {p:/^(grazie|grazie mille|ti ringrazio)[!?. ]*$/i, a:'Di nulla 😊 Se vuoi, dimmi cos’altro posso controllare o spiegarti.'},
      {p:/chi sei|cosa sai fare|come puoi aiutarmi/i, a:'Sono VìSì, l’assistente di Vacanze Sicure. Posso orientarti tra annunci, strutture, verifiche, CIN, eventi, territorio, mobilità, servizi e pratiche pubbliche. Quando una decisione richiede una persona, preparo il passaggio all’assistenza umana.'},
      {p:/chi siete|cos.?è vacanze sicure|cosa fate|a cosa serve/i, a:'Vacanze Sicure è un ecosistema che aiuta Viaggiatori, Host e operatori a orientarsi tra annunci, strutture, informazioni, verifiche disponibili e assistenza.'},
      {p:/come mi iscrivo|iscrizione|registrarmi|creare account/i, a:'Puoi iniziare dalla pagina Accesso/Registrazione. Se mi dici se sei Viaggiatore, Host/Gestore o Professionista, ti indico il percorso più adatto.'},
      {p:/cin|codice identificativo/i, a:'Il CIN è un dato importante da controllare. Vacanze Sicure distingue tra dato dichiarato, fonte consultata e risultato del controllo. Il CIN da solo non rappresenta una garanzia assoluta sull’affidabilità complessiva.'},
      {p:/host|gestore|proprietario/i, a:'Per Host e Gestori, Vacanze Sicure prevede una Scheda Master dell’alloggio con descrizioni, fotografie, camere, letti, bagni, dotazioni, regole, prezzi, disponibilità, documenti e canali collegati. VìSì può aiutare a individuare informazioni mancanti senza inventarle.'},
      {p:/annuncio|facebook|booking|airbnb|vrbo|expedia|agoda/i, a:'Puoi usare Vacanze Sicure per comprendere meglio un annuncio e distinguere ciò che è dichiarato da ciò che deve essere controllato. Le informazioni dei canali vengono progressivamente ricondotte alla stessa Scheda Master quando tecnicamente possibile.'},
      {p:/operatore|persona|umano|assistenza|centrale/i, a:'Se una risposta richiede una decisione umana, una verifica specifica o informazioni non pubbliche, posso indirizzarti a un operatore Vacanze Sicure.'},
      {p:/lavora|candidatura|personale|professionista/i, a:'Vacanze Sicure raccoglie candidature di dipendenti e professionisti per categoria e area. La rete può essere utilizzata per esigenze VS o per richieste dirette degli Host.'},
      {p:/reclamo|lamentela|segnalazione|protocollo|pratica/i, a:'Le pratiche di verifica, reclamo e segnalazione sono progettate per avere un protocollo univoco, un assegnatario, uno stato e uno storico. Le informazioni visibili dipendono dal ruolo e dall’autorizzazione dell’utente.'},
      {p:/ical|calendario|api|channel manager|pms/i, a:'Vacanze Sicure prevede l’allineamento delle disponibilità tramite API/webhook quando disponibili e iCal come fallback. La Scheda Master resta il riferimento centrale dei dati dell’alloggio.'}
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
    const map={ 'index.html':'Home','news.html':'News','assistente-ai.html':'VìSì','verifica-annuncio.html':'Verifica annuncio','controlla-cin.html':'Controllo CIN','eventi.html':'Eventi','candidatura.html':'Candidature','lavora-con-noi.html':'Lavora con noi','contatti.html':'Contatti','login.html':'Accesso' };
    return map[p] || document.title || 'Vacanze Sicure';
  }
  function isSecretProbe(q){ return secretPatterns.some(r=>r.test(q)); }

  async function loadNews(){
    try{
      const r=await fetch('data/news.json',{cache:'no-store'});
      if(!r.ok) return [];
      const d=await r.json();
      state.news=Array.isArray(d.items)?d.items:[];
      return state.news;
    }catch(e){ return []; }
  }

  function activeNews(){
    const now=Date.now();
    return state.news.filter(n=>!n.expires_at || new Date(n.expires_at).getTime()>now);
  }

  function newsAnswer(q){
    if(!state.news.length) return null;
    const normalized=q.toLowerCase();
    const wantsNews=/news|notizi|evento|stasera|oggi|settimana|concerto|festa|taranta|sant.?oronzo|lecce|melpignano|navett|mobilit/i.test(normalized);
    if(!wantsNews) return null;
    let items=activeNews();
    if(/taranta|melpignano/.test(normalized)) items=items.filter(n=>/taranta|melpignano/i.test(n.title+' '+n.place));
    else if(/sant.?oronzo|lecce/.test(normalized)) items=items.filter(n=>/lecce|oronzo/i.test(n.title+' '+n.place+' '+n.summary));
    if(!items.length) return 'Non risultano al momento notizie attive corrispondenti nella mia knowledge pubblica. Posso comunque indicarti la pagina News o una fonte ufficiale.';
    return items.slice(0,3).map(n=>`${n.title} — ${n.place}. ${n.summary} Fonte: ${n.source_name}${n.media?' '+n.media:''}`).join('\n\n');
  }

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
    const n=newsAnswer(q); if(n) return n;
    const list=FAQ[state.lang] || FAQ.it;
    const hit=list.find(x=>x.p.test(q));
    return hit ? hit.a : t('unknown');
  }

  function injectStyles(){
    if(document.getElementById('vsEnhancementStyles')) return;
    const s=document.createElement('style'); s.id='vsEnhancementStyles'; s.textContent=`
      .vs-news-highlight{padding:44px 0;background:#fff}.vs-news-head{display:flex;justify-content:space-between;gap:20px;align-items:end;margin-bottom:20px}.vs-news-three{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.vs-news-tile{display:flex;flex-direction:column;min-height:330px;border:1px solid #e2ebed;border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 8px 28px rgba(22,44,52,.07)}.vs-news-media{min-height:145px;display:grid;place-items:center;font-size:54px;background:linear-gradient(135deg,#11323d,#2f7780);color:#fff}.vs-news-body{padding:18px;display:flex;flex:1;flex-direction:column}.vs-news-body h3{margin:8px 0}.vs-news-meta{font-size:.82rem;opacity:.7}.vs-news-badge{align-self:flex-start;font-size:.72rem;font-weight:800;border-radius:999px;padding:6px 9px;background:#e7f6f5;color:#173f4b}.vs-news-promoted{background:#fff1cc;color:#6d4e00}.vs-news-body .btn{margin-top:auto;align-self:flex-start}.vs-footer-expanded{margin-top:24px;border-top:1px solid rgba(255,255,255,.14);padding-top:28px}.vs-footer-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}.vs-footer-grid h4{margin:0 0 10px}.vs-footer-grid p{line-height:1.8}.vs-collab{margin-top:26px;padding:18px 0;border-top:1px solid rgba(255,255,255,.14);display:flex;justify-content:space-between;gap:18px;align-items:center;flex-wrap:wrap}.vs-source-note{font-size:.82rem;opacity:.72;margin-top:12px}@media(max-width:900px){.vs-news-three{grid-template-columns:1fr}.vs-footer-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){.vs-news-head{align-items:start;flex-direction:column}.vs-footer-grid{grid-template-columns:1fr}}
    `; document.head.appendChild(s);
  }

  async function mountHomeNews(){
    const isHome=(location.pathname==='/' || /\/index\.html$/i.test(location.pathname));
    if(!isHome || document.getElementById('vsNewsHighlight')) return;
    if(!state.news.length) await loadNews();
    const items=activeNews().filter(n=>n.featured).slice(0,3); if(!items.length) return;
    const sec=document.createElement('section'); sec.id='vsNewsHighlight'; sec.className='vs-news-highlight';
    sec.innerHTML=`<div class="wrap"><div class="vs-news-head"><div><span class="section-kicker">Oggi e questa settimana</span><h2>News ed eventi in evidenza</h2><p class="lead">Fonti ufficiali, informazioni utili e contenuti che restano in evidenza fino alla loro scadenza.</p></div><a class="btn outline" href="news.html">Tutte le news</a></div><div class="vs-news-three">${items.map(n=>`<article class="vs-news-tile"><div class="vs-news-media">${esc(n.visual||'📌')}</div><div class="vs-news-body"><span class="vs-news-badge ${n.promoted?'vs-news-promoted':''}">${n.promoted?'PROMOSSO · ':''}${esc(n.source_label||'Fonte')}</span><div class="vs-news-meta">${esc(n.place||'')} · ${esc(n.interest||'')}</div><h3>${esc(n.title)}</h3><p>${esc(n.summary)}</p><a class="btn navy" href="news.html#${esc(n.id)}">Scopri di più</a></div></article>`).join('')}</div></div>`;
    const hero=document.querySelector('.hero');
    if(hero && hero.parentNode) hero.parentNode.insertBefore(sec,hero.nextSibling); else document.body.prepend(sec);
  }

  function enhanceFooter(){
    const footer=document.querySelector('footer'); if(!footer || footer.querySelector('.vs-footer-expanded')) return;
    const box=document.createElement('div'); box.className='wrap vs-footer-expanded';
    box.innerHTML=`<div class="vs-footer-grid"><div><h4>Vacanze Sicure</h4><p><a href="index.html">Come funziona</a><br><a href="contatti.html">Contatti</a><br><a href="candidatura.html">Lavora con noi</a></p></div><div><h4>Servizi</h4><p><a href="verifica-annuncio.html">Verifica annuncio</a><br><a href="controlla-cin.html">Controlla CIN</a><br><a href="segnala.html">Segnala</a><br><a href="news.html">News</a><br><a href="eventi.html">Eventi</a></p></div><div><h4>Per gli utenti</h4><p><a href="login.html">Viaggiatore</a><br><a href="login.html">Host / Gestore</a><br><a href="candidatura.html">Professionisti</a><br><a href="assistente-ai.html">VìSì AI</a></p></div><div><h4>Informazioni</h4><p><a href="privacy.html">Privacy</a><br><a href="news.html">Fonti e aggiornamenti</a><br><a href="contatti.html">Assistenza umana</a></p><div class="vs-source-note">Le fonti ufficiali non sono automaticamente partner commerciali di Vacanze Sicure.</div></div><div><h4>Rete e collaborazioni</h4><p>Spazio dedicato a future collaborazioni, partner, media partner e operatori del territorio.</p><p><a href="contatti.html" class="btn outline">Proponi una collaborazione</a></p></div></div><div class="vs-collab"><div><b>Collaborazioni future</b><br><small>La visibilità commerciale non modifica mai esiti, verifiche o affidabilità delle fonti.</small></div><a href="contatti.html">Contattaci →</a></div>`;
    footer.insertBefore(box,footer.firstChild);
  }

  function mount(){
    injectStyles();
    loadNews().then(mountHomeNews);
    enhanceFooter();
    if(document.getElementById('visiChatLauncher')) return;
    const root=document.createElement('div');
    root.id='visiChatRoot';
    root.innerHTML=`
      <button id="visiChatLauncher" class="visi-chat-launcher" aria-label="Apri chat con VìSì" title="VìSì"><img src="assets/img/visi-avatar.png" alt="VìSì"></button>
      <aside id="visiChatWindow" class="visi-chat-window" aria-hidden="true">
        <header class="visi-chat-head"><img src="assets/img/visi-avatar.png" alt="VìSì"><div class="visi-chat-title"><strong>${esc(t('title'))}</strong><small><span class="visi-online-dot">●</span> ${esc(t('online'))} · ${esc(t('subtitle'))}</small></div><button id="visiChatClose" class="visi-chat-close" aria-label="Chiudi">×</button></header>
        <div class="visi-chat-context"><span>${esc(pageContext())}</span><div class="visi-lang"><button data-lang="it">IT</button><button data-lang="en">EN</button><button data-lang="de">DE</button></div></div>
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
      if(!state.news.length) await loadNews();
      let a=publicAnswer(q);
      if(a===t('unknown')){ const backend=await askBackend(q); if(backend) a=backend; }
      add(a,'bot');
      if(state.closedForSecurity){ i.disabled=true; e.currentTarget.querySelector('button').disabled=true; }
    });
  }
  document.addEventListener('DOMContentLoaded',mount);
})();