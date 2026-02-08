# 🧠 KI-Gedächtnissystem (RLM-Anchor)

> **Langzeitgedächtnis für KI-Assistenten basierend auf RLM**

Ein persistentes Gedächtnissystem für KI-Entwicklungsumgebungen, basierend auf den Prinzipien von [Recursive Language Models](https://arxiv.org/abs/2512.24601) (MIT-Forschung) (siehe [Video-Anleitung](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Geben Sie Ihrem KI-Assistenten ein **dauerhaftes Gedächtnis**, das zwischen Chat-Sitzungen erhalten bleibt.

---

## 💡 Das Problem

Jedes Mal, wenn Sie einen neuen Chat mit KI starten, vergisst sie alles:
- Projektarchitektur
- Vergangene Entscheidungen und deren Gründe
- Bekannte Bugs und Workarounds
- Ihren Coding-Stil
- Woran Sie gestern gearbeitet haben

**RLM-Anchor löst dieses Problem.** Es gibt der KI ein strukturiertes Langzeitgedächtnis — als einfache Markdown-Dateien direkt in Ihrem Projekt.

---

---

## 🌟 Funktionen

- **📁 13 organisierte Kategorien** — strukturierte Speicherung von Projektwissen
- **🔍 RLM-Stil-Suche** — Examine → Decompose → Recurse → Aggregate
- **🌍 Mehrsprachig** — Antworten und Einträge in jeder Sprache
- **⚡ Einfache Befehle** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Kontextübergabe** — nahtloses Wechseln zwischen KI-Modellen
- **📝 Markdown-basiert** — menschenlesbar, Git-freundlich
- **🔄 Sitzungspersistenz** — Kontext bleibt zwischen Sitzungen erhalten

---

## 📦 Quick Start & Usage

> ⚠️ **WICHTIG**: Jedes Projekt benötigt eine SEPARATE RLM-Anchor-Installation! Die Verwendung eines Gedächtnisses für mehrere Projekte verwirrt die KI durch widersprüchlichen Kontext. Installieren Sie immer neu für jedes neue Projekt.

1. **Importieren Sie den `.agent/`-Ordner** in Ihr Projekt via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Sprache einstellen** in `.agent/memory/13_preferences/language.md`
3. **Führen Sie diesen Prompt aus** (kopieren Sie den gesamten Block):
   ```
   /anchor_agent überprüfe die aktuellen Projektverzeichnisse auf Daten, die helfen, den Kontext richtig aufzubauen und das Gedächtnis zu konfigurieren (technische Daten, Geschäftsmodelle, Designregeln und alle anderen typischen Vorlagen zum Finden und Bewahren des Projektkontexts)
   ```
4. **Arbeit beginnen** mit Chat-Befehl `/wakeup`.
5. **In Ihrer IDE arbeiten** (Entwicklung, Problemlösung, Geschäftsentscheidungen, alles wie gewohnt).

*Während der Arbeit können Sie an wichtigen Stellen* `/remember` *verwenden, um wichtigen Kontext zu speichern.*

6. **Wenn Sie die Arbeit beenden** in der IDE, z.B. vor dem Schlafengehen, führen Sie `/sleep` aus, damit RLM-Anchor den Kontext speichert.

*Jedes Mal, wenn Sie zur Projektarbeit zurückkehren — wecken Sie einfach RLM-Anchor mit* `/wakeup` *und am Ende der Sitzung schicken Sie ihn wieder schlafen* `/sleep`*, damit er sich an alles erinnert.*

---

## 🌍 Spracheinstellungen

Bearbeiten Sie `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=de    # Deutsch
LANGUAGE=en    # Englisch
LANGUAGE=ru    # Russisch  
...
```

---

## ⚡ Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `/wakeup` | Sitzung starten, Kontext laden |
| `/sleep` | Sitzung beenden, in Historie archivieren |
| `/remember` | Information im Gedächtnis speichern |
| `/recall` | Information im Gedächtnis finden |
| `/handoff` | Zusammenfassung für Modellwechsel erstellen |
| `/walkthrough` | Feature-Dokumentation generieren |
| `/anchor_agent` | Sichere Projektintegration |
| `/anchor_briefing` | Vollständiges Projekt-Briefing (alle 13 Kategorien) |
| `/anchor_backup` | Manuelles Backup erstellen (für Transfer) |
| `/anchor_restore` | Aus ZIP-Backup wiederherstellen |
| `/anchor_remove` | Sichere Systementfernung (mit Backup) |
| `/anchor_cleanup` | Intelligente Gedächtnisbereinigung (TTL, Scoring) |
| `/anchor_update` | Auf neueste Version von GitHub aktualisieren |
| `/anchor_validate` | Gedächtnisintegritätsprüfung (5 Prüfungen) |
| `/memory-stats` | Gedächtnisstatistiken mit Trends anzeigen |

📖 **Vollständige Befehlsdokumentation**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Struktur

```
.agent/
├── MEMORY_INDEX.md           # Hauptgedächtnisindex
├── skills/
│   └── MEMORY_SKILL.md       # KI-Anweisungen
├── workflows/                 # Befehlsdefinitionen
├── scripts/                   # Python-Utilities
└── memory/
    ├── 01_project/           # Projektinformationen
    ├── 02_architecture/      # Systemarchitektur
    ├── 03_decisions/         # Architekturentscheidungen (ADR)
    ├── 04_domain/            # Business-Domäne
    ├── 05_code/              # Code-Dokumentation
    ├── 06_problems/          # Probleme und Lösungen
    ├── 07_context/           # Sitzungskontext
    ├── 08_people/            # Personen und Rollen
    ├── 09_external/          # Externe Abhängigkeiten
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Deployment
    ├── 12_roadmap/           # Pläne und Zukunft
    └── 13_preferences/       # Einstellungen und SPRACHE
```

---

## 🔄 Wie es funktioniert

### RLM-Stil-Prozess

```
Benutzeranfrage
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Gedächtnisindex lesen  │
│ 2. DECOMPOSE — Kategorien bestimmen │
│ 3. RECURSE — In Dateien suchen      │
│ 4. AGGREGATE — Daten zusammenführen │
└─────────────────────────────────────┘
    ↓
Kontextuelle Antwort (in konfigurierter Sprache)
```

---

## 📝 Anwendungsbeispiele

### 🚀 Initialisierung / Verbindung
```
Benutzer: /anchor_agent
KI: 📋 INTEGRATIONSANALYSE... [Scannt und bietet sichere Integrationsoptionen]
```

### ☀️ Sitzung starten
```
Benutzer: /wakeup
KI: 🚀 Lade Projektkontext...
    ✅ Sitzung gestartet!
    📌 Offene Aufgaben: 2
```

### 📌 Information speichern
```
Benutzer: /remember Wir haben PostgreSQL für ACID-Transaktionen gewählt
KI: ✅ Gespeichert in memory/03_decisions/ADR-002-database.md
```

### 🔍 Wissen suchen
```
Benutzer: /recall Warum haben wir PostgreSQL gewählt?
KI: 📁 Im Gedächtnis gefunden:
    Quelle: memory/03_decisions/ADR-002-database.md
    Wir haben PostgreSQL für ACID-Transaktionsunterstützung gewählt...
```

### 🔄 Kontextübergabe (Handoff)
```
Benutzer: /handoff
KI: 🔄 Erstelle Kontextübergabe-Zusammenfassung... [Generiert Zusammenfassung für anderes Modell]
```

### 📖 Dokumentation generieren
```
Benutzer: /walkthrough Neue Autorisierung
KI: 📖 Walkthrough erstellt! Gespeichert in memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Gedächtnisstatistik
```
Benutzer: /memory-stats
KI: 📊 Statistik: 42 Dateien, 13 Kategorien...
```

### 🌙 Sitzung beenden
```
Benutzer: /sleep
KI: 📝 Fasse Sitzung zusammen...
    ✅ Historie gespeichert.
    👋 Bis bald!
```

---

## 🛠️ Anpassung

### Neue Kategorien hinzufügen
1. Ordner in `memory/` erstellen
2. `_index.md` hinzufügen 
3. `MEMORY_INDEX.md` aktualisieren

### Workflows erweitern
Dateien in `workflows/` bearbeiten, um Befehle anzupassen.

---

## 📄 Lizenz
MIT License — forken und verbessern!

---

## 🙏 Danksagungen
Inspiriert durch [RLM-Forschung vom MIT](https://arxiv.org/abs/2512.24601) über Recursive Language Models und [dieses Video-Tutorial](https://www.youtube.com/watch?v=huszaaJPjU8).
