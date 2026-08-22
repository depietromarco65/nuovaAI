(function(){
  function isHome(){
    var p=(location.pathname||'/').toLowerCase();
    return p==='/' || p.endsWith('/index.html') || p.endsWith('index.html');
  }

  function addStyles(){
    if(document.getElementById('vsHomeNewsStyles')) return;
    var s=document.createElement('style');
    s.id='vsHomeNewsStyles';
    s.textContent='\
    .vs-home-news{padding:44px 0;background:#fff;border-top:1px solid #edf2f3;border-bottom:1px solid #edf2f3}\
    .vs-home-news-head{display:flex;justify-content:space-between;gap:20px;align-items:end;margin-bottom:22px}\
    .vs-home-news-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}\
    .vs-home-news-card{display:flex;flex-direction:column;overflow:hidden;border:1px solid #dfe9eb;border-radius:18px;background:#fff;box-shadow:0 8px 28px rgba(22,44,52,.07)}\
    .vs-home-news-visual{min-height:150px;display:grid;place-items:center;font-size:58px;background:linear-gradient(135deg,#12343f,#2f7880);color:#fff}\
    .vs-home-news-body{display:flex;flex:1;flex-direction:column;padding:18px}\
    .vs-home-news-badge{align-self:flex-start;padding:6px 9px;border-radius:999px;background:#e7f6f5;color:#173f4b;font-size:.72rem;font-weight:800}\
    .vs-home-news-meta{font-size:.82rem;opacity:.72;margin:10px 0 6px}\
    .vs-home-news-card h3{margin:6px 0 10px}\
    .vs-home-news-card .btn{margin-top:auto;align-self:flex-start}\
    .vs-home-news-source{margin-top:12px;font-size:.8rem;opacity:.72}\
    @media(max-width:900px){.vs-home-news-grid{grid-template-columns:1fr}.vs-home-news-head{align-items:start;flex-direction:column}}';
    document.head.appendChild(s);
  }

  function build(){
    if(!isHome() || document.getElementById('vsHomeNews')) return;
    addStyles();
    var sec=document.createElement('section');
    sec.id='vsHomeNews';
    sec.className='vs-home-news';
    sec.innerHTML='<div class="wrap">\
      <div class="vs-home-news-head">\
        <div><span class="section-kicker">Oggi e questa settimana</span><h2>News ed eventi in evidenza</h2><p class="lead">Eventi, mobilità e informazioni utili selezionate da fonti ufficiali e affidabili.</p></div>\
        <a class="btn outline" href="news.html">Tutte le news</a>\
      </div>\
      <div class="vs-home-news-grid">\
        <article class="vs-home-news-card">\
          <div class="vs-home-news-visual">🎶</div>\
          <div class="vs-home-news-body"><span class="vs-home-news-badge">FONTE UFFICIALE · OGGI</span><div class="vs-home-news-meta">Melpignano (LE) · 22 agosto 2026 · Interesse nazionale</div><h3>Concertone La Notte della Taranta 2026</h3><p>Questa sera a Melpignano si tiene il Concertone de La Notte della Taranta 2026, con Ermal Meta Maestro Concertatore.</p><p><b>TV e streaming:</b> Rai 3 e RaiPlay.</p><a class="btn navy" href="news.html">Leggi la notizia</a><div class="vs-home-news-source">Fonte: Fondazione La Notte della Taranta · RaiPlay</div></div>\
        </article>\
        <article class="vs-home-news-card">\
          <div class="vs-home-news-visual">🎆</div>\
          <div class="vs-home-news-body"><span class="vs-home-news-badge">FONTE ISTITUZIONALE</span><div class="vs-home-news-meta">Lecce · 23–26 agosto 2026</div><h3>Festa dei Santi Patroni Oronzo, Giusto e Fortunato</h3><p>Festeggiamenti civili, religiosi, musicali e tradizionali nel capoluogo salentino.</p><a class="btn navy" href="news.html">Programma e dettagli</a><div class="vs-home-news-source">Fonte: Comune di Lecce</div></div>\
        </article>\
        <article class="vs-home-news-card">\
          <div class="vs-home-news-visual">🚌</div>\
          <div class="vs-home-news-body"><span class="vs-home-news-badge">MOBILITÀ</span><div class="vs-home-news-meta">Lecce · 23–26 agosto 2026</div><h3>Navette gratuite per Sant’Oronzo</h3><p>Collegamenti serali tra parcheggi di interscambio, centro città e luna park. Verificare sempre l’ultimo avviso ufficiale prima di partire.</p><a class="btn navy" href="news.html">Info mobilità</a><div class="vs-home-news-source">Fonte: Comune di Lecce</div></div>\
        </article>\
      </div>\
    </div>';

    var anchor=document.querySelector('.section.soft.home-section-divider') || document.querySelector('#territori') || document.querySelector('footer');
    if(anchor && anchor.parentNode) anchor.parentNode.insertBefore(sec,anchor); else document.body.appendChild(sec);
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',build); else build();
})();