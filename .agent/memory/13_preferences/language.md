# 🌍 Language Setting

This file controls the language for ALL AI interactions, memory entries, and response formatting.

```
LANGUAGE=en
```

---

## Supported Languages

| Code | Language |
|------|----------|
| `en` | English (default) |
| `ru` | Russian |
| `uk` | Ukrainian |
| `es` | Spanish |
| `de` | German |
| `fr` | French |
| `ja` | Japanese |
| `pt` | Portuguese |
| `it` | Italian |
| `ko` | Korean |
| `zh-CN` | Chinese (Simplified) |

---

## 🔀 Local Override

If file `language_local.md` exists in this same folder, it takes **priority** over this file.

This is useful for developers who want to:
- Keep `language.md` = `en` for the public GitHub repo
- Use `language_local.md` = `ru` (or other) for local work

`language_local.md` is excluded from git via `.gitignore`.

**AI: Always check `language_local.md` first. If it exists, use it. If not, use this file.**

---
