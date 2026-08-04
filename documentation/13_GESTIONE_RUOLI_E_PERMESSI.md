# 13_GESTIONE_RUOLI_E_PERMESSI.md

# GESTIONE RUOLI E PERMESSI

## Missione

Vacanze Sicure adotta un modello di gestione degli accessi basato su ruoli, deleghe e autorizzazioni.

L'identità digitale identifica la persona.

I ruoli definiscono le funzioni che può svolgere.

I permessi determinano le operazioni che può eseguire.

Le autorizzazioni sono sempre tracciabili, modificabili e revocabili.

---

# Principi

Il sistema si basa sui seguenti principi.

- minima autorizzazione necessaria;
- separazione dei ruoli;
- tracciabilità delle operazioni;
- delegabilità controllata;
- revocabilità immediata;
- audit permanente.

---

# Architettura

Persona

↓

Identità Digitale

↓

Ruoli

↓

Permessi

↓

Autorizzazioni

↓

Operazioni

---

# Ruoli

Una persona può possedere contemporaneamente uno o più ruoli.

I ruoli possono essere:

- permanenti;
- temporanei;
- delegati;
- istituzionali.

---

# Ruoli disponibili

## Ospite

Può:

- effettuare ricerche;
- richiedere preventivi;
- effettuare prenotazioni;
- gestire il proprio Fascicolo;
- consultare documenti;
- inviare recensioni;
- aprire richieste di assistenza.

---

## Proprietario

Può:

- gestire le proprie strutture;
- pubblicare annunci;
- gestire disponibilità;
- definire prezzi;
- rispondere ai preventivi;
- consultare report;
- utilizzare gli strumenti AI.

---

## Gestore

Può operare su strutture affidate mediante delega.

---

## Property Manager

Può gestire contemporaneamente più strutture appartenenti a soggetti differenti.

---

## Agenzia

Può operare per conto dei proprietari autorizzati.

---

## Collaboratore

Può ricevere autorizzazioni limitate.

Ad esempio:

- check-in;
- pulizie;
- manutenzione;
- fotografie;
- inventario.

---

## Validatore

Può:

- effettuare verifiche;
- compilare verbali;
- allegare documentazione;
- proporre certificazioni.

Non può modificare dati commerciali.

---

## Revisore

Può riesaminare pratiche oggetto di contestazione.

---

## Operatore Vacanze Sicure

Può gestire:

- assistenza;
- ticket;
- segnalazioni;
- procedure amministrative.

---

## Ente

Ruolo destinato a:

- Comuni;
- Province;
- Regioni;
- Camere di Commercio;
- Associazioni di categoria;
- Enti religiosi;
- Organizzazioni del Terzo Settore.

---

## Amministratore

Gestisce esclusivamente le funzioni tecniche della piattaforma.

Le operazioni amministrative sono integralmente registrate.

---

# Permessi

I permessi definiscono ciò che ogni ruolo può eseguire.

Ad esempio.

## Consultazione

- leggere dati;
- consultare documenti;
- visualizzare report.

---

## Inserimento

- creare strutture;
- inserire prenotazioni;
- caricare documenti.

---

## Modifica

- aggiornare dati;
- modificare disponibilità;
- correggere informazioni.

---

## Eliminazione

Consente la cancellazione secondo le regole previste.

Ogni eliminazione viene registrata.

---

## Validazione

Permette di:

- approvare;
- respingere;
- certificare;
- sospendere.

---

## Firma

Consente la sottoscrizione digitale di documenti.

---

## Delega

Permette di attribuire autorizzazioni ad altri utenti.

---

# Livelli di autorizzazione

## Nessun accesso

L'utente non può visualizzare il contenuto.

---

## Lettura

Può consultare.

---

## Lettura e modifica

Può aggiornare.

---

## Gestione

Può creare, modificare e chiudere.

---

## Supervisione

Può controllare le attività di altri utenti.

---

## Amministrazione

Massimo livello disponibile.

---

# Deleghe

Ogni delega deve specificare:

- delegante;
- delegato;
- ruolo;
- ambito;
- durata;
- permessi;
- eventuali limitazioni.

---

# Delega temporanea

Può essere limitata:

- nel tempo;
- alle strutture;
- ai documenti;
- alle prenotazioni;
- ai servizi.

---

# Revoca

Ogni delega può essere revocata.

La revoca produce effetto immediato.

Lo storico rimane conservato.

---

# Audit

Ogni operazione viene registrata.

Per ogni attività vengono memorizzati:

- utente;
- ruolo utilizzato;
- data;
- ora;
- operazione;
- oggetto;
- esito.

---

# Cambio ruolo

Una persona può cambiare ruolo in qualsiasi momento.

Ad esempio.

Ospite

↓

Proprietario

↓

Property Manager

↓

Validatore

La sua Identità Digitale rimane invariata.

---

# Multi-ruolo

Una persona può utilizzare più ruoli contemporaneamente.

Ad esempio.

Marco

✓ Proprietario

✓ Ospite

✓ Property Manager

✓ Fotografo certificato

Il sistema consente di scegliere il ruolo operativo quando necessario.

---

# Multi-organizzazione

Una persona può appartenere contemporaneamente a:

- una società;
- un'associazione;
- una cooperativa;
- un Comune;
- una DMO.

Ogni organizzazione mantiene autorizzazioni indipendenti.

---

# Matrice dei permessi

Ogni ruolo è associato ad una matrice ufficiale dei permessi.

La matrice viene mantenuta separatamente e aggiornata senza modificare il presente documento.

---

# Principio Vacanze Sicure

Le autorizzazioni appartengono ai ruoli.

La reputazione appartiene alla Persona.

Le strutture appartengono ai rispettivi proprietari o alle organizzazioni.

Le deleghe attribuiscono esclusivamente il diritto di operare e non trasferiscono la titolarità dei beni o delle informazioni.

---

# Documenti correlati

- 12_IDENTITA_DIGITALE.md
- 22_VALIDAZIONE_STRUTTURE.md
- 23_CERTIFICAZIONE.md
- 24_KNOWLEDGE_ENGINE.md
- 25_ASSISTENTE_AI.md
- 32_AREA_PROPRIETARI.md
- 33_AREA_OSPITI.md
- 36_TUTELA_TURISTA.md
- 39_MODALITA_DI_ADESIONE.md
- DATABASE_MASTER.md

---

# Conclusione

La gestione dei ruoli e dei permessi rappresenta uno degli elementi fondamentali dell'architettura di Vacanze Sicure.

Separando l'identità della persona dalle autorizzazioni operative, la piattaforma garantisce maggiore sicurezza, flessibilità e tracciabilità, consentendo a ogni utente di assumere ruoli differenti nel corso del tempo senza perdere la propria storia, reputazione e identità digitale.

---

# Esperienza Mobile

## Principio

Vacanze Sicure deve essere progettata secondo un approccio **Mobile First**.

L'applicazione mobile non rappresenta una semplice estensione del portale web, ma uno strumento operativo pensato per accompagnare il proprietario durante l'intera giornata lavorativa.

L'obiettivo è consentire la gestione della struttura ovunque ci si trovi, riducendo al minimo il tempo necessario per svolgere le attività quotidiane.

---

# Dashboard Operativa

All'apertura dell'app il proprietario non visualizza il calendario, ma una Dashboard Operativa che riassume le attività più importanti della giornata.

Ad esempio:

- check-in previsti;
- check-out programmati;
- nuove richieste;
- preventivi da confermare;
- pagamenti ricevuti;
- comunicazioni in attesa;
- scadenze amministrative;
- manutenzioni programmate;
- notifiche dell'Assistente AI.

La dashboard rappresenta il punto di partenza dell'attività quotidiana.

---

# Assistente Operativo

L'Assistente AI supporta il proprietario suggerendo le azioni più opportune.

Ad esempio:

- inviare il messaggio di benvenuto;
- richiedere i documenti mancanti;
- ricordare una scadenza amministrativa;
- preparare la comunicazione per il check-in;
- segnalare un ospite abituale;
- suggerire un'offerta personalizzata.

L'Assistente AI propone.

La decisione finale rimane sempre dell'operatore.

---

# Gestione Rapida

Le operazioni più frequenti devono essere eseguibili con pochi tocchi.

Ad esempio:

- confermare una prenotazione;
- inviare una comunicazione;
- registrare un pagamento;
- aggiornare la disponibilità;
- consultare il Fascicolo della Prenotazione;
- contattare l'ospite;
- aprire il navigatore;
- registrare una manutenzione.

---

# Unica Applicazione

Vacanze Sicure prevede un'unica applicazione.

Le funzionalità disponibili cambiano automaticamente in base al ruolo dell'utente autenticato.

Ad esempio:

- Ospite;
- Proprietario;
- Collaboratore;
- Property Manager;
- Manutentore;
- Istituzione;
- Amministratore.

Ogni utente visualizza esclusivamente gli strumenti necessari allo svolgimento delle proprie attività.

---

# Principio Vacanze Sicure

L'applicazione mobile non deve limitarsi a replicare il portale web.

Deve diventare il principale strumento di lavoro quotidiano del proprietario, anticipando le esigenze dell'operatore e semplificando ogni attività attraverso informazioni contestuali, assistenza intelligente e accesso immediato alle funzionalità essenziali.
