# 🧠 Sistema de Memoria IA (RLM-Anchor)

> **Memoria a largo plazo para asistentes de IA basada en RLM**

Un sistema de memoria persistente para entornos de desarrollo de IA, basado en los principios de [Recursive Language Models](https://arxiv.org/abs/2512.24601) (investigación del MIT) (ver [Guía en video](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Dale a tu asistente de IA una **memoria persistente** que sobrevive entre sesiones de chat.

---

## 💡 El Problema

Cada vez que inicias un nuevo chat con IA, olvida todo:
- La arquitectura del proyecto
- Decisiones pasadas y sus razones
- Bugs conocidos y soluciones alternativas
- Tu estilo de programación
- En qué trabajaste ayer

**RLM-Anchor resuelve este problema.** Le da a la IA una memoria estructurada a largo plazo — como simples archivos Markdown directamente en tu proyecto.

---

---

## 🌟 Características

- **📁 13 categorías organizadas** — almacenamiento estructurado del conocimiento del proyecto
- **🔍 Búsqueda estilo RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multilingüe** — respuestas y entradas en cualquier idioma
- **⚡ Comandos simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Transferencia de contexto** — cambio fluido entre modelos de IA
- **📝 Basado en Markdown** — legible por humanos, compatible con Git
- **🔄 Persistencia de sesiones** — el contexto se preserva entre sesiones

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANTE**: ¡Cada proyecto requiere una instalación SEPARADA de RLM-Anchor! Usar una memoria para múltiples proyectos confundirá a la IA debido a contextos conflictivos. Siempre instala de nuevo para cada proyecto.

1. **Importa la carpeta `.agent/`** en tu proyecto vía Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Configura el idioma** en `.agent/memory/13_preferences/language.md`
3. **Ejecuta este prompt** (copia el bloque completo):
   ```
   /anchor_agent revisa los directorios del proyecto actual para encontrar datos que ayuden a construir el contexto y configurar la memoria correctamente (datos técnicos, modelos de negocio, reglas de diseño y todas las demás plantillas típicas para encontrar y preservar el contexto del proyecto)
   ```
4. **Comienza a trabajar** con el comando de chat `/wakeup`.
5. **Trabaja en tu IDE** (desarrollo, resolución de problemas, decisiones de negocio, todo como siempre).

*Durante el trabajo, en etapas importantes puedes usar* `/remember` *para guardar contexto importante.*

6. **Cuando termines de trabajar** en el IDE, por ejemplo antes de dormir, ejecuta `/sleep` para que RLM-Anchor guarde el contexto en memoria.

*Ahora cada vez que vuelvas a trabajar en el proyecto — simplemente despierta RLM-Anchor con* `/wakeup` *y al final de la sesión envíalo a dormir de nuevo* `/sleep` *para que recuerde todo lo que hiciste.*

---

## 🌍 Configuración de Idioma

Edita `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=es    # Español
LANGUAGE=en    # Inglés
LANGUAGE=ru    # Ruso  
...
```

---

## ⚡ Comandos

| Comando | Descripción |
|---------|-------------|
| `/wakeup` | Iniciar sesión, cargar contexto |
| `/sleep` | Terminar sesión, archivar en historial |
| `/remember` | Guardar información en memoria |
| `/recall` | Buscar información en memoria |
| `/handoff` | Crear resumen para cambio de modelo |
| `/walkthrough` | Generar documentación de feature |
| `/anchor_agent` | Integración segura al proyecto |
| `/anchor_briefing` | Briefing completo del proyecto (las 13 categorías) |
| `/anchor_backup` | Crear backup manual (para transferencia) |
| `/anchor_restore` | Restaurar desde backup ZIP |
| `/anchor_remove` | Eliminación segura del sistema (con backup) |
| `/anchor_cleanup` | Limpieza inteligente de memoria (TTL, scoring) |
| `/anchor_update` | Actualizar a la última versión desde GitHub |
| `/anchor_validate` | Verificación de integridad de memoria (5 verificaciones) |
| `/memory-stats` | Mostrar estadísticas de memoria con tendencias |

📖 **Documentación completa de comandos**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Estructura

```
.agent/
├── MEMORY_INDEX.md           # Índice principal de memoria
├── skills/
│   └── MEMORY_SKILL.md       # Instrucciones para IA
├── workflows/                 # Definiciones de comandos
├── scripts/                   # Utilidades Python
└── memory/
    ├── 01_project/           # Información del proyecto
    ├── 02_architecture/      # Arquitectura del sistema
    ├── 03_decisions/         # Decisiones arquitectónicas (ADR)
    ├── 04_domain/            # Dominio de negocio
    ├── 05_code/              # Documentación de código
    ├── 06_problems/          # Problemas y soluciones
    ├── 07_context/           # Contexto de sesiones
    ├── 08_people/            # Personas y roles
    ├── 09_external/          # Dependencias externas
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Deployment
    ├── 12_roadmap/           # Planes y futuro
    └── 13_preferences/       # Preferencias e IDIOMA
```

---

## 🔄 Cómo Funciona

### Proceso Estilo RLM

```
Solicitud del usuario
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Leer índice de memoria │
│ 2. DECOMPOSE — Determinar categorías│
│ 3. RECURSE — Buscar en archivos     │
│ 4. AGGREGATE — Combinar datos       │
└─────────────────────────────────────┘
    ↓
Respuesta contextual (en idioma configurado)
```

---

## 📝 Ejemplos de Uso

### 🚀 Inicialización / Conexión
```
Usuario: /anchor_agent
IA: 📋 ANÁLISIS DE INTEGRACIÓN... [Escanea y ofrece opciones de integración segura]
```

### ☀️ Iniciar Sesión
```
Usuario: /wakeup
IA: 🚀 Cargando contexto del proyecto...
    ✅ ¡Sesión iniciada!
    📌 Tareas pendientes: 2
```

### 📌 Guardar Información
```
Usuario: /remember Elegimos PostgreSQL para transacciones ACID
IA: ✅ Guardado en memory/03_decisions/ADR-002-database.md
```

### 🔍 Buscar Conocimiento
```
Usuario: /recall ¿Por qué elegimos PostgreSQL?
IA: 📁 Encontrado en memoria:
    Fuente: memory/03_decisions/ADR-002-database.md
    Elegimos PostgreSQL para soporte de transacciones ACID...
```

### 🔄 Transferencia de Contexto (Handoff)
```
Usuario: /handoff
IA: 🔄 Creando resumen de transferencia de contexto... [Genera resumen para otro modelo]
```

### 📖 Generación de Documentación
```
Usuario: /walkthrough Nueva autorización
IA: 📖 ¡Walkthrough creado! Guardado en memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Estadísticas de Memoria
```
Usuario: /memory-stats
IA: 📊 Estadísticas: 42 archivos, 13 categorías...
```

### 🌙 Terminar Sesión
```
Usuario: /sleep
IA: 📝 Resumiendo sesión...
    ✅ Historial guardado.
    👋 ¡Hasta pronto!
```

---

## 🛠️ Personalización

### Agregar Nuevas Categorías
1. Crear carpeta en `memory/`
2. Agregar `_index.md` 
3. Actualizar `MEMORY_INDEX.md`

### Extender Workflows
Edita archivos en `workflows/` para personalizar comandos.

---

## 📄 Licencia
MIT License — ¡forkea y mejora!

---

## 🙏 Agradecimientos
Inspirado por [investigación RLM del MIT](https://arxiv.org/abs/2512.24601) sobre Recursive Language Models y [esta guía en video](https://www.youtube.com/watch?v=huszaaJPjU8).
