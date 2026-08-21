<?php
declare(strict_types=1);
function s($v){return htmlspecialchars((string)$v,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
$area=trim((string)($_GET['territorio']??''));
$data=json_decode((string)@file_get_contents(__DIR__.'/data/territori_geo.json'),true) ?: [];
$info=$data[$area] ?? null;
if(!$info){$info=['center'=>[42.4,12.6],'zoom'=>6,'localita'=>[]];}
$center=$info['center']; $zoom=(int)$info['zoom']; $localita=$info['localita'];
?>
<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title><?php echo s($area); ?> | Vacanze Sicure</title>
<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"><script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script></head><body>
<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><img src="assets/img/logo-vs.svg" alt="">VACANZE <span>SICURE</span></a><nav class="links"><a href="index.html">Home</a><a href="verifica-annuncio.html">Verifica annuncio</a><a href="controlla-cin.html">Controlla CIN</a><a href="segnala.html">Segnala</a><a href="candidatura.html">Lavora con noi</a></nav></div></header>
<section class="pagehead"><div class="wrap"><div class="breadcrumbs"><a href="index.html#territori">Italia</a> › <?php echo s($area); ?></div><span class="badge">APPROFONDIMENTO TERRITORIALE</span><h1><?php echo s($area); ?></h1><p class="lead">Scegli una località. Le tue ricerche ci aiutano a capire dove concentrare le verifiche e l'attivazione dei servizi.</p></div></section>
<section class="section white"><div class="wrap">
<div id="area-map" class="map-frame"></div>
<div class="territory-message" style="margin-top:25px"><h2>Le verifiche delle strutture sono in corso.</h2><p>Le strutture che hanno già completato il percorso Vacanze Sicure sono riconoscibili dallo specifico scudo. Nuove strutture e servizi saranno pubblicati progressivamente dopo i controlli previsti.</p></div>
</div></section>
<script>
const map=L.map('area-map',{scrollWheelZoom:false}).setView([<?php echo (float)$center[0]; ?>,<?php echo (float)$center[1]; ?>],<?php echo $zoom; ?>);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; OpenStreetMap contributors'}).addTo(map);
const locs=<?php echo json_encode($localita,JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES); ?>;
locs.forEach(l=>{
 const isTorrePali=(l[0]||'').toLowerCase()==='torre pali';
 let m;
 if(isTorrePali){
   const g=L.divIcon({className:'',html:'<div class="mapshield gold-mapshield">VS</div>',iconSize:[31,35],iconAnchor:[15,18]});
   m=L.marker([l[1],l[2]],{icon:g}).addTo(map);
 } else {
   m=L.circleMarker([l[1],l[2]],{radius:9,color:'#fff',weight:3,fillColor:'#1c8b8f',fillOpacity:1}).addTo(map);
 }
 m.bindTooltip(isTorrePali ? 'Torre Pali · struttura verificata presente' : l[0],{direction:'top',offset:[0,-8]});
 m.on('click',()=>{try{fetch('interesse-click.php?territorio='+encodeURIComponent('<?php echo addslashes($area); ?>')+'&localita='+encodeURIComponent(l[0]));}catch(e){};location.href='localita.php?territorio='+encodeURIComponent('<?php echo addslashes($area); ?>')+'&localita='+encodeURIComponent(l[0]);});
});
</script></body></html>