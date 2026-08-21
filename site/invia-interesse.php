<?php
declare(strict_types=1);
function c($v){return trim(preg_replace('/[\r\n]+/',' ',(string)$v));}
if($_SERVER['REQUEST_METHOD']!=='POST'){header('Location:index.html');exit;} if(!empty($_POST['website']??'')){header('Location:index.html');exit;}
$email=c($_POST['email']??'');$nome=c($_POST['nome']??'');$territorio=c($_POST['territorio']??'');$localita=c($_POST['localita']??'');
if(!filter_var($email,FILTER_VALIDATE_EMAIL)||$territorio===''){http_response_code(400);exit('Dati non validi.');}
$dir=__DIR__.'/data';if(!is_dir($dir))@mkdir($dir,0750,true);$file=$dir.'/interessi_territori.csv';$new=!file_exists($file);$fp=@fopen($file,'a');
if($fp){if(flock($fp,LOCK_EX)){if($new)fputcsv($fp,['Data','Ora','Territorio','Localita','Tipo','Nome','Email']);fputcsv($fp,[date('Y-m-d'),date('H:i:s'),$territorio,$localita,'EMAIL',$nome,$email]);flock($fp,LOCK_UN);}fclose($fp);}
$luogo=$localita!==''?"$localita ($territorio)":$territorio;
$subject='Interesse territorio/località '.$luogo.' - Vacanze Sicure';$msg="Territorio: $territorio\nLocalità: $localita\nNome: $nome\nEmail: $email";
$h=['From: Vacanze Sicure <postmaster@vacanzesicure.online>','Reply-To: '.$email,'Content-Type: text/plain; charset=UTF-8'];
@mail('info@vacanzesicure.online',$subject,$msg,implode("\r\n",$h));
@mail($email,'Vacanze Sicure - '.$luogo,"Abbiamo registrato il tuo interesse per $luogo.\n\nTi informeremo quando saranno disponibili le prime strutture e i primi servizi verificati.\n\nVacanze Sicure",implode("\r\n",['From: Vacanze Sicure <postmaster@vacanzesicure.online>','Reply-To: info@vacanzesicure.online','Content-Type: text/plain; charset=UTF-8']));
header('Location: grazie-territorio.php?territorio='.urlencode($territorio).'&localita='.urlencode($localita));exit;
?>