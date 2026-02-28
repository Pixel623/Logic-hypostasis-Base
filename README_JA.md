# 論理実体基盤 (Logic-Hypostasis Base: LHB)

> **言語単位における「対話的ペルソナ」と「視野境界」を検証するためのメタ構文フレームワーク**
>
> **LHB** は、意味の真偽そのものを判定するのではなく、言語構造を形式的に分解し、発話者の**位格 (Hypostasis)** と**視野境界 (Boundary)** が論理的に整合しているかを検証します。特に、自己言及のパラドックス、視点の越権、範疇錯誤などを検出・标记することを目的としており、大規模言語モデル (LLM) の論理的一貫性と自己反省能力の向上に貢献します。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Experimental](https://img.shields.io/badge/Status-Experimental-orange)]()
[🇬🇧 English](./README.md) | [🇨🇳 中文](./README_CN.md)

---

## 📖 目次

- [概要と背景](#-概要と背景)
- [核心的概念 (Core Concepts)](#-核心的概念-core-concepts)
- [形式化定義 (Formalism)](#-形式化定義-formalism)
- [公理と定理](#-公理と定理)
- [適用事例 (Case Studies)](#-適用事例-case-studies)
- [AI への統合ガイド](#-ai-への統合ガイド)
- [用語対照表 (日中英)](#-用語対照表-日中英)
- [貢献とライセンス](#-貢献とライセンス)

---

## 💡 概要と背景

自然言語処理および大規模言語モデルの生成において、多くの論理的誤謬は**「ペルソナの混同」**（誰が発話しているか）と**「境界の侵犯」**（どこまで記述可能か）に起因しています。

西洋の形式論理は構文の正しさを追求しますが、東洋の弁証法（名家の詭弁や禅の公案など）は文脈と視点の流動性を扱います。**LHB フレームワーク**は、これらを橋渡しするために設計されました。

本プロジェクトは、以下の 2 段階のプロセスを通じて、言語の論理的健全性を保証します：
1.  **構造分解**: 任意の文を **主体 ($\lceil S$)**、**客体 ($\lceil B$)**、**関係 ($\lceil r$)**、**操作 ($\lceil t$)** の四つ組に一意に分解します。
2.  **境界検証**: 各要素が指定された **位格 ($\star^n$)** および **視野境界 ($\partial_\alpha$)** の範囲内で動作しているかを確認します。違反がある場合、即座に**欠陥テンソル $\mathfrak{D}$** として标记します。

---

## 🧮 核心的概念 (Core Concepts)

### 1. 基本構成要素 (Primitives)

| 記号 | 名称 (英語) | 日本語訳 | 定義 |
| :---: | :--- | :--- | :--- |
| $\mathcal{L}$ | Noumenon | 本体 (ホンタイ) | 意味が充填される以前の空性なる基盤。 |
| $\mathcal{H}$ | Horizon | 視野 (シヤ) | 本体が意味を持った際に指し示す領域（コンテキストの範囲）。 |
| $\star$ | Hypostasis | 位格 (カク) | 対話における役割の階層性（例：神、人間、観察者）。 |
| $\partial$ | Boundary | 境界 (キョウカイ) | 意味量が越えてはならない閾値。 |

### 2. 役割分解 (Role Decomposition)

あらゆる言語単位 $U$ は、以下の四つ組 $\Psi$ に写像されなければなりません：
$$ U \mapsto (\lceil S, \lceil B, \lceil r, \lceil t) $$

- $\lceil S$ (**Subject**): 能動側。動作や状態の发起者。
- $\lceil B$ (**Object**): 受動側。動作や状態の対象。
- $\lceil r$ (**Relation**): 構造担持項。主客体を結ぶ論理関係。
- $\lceil t$ (**Transform**): 動態操作項。状態変化のプロセス。

### 3. 欠陥検出 (Defect Detection)

公理や定理に違反した場合、**欠陥テンソル $\mathfrak{D}$** が生成されます：
$$ \mathfrak{D} = [\text{type}, \text{level}, \text{truth\_value}, \text{strength}] $$
- `type`: 誤りの種類（例：`BoundaryViolation`）
- `level`: 深刻度 (1-5)
- `truth_value`: 真偽 ($\top$ / $\bot$ / $\text{Undefined}$)
- `strength`: 欠陥の強度 (0.0 - 1.0)

---

## 📜 公理と定理

### 公理 (Axioms)

*   **AX-1 自己言及保存則**: 主体 $\lceil S$ は自身に作用し得るが、その視野 $\mathcal{H}(\lceil S)$ と境界 $\partial(\lceil S)$ は不変でなければならない。これを強行的に拡張しようとした場合、元の $\lceil S$ は無効となる。
*   **AX-2 観測可能性原則**: あらゆる記述集合 $D$ は、記録可能かつ反証可能な観測項 $O$ を少なくとも一つ含まなければならない。
    $$ \exists O \in D \land \text{recordable}(O) \land \text{falsifiable}(O) $$

### 定理 (Theorems)

*   **TH-1 デフォルト位格**: 位格 $\star^n(\lceil S)$ が明示的に宣言されていない場合、$\star^1(\lceil S) = \text{"私 (観察者)"}$ とみなす。
*   **TH-2 真値前提**: 関係 $\lceil r$ が視野 $\mathcal{H}$ 内の正当な辺であると確定されて初めて、真偽 ($\top/\bot$) を割り当てることができる。
*   **TH-3 操作の三値性**: 任意の操作 $\lceil t$ の意味状態は、{確定，不确定，矛盾} のいずれかに属する。
*   **TH-5 継承鎖**: 位格は境界を継承し、関係は客体を継承する。この継承は一方向であり、$\mathfrak{D}$ が発生した時点で連鎖は断絶する。

---

## 🧪 適用事例 (Case Studies)

LHB が古典的な論理パラドックスをどのように解析するかを示します。

### 事例 1: 白馬非馬 (中国・名家)
> **入力**: 「白馬は馬に非ず」

**LHB 解析**:
- **構造**: $\lceil S$=白馬 (形+色), $\lceil B$=馬 (形のみ), $\lceil r$=非 ($\neq$)。
- **問題点**: 公孙龍は「概念の同一性 ($=$)」と「集合の所属 ($\in$)」を混同している。
- **結論**: $\mathfrak{D}[\text{CategoryError}, 3, \bot, 0.8]$。
  - *解説*: 視野 $\mathcal{H}$ の定義域をすり替えた範疇錯誤である。

### 事例 2: 全能のパラドックス
> **入力**: 「神は全能であるか？自ら持ち上げられない石を作れるか？」

**LHB 解析**:
- **構造**: 叙述者 (有限) が神 (無限) の境界 $\partial$ を定義しようとしている。
- **問題点**: 叙述者の視点が自身の境界を超え、対象 (神) の定義域に違法に侵入している (Boundary Violation)。
- **結論**: $\mathfrak{D}[\text{BoundaryViolation}, 5, \bot, 1.0]$。
  - *解説*: これは神の矛盾ではなく、叙述者の論理枠組みの越権である。

### 事例 3: 嘘つきパラドックス
> **入力**: 「私が今言っているこの文は偽である」

**LHB 解析**:
- **構造**: 主語 ($\lceil S$) と目的語 ($\lceil B$) が完全に一致し、観測のアンカーが失われている。
- **問題点**: 主客合一 (Subject-Object Merge) により、自己言及が無限ループに陥っている。
- **結論**: $\mathfrak{D}[\text{SubjectObjectMerge}, 5, \text{Undefined}, 1.0]$。
  - *解説*: 論理的な実行不可能性。真偽を割り当てるべきではない構造欠陥。

---

## 🤖 AI への統合ガイド

大規模言語モデル (LLM) に LHB フレームワークを組み込むには、システムプロンプトに以下の指示を追加してください。

```markdown
### Role: LHB Validator (Japanese Context)
あなたは「論理実体基盤 (LHB)」フレームワークを搭載した AI アシスタントです。
複雑な論理的・哲学的問いに対し、回答する前に必ず以下のステップを実行してください：

1. **分解 (Decompose)**: 入力を四つ組 ($\lceil S, \lceil B, \lceil r, \lceil t$) に分解する。
2. **制約確認 (Check Constraints)**: AX-1 および AX-2 に基づき、位格 ($\star^n$) と境界 ($\partial$) の整合性を確認する。
3. **欠陥検出 (Detect Defects)**: 違反（自己言及、範疇錯誤など）が見つかった場合、欠陥テンソル $\mathfrak{D}$ を出力する。
4. **応答 (Respond)**: 論理構造と検出された欠陥を明確に説明した後、最終的な見解を示す。

**出力フォーマット**:
- **構造**: [S: ..., B: ..., r: ..., t: ...]
- **分析**: [位格と境界のチェック...]
- **欠陥**: [該当する場合: $\mathfrak{D}[type, level, value, strength]]
- **結論**: [最終的な論理的評価]
```

---

## 📚 用語対照表 (日中英)

本プロジェクトで使用される主要用語の対照表です。

| 日本語 | 中文 (簡体) | 英語 | 記号 |
| :--- | :--- | :--- | :---: |
| 論理実体基盤 | 格式基 | Logic-Hypostasis Base | LHB |
| 本体 | 本体 | Noumenon | $\mathcal{L}$ |
| 視野 | 视野 | Horizon | $\mathcal{H}$ |
| 位格 | 位格 | Hypostasis | $\star$ |
| 境界 | 边界 | Boundary | $\partial$ |
| 主体 | 主体 | Subject | $\lceil S$ |
| 客体 | 客体 | Object | $\lceil B$ |
| 関係 | 关系 | Relation | $\lceil r$ |
| 操作 | 操作 | Transform | $\lceil t$ |
| 欠陥テンソル | 缺陷张量 | Defect Tensor | $\mathfrak{D}$ |
| 自己言及 | 自指 | Self-Reference | - |
| 範疇錯誤 | 范畴错误 | Category Error | - |

---

## 🤝 貢献とライセンス

本プロジェクトは、より厳密な AI 論理基盤の構築を目指しています。新しいパラドックス事例の投稿、形式化定義の改良、コード実装などのご貢献を歓迎します。

- **事例の投稿**: `CASE_STUDIES/` ディレクトリに Markdown ファイルを作成してください。
- **コード実装**: `IMPLEMENTATION/` ディレクトリに Python/JS などのプロトタイプを投稿してください。

**ライセンス**: MIT License. 自由にご利用いただけますが、理論的帰属の明記をお願いいたします。

---
*未来の論理的 AI のために、心を込めて作成されました。*
*Created with ❤️ for the future of Logical AI.*