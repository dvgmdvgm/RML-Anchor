# ⚙️ Memory Settings / Настройки Памяти

> **Configures behavior of the memory system.**
> **Настраивает поведение системы памяти.**

---

## 💾 Auto-Save Behavior / Авто-сохранение

Controls whether AI saves important information automatically or asks first.

```
AUTO_SAVE=ask
```

**Options / Опции:**
- `ask` (Recommended/Рекомендуется) — AI will ask: "Do you want to save this?" (High data quality)
- `auto` — AI will save without asking (May collect noise)

---

## 🔔 Notifications / Уведомления

Controls if AI notifies you when data is saved.

```
NOTIFY_ON_SAVE=true
```

**Options:**
- `true` — Always confirm: "✅ Saved to..."
- `false` — Save silently (only logic)

---

## ⚠️ Stability Note

For RLM (Recursive Language Models), **Quality > Quantity**.
Using `AUTO_SAVE=ask` ensures that only truly important information enters the long-term memory, keeping searches fast and accurate.

Для RLM **Качество > Количество**.
Использование `AUTO_SAVE=ask` гарантирует, что в память попадает только действительно важная информация, сохраняя поиск точным и быстрым.
