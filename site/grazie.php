<?php
$practice = htmlspecialchars($_GET['pratica'] ?? 'nd', ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
$type = $_GET['tipo'] ?? '';
$isReport = ($type === 'segnalazione');
?>
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pratica presa in carico | Vacanze Sicure</title><link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a></div></header>
<section class="section"><div class="wrap"><div class="success-card">
<span class="badge">PRESA IN CARICO</span>
<h1>Abbiamo preso in carico tutte le informazioni.</h1>
<p style="font-size:20px"><strong>Numero pratica: <?php echo $practice; ?></strong></p>
<p>Conservi questo numero e lo indichi ogni volta che ci scrive o ci contatta telefonicamente. In questo modo i nostri operatori potranno individuare immediatamente la pratica e avere a disposizione lo storico delle informazioni.</p>
<?php if ($isReport): ?>
<div class="info"><strong>Riceverà una notifica ad ogni evolversi della vicenda.</strong></div>
<?php else: ?>
<div class="info"><strong>La richiesta è stata registrata e verrà gestita utilizzando questo numero di pratica.</strong></div>
<?php endif; ?>
<p><strong>Stato attuale:</strong> Presa in carico</p>
<p><a class="btn navy" href="index.html">Torna alla Home</a></p>
</div></div></section>
</body></html>