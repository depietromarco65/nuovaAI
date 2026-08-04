Data

04 Agosto 2026

---

Analisi

Dashboard Traum Ferienwohnungen

---

Osservazione

L'area riservata dedica gran parte dello spazio a banner commerciali.

---

Decisione

Vacanze Sicure utilizzerà la dashboard esclusivamente come area operativa.

---

Documenti interessati

32_AREA_PROPRIETARI.md

101_ANALISI_E_BENCHMARK.md

100.11_CUSTOMER_EXPERIENCE.md

---

Stato

Approvata

Data

04 Agosto 2026

---

Analisi

Landing Booking.com per Host

---

Osservazione

La comunicazione è orientata principalmente a:

- prenotazioni;
- visibilità;
- pagamenti.

---

Decisione

Vacanze Sicure comunicherà principalmente:

- fiducia;
- serenità;
- qualità del lavoro;
- collaborazione.

---

Documenti

32_AREA_PROPRIETARI.md

34_MARKETING_INTELLIGENTE.md

100.11_CUSTOMER_EXPERIENCE.md

---

Stato

Approvata

# Decisione Progettuale n. 004

## Data

04 Agosto 2026

---

# Titolo

L'integrazione tramite iCal rappresenta un livello di compatibilità, non il modello dati di riferimento.

---

# Origine

Analisi comparativa delle piattaforme:

- Holidu
- Octorate

Durante l'analisi è emerso che alcune piattaforme mostrano informazioni limitate perché sincronizzano i calendari principalmente tramite protocollo iCal.

---

# Osservazione

Il protocollo iCal è estremamente utile per sincronizzare la disponibilità tra piattaforme differenti, ma trasporta un insieme molto limitato di informazioni.

Generalmente consente di sincronizzare:

- disponibilità;
- periodi occupati;
- date di check-in e check-out.

Non consente invece di condividere informazioni fondamentali quali:

- dati completi dell'ospite;
- pagamenti;
- comunicazioni;
- documentazione;
- certificazioni;
- richieste particolari;
- stato della prenotazione;
- Fascicolo della Prenotazione;
- workflow operativi.

Per questo motivo le piattaforme basate esclusivamente su iCal non possono offrire una gestione completa del rapporto tra ospite e struttura.

---

# Decisione progettuale

Vacanze Sicure utilizza iCal esclusivamente come strumento di interoperabilità con sistemi esterni.

Il protocollo iCal rappresenta un livello minimo di integrazione e non costituisce il modello dati principale della piattaforma.

Il patrimonio informativo di Vacanze Sicure risiede nel Database Centrale e nel Fascicolo della Prenotazione.

---

# Gerarchia delle fonti informative

1. Fascicolo della Prenotazione
2. Database Centrale Vacanze Sicure
3. PMS integrati tramite API
4. OTA integrate tramite API
5. Sincronizzazione iCal

Le informazioni provenienti da livelli superiori prevalgono sempre su quelle ottenute tramite sincronizzazione iCal.

---

# Motivazione

L'obiettivo della piattaforma non è soltanto sincronizzare calendari.

L'obiettivo è costruire un ecosistema capace di gestire l'intero ciclo di vita della prenotazione:

- ricerca;
- richiesta;
- preventivo;
- conferma;
- comunicazioni;
- pagamenti;
- documentazione;
- certificazione;
- assistenza;
- eventuale ricollocazione;
- archiviazione nel Fascicolo della Prenotazione.

Tali informazioni non possono essere rappresentate dal solo protocollo iCal.

---

# Principio progettuale

L'interoperabilità non deve limitare le funzionalità della piattaforma.

Vacanze Sicure garantisce la compatibilità con gli strumenti già utilizzati dagli operatori, mantenendo però un proprio modello dati completo e indipendente.

---

# Impatto sul progetto

Questa decisione influenza direttamente:

- 38_SISTEMA_UNICO_PRENOTAZIONI.md
- DATABASE_MASTER.md
- 24_KNOWLEDGE_ENGINE.md
- 25_ASSISTENTE_AI.md
- 27_NOTIFICHE_INTELLIGENTI.md
- 32_AREA_PROPRIETARI.md
- 33_AREA_OSPITI.md
- 60_GESTIONE_PAGAMENTI.md
- 100.09_FASCICOLO_PRENOTAZIONE.md
- 101_ANALISI_E_BENCHMARK.md

---

# Stato

✅ Approvata

---

# Nota

La compatibilità rappresenta un punto di partenza.

Il valore di Vacanze Sicure nasce dalla ricchezza delle informazioni che accompagnano ogni prenotazione e dalla capacità della piattaforma di trasformarle in servizi, tutela, automazioni intelligenti e strumenti di fiducia per ospiti e operatori.
