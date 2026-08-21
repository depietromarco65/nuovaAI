<?php
declare(strict_types=1);

function clean($v): string {
  $v = trim((string)$v);
  $v = preg_replace('/[\r\n]+/', ' ', $v);
  return $v;
}

function nextPracticeId(string $dataDir): string {
  if (!is_dir($dataDir)) {
    @mkdir($dataDir, 0750, true);
  }
  $counterFile = $dataDir . '/counter.txt';
  $fp = fopen($counterFile, 'c+');
  if (!$fp) {
    return 'VS-' . date('Y') . '-' . substr((string)time(), -6);
  }
  flock($fp, LOCK_EX);
  rewind($fp);
  $raw = trim(stream_get_contents($fp));
  $n = ctype_digit($raw) ? ((int)$raw + 1) : 1;
  ftruncate($fp, 0);
  rewind($fp);
  fwrite($fp, (string)$n);
  fflush($fp);
  flock($fp, LOCK_UN);
  fclose($fp);
  return sprintf('VS-%s-%06d', date('Y'), $n);
}

function appendAudit(string $dataDir, array $row): void {
  if (!is_dir($dataDir)) @mkdir($dataDir, 0750, true);
  $file = $dataDir . '/pratiche.csv';
  $isNew = !file_exists($file);
  $fp = @fopen($file, 'a');
  if (!$fp) return;
  if (flock($fp, LOCK_EX)) {
    if ($isNew) {
      fputcsv($fp, ['Numero_Pratica','Data','Ora','Tipo','Nome','Email','Telefono','Territorio','Oggetto','Stato']);
    }
    fputcsv($fp, $row);
    flock($fp, LOCK_UN);
  }
  fclose($fp);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
  header('Location: index.html');
  exit;
}
if (!empty($_POST['website'] ?? '')) {
  header('Location: index.html');
  exit;
}

$type = clean($_POST['form_type'] ?? '');
$name = clean($_POST['nome'] ?? '');
$email = clean($_POST['email'] ?? '');
$phone = clean($_POST['telefono'] ?? '');
$territory = clean($_POST['territorio'] ?? '');

if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  http_response_code(400);
  exit('Dati non validi.');
}

$dataDir = __DIR__ . '/data';
$practiceId = nextPracticeId($dataDir);

$recipient = ($type === 'candidatura')
  ? 'partner@vacanzesicure.online'
  : 'info@vacanzesicure.online';

$subjects = [
  'verifica' => 'Richiesta verifica annuncio',
  'segnalazione' => 'Nuova segnalazione',
  'candidatura' => 'Nuova candidatura rete VS',
  'contatto' => 'Nuovo contatto dal sito'
];

$subjectBase = $subjects[$type] ?? 'Messaggio dal sito';
$subject = $subjectBase . ' - ' . $practiceId;

$skip = ['website','privacy','form_type'];
$lines = [];
$object = '';
foreach ($_POST as $k=>$v) {
  if (in_array($k,$skip,true) || is_array($v)) continue;
  $val = clean($v);
  if ($val === '') continue;
  $label = strtoupper(str_replace('_',' ',$k));
  $lines[] = $label . ': ' . $val;
  if ($object === '' && in_array($k, ['titolo','link_annuncio','tipologia_attivita'], true)) {
    $object = $val;
  }
}
$lines[] = 'NUMERO PRATICA: ' . $practiceId;
$lines[] = 'STATO: Presa in carico';
$lines[] = 'DATA SERVER: ' . date('d/m/Y H:i:s');
$message = implode("\n\n",$lines);

appendAudit($dataDir, [
  $practiceId,
  date('Y-m-d'),
  date('H:i:s'),
  $type,
  $name,
  $email,
  $phone,
  $territory,
  $object,
  'Presa in carico'
]);

$headers = [
  'From: Vacanze Sicure <postmaster@vacanzesicure.online>',
  'Reply-To: ' . $email,
  'Content-Type: text/plain; charset=UTF-8'
];
@mail($recipient, $subject, $message, implode("\r\n",$headers));

/* Conferma al richiedente */
$userSubject = 'Vacanze Sicure - pratica ' . $practiceId;
if ($type === 'segnalazione') {
  $userMessage =
    "Abbiamo preso in carico tutte le informazioni.\n\n" .
    "Numero pratica: " . $practiceId . "\n\n" .
    "Conservi questo numero e lo indichi ogni volta che ci scrive o ci contatta telefonicamente: ci permetterà di individuare immediatamente lo storico della vicenda.\n\n" .
    "Riceverà una notifica ad ogni evolversi della vicenda.\n\n" .
    "Stato attuale: Presa in carico.\n\nVacanze Sicure";
} else {
  $userMessage =
    "Abbiamo preso in carico la sua richiesta.\n\n" .
    "Numero pratica: " . $practiceId . "\n\n" .
    "Conservi questo numero per le successive comunicazioni con Vacanze Sicure.\n\n" .
    "Stato attuale: Presa in carico.\n\nVacanze Sicure";
}
$userHeaders = [
  'From: Vacanze Sicure <postmaster@vacanzesicure.online>',
  'Reply-To: ' . $recipient,
  'Content-Type: text/plain; charset=UTF-8'
];
@mail($email, $userSubject, $userMessage, implode("\r\n",$userHeaders));

header('Location: grazie.php?pratica=' . urlencode($practiceId) . '&tipo=' . urlencode($type));
exit;
?>