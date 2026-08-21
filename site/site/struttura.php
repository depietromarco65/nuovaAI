<?php
$id=trim((string)($_GET['id']??''));
function s($v){return htmlspecialchars((string)$v,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
$data=json_decode((string)@file_get_contents(__DIR__.'/data/strutture.json'),true) ?: [];
$p=null;
foreach($data as $arr){foreach($arr as $row){if(($row['id']??'')===$id){$p=$row;break 2;}}}
if(!$p){http_response_code(404);exit('Struttura non trovata');}
?><!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title><?php echo s($p['nome']); ?> | Vacanze Sicure</title><link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg"><link rel="stylesheet" href="assets/style.css"></head><body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a><nav class="links"><a href="index.html">Home</a><a href="verifica-annuncio.html">Verifica annuncio</a><a href="controlla-cin.html">Controlla CIN</a><a href="segnala.html">Segnala</a></nav></div></header>

<section class="pagehead"><div class="wrap"><div class="breadcrumbs"><a href="index.html#territori">Italia</a> › <a href="territorio.php?territorio=<?php echo urlencode($p['territorio']); ?>"><?php echo s($p['territorio']); ?></a> › <a href="localita.php?territorio=<?php echo urlencode($p['territorio']); ?>&localita=Torre%20Pali">Torre Pali</a> › <?php echo s($p['nome']); ?></div>
<span class="verified-pill">✓ <?php echo s($p['stato_vs']); ?></span>
<div class="structure-title-row"><h1><?php echo s($p['nome']); ?></h1><div class="title-gold-shield">✓<small>STRUTTURA<br>VERIFICATA</small></div></div><p class="lead"><?php echo s($p['tipologia']); ?> · <?php echo s($p['localita']); ?></p></div></section>

<section class="section white"><div class="wrap property-detail">
<div>
<div class="real-cover">
<img class="cover" src="assets/img/acasa-copertina-aerea.jpg" alt="Vista aerea A Casa di Amici">
<div class="host-logo"><img src="assets/img/acasa-logo.png" alt="Logo A Casa di Amici"></div>
<div class="gold-shield-wrap"><div class="vs-shield gold"><div class="check">✓</div>STRUTTURA<br>VERIFICATA<div class="small">VACANZE SICURE</div></div></div>
</div>

<h2 style="margin-top:28px">Informazioni principali</h2>
<div class="fact-grid">
<div class="fact"><b>CIN</b><br><?php echo s($p['cin']); ?></div>
<div class="fact"><b>Territorio</b><br><?php echo s($p['territorio']); ?> · Torre Pali</div>
<div class="fact"><b>Sito ufficiale</b><br><a href="<?php echo s($p['sito']); ?>" target="_blank" rel="noopener"><?php echo s($p['sito']); ?></a></div>
<div class="fact"><b>Contatto</b><br><?php echo s($p['telefono']); ?><br><?php echo s($p['email']); ?></div>
</div>

<h2 style="margin-top:28px">Distanze indicative</h2><ul><?php foreach($p['distanze'] as $v): ?><li><?php echo s($v); ?></li><?php endforeach; ?></ul>
<h2>Servizi principali</h2><ul><?php foreach($p['servizi'] as $v): ?><li><?php echo s($v); ?></li><?php endforeach; ?></ul>
</div>

<aside class="verify-panel">
<span class="badge">PERCORSO DI VERIFICA</span>
<h2>Stato dei controlli</h2>
<?php foreach($p['controlli'] as $row): ?>
<div class="verify-row"><span><?php echo s($row[0]); ?></span><span class="ok">✓ <?php echo s($row[1]); ?></span></div>
<?php endforeach; ?>
<div class="notice" style="margin-top:18px"><b>Il CIN è un controllo, non una garanzia.</b><p>La verifica Vacanze Sicure considera più elementi. Il CIN da solo non determina l'affidabilità complessiva di una struttura o di un annuncio.</p></div>
<p><a class="btn primary" href="<?php echo s($p['sito']); ?>" target="_blank" rel="noopener">Visita il sito ufficiale</a></p>
</aside>

<section style="margin-top:54px"><span class="section-kicker">Legenda scudi</span><h2>Livelli di verifica Vacanze Sicure</h2>
<p class="lead">Gli scudi indicano lo stato del percorso Vacanze Sicure. Non rappresentano una classificazione alberghiera.</p>
<div class="shield-legend">
<div class="shield-key"><span class="mini-shield mini-gray"></span><b>Attività non accertata</b><p>Presente nel sistema, ma senza accertamenti sufficienti.</p></div>
<div class="shield-key"><span class="mini-shield mini-white"></span><b>In fase di verifica</b><p>Il percorso di controllo è stato avviato.</p></div>
<div class="shield-key"><span class="mini-shield mini-blue"></span><b>Identità verificata</b><p>Identità del soggetto o della struttura controllata.</p></div>
<div class="shield-key"><span class="mini-shield mini-green"></span><b>Verifica avanzata</b><p>Una parte significativa dei controlli è stata completata.</p></div>
<div class="shield-key"><span class="mini-shield mini-gold"></span><b>Struttura verificata</b><p>Tutte le fasi previste dal protocollo VS risultano completate.</p></div>
<div class="shield-key"><span class="mini-shield mini-platinum"></span><b>Struttura verificata PLUS</b><p>Verifica completa e ulteriori criteri di esperienza previsti dal protocollo PLUS.</p></div>
<div class="shield-key"><span class="mini-shield mini-orange"></span><b>Attività sospesa</b><p>Stato sospeso mentre sono in corso approfondimenti.</p></div>
<div class="shield-key"><span class="mini-shield mini-red"></span><b>Attività da evitare</b><p>Stato critico attribuito solo a seguito di accertamenti documentati.</p></div>
</div></section></div></section>
</body></html>