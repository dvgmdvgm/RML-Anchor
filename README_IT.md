# 🧠 Sistema di Memoria IA (RLM-Anchor)

> **Memoria a lungo termine per assistenti IA basata su RLM**

Un sistema di memoria persistente per ambienti di sviluppo IA, basato sui principi dei [Recursive Language Models](https://arxiv.org/abs/2512.24601) (ricerca MIT) (vedi [Guida video](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Dai al tuo assistente IA una **memoria persistente** che sopravvive tra le sessioni di chat.

---

## 💡 Il Problema

Ogni volta che inizi una nuova chat con l'IA, dimentica tutto:
- L'architettura del progetto
- Le decisioni passate e i loro motivi
- Bug conosciuti e soluzioni alternative
- Il tuo stile di programmazione
- Su cosa hai lavorato ieri

**RLM-Anchor risolve questo problema.** Dà all'IA una memoria strutturata a lungo termine — come semplici file Markdown direttamente nel tuo progetto.

---

---

## 🌟 Caratteristiche

- **📁 13 categorie organizzate** — archiviazione strutturata della conoscenza del progetto
- **🔍 Ricerca stile RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multilingue** — risposte e voci in qualsiasi lingua
- **⚡ Comandi semplici** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Passaggio di contesto** — cambio fluido tra modelli IA
- **📝 Basato su Markdown** — leggibile dagli umani, compatibile con Git
- **🔄 Persistenza delle sessioni** — il contesto viene preservato tra le sessioni

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANTE**: Ogni progetto richiede un'installazione SEPARATA di RLM-Anchor! Usare una memoria per più progetti confonderà l'IA a causa di contesti conflittuali. Installa sempre di nuovo per ogni nuovo progetto.

1. **Importa la cartella `.agent/`** nel tuo progetto via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Imposta la lingua** in `.agent/memory/13_preferences/language.md`
3. **Esegui questo prompt** (copia l'intero blocco):
   ```
   /anchor_agent controlla le directory del progetto corrente per trovare dati che aiuteranno a costruire il contesto e configurare la memoria correttamente (dati tecnici, modelli di business, regole di design e tutti gli altri modelli tipici per trovare e preservare il contesto del progetto)
   ```
4. **Inizia a lavorare** con il comando chat `/wakeup`.
5. **Lavora nel tuo IDE** (sviluppo, risoluzione problemi, decisioni aziendali, tutto come al solito).

*Durante il lavoro, nelle fasi importanti puoi usare* `/remember` *per salvare contesto importante.*

6. **Quando finisci di lavorare** nell'IDE, ad esempio prima di dormire, esegui `/sleep` affinché RLM-Anchor salvi il contesto in memoria.

*Ora ogni volta che torni a lavorare sul progetto — sveglia semplicemente RLM-Anchor con* `/wakeup` *e alla fine della sessione mandalo di nuovo a dormire* `/sleep` *così ricorda tutto quello che hai fatto.*

---

## 🌍 Impostazioni Lingua

Modifica `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=it    # Italiano
LANGUAGE=en    # Inglese
LANGUAGE=ru    # Russo  
...
```

---

## ⚡ Comandi

| Comando | Descrizione |
|---------|-------------|
| `/wakeup` | Inizia sessione, carica contesto |
| `/sleep` | Termina sessione, archivia nella cronologia |
| `/remember` | Salva informazione in memoria |
| `/recall` | Trova informazione in memoria |
| `/handoff` | Crea sommario per cambio modello |
| `/walkthrough` | Genera documentazione feature |
| `/anchor_agent` | Integrazione sicura nel progetto |
| `/anchor_briefing` | Briefing completo del progetto (tutte le 13 categorie) |
| `/anchor_backup` | Crea backup manuale (per trasferimento) |
| `/anchor_restore` | Ripristina da backup ZIP |
| `/anchor_remove` | Rimozione sicura del sistema (con backup) |
| `/anchor_cleanup` | Pulizia intelligente memoria (TTL, scoring) |
| `/anchor_update` | Aggiorna all'ultima versione da GitHub |
| `/anchor_validate` | Verifica integrità memoria (5 controlli) |
| `/memory-stats` | Mostra statistiche memoria con trend |

📖 **Documentazione completa comandi**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Struttura

```
.agent/
├── MEMORY_INDEX.md           # Indice principale memoria
├── skills/
│   └── MEMORY_SKILL.md       # Istruzioni per IA
├── workflows/                 # Definizioni comandi
├── scripts/                   # Utility Python
└── memory/
    ├── 01_project/           # Informazioni progetto
    ├── 02_architecture/      # Architettura sistema
    ├── 03_decisions/         # Decisioni architetturali (ADR)
    ├── 04_domain/            # Dominio business
    ├── 05_code/              # Documentazione codice
    ├── 06_problems/          # Problemi e soluzioni
    ├── 07_context/           # Contesto sessioni
    ├── 08_people/            # Persone e ruoli
    ├── 09_external/          # Dipendenze esterne
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Deployment
    ├── 12_roadmap/           # Piani e futuro
    └── 13_preferences/       # Preferenze e LINGUA
```

---

## 🔄 Come Funziona

### Processo Stile RLM

```
Richiesta utente
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Leggi indice memoria   │
│ 2. DECOMPOSE — Determina categorie  │
│ 3. RECURSE — Cerca nei file         │
│ 4. AGGREGATE — Combina dati         │
└─────────────────────────────────────┘
    ↓
Risposta contestuale (nella lingua configurata)
```

---

## 📝 Esempi d'Uso

### 🚀 Inizializzazione / Connessione
```
Utente: /anchor_agent
IA: 📋 ANALISI INTEGRAZIONE... [Scansiona e offre opzioni d'integrazione sicura]
```

### ☀️ Inizia Sessione
```
Utente: /wakeup
IA: 🚀 Caricamento contesto progetto...
    ✅ Sessione iniziata!
    📌 Attività in sospeso: 2
```

### 📌 Salvare Informazione
```
Utente: /remember Abbiamo scelto PostgreSQL per transazioni ACID
IA: ✅ Salvato in memory/03_decisions/ADR-002-database.md
```

### 🔍 Ricerca Conoscenze
```
Utente: /recall Perché abbiamo scelto PostgreSQL?
IA: 📁 Trovato in memoria:
    Fonte: memory/03_decisions/ADR-002-database.md
    Abbiamo scelto PostgreSQL per il supporto transazioni ACID...
```

### 🔄 Passaggio Contesto (Handoff)
```
Utente: /handoff
IA: 🔄 Creazione sommario passaggio contesto... [Genera sommario per altro modello]
```

### 📖 Generazione Documentazione
```
Utente: /walkthrough Nuova autorizzazione
IA: 📖 Walkthrough creato! Salvato in memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Statistiche Memoria
```
Utente: /memory-stats
IA: 📊 Statistiche: 42 file, 13 categorie...
```

### 🌙 Termina Sessione
```
Utente: /sleep
IA: 📝 Riepilogo sessione...
    ✅ Cronologia salvata.
    👋 A presto!
```

---

## 🛠️ Personalizzazione

### Aggiungere Nuove Categorie
1. Crea cartella in `memory/`
2. Aggiungi `_index.md` 
3. Aggiorna `MEMORY_INDEX.md`

### Estendere Workflows
Modifica file in `workflows/` per personalizzare comandi.

---

## 📄 Licenza
MIT License — forkalo e miglioralo!

---

## 🙏 Ringraziamenti
Ispirato dalla [ricerca RLM del MIT](https://arxiv.org/abs/2512.24601) su Recursive Language Models e [questa guida video](https://www.youtube.com/watch?v=huszaaJPjU8).
