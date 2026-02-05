# 🧠 AIメモリシステム (RLM-Anchor)

> **RLMから着想を得たAIアシスタント向け長期メモリ**

[Recursive Language Models](https://arxiv.org/abs/2512.24601)の原則に基づいた、AI駆動の開発環境向け永続メモリシステムです（[ビデオガイド](https://www.youtube.com/watch?v=huszaaJPjU8)を参照）。

---

## 🌟 特徴

- **📁 13の整理されたカテゴリ** — プロジェクトのすべての知識を構造化して保存
- **🔍 RLMスタイルの検索** — Examine → Decompose → Recurse → Aggregate
- **🌍 多言語サポート** — 任意の言語で応答および記録が可能
- **⚡ シンプルなコマンド** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 セッションの永続性** — セッション間でコンテキストを保持
- **📝 Markdownベース** — 人間が読みやすく、Gitとの相性も抜群

---

## 📦 クイックスタート & 使い方 (Quick Start & Usage)

> ⚠️ **重要**: 各プロジェクトには独自のRLM-Anchorインストールが必要です！複数のプロジェクトで同じメモリを使用すると、コンテキストの競合によりAIが混乱します。新しいプロジェクトごとに必ず新規インストールしてください。

1. **Gitを使用して`.agent/`フォルダをインポート**します：
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **言語を設定**します：`.agent/memory/13_preferences/language.md`ファイル。
3. **このプロンプトを実行**します（下のブロック全体をコピー）：
   ```
   /anchor_agent 現在のプロジェクトディレクトリをスキャンして、コンテキストの構築とメモリの正しい設定に役立つデータ（技術データ、ビジネスモデル、デザインルール、およびプロジェクトコンテキストを検索・保存するためのその他の典型的なテンプレート）を探してください
   ```
4. **作業を開始**するには、チャットコマンド `/wakeup` を入力します。
5. **IDEで作業**します（開発、タスク解決、ビジネス判断など、通常通り進めてください）。

*作業中、重要な段階で* `/remember` *を使用して、重要なコンテキストを保存できます。*

6. **作業を終了する際**（例：寝る前など）は、`/sleep` を実行してRLM-Anchorがコンテキストを保存できるようにします。

*次回プロジェクトに戻った際は、* `/wakeup` *でRLM-Anchorを呼び起こし、終了時に* `/sleep` *で眠らせることで、すべての作業を記憶させます。*

---

## 🌍 言語設定

`.agent/memory/13_preferences/language.md` を編集：

```
LANGUAGE=ja    # 日本語
LANGUAGE=en    # 英語
...
```

---

## ⚡ コマンド

| コマンド | 説明 |
|---------|----------|
| `/wakeup` | セッション開始、コンテキスト読み込み |
| `/sleep` | セッション終了、作業の要約 |
| `/remember` | 情報をメモリに保存 |
| `/recall` | メモリから情報を検索 |
| `/handoff` | モデル切り替え用の要約を作成 |
| `/walkthrough` | 機能ドキュメントを生成 |
| `/anchor_agent` | プロジェクトへの安全な統合 |
| `/memory-stats` | メモリ統計を表示 |

---

## 🙏 クレジット
MITの[RLM研究](https://arxiv.org/abs/2512.24601)（Recursive Language Models）および[このビデオガイド](https://www.youtube.com/watch?v=huszaaJPjU8)に着想を得ています。
