# 🧠 Sistema de Memória IA (RLM-Anchor)

> **Memória a longo prazo inspirada em RLM para assistentes de IA**

Um sistema de memória persistente para ambientes de desenvolvimento baseados em IA, fundado nos princípios de [Recursive Language Models](https://arxiv.org/abs/2512.24601).

---

## 🌟 Funcionalidades

- **📁 13 Categorias Organizadas** — armazenamento estruturado de todo o conhecimento do projeto
- **🔍 Busca estilo RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Suporte Multi-idioma** — responda e registre em qualquer idioma
- **⚡ Comandos Simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Persistência de Sessão** — contexto preservado entre sessões
- **📝 Baseado em Markdown** — legível por humanos e compatível com Git

---

## 📦 Quick Start & Usage

1. **Importe a pasta `.agent/`** para o seu projeto via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Defina seu idioma** no arquivo `.agent/memory/13_preferences/language.md`.
3. **Execute** ```/agent_anchor``` para implementar o RLM-Anchor com segurança no seu projeto.
4. **Comece a trabalhar** com o comando de chat ```/wakeup```.
5. **Trabalhe na sua IDE** (desenvolva, resolva tarefas, tome decisões, faça tudo normalmente).

*Durante o trabalho, em etapas importantes, você pode usar* ```/remember``` *para salvar o contexto relevante.*

6. **Quando terminar o trabalho**, por exemplo, antes de dormir, execute o comando ```/sleep``` para que o RLM-Anchor salve o seu contexto na memória.

*Toda vez que voltar a trabalhar, basta acordar o RLM-Anchor com* ```/wakeup``` *e, ao final, enviá-lo para dormir com* ```/sleep``` *para que ele lembre de tudo o que foi feito.*

---

## 🌍 Configuração de Idioma

Edite `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=pt    # Português
LANGUAGE=en    # Inglês
...
```

---

## ⚡ Comandos

| Comando | Descrição |
|---------|-------------|
| `/wakeup` | Iniciar sessão, carregar contexto |
| `/sleep` | Encerrar sessão, resumir trabalho |
| `/remember` | Salvar informações na memória |
| `/recall` | Buscar informações na memória |
| `/handoff` | Criar resumo para troca de modelo |
| `/walkthrough` | Gerar documentação de funcionalidade |
| `/agent_anchor` | Integração segura no projeto |
| `/memory-stats` | Mostrar estatísticas de memória |

---

## 🙏 Créditos
Inspirado na [Pesquisa RLM do MIT](https://arxiv.org/abs/2512.24601) sobre Modelos de Linguagem Recursivos.
