# 🛠️ Предпочитаемые инструменты

- **Дата**: 2026-02-09
- **Теги**: инструменты, терминал, Windows

---

## Правила терминала

### ❌ НЕ использовать Unix-специфичные команды на Windows

Unix-утилиты (`du`, `wc`, `find`, `grep`, `sed`, `awk` и т.д.) на Windows работают **непредсказуемо**:
- Могут зависать на путях с пробелами
- `du -sk` может не завершаться
- `/dev/null` не работает в cmd/PowerShell
- Эмуляция через Git Bash ненадёжна

### ✅ Альтернативы для Windows

| Unix | Windows (PowerShell) |
|------|---------------------|
| `du -sk folder/` | `powershell -Command "(Get-ChildItem -Recurse 'folder' | Measure-Object -Property Length -Sum).Sum / 1KB"` |
| `find . -name "*.md" | wc -l` | `powershell -Command "(Get-ChildItem -Recurse -Filter '*.md').Count"` |
| `grep -r "text" folder/` | Использовать встроенный `grep_search` tool |
| `cat file.txt` | Использовать встроенный `view_file` tool |

### 💡 Принцип

Предпочитать встроенные инструменты агента (`view_file`, `grep_search`, `find_by_name`, `list_dir`) вместо shell-команд, когда это возможно.
