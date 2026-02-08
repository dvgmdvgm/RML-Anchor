# 🧠 AIメモリシステム（RLM-Anchor）

> **RLMに基づくAIアシスタントのための長期記憶**

AI開発環境のための永続的メモリシステム、[Recursive Language Models](https://arxiv.org/abs/2512.24601)（MIT研究）の原則に基づいています（[ビデオガイド](https://www.youtube.com/watch?v=huszaaJPjU8)参照）。

> AIアシスタントにチャットセッション間で持続する**永続的な記憶**を与えましょう。

---

## 💡 問題

AIと新しいチャットを始めるたびに、すべてを忘れてしまいます：
- プロジェクトのアーキテクチャ
- 過去の決定とその理由
- 既知のバグと回避策
- あなたのコーディングスタイル
- 昨日何に取り組んでいたか

**RLM-Anchorはこの問題を解決します。** AIに構造化された長期記憶を与えます — プロジェクト内のシンプルなMarkdownファイルとして。

---

---

## 🌟 機能

- **📁 13の整理されたカテゴリ** — プロジェクト知識の構造化されたストレージ
- **🔍 RLMスタイルの検索** — Examine → Decompose → Recurse → Aggregate
- **🌍 多言語対応** — 任意の言語での応答とエントリ
- **⚡ シンプルなコマンド** — `/remember`、`/recall`、`/wakeup`、`/sleep`
- **🔄 コンテキストの引き継ぎ** — AIモデル間のシームレスな切り替え
- **📝 Markdownベース** — 人間が読める、Git対応
- **🔄 セッションの永続化** — セッション間でコンテキストが保持される

---

## 📦 クイックスタート＆使い方

> ⚠️ **重要**: 各プロジェクトには別々のRLM-Anchorインストールが必要です！複数のプロジェクトで1つのメモリを使用すると、コンテキストの競合によりAIが混乱します。新しいプロジェクトごとに必ず新規インストールしてください。

1. **`.agent/`フォルダをインポート** GitでプロジェクトにImport：
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **言語を設定** `.agent/memory/13_preferences/language.md`で
3. **このプロンプトを実行**（ブロック全体をコピー）：
   ```
   /anchor_agent 現在のプロジェクトディレクトリをスキャンして、コンテキストの構築とメモリの正しい設定に役立つデータを見つけてください（技術データ、ビジネスモデル、デザインルール、その他プロジェクトコンテキストを見つけて保存するための典型的なテンプレート）
   ```
4. **作業を開始** チャットコマンド`/wakeup`で。
5. **IDEで作業**（開発、問題解決、ビジネス決定、すべていつも通りに）。

*作業中、重要な段階で* `/remember` *を使用して重要なコンテキストを保存できます。*

6. **作業を終了したら** IDEで、例えば寝る前に、`/sleep`を実行してRLM-Anchorがコンテキストをメモリに保存するようにします。

*これで、プロジェクトの作業に戻るたびに — `/wakeup`でRLM-Anchorを起こすだけ、セッションの終わりに再び`/sleep`で眠らせれば、行ったことすべてを覚えています。*

---

## 🌍 言語の設定

`.agent/memory/13_preferences/language.md`を編集：

```
LANGUAGE=ja    # 日本語
LANGUAGE=en    # 英語
LANGUAGE=ru    # ロシア語  
...
```

---

## ⚡ コマンド

| コマンド | 説明 |
|----------|------|
| `/wakeup` | セッション開始、コンテキストをロード |
| `/sleep` | セッション終了、履歴にアーカイブ |
| `/remember` | 情報をメモリに保存 |
| `/recall` | メモリ内の情報を検索 |
| `/handoff` | モデル切り替え用のサマリーを作成 |
| `/walkthrough` | 機能ドキュメントを生成 |
| `/anchor_agent` | プロジェクトへの安全な統合 |
| `/anchor_briefing` | プロジェクトのフルブリーフィング（全13カテゴリ） |
| `/anchor_backup` | 手動バックアップを作成（転送用） |
| `/anchor_restore` | ZIPバックアップから復元 |
| `/anchor_remove` | システムの安全な削除（バックアップ付き） |
| `/anchor_cleanup` | スマートメモリクリーンアップ（TTL、スコアリング） |
| `/anchor_update` | GitHubから最新バージョンに更新 |
| `/anchor_validate` | メモリ整合性チェック（5つのチェック） |
| `/memory-stats` | トレンド付きメモリ統計を表示 |

📖 **コマンドの完全なドキュメント**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 構造

```
.agent/
├── MEMORY_INDEX.md           # メインメモリインデックス
├── skills/
│   └── MEMORY_SKILL.md       # AI向け指示
├── workflows/                 # コマンド定義
├── scripts/                   # Pythonユーティリティ
└── memory/
    ├── 01_project/           # プロジェクト情報
    ├── 02_architecture/      # システムアーキテクチャ
    ├── 03_decisions/         # アーキテクチャ決定（ADR）
    ├── 04_domain/            # ビジネスドメイン
    ├── 05_code/              # コードドキュメント
    ├── 06_problems/          # 問題と解決策
    ├── 07_context/           # セッションコンテキスト
    ├── 08_people/            # 人々と役割
    ├── 09_external/          # 外部依存関係
    ├── 10_testing/           # テスト
    ├── 11_deployment/        # デプロイ
    ├── 12_roadmap/           # 計画と将来
    └── 13_preferences/       # 設定と言語
```

---

## 🔄 仕組み

### RLMスタイルのプロセス

```
ユーザーリクエスト
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — メモリインデックスを読む│
│ 2. DECOMPOSE — カテゴリを決定       │
│ 3. RECURSE — ファイル内を検索       │
│ 4. AGGREGATE — データを統合         │
└─────────────────────────────────────┘
    ↓
コンテキスト応答（設定された言語で）
```

---

## 📝 使用例

### 🚀 初期化/接続
```
ユーザー: /anchor_agent
AI: 📋 統合分析中... [スキャンして安全な統合オプションを提供]
```

### ☀️ セッション開始
```
ユーザー: /wakeup
AI: 🚀 プロジェクトコンテキストをロード中...
    ✅ セッション開始！
    📌 保留中のタスク: 2
```

### 📌 情報を保存
```
ユーザー: /remember PostgreSQLをACIDトランザクション用に選択しました
AI: ✅ memory/03_decisions/ADR-002-database.mdに保存
```

### 🔍 知識を検索
```
ユーザー: /recall なぜPostgreSQLを選んだのですか？
AI: 📁 メモリで見つかりました：
    ソース: memory/03_decisions/ADR-002-database.md
    ACIDトランザクションサポートのためにPostgreSQLを選択しました...
```

### 🔄 コンテキストの引き継ぎ（Handoff）
```
ユーザー: /handoff
AI: 🔄 コンテキスト引き継ぎサマリーを作成中... [別のモデル用のサマリーを生成]
```

### 📖 ドキュメント生成
```
ユーザー: /walkthrough 新しい認証
AI: 📖 ウォークスルー作成！memory/07_context/walkthroughs/2026-02-05_auth.mdに保存
```

### 📊 メモリ統計
```
ユーザー: /memory-stats
AI: 📊 統計: 42ファイル、13カテゴリ...
```

### 🌙 セッション終了
```
ユーザー: /sleep
AI: 📝 セッションをまとめています...
    ✅ 履歴保存完了。
    👋 またね！
```

---

## 🛠️ カスタマイズ

### 新しいカテゴリを追加
1. `memory/`にフォルダを作成
2. `_index.md`を追加 
3. `MEMORY_INDEX.md`を更新

### ワークフローを拡張
`workflows/`内のファイルを編集してコマンドをカスタマイズ。

---

## 📄 ライセンス
MIT License — フォークして改善しましょう！

---

## 🙏 謝辞
[MITのRLM研究](https://arxiv.org/abs/2512.24601)のRecursive Language Modelsと[このビデオガイド](https://www.youtube.com/watch?v=huszaaJPjU8)に触発されました。
