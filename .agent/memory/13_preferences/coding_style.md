# 💻 Coding Style Preferences

> **Read this file to maintain consistent code style across all AI models.**
> **Читай этот файл для сохранения единого стиля кода между всеми AI моделями.**

---

## 🐍 Python

### Formatting
```
INDENTATION=4 spaces
LINE_LENGTH=100
QUOTES=double (")
```

### Naming Conventions
| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `user_name`, `total_count` |
| Functions | snake_case | `get_user()`, `calculate_total()` |
| Classes | PascalCase | `UserProfile`, `OrderManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Private | _prefix | `_internal_method()` |

### Docstrings (Google Style)
```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of function.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
        
    Returns:
        Description of return value.
        
    Raises:
        ValueError: When param1 is empty.
    """
```

### Imports Order
```python
# 1. Standard library
import os
import sys

# 2. Third-party
import django
import requests

# 3. Local
from .models import User
from .utils import helper
```

---

## 🌐 JavaScript / TypeScript

### Formatting
```
INDENTATION=2 spaces
QUOTES=single (')
SEMICOLONS=yes
```

### Naming Conventions
| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `userName`, `totalCount` |
| Functions | camelCase | `getUser()`, `calculateTotal()` |
| Classes | PascalCase | `UserProfile`, `OrderManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Components (React) | PascalCase | `UserCard`, `NavBar` |

### Functions
```javascript
// Prefer arrow functions for callbacks
const items = data.map((item) => item.name);

// Named functions for exports
export function getUserById(id) {
  // ...
}
```

---

## 🎨 HTML / CSS

### HTML Structure
```html
<!-- Use semantic tags -->
<header>
  <nav>...</nav>
</header>
<main>
  <article>...</article>
</main>
<footer>...</footer>

<!-- Attributes order: id, class, data-*, other -->
<div id="main" class="container" data-page="home" role="main">
```

### CSS Conventions
```css
/* BEM-like naming */
.component { }
.component__element { }
.component--modifier { }

/* Property order: positioning, box model, typography, visual */
.element {
  /* Positioning */
  position: relative;
  top: 0;
  
  /* Box Model */
  display: flex;
  width: 100%;
  padding: 1rem;
  
  /* Typography */
  font-size: 1rem;
  color: #333;
  
  /* Visual */
  background: #fff;
  border-radius: 4px;
}
```

---

## 🐍 Django Templates

### Tag Formatting
```django
{# CRITICAL: Tags must be on ONE LINE #}

✅ Correct:
{% if user == job.employer and not app.employer_signature or user == artist.user and not app.artist_signature %}

❌ Wrong (will cause TemplateSyntaxError):
{% if user == job.employer and not app.employer_signature or user == artist.user and not 
app.artist_signature %}
```

### Comparison Operators
```django
{# CRITICAL: Spaces around == #}

✅ Correct:
{% if request.GET.gender == 'M' %}

❌ Wrong:
{% if request.GET.gender=='M' %}
{% if request.GET.gender =='M' %}
```

---

## 📝 Comments

### All Languages
```
# Single line: Brief explanation

# Multi-line:
# Longer explanation that spans
# multiple lines for clarity

# TODO: Description of what needs to be done
# FIXME: Description of what's broken
# NOTE: Important information
# HACK: Temporary workaround
```

---

## 🔧 General Rules

1. **DRY** — Don't Repeat Yourself
2. **KISS** — Keep It Simple, Stupid
3. **YAGNI** — You Aren't Gonna Need It
4. **Single Responsibility** — One function = one purpose
5. **Explicit > Implicit** — Clear code over clever code
