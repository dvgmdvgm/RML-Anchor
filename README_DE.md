# 🧠 KI-Gedächtnissystem (RLM-Anchor)

> **RLM-inspiriertes Langzeitgedächtnis für KI-Assistenten**

Ein persistentes Gedächtnissystem für KI-gestützte Entwicklungsumgebungen, basierend auf den Prinzipien der [Recursive Language Models](https://arxiv.org/abs/2512.24601) (siehe [Video-Guide](https://www.youtube.com/watch?v=huszaaJPjU8)).

---

## 🌟 Funktionen

- **📁 13 organisierte Kategorien** — strukturierte Speicherung des gesamten Projektwissens
- **🔍 RLM-Suche** — Examine → Decompose → Recurse → Aggregate
- **🌍 Mehrsprachige Unterstützung** — Antworten und Aufzeichnungen in jeder Sprache
- **⚡ Einfache Befehle** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Sitzungspersistenz** — Kontext bleibt zwischen Sitzungen erhalten
- **📝 Markdown-basiert** — menschenlesbar, Git-freundlich

---

## 📦 Quick Start & Usage

1. **Importieren Sie den `.agent/`-Ordner** mit Git in Ihr Projekt:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Stellen Sie Ihre Sprache** in der Datei `.agent/memory/13_preferences/language.md` ein.
3. **Führe genau diesen Prompt aus:** ```/anchor_agent scanne die aktuellen Projektverzeichnisse nach Daten, die helfen, den Kontext aufzubauen und den Speicher korrekt zu konfigurieren (technische Daten, Geschäftsmodelle, Designregeln und alle anderen typischen Vorlagen zum Finden und Erhalten des Projektkontexts)``` um RLM-Anchor sicher in Ihr aktuelles Projekt zu implementieren.
4. **Beginnen Sie mit der Arbeit** über den Chat-Befehl ```/wakeup```.
5. **Arbeiten Sie in Ihrer IDE** (entwickeln, Aufgaben lösen, Geschäftsentscheidungen treffen, alles wie gewohnt).

*Während der Arbeit können Sie in wichtigen Phasen* ```/remember``` *verwenden, um wichtigen Kontext zu speichern.*

6. **Wenn Sie die Arbeit beendet haben**, z. B. bevor Sie schlafen gehen, führen Sie den Befehl ```/sleep``` aus, damit RLM-Anchor Ihren Kontext im Gedächtnis speichern kann.

*Jedes Mal, wenn Sie zur Arbeit an Ihrem Projekt zurückkehren, wecken Sie RLM-Anchor einfach mit* ```/wakeup``` *auf und schicken ihn am Ende der Sitzung mit* ```/sleep``` *wieder schlafen, damit er sich an alles erinnert, was Sie getan haben.*

---

## 🌍 Sprachkonfiguration

Bearbeiten Sie `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=de    # Deutsch
LANGUAGE=en    # Englisch
...
```

---

## ⚡ Befehle

| Befehl | Beschreibung |
|---------|-------------|
| `/wakeup` | Sitzung starten, Kontext laden |
| `/sleep` | Sitzung beenden, Arbeit zusammenfassen |
| `/remember` | Informationen im Gedächtnis speichern |
| `/recall` | Informationen im Gedächtnis suchen |
| `/handoff` | Kontext-Zusammenfassung für Modellwechsel erstellen |
| `/walkthrough` | Feature-Dokumentation generieren |
| `/anchor_agent` | Sicher in das Projekt integrieren |
| `/memory-stats` | Gedächtnisstatistiken anzeigen |

---

## 🙏 Credits
Inspiriert durch die [MIT RLM-Forschung](https://arxiv.org/abs/2512.24601) zu Recursive Language Models und [diesen Video-Guide](https://www.youtube.com/watch?v=huszaaJPjU8).
