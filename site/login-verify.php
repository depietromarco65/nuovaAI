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

$code = trim((string)($_POST['code'] ?? ''));
$destKey = trim((string)($_POST['dest'] ?? 'home'));
$dest = safeDest($destKey);

if (!preg_match('/^[0-9]{6}$/', $code)) {
  http_response_code(400);
  exit('Codice non valido.');
}

$email = (string)($_SESSION['otp_email'] ?? '');
$hash = (string)($_SESSION['otp_hash'] ?? '');
$expires = (int)($_SESSION['otp_expires'] ?? 0);
$attempts = (int)($_SESSION['otp_attempts'] ?? 0) + 1;
$_SESSION['otp_attempts'] = $attempts;

if ($email === '' || $hash === '' || time() > $expires) {
  http_response_code(401);
  exit('Codice scaduto. Torna alla pagina di accesso e richiedine uno nuovo.');
}
if ($attempts > 5) {
  unset($_SESSION['otp_hash'], $_SESSION['otp_email'], $_SESSION['otp_expires']);
  http_response_code(429);
  exit('Troppi tentativi. Richiedi un nuovo codice.');
}
if (!password_verify($code, $hash)) {
  http_response_code(401);
  exit('Codice non corretto.');
}

session_regenerate_id(true);
$_SESSION['auth_email'] = $email;
$_SESSION['auth_at'] = time();
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));
unset($_SESSION['otp_hash'], $_SESSION['otp_email'], $_SESSION['otp_expires'], $_SESSION['otp_attempts']);

header('Location: ' . $dest);
exit;
?>