# 🧠 Sistema de Memoria IA (RLM-Anchor)

> **Memoria a largo plazo inspirada en RLM para asistentes de IA**

Un sistema de memoria persistente para entornos de desarrollo impulsados por IA basado en los principios de [Recursive Language Models](https://arxiv.org/abs/2512.24601) (ver [Guía en Video](https://www.youtube.com/watch?v=huszaaJPjU8)).

---

## 🌟 Características

- **📁 13 Categorías Organizadas** — almacenamiento estructurado para todo el conocimiento del proyecto
- **🔍 Búsqueda estilo RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Soporte Multiidioma** — responda y grabe en cualquier idioma
- **⚡ Comandos Simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Persistencia de Sesión** — contexto preservado entre sesiones
- **📝 Basado en Markdown** — legible por humanos, amigable con Git

---

## 📦 Quick Start & Usage

1. **Importa la carpeta `.agent/`** a tu proyecto usando Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Configura tu idioma** en el archivo `.agent/memory/13_preferences/language.md`.
3. **Ejecuta exactamente este prompt:** ```/agent_anchor escanea los directorios del proyecto actual en busca de datos que ayuden a construir el contexto y configurar la memoria correctamente (datos técnicos, modelos de negocio, reglas de diseño y todas las demás plantillas típicas para encontrar y preservar el contexto del proyecto)``` para implementar RLM-Anchor de forma segura en tu proyecto actual.
4. **Comienza a trabajar** con el comando de chat ```/wakeup```.
5. **Trabaja en tu IDE** (desarrolla, resuelve tareas, toma decisiones de negocio, haz todo como de costumbre).

*En el proceso de trabajo, en etapas importantes puedes usar* ```/remember``` *para guardar el contexto importante.*

6. **Cuando termines de trabajar** en tu IDE, por ejemplo, antes de irte a dormir, ejecuta el comando ```/sleep``` para que RLM-Anchor pueda guardar tu contexto en la memoria.

*Ahora, cada vez que vuelvas a trabajar en tu proyecto, simplemente despierta a RLM-Anchor ejecutando* ```/wakeup``` *y al final de la sesión, envíalo de nuevo a dormir con* ```/sleep``` *para que recuerde todo lo que hiciste.*

---

## 🌍 Configuración de Idioma

Edita `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=es    # Español
LANGUAGE=en    # Inglés
...
```

---

## ⚡ Comandos

| Comando | Descripción |
|---------|-------------|
| `/wakeup` | Iniciar sesión, cargar contexto |
| `/sleep` | Finalizar sesión, resumir trabajo |
| `/remember` | Guardar información en memoria |
| `/recall` | Buscar información en memoria |
| `/handoff` | Crear resumen para cambio de modelo |
| `/walkthrough` | Generar documentación de funcionalidad |
| `/agent_anchor` | Integrar de forma segura en el proyecto |
| `/memory-stats` | Mostrar estadísticas de memoria |

---

## 📁 Estructura

```
.agent/
├── MEMORY_INDEX.md           # Índice principal de memoria
├── skills/
│   └── MEMORY_SKILL.md       # Instrucciones de IA
├── workflows/                 # Definiciones de comandos
└── memory/
    ├── 01_project/           # Información del proyecto
    ├── 03_decisions/         # Decisiones de arquitectura (ADR)
    ├── 07_context/           # Contexto de sesión
    └── 13_preferences/       # Preferencias e IDIOMA
```

---

## 🔄 Cómo funciona

### Proceso estilo RLM

```
Consulta del usuario
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Leer índice de memoria │
│ 2. DECOMPOSE — Identificar categorías│
│ 3. RECURSE — Buscar archivos         │
│ 4. AGGREGATE — Combinar información  │
└─────────────────────────────────────┘
    ↓
Respuesta contextual (en el idioma configurado)
```

---

## 🙏 Créditos
Inspirado en la [Investigación RLM de MIT](https://arxiv.org/abs/2512.24601) sobre Modelos de Lenguaje Recursivos y [esta guía en video](https://www.youtube.com/watch?v=huszaaJPjU8).
