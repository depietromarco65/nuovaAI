<?php
declare(strict_types=1);

$isHttps = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off');
session_set_cookie_params([
  'lifetime' => 0,
  'path' => '/',
  'secure' => $isHttps,
  'httponly' => true,
  'samesite' => 'Lax'
]);
session_start();

function clean(string $v): string { return trim(preg_replace('/[\r\n]+/', ' ', $v)); }
function safeDest(string $dest): string {
  $map = [
    'evento' => 'segnala-evento.php',
    'stasera' => 'stasera.html',
    'home' => 'index.html'
  ];
  return $map[$dest] ?? 'index.html';
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
  header('Location: login.html');
  exit;
}

$email = clean((string)($_POST['email'] ?? ''));
$destKey = clean((string)($_POST['dest'] ?? 'home'));
$dest = safeDest($destKey);

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  http_response_code(400);
  exit('Indirizzo e-mail non valido.');
}

$now = time();
$last = (int)($_SESSION['otp_last_sent'] ?? 0);
if ($last > 0 && ($now - $last) < 60) {
  http_response_code(429);
  exit('Attendi almeno 60 secondi prima di richiedere un nuovo codice.');
}

$code = (string)random_int(100000, 999999);
$_SESSION['otp_hash'] = password_hash($code, PASSWORD_DEFAULT);
$_SESSION['otp_email'] = $email;
$_SESSION['otp_expires'] = $now + 600;
$_SESSION['otp_attempts'] = 0;
$_SESSION['otp_last_sent'] = $now;
$_SESSION['login_dest'] = $dest;

$subject = 'Vacanze Sicure - codice di accesso';
$message = "Il tuo codice di accesso a Vacanze Sicure è: {$code}\n\n" .
           "Il codice scade tra 10 minuti.\n\n" .
           "Se non hai richiesto tu questo accesso, ignora questa e-mail.\n\nVacanze Sicure";
$headers = [
  'From: Vacanze Sicure <postmaster@vacanzesicure.online>',
  'Reply-To: info@vacanzesicure.online',
  'Content-Type: text/plain; charset=UTF-8'
];
@mail($email, $subject, $message, implode("\r\n", $headers));
?>
<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Verifica accesso | Vacanze Sicure</title><link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg"><link rel="stylesheet" href="assets/style.css"></head><body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a></div></header>
<section class="pagehead"><div class="wrap"><span class="badge">CODICE INVIATO</span><h1>Controlla la tua e-mail</h1><p class="lead">Abbiamo inviato un codice monouso a <b><?= htmlspecialchars($email, ENT_QUOTES, 'UTF-8') ?></b>.</p></div></section>
<section class="section white"><div class="wrap formwrap"><form class="form-card" action="login-verify.php" method="post" autocomplete="off"><h2>Inserisci il codice</h2><label>Codice a 6 cifre<input name="code" inputmode="numeric" pattern="[0-9]{6}" maxlength="6" required></label><input type="hidden" name="dest" value="<?= htmlspecialchars($destKey, ENT_QUOTES, 'UTF-8') ?>"><button class="btn primary" type="submit">Accedi</button><p class="small">Il codice scade dopo 10 minuti.</p></form></div></section>
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>