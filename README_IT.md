# 🧠 Sistema di Memoria IA (RLM-Anchor)

> **Memoria a lungo termine ispirata a RLM per assistenti IA**

Un sistema di memoria persistente per ambienti di sviluppo basati su IA, fondato sui principi dei [Recursive Language Models](https://arxiv.org/abs/2512.24601) (vedi [Guia Video](https://www.youtube.com/watch?v=huszaaJPjU8)).

---

## 🌟 Funzionalità

- **📁 13 Categorie Organizzate** — archiviazione strutturata di tutta la conoscenza del progetto
- **🔍 Ricerca stile RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Supporto Multilingua** — rispondi e registra in qualsiasi lingua
- **⚡ Comandi Semplici** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Persistenza della Sessione** — contesto preservato tra le sessioni
- **📝 Basato su Markdown** — leggibile dall'uomo e compatibile con Git

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANTE**: Ogni progetto ha bisogno della sua PROPRIA installazione RLM-Anchor! Usare la stessa memoria per più progetti causerà confusione dell'IA a causa di contesti in conflitto. Installa sempre di nuovo per ogni nuovo progetto.

1. **Importa la cartella `.agent/`** nel tuo progetto via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Imposta la tua lingua** nel file `.agent/memory/13_preferences/language.md`.
3. **Esegui questo prompt** (copia l'intero blocco sotto):
   ```
   /anchor_agent scansiona le directory del progetto corrente alla ricerca di dati che aiutino a costruire il contesto e configurare correttamente la memoria (dati tecnici, modelli di business, regole di progettazione e tutti gli altri modelli tipici per trovare e preservare il contesto del progetto)
   ```
4. **Inizia a lavorare** con il comando chat `/wakeup`.
5. **Lavora nel tuo IDE** (sviluppa, risolvi task, prendi decisioni, fai tutto come al solito).

*Durante il lavoro, in fasi importanti, puoi usare* `/remember` *per salvare il contesto rilevante.*

6. **Quando hai finito di lavorare**, ad esempio prima di andare a dormire, esegui `/sleep` affinché RLM-Anchor salvi il tuo contesto.

*Ogni volta che torni al lavoro, basta svegliare RLM-Anchor con* `/wakeup` *e, al termine, mandarlo a dormire con* `/sleep` *perché ricordi tutto.*

---

## 🌍 Configurazione Lingua

Modifica `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=it    # Italiano
LANGUAGE=en    # Inglese
...
```

---

## ⚡ Comandi

| Comando | Descrizione |
|---------|-------------|
| `/wakeup` | Inizia sessione, carica contesto |
| `/sleep` | Fine sessione, riasummi lavoro |
| `/remember` | Salva informazioni in memoria |
| `/recall` | Cerca informazioni in memoria |
| `/handoff` | Crea riassunto per cambio modello |
| `/walkthrough` | Genera documentazione funzionalità |
| `/anchor_agent` | Integrazione sicura nel progetto |
| `/memory-stats` | Mostra statistiche memoria |

---

## 🙏 Crediti
Ispirato alla [Ricerca RLM del MIT](https://arxiv.org/abs/2512.24601) sui Modelli di Linguaggio Ricorsivi e a [questa video guida](https://www.youtube.com/watch?v=huszaaJPjU8).
