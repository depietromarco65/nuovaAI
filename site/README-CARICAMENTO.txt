VACANZE SICURE - V12
====================

Questa versione elimina i riferimenti "demo/sito in sviluppo" dalle pagine principali e introduce:

- VìSì globale con icona flottante e pannello laterale richiudibile.
- FAQ pubbliche integrate come fallback sicuro.
- Regola sicurezza 3 livelli per richieste di informazioni riservate.
- Predisposizione backend tramite assets/config.js (senza segreti).
- Lingue iniziali per VìSì: IT / EN / DE.
- File strutture rinominato da strutture_demo.json a strutture.json.
- Nessuna chiave privata, password o service_role nel codice pubblico.

IMPORTANTE
----------
La V12 può funzionare subito come assistente informativo FAQ.
Per una vera AI generativa e per interrogare il Data Core è necessario valorizzare
visiEndpoint/apiBaseUrl in assets/config.js con endpoint SERVER-SIDE sicuri.

Non mettere mai chiavi segrete nel file config.js.
