# 🧠 AI记忆系统（RLM-Anchor）

> **基于RLM的AI助手长期记忆**

基于[递归语言模型](https://arxiv.org/abs/2512.24601)（MIT研究）原则的AI开发环境持久化记忆系统（参见[视频指南](https://www.youtube.com/watch?v=huszaaJPjU8)）。

> 给你的AI助手一个能在聊天会话之间保持的**持久记忆**。

---

## 💡 问题

每次你与AI开始新的聊天时，它都会忘记一切：
- 项目架构
- 过去的决策及其原因
- 已知的bug和解决方法
- 你的编码风格
- 你昨天在做什么

**RLM-Anchor解决了这个问题。** 它为AI提供结构化的长期记忆——以简单的Markdown文件形式直接存储在你的项目中。

---

---

## 🌟 功能特点

- **📁 13个组织化的类别** — 项目知识的结构化存储
- **🔍 RLM风格搜索** — Examine → Decompose → Recurse → Aggregate
- **🌍 多语言支持** — 任何语言的响应和条目
- **⚡ 简单命令** — `/remember`、`/recall`、`/wakeup`、`/sleep`
- **🔄 上下文传递** — AI模型之间的无缝切换
- **📝 基于Markdown** — 人类可读，Git友好
- **🔄 会话持久化** — 上下文在会话之间保持

---

## 📦 快速开始和使用

> ⚠️ **重要提示**：每个项目都需要单独安装RLM-Anchor！在多个项目中使用同一个记忆会因为上下文冲突而让AI感到困惑。每个新项目都要重新安装。

1. **导入`.agent/`文件夹** 通过Git导入到你的项目：
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **设置语言** 在`.agent/memory/13_preferences/language.md`中
3. **执行这个提示词**（复制整个代码块）：
   ```
   /anchor_agent 扫描当前项目目录以查找有助于构建上下文和正确配置记忆的数据（技术数据、业务模型、设计规则以及所有其他用于查找和保存项目上下文的典型模板）
   ```
4. **开始工作** 使用聊天命令`/wakeup`。
5. **在你的IDE中工作**（开发、解决问题、业务决策，一切照常进行）。

*在工作过程中，在重要阶段你可以使用* `/remember` *来保存重要的上下文。*

6. **当你结束工作时** 在IDE中，例如睡觉前，执行`/sleep`命令让RLM-Anchor将上下文保存到记忆中。

*现在每次你回来继续项目工作时——只需用* `/wakeup` *唤醒RLM-Anchor，在会话结束时再用* `/sleep` *让它休息，它就会记住你所做的一切。*

---

## 🌍 语言设置

编辑`.agent/memory/13_preferences/language.md`：

```
LANGUAGE=zh    # 中文
LANGUAGE=en    # 英语
LANGUAGE=ru    # 俄语  
...
```

---

## ⚡ 命令

| 命令 | 描述 |
|------|------|
| `/wakeup` | 开始会话，加载上下文 |
| `/sleep` | 结束会话，归档到历史记录 |
| `/remember` | 将信息保存到记忆 |
| `/recall` | 在记忆中查找信息 |
| `/handoff` | 创建模型切换摘要 |
| `/walkthrough` | 生成功能文档 |
| `/anchor_agent` | 安全集成到项目 |
| `/anchor_briefing` | 完整项目简报（全部13个类别） |
| `/anchor_backup` | 创建手动备份（用于转移） |
| `/anchor_restore` | 从ZIP备份恢复 |
| `/anchor_remove` | 安全删除系统（带备份） |
| `/anchor_cleanup` | 智能记忆清理（TTL、评分） |
| `/anchor_update` | 从GitHub更新到最新版本 |
| `/anchor_validate` | 记忆完整性检查（5项检查） |
| `/memory-stats` | 显示带趋势的记忆统计 |

📖 **完整命令文档**：[COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 结构

```
.agent/
├── MEMORY_INDEX.md           # 主记忆索引
├── skills/
│   └── MEMORY_SKILL.md       # AI指令
├── workflows/                 # 命令定义
├── scripts/                   # Python工具
└── memory/
    ├── 01_project/           # 项目信息
    ├── 02_architecture/      # 系统架构
    ├── 03_decisions/         # 架构决策（ADR）
    ├── 04_domain/            # 业务领域
    ├── 05_code/              # 代码文档
    ├── 06_problems/          # 问题和解决方案
    ├── 07_context/           # 会话上下文
    ├── 08_people/            # 人员和角色
    ├── 09_external/          # 外部依赖
    ├── 10_testing/           # 测试
    ├── 11_deployment/        # 部署
    ├── 12_roadmap/           # 计划和未来
    └── 13_preferences/       # 偏好设置和语言
```

---

## 🔄 工作原理

### RLM风格流程

```
用户请求
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — 读取记忆索引           │
│ 2. DECOMPOSE — 确定类别             │
│ 3. RECURSE — 在文件中搜索           │
│ 4. AGGREGATE — 合并数据             │
└─────────────────────────────────────┘
    ↓
上下文响应（使用配置的语言）
```

---

## 📝 使用示例

### 🚀 初始化/连接
```
用户: /anchor_agent
AI: 📋 集成分析中... [扫描并提供安全的集成选项]
```

### ☀️ 开始会话
```
用户: /wakeup
AI: 🚀 加载项目上下文中...
    ✅ 会话已开始！
    📌 待处理任务：2
```

### 📌 保存信息
```
用户: /remember 我们选择PostgreSQL用于ACID事务
AI: ✅ 已保存到 memory/03_decisions/ADR-002-database.md
```

### 🔍 搜索知识
```
用户: /recall 为什么我们选择PostgreSQL？
AI: 📁 在记忆中找到：
    来源：memory/03_decisions/ADR-002-database.md
    我们选择PostgreSQL以支持ACID事务...
```

### 🔄 上下文传递（Handoff）
```
用户: /handoff
AI: 🔄 创建上下文传递摘要中... [为其他模型生成摘要]
```

### 📖 生成文档
```
用户: /walkthrough 新的授权
AI: 📖 Walkthrough已创建！保存到 memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 记忆统计
```
用户: /memory-stats
AI: 📊 统计：42个文件，13个类别...
```

### 🌙 结束会话
```
用户: /sleep
AI: 📝 总结会话中...
    ✅ 历史已保存。
    👋 下次见！
```

---

## 🛠️ 自定义

### 添加新类别
1. 在`memory/`中创建文件夹
2. 添加`_index.md` 
3. 更新`MEMORY_INDEX.md`

### 扩展工作流
编辑`workflows/`中的文件来自定义命令。

---

## 📄 许可证
MIT许可证 — 自由使用、fork和改进！

---

## 🙏 致谢
受到[MIT的RLM研究](https://arxiv.org/abs/2512.24601)关于递归语言模型和[这个视频指南](https://www.youtube.com/watch?v=huszaaJPjU8)的启发。
