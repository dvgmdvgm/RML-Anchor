# 🧠 Sistema de Memória IA (RLM-Anchor)

> **Memória de longo prazo para assistentes de IA baseada em RLM**

Um sistema de memória persistente para ambientes de desenvolvimento de IA, baseado nos princípios dos [Recursive Language Models](https://arxiv.org/abs/2512.24601) (pesquisa do MIT) (ver [Guia em vídeo](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Dê ao seu assistente de IA uma **memória persistente** que sobrevive entre sessões de chat.

---

## 💡 O Problema

Cada vez que você inicia um novo chat com IA, ela esquece tudo:
- A arquitetura do projeto
- Decisões passadas e suas razões
- Bugs conhecidos e soluções alternativas
- Seu estilo de programação
- No que você trabalhou ontem

**RLM-Anchor resolve este problema.** Ele dá à IA uma memória estruturada de longo prazo — como simples arquivos Markdown diretamente no seu projeto.

---

---

## 🌟 Funcionalidades

- **📁 13 categorias organizadas** — armazenamento estruturado do conhecimento do projeto
- **🔍 Busca estilo RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multilíngue** — respostas e entradas em qualquer idioma
- **⚡ Comandos simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Transferência de contexto** — troca fluida entre modelos de IA
- **📝 Baseado em Markdown** — legível por humanos, compatível com Git
- **🔄 Persistência de sessões** — o contexto é preservado entre sessões

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANTE**: Cada projeto requer uma instalação SEPARADA do RLM-Anchor! Usar uma memória para múltiplos projetos confundirá a IA devido a contextos conflitantes. Sempre instale novamente para cada novo projeto.

1. **Importe a pasta `.agent/`** no seu projeto via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Configure o idioma** em `.agent/memory/13_preferences/language.md`
3. **Execute este prompt** (copie o bloco inteiro):
   ```
   /anchor_agent verifique os diretórios do projeto atual para encontrar dados que ajudarão a construir o contexto e configurar a memória corretamente (dados técnicos, modelos de negócio, regras de design e todos os outros modelos típicos para encontrar e preservar o contexto do projeto)
   ```
4. **Comece a trabalhar** com o comando de chat `/wakeup`.
5. **Trabalhe na sua IDE** (desenvolvimento, resolução de problemas, decisões de negócio, tudo como sempre).

*Durante o trabalho, em etapas importantes você pode usar* `/remember` *para salvar contexto importante.*

6. **Quando terminar de trabalhar** na IDE, por exemplo antes de dormir, execute `/sleep` para que o RLM-Anchor salve o contexto na memória.

*Agora toda vez que você voltar a trabalhar no projeto — simplesmente acorde o RLM-Anchor com* `/wakeup` *e no final da sessão mande-o dormir novamente* `/sleep` *para que ele lembre de tudo que você fez.*

---

## 🌍 Configuração de Idioma

Edite `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=pt    # Português
LANGUAGE=en    # Inglês
LANGUAGE=ru    # Russo  
...
```

---

## ⚡ Comandos

| Comando | Descrição |
|---------|-----------|
| `/wakeup` | Iniciar sessão, carregar contexto |
| `/sleep` | Terminar sessão, arquivar no histórico |
| `/remember` | Salvar informação na memória |
| `/recall` | Encontrar informação na memória |
| `/handoff` | Criar resumo para troca de modelo |
| `/walkthrough` | Gerar documentação de feature |
| `/anchor_agent` | Integração segura no projeto |
| `/anchor_briefing` | Briefing completo do projeto (todas as 13 categorias) |
| `/anchor_backup` | Criar backup manual (para transferência) |
| `/anchor_restore` | Restaurar de backup ZIP |
| `/anchor_remove` | Remoção segura do sistema (com backup) |
| `/anchor_cleanup` | Limpeza inteligente de memória (TTL, scoring) |
| `/anchor_update` | Atualizar para última versão do GitHub |
| `/anchor_validate` | Verificação de integridade da memória (5 verificações) |
| `/memory-stats` | Mostrar estatísticas de memória com tendências |

📖 **Documentação completa de comandos**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Estrutura

```
.agent/
├── MEMORY_INDEX.md           # Índice principal de memória
├── skills/
│   └── MEMORY_SKILL.md       # Instruções para IA
├── workflows/                 # Definições de comandos
├── scripts/                   # Utilitários Python
└── memory/
    ├── 01_project/           # Informações do projeto
    ├── 02_architecture/      # Arquitetura do sistema
    ├── 03_decisions/         # Decisões arquiteturais (ADR)
    ├── 04_domain/            # Domínio de negócio
    ├── 05_code/              # Documentação de código
    ├── 06_problems/          # Problemas e soluções
    ├── 07_context/           # Contexto de sessões
    ├── 08_people/            # Pessoas e papéis
    ├── 09_external/          # Dependências externas
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Deployment
    ├── 12_roadmap/           # Planos e futuro
    └── 13_preferences/       # Preferências e IDIOMA
```

---

## 🔄 Como Funciona

### Processo Estilo RLM

```
Solicitação do usuário
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Ler índice de memória  │
│ 2. DECOMPOSE — Determinar categorias│
│ 3. RECURSE — Buscar nos arquivos    │
│ 4. AGGREGATE — Combinar dados       │
└─────────────────────────────────────┘
    ↓
Resposta contextual (no idioma configurado)
```

---

## 📝 Exemplos de Uso

### 🚀 Inicialização / Conexão
```
Usuário: /anchor_agent
IA: 📋 ANÁLISE DE INTEGRAÇÃO... [Escaneia e oferece opções de integração segura]
```

### ☀️ Iniciar Sessão
```
Usuário: /wakeup
IA: 🚀 Carregando contexto do projeto...
    ✅ Sessão iniciada!
    📌 Tarefas pendentes: 2
```

### 📌 Salvar Informação
```
Usuário: /remember Escolhemos PostgreSQL para transações ACID
IA: ✅ Salvo em memory/03_decisions/ADR-002-database.md
```

### 🔍 Buscar Conhecimento
```
Usuário: /recall Por que escolhemos PostgreSQL?
IA: 📁 Encontrado na memória:
    Fonte: memory/03_decisions/ADR-002-database.md
    Escolhemos PostgreSQL para suporte a transações ACID...
```

### 🔄 Transferência de Contexto (Handoff)
```
Usuário: /handoff
IA: 🔄 Criando resumo de transferência de contexto... [Gera resumo para outro modelo]
```

### 📖 Geração de Documentação
```
Usuário: /walkthrough Nova autorização
IA: 📖 Walkthrough criado! Salvo em memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Estatísticas de Memória
```
Usuário: /memory-stats
IA: 📊 Estatísticas: 42 arquivos, 13 categorias...
```

### 🌙 Terminar Sessão
```
Usuário: /sleep
IA: 📝 Resumindo sessão...
    ✅ Histórico salvo.
    👋 Até breve!
```

---

## 🛠️ Personalização

### Adicionar Novas Categorias
1. Crie pasta em `memory/`
2. Adicione `_index.md` 
3. Atualize `MEMORY_INDEX.md`

### Estender Workflows
Edite arquivos em `workflows/` para personalizar comandos.

---

## 📄 Licença
MIT License — faça fork e melhore!

---

## 🙏 Agradecimentos
Inspirado pela [pesquisa RLM do MIT](https://arxiv.org/abs/2512.24601) sobre Recursive Language Models e [este guia em vídeo](https://www.youtube.com/watch?v=huszaaJPjU8).
