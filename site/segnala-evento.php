<?php
declare(strict_types=1);
$isHttps = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off');
session_set_cookie_params(['lifetime'=>0,'path'=>'/','secure'=>$isHttps,'httponly'=>true,'samesite'=>'Lax']);
session_start();
$email = (string)($_SESSION['auth_email'] ?? '');
if ($email === '') {
  header('Location: login.html?dest=evento');
  exit;
}
$csrf = (string)($_SESSION['csrf_token'] ?? '');
if ($csrf === '') { $csrf = bin2hex(random_bytes(32)); $_SESSION['csrf_token'] = $csrf; }
?>
<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Segnala un evento | Vacanze Sicure</title><meta name="description" content="Segnala un evento a Vacanze Sicure."><link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg"><link rel="stylesheet" href="assets/style.css"></head><body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a><nav class="links"><a href="index.html">Home</a><a href="news.html">News</a><a href="eventi.html">Eventi</a><a href="assistente-ai.html">VìSì AI</a><a href="contatti.html">Contatti</a></nav></div></header>
<section class="pagehead"><div class="wrap"><span class="badge">UTENTE AUTENTICATO</span><h1>Segnala una festa o un evento</h1><p class="lead">La segnalazione viene protocollata. Gli eventi da fonte ufficiale possono essere pubblicati direttamente; gli altri seguono il percorso di verifica previsto.</p></div></section>
<section class="section white"><div class="wrap formwrap"><form class="form-card" action="invia.php" method="post">
<input type="hidden" name="form_type" value="evento"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars($csrf, ENT_QUOTES, 'UTF-8') ?>"><input type="text" name="website" value="" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
<label>Nome e cognome<input name="nome" required></label>
<label>E-mail<input name="email" type="email" value="<?= htmlspecialchars($email, ENT_QUOTES, 'UTF-8') ?>" readonly required></label>
<label>Telefono<input name="telefono" type="tel"></label>
<label>Titolo evento<input name="titolo" required></label>
<label>Comune<input name="comune" required></label>
<label>Luogo / sede<input name="luogo"></label>
<label>Territorio / provincia<input name="territorio" required></label>
<label>Tipologia<select name="tipo_evento" required><option value="">Seleziona</option><option>Evento organizzato da Comune/ente pubblico</option><option>Festa patronale</option><option>Evento di organizzatore ufficiale</option><option>Evento privato / locale pubblico</option><option>Altro</option></select></label>
<label>Categoria<select name="categoria"><option>Festa / tradizione</option><option>Concerto / musica</option><option>Sagra / enogastronomia</option><option>Cultura</option><option>Sport</option><option>Mercatino / fiera</option><option>Altro</option></select></label>
<label>Data inizio<input name="data_inizio" type="date" required></label>
<label>Ora inizio<input name="ora_inizio" type="time"></label>
<label>Data fine<input name="data_fine" type="date"></label>
<label>Fonte ufficiale o pagina evento<input name="fonte_url" type="url" placeholder="https://..."></label>
<label>Descrizione<textarea name="descrizione" rows="6" required></textarea></label>
<label>Link locandina / immagine<input name="locandina_url" type="url" placeholder="https://..."></label>
<label><input type="checkbox" name="privacy" value="1" required> Confermo di aver letto l'informativa privacy e che i dati inseriti sono corretti per quanto a mia conoscenza.</label>
<button class="btn primary" type="submit">Invia evento</button>
<p class="small">Le locandine di eventi patronali segnalate da terzi vengono riscontrate sul canale ufficiale del Comune; gli eventi privati possono richiedere verifica da parte del referente territoriale.</p>
</form></div></section>
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>