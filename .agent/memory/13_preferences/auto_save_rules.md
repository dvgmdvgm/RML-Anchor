# 📦 Auto-Save Rules / Правила автосохранения

> **Version**: 1.0.0  
> **Last Updated**: 2026-02-05

---

## 🎯 Concept / Концепция

This file defines patterns that trigger automatic memory saving without asking the user.
Этот файл определяет шаблоны, которые активируют автоматическое сохранение в память без вопроса пользователю.

---

## 🤖 AUTO_SAVE Patterns

These patterns trigger AUTOMATIC saving (no confirmation needed):

### 1. Architectural Decisions (ADR)
```yaml
CATEGORY: 03_decisions
TRIGGERS:
  - "мы решили"
  - "решили использовать"
  - "выбрали"
  - "будем использовать"
  - "we decided"
  - "chose to use"
  - "will use"
  - "going with"
CONFIDENCE: 0.9
TTL: 365
IMPORTANCE_BASE: 0.9
```

### 2. Bug Fixes & Workarounds
```yaml
CATEGORY: 06_problems
TRIGGERS:
  - "баг"
  - "bug"
  - "исправил"
  - "fixed"
  - "workaround"
  - "хак"
  - "hack"
  - "временное решение"
CONFIDENCE: 0.8
TTL: 90
IMPORTANCE_BASE: 0.7
```

### 3. External Integrations
```yaml
CATEGORY: 09_external
TRIGGERS:
  - "API ключ"
  - "API key"
  - "endpoint"
  - "интеграция с"
  - "integration with"
  - "webhook"
  - "SDK"
CONFIDENCE: 0.7
TTL: 180
IMPORTANCE_BASE: 0.6
```

### 4. Architecture Changes
```yaml
CATEGORY: 02_architecture
TRIGGERS:
  - "архитектура"
  - "architecture"
  - "компонент"
  - "component"
  - "паттерн"
  - "pattern"
  - "data flow"
  - "поток данных"
CONFIDENCE: 0.7
TTL: 365
IMPORTANCE_BASE: 0.8
```

### 5. Tech Stack Changes
```yaml
CATEGORY: 01_project
TRIGGERS:
  - "добавили библиотеку"
  - "added library"
  - "обновили до"
  - "upgraded to"
  - "перешли на"
  - "migrated to"
  - "новая зависимость"
  - "new dependency"
CONFIDENCE: 0.8
TTL: 365
IMPORTANCE_BASE: 0.7
```

---

## ❓ ASK_USER Patterns

These patterns trigger a CONFIRMATION prompt:

### 1. Business Logic
```yaml
CATEGORY: 04_domain
TRIGGERS:
  - "бизнес-правило"
  - "business rule"
  - "логика"
  - "logic"
  - "требование"
  - "requirement"
PROMPT: "💡 Обнаружено бизнес-правило. Сохранить в память? [y/N]"
```

### 2. Code Snippets
```yaml
CATEGORY: 05_code
TRIGGERS:
  - "код для"
  - "code for"
  - "пример кода"
  - "code example"
  - "сниппет"
  - "snippet"
PROMPT: "💡 Сохранить этот код-сниппет в память? [y/N]"
```

### 3. Personal Preferences
```yaml
CATEGORY: 13_preferences
TRIGGERS:
  - "я предпочитаю"
  - "I prefer"
  - "мне нравится"
  - "I like"
  - "настройка"
  - "setting"
PROMPT: "💡 Сохранить это как предпочтение? [y/N]"
```

---

## ⚙️ Global Settings

```yaml
# Enable/disable auto-save system
AUTO_SAVE_ENABLED: true

# Minimum confidence to trigger auto-save (0.0 - 1.0)
MIN_CONFIDENCE: 0.7

# Show notification when auto-saving
NOTIFY_ON_AUTO_SAVE: true

# Format of notification
NOTIFICATION_FORMAT: "✅ Auto-saved to {category}: {summary}"

# Maximum auto-saves per session (prevent spam)
MAX_AUTO_SAVES_PER_SESSION: 10

# Cooldown between saves of same category (minutes)
CATEGORY_COOLDOWN: 5
```

---

## 📝 How It Works / Как это работает

1. **AI анализирует** каждое сообщение пользователя
2. **Ищет триггеры** из списков выше
3. **Если найден AUTO_SAVE триггер** → сохраняет + уведомляет
4. **Если найден ASK_USER триггер** → спрашивает подтверждение
5. **Если ничего не найдено** → не сохраняет (можно вручную /remember)

---

## 🔧 Customization / Кастомизация

Добавляй свои триггеры в соответствующие секции выше.

Example / Пример:
```yaml
# Добавить триггер для DevOps
CATEGORY: 11_deployment
TRIGGERS:
  - "docker"
  - "kubernetes"
  - "CI/CD"
CONFIDENCE: 0.8
```
