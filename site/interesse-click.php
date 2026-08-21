<?php
declare(strict_types=1);
function c($v){return mb_substr(trim(preg_replace('/[\r\n]+/',' ',(string)$v)),0,120);}
$t=c($_GET['territorio']??'');$l=c($_GET['localita']??''); if($t===''){http_response_code(204);exit;}
$dir=__DIR__.'/data';if(!is_dir($dir))@mkdir($dir,0750,true);$file=$dir.'/interessi_territori.csv';$new=!file_exists($file);$fp=@fopen($file,'a');
if($fp){if(flock($fp,LOCK_EX)){if($new)fputcsv($fp,['Data','Ora','Territorio','Localita','Tipo','Nome','Email']);fputcsv($fp,[date('Y-m-d'),date('H:i:s'),$t,$l,'CLICK','','']);flock($fp,LOCK_UN);}fclose($fp);}http_response_code(204);
?>