# 🧠 AI 记忆系统 (RLM-Anchor)

> **基于 RLM 的 AI 助手长期记忆系统**

一个基于 [Recursive Language Models](https://arxiv.org/abs/2512.24601) 原理的 AI 辅助开发环境持久化记忆系统。

---

## 🌟 功能特性

- **📁 13 个分类目录** — 结构化存储项目所有知识
- **🔍 RLM 风格搜索** — Examine → Decompose → Recurse → Aggregate
- **🌍 多语言支持** — 使用任何语言进行响应和记录
- **⚡ 简单指令** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 会话持久化** — 在不同会话间保留上下文
- **📝 基于 Markdown** — 易于阅读，Git 友好

---

## 📦 快速开始与使用 (Quick Start & Usage)

1. **通过 Git 导入 `.agent/` 文件夹**到你的项目：
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **设置语言**: 在 `.agent/memory/13_preferences/language.md` 文件中。
3. **运行** ```/agent_anchor``` 以安全地将 RLM-Anchor 集成到当前项目中。
4. **通过聊天指令** ```/wakeup``` **开始工作**。
5. **在 IDE 中正常工作**（开发、解决任务、做决策等）。

*在工作过程中，可以在重要阶段使用* ```/remember``` *来保存重要上下文。*

6. **结束工作时**（例如睡觉前），执行指令 ```/sleep```，以便 RLM-Anchor 将上下文保存到记忆中。

*之后每次回到项目工作时，只需运行* ```/wakeup``` *唤醒 RLM-Anchor，并在结束时运行* ```/sleep``` *让它记录你所做的一切。*

---

## 🌍 语言配置

编辑 `.agent/memory/13_preferences/language.md`：

```
LANGUAGE=zh-CN    # 简体中文
LANGUAGE=en       # 英语
...
```

---

## ⚡ 指令列表

| 指令 | 描述 |
|---------|----------|
| `/wakeup` | 开始会话，加载上下文 |
| `/sleep` | 结束会话，总结工作 |
| `/remember` | 将信息保存到记忆 |
| `/recall` | 从记忆中检索信息 |
| `/handoff` | 为切换模型生成上下文总结 |
| `/walkthrough` | 生成功能文档 |
| `/agent_anchor` | 安全集成到项目中 |
| `/memory-stats` | 显示记忆统计信息 |

---

## 🙏 鸣谢
灵感来自 MIT 关于递归语言模型 (Recursive Language Models) 的 [RLM 研究](https://arxiv.org/abs/2512.24601)。
