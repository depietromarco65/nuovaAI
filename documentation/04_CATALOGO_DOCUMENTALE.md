# 04_CATALOGO_DOCUMENTALE.md

# CATALOGO DOCUMENTALE

## Missione

Il Catalogo Documentale definisce l'organizzazione ufficiale della documentazione di Vacanze Sicure.

Ogni informazione deve essere archiviata una sola volta, nel documento che ne rappresenta la fonte ufficiale.

L'obiettivo è evitare duplicazioni, garantire coerenza e rendere la documentazione facilmente consultabile e mantenibile nel tempo.

---

# Principi

La documentazione rappresenta il patrimonio di conoscenza del progetto.

Ogni documento ha uno scopo preciso.

Ogni informazione appartiene ad un solo documento.

Gli altri documenti possono richiamarla, ma non duplicarla.

---

# Principio della Fonte Ufficiale

Ogni argomento deve avere un solo documento di riferimento.

Tale documento costituisce la fonte ufficiale.

Eventuali riferimenti presenti in altri documenti devono limitarsi a richiamare la fonte senza ripetere integralmente il contenuto.

---

# Principio della Non Duplicazione

La stessa informazione non deve essere mantenuta in più documenti.

Le duplicazioni generano:

- incoerenze;
- errori;
- difficoltà di aggiornamento;
- aumento della manutenzione.

Quando un'informazione cambia, deve essere aggiornata esclusivamente nella propria fonte ufficiale.

---

# Classificazione della Documentazione

La documentazione viene organizzata per dominio funzionale.

Ogni documento appartiene ad un preciso ambito del progetto.

---

## Filosofia

Descrive:

- valori;
- missione;
- principi;
- identità del progetto.

Esempi:

- 00_FILOSOFIA_DEL_PROGETTO.md
- 99_MANIFESTO.md

---

## Governance

Descrive:

- organizzazione;
- processi;
- responsabilità;
- metodo di lavoro.

Esempi:

- 02_GOVERNANCE_DEL_PROGETTO.md
- 02_PROCESSI_DEL_PROGETTO.md
- 03_CARTA_DEI_DIRITTI_E_DOVERI.md

---

## Architettura

Definisce la struttura tecnica e logica del sistema.

Esempi:

- 01_ARCHITETTURA_DEL_PROGETTO.md
- DATABASE_MASTER.md

---

## Identità

Gestisce:

- persone;
- organizzazioni;
- ruoli;
- permessi;
- workflow autorizzativi.

Esempi:

- 12_IDENTITA_DIGITALE.md
- 13_GESTIONE_RUOLI_E_PERMESSI.md
- 14_WORKFLOW_AUTORIZZATIVI.md

---

## AI

Descrive i componenti intelligenti della piattaforma.

Esempi:

- 24_KNOWLEDGE_ENGINE.md
- 25_ASSISTENTE_AI.md
- 26_KNOWLEDGE_BASE.md
- 27_NOTIFICHE_INTELLIGENTI.md
- 28_CONTENT_ENGINE.md
- 29_SEARCH_ENGINE.md
- 31_RECOMMENDATION_ENGINE.md

---

## Proprietari

Raccoglie tutte le funzionalità dedicate agli operatori dell'ospitalità.

Esempi:

- 32_AREA_PROPRIETARI.md
- 39_MODALITA_DI_ADESIONE.md
- 40_MODELLO_ECONOMICO.md

---

## Ospiti

Descrive l'esperienza del turista.

Esempi:

- 33_AREA_OSPITI.md
- 36_TUTELA_TURISTA.md
- 37_TURISMO_SOLIDALE.md

---

## Prenotazioni

Definisce il ciclo di vita della prenotazione.

Esempi:

- 38_SISTEMA_UNICO_PRENOTAZIONI.md
- 60_GESTIONE_PAGAMENTI.md
- 100.09_FASCICOLO_PRENOTAZIONE.md

---

## Integrazioni

Descrive le comunicazioni con sistemi esterni.

Esempi:

- 62_INTEGRAZIONI_E_INTEROPERABILITA.md

Comprende:

- OTA;
- PMS;
- Channel Manager;
- API;
- Webhook;
- iCal;
- sistemi istituzionali;
- servizi regionali;
- interoperabilità.

---

## Certificazione

Comprende:

- validazione;
- certificazione;
- controlli;
- verifiche.

Esempi:

- 22_VALIDAZIONE_STRUTTURE.md
- 23_CERTIFICAZIONE.md

---

## Marketing

Comprende:

- home page;
- contenuti;
- ranking;
- customer experience;
- comunicazione.

Esempi:

- 30.01_HOME_PAGE.md
- 34_MARKETING_INTELLIGENTE.md
- 35_VISIBILITA_E_RANKING.md
- 100.01_HOME_E_MARKETING.md
- 100.11_CUSTOMER_EXPERIENCE.md

---

## Analisi

Documenta gli studi effettuati.

Esempi:

- 09_ANALISI_COMPARATIVA_PIATTAFORME.md
- 09_BENCHMARK_PIATTAFORME.md
- 101_ANALISI_E_BENCHMARK.md

---

## Memoria del progetto

Conserva:

- idee;
- decisioni;
- motivazioni;
- storia del progetto.

Esempi:

- 05_STORIA_DEL_PROGETTO.md
- 100_REGISTRO_IDEE.md
- 102_MEMORIA_EVOLUTIVA.md

---

# Regola di Classificazione

Ogni nuova informazione deve essere classificata prima di essere documentata.

La classificazione segue sempre queste domande.

## 1. Perché?

Il contenuto riguarda:

- filosofia;
- principi;
- missione.

↓

00_FILOSOFIA_DEL_PROGETTO.md

---

## 2. Come funziona?

Descrive un processo o una funzionalità.

↓

Documento funzionale specifico.

---

## 3. Chi la utilizza?

Descrive l'esperienza dell'utente.

↓

Area Proprietari

oppure

Area Ospiti

---

## 4. Come interviene l'AI?

↓

25_ASSISTENTE_AI.md

---

## 5. Quali notifiche produce?

↓

27_NOTIFICHE_INTELLIGENTI.md

---

## 6. Quali dati gestisce?

↓

DATABASE_MASTER.md

---

## 7. Come dialoga con sistemi esterni?

↓

62_INTEGRAZIONI_E_INTEROPERABILITA.md

---

## 8. Come viene sviluppata?

↓

Documento tecnico competente.

---

# Regola della Fonte Unica

Ogni informazione viene descritta completamente una sola volta.

Gli altri documenti:

- richiamano;
- collegano;
- contestualizzano.

Non duplicano.

---

# Collegamenti

Ogni documento deve riportare i documenti correlati.

I collegamenti consentono di navigare facilmente tra le diverse aree del progetto.

---

# Evoluzione della Documentazione

Ogni nuovo documento deve rispondere ad almeno uno dei seguenti requisiti:

- introduce un nuovo dominio funzionale;
- documenta un nuovo processo;
- definisce un nuovo principio;
- descrive una nuova architettura.

Se il contenuto appartiene ad un dominio già esistente, deve essere integrato nel documento competente.

---

# Metodo Vacanze Sicure

Prima di creare un nuovo documento occorre verificare che l'argomento non sia già trattato.

La sequenza è sempre la seguente:

1. Analizzare l'idea.
2. Individuare il dominio funzionale.
3. Cercare il documento competente.
4. Integrare il documento esistente.
5. Creare un nuovo documento solo se il dominio non esiste.

---

# Principio Vacanze Sicure

La documentazione cresce per approfondimento, non per frammentazione.

Ogni nuovo contenuto deve aumentare la conoscenza del progetto senza aumentare inutilmente il numero dei documenti.

La semplicità dell'organizzazione documentale costituisce un valore fondamentale del progetto.

---

# Conclusione

Il Catalogo Documentale rappresenta il sistema di governo della conoscenza di Vacanze Sicure.

Ogni documento contribuisce a costruire un patrimonio condiviso, coerente e facilmente evolvibile.

L'obiettivo non è produrre molti documenti, ma creare una documentazione unica, ordinata, affidabile e capace di accompagnare lo sviluppo della piattaforma nel tempo.
