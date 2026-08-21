<?php
$t=trim((string)($_GET['territorio']??'')); $l=trim((string)($_GET['localita']??''));
function s($v){return htmlspecialchars((string)$v,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
$structuresData=json_decode((string)@file_get_contents(__DIR__.'/data/strutture.json'),true) ?: [];
$key=strtolower(str_replace([' ','à','è','é','ì','ò','ù'],['-','a','e','e','i','o','u'],$l));
$structures=$structuresData[$key] ?? [];
?><!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title><?php echo s($l); ?> | Vacanze Sicure</title><link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg"><link rel="stylesheet" href="assets/style.css"></head><body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a></div></header>
<section class="pagehead"><div class="wrap"><div class="breadcrumbs"><a href="index.html#territori">Italia</a> › <a href="territorio.php?territorio=<?php echo urlencode($t); ?>"><?php echo s($t); ?></a> › <?php echo s($l); ?></div><span class="badge">LOCALITÀ SELEZIONATA</span><h1><?php echo s($l); ?></h1><p class="lead"><?php echo s($t); ?></p></div></section>

<section class="section white"><div class="wrap">
<?php if($structures): ?>
<span class="section-kicker">Strutture disponibili</span>
<h2>Strutture già presenti su Vacanze Sicure</h2>
<p class="lead">In questa località sono già presenti strutture inserite nel percorso di verifica Vacanze Sicure.</p>
<div class="property-list">
<?php foreach($structures as $p): ?>
<article class="property-card">
<div class="property-mark"><img src="assets/img/acasa-logo.png" alt="Logo A Casa di Amici" style="max-width:130px;max-height:95px"></div>
<div>
<div class="locality-verified"><div class="tiny-gold">✓</div><div><b>STRUTTURA VERIFICATA</b><br><span class="small">Vacanze Sicure</span></div></div>
<h3><?php echo s($p['nome']); ?></h3>
<div class="property-meta"><?php echo s($p['tipologia']); ?> · <?php echo s($p['localita']); ?></div>
<p><?php echo s($p['claim']); ?></p>
</div>
<div><a class="btn navy" href="struttura.php?id=<?php echo urlencode($p['id']); ?>">Apri scheda</a></div>
</article>
<?php endforeach; ?>
</div>
<?php else: ?>
<div class="territory-message"><h2>Stiamo completando tutte le verifiche necessarie.</h2><p>Le strutture ricettive e i servizi di <strong><?php echo s($l); ?></strong> sono ancora in fase di verifica e <strong>presto saranno progressivamente online su Vacanze Sicure</strong>.</p><p>Se ci lasci la tua email, ti informeremo appena avremo completato i primi controlli.</p></div>
<form action="invia-interesse.php" method="post"><input type="hidden" name="territorio" value="<?php echo s($t); ?>"><input type="hidden" name="localita" value="<?php echo s($l); ?>"><input type="text" name="website" style="display:none">
<div class="two"><label>Nome e cognome<input name="nome"></label><label>Email *<input required type="email" name="email"></label></div>
<label class="checkline"><input required type="checkbox" name="privacy" value="1"><span>Chiedo di essere informato quando saranno disponibili strutture e servizi verificati nella località selezionata.</span></label>
<button class="btn secondary" type="submit">AVVISAMI</button></form>
<?php endif; ?>

<div class="notice" style="margin-top:28px"><b>Hai già trovato un altro annuncio a <?php echo s($l); ?>?</b><p>Puoi inviarcelo subito per richiedere un controllo.</p><a class="btn primary" href="verifica-annuncio.html">Verifica un annuncio</a></div>
</div></section></body></html>