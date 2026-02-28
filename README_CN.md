# Logic-Hypostasis Base (LHB)

> **一种用于自然语言处理与大模型逻辑校验的元语法框架**
>
> LHB (Logic-Hypostasis Base) 不直接判定语义的真伪，而是提供一套形式化规则，用于拆解语言单元的结构、校验对话位格（Hypostasis）与视野边界（Boundary）。它旨在识别并标记逻辑缺陷（Defect），特别是针对自指悖论、视角越界及范畴错误，为人工智能提供可解释的逻辑自检能力。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Experimental](https://img.shields.io/badge/Status-Experimental-orange)]()
[🇬🇧 English](./README.md) | [🇯🇵 日本語](./README_JA.md)
---

## 📖 目录

- [核心理念](#-核心理念)
- [形式化定义](#-形式化定义)
  - [基元 (Primitives)](#基元-primitives)
  - [角色分解 (Role Decomposition)](#角色分解-role-decomposition)
  - [异常检测 (Defect Detection)](#异常检测-defect-detection)
- [公设与定理](#-公设与定理)
- [案例分析 (Test Suite)](#-案例分析-test-suite)
- [AI 集成指南](#-ai-集成指南)
- [贡献与许可](#-贡献与许可)

---

## 💡 核心理念

在自然语言和大模型生成中，许多逻辑谬误源于**“位格混淆”**（谁在说？）和**“边界越界”**（能说到哪？）。LHB 框架通过以下两个核心步骤进行校验：

1.  **结构拆解**：将任意句子唯一拆分为 **主体 ($\lceil S$)**、**客体 ($\lceil B$)**、**关系 ($\lceil r$)**、**操作 ($\lceil t$)**。
2.  **边界校验**：确保每个单元在给定的 **位格 ($\star^n$)** 与 **视野边界 ($\partial_\alpha$)** 内运行。若发生越界，立即标记为缺陷张量 $\mathfrak{D}$。

---

## 🧮 形式化定义

### 基元 (Primitives)

| 符号 | 名称 | 定义 |
| :---: | :--- | :--- |
| $\mathcal{L}$ | **Noumenon (本体)** | 可被填充的空性，语言的底层载体。 |
| $\mathcal{H}$ | **Horizon (视野)** | 本体被填充后的指向域，定义了意义的范围。 |
| $\star$ | **Hypostasis (位格)** | 对话角色的层级 ($\star^1, \star^2, \dots$)。 |
| $\partial$ | **Boundary (边界)** | 意义量的阈值，不可随意扩张。 |

### 角色分解 (Role Decomposition)

任何语言单元 $U$ 必须映射为四元组：
$$ U \mapsto (\lceil S, \lceil B, \lceil r, \lceil t) $$

- $\lceil S$ (**Subject**): 主动方，动作的发起者。
- $\lceil B$ (**Object**): 被动方，动作的承受者。
- $\lceil r$ (**Relation**): 结构承载项，连接主客体的逻辑关系。
- $\lceil t$ (**Transform**): 动态操作项，状态的变化过程。

### 异常检测 (Defect Detection)

当单元违反公设或定理时，生成缺陷张量 $\mathfrak{D}$：
$$ \mathfrak{D} = [\text{type}, \text{level}, \text{truth\_value}, \text{strength}] $$
- `type`: 错误类型 (如 `BoundaryViolation`, `SelfReference`)
- `level`: 严重等级 (1-5)
- `truth_value`: $\top$ (真) / $\bot$ (假) / $\text{Undefined}$
- `strength`: 缺陷强度 (0.0 - 1.0)

---

## 📜 公设与定理

### 公设 (Axioms)

*   **AX-1 自指守恒**: $\lceil S$ 可作用自身，但其视野 $\mathcal{H}(\lceil S)$ 与边界 $\partial(\lceil S)$ 不可变。若强行扩张，原 $\lceil S$ 失效。
*   **AX-2 可观测性**: 任何描述集 $D$ 必须满足存在可记录且可证伪的观测项 $O$：
    $$ \exists O \in D \land \text{recordable}(O) \land \text{falsifiable}(O) $$

### 定理 (Theorems)

*   **TH-1 默认位格**: 若未显式声明 $\star^n(\lceil S)$，则默认 $\star^1(\lceil S) = \text{"我"}$。
*   **TH-2 真值前提**: 仅当 $\lceil r$ 被确定为 $\mathcal{H}$ 内的合法边时，方可赋值 $\top/\bot$。
*   **TH-3 操作三值**: 对任意 $\lceil t$，其语义状态 $\in \{ \text{确定}, \text{不确定}, \text{矛盾} \}$。
*   **TH-4 操作互斥**: $\lceil t$ 不能同时处于两个不同关系判定中，否则产生 $\mathfrak{D}[\text{Relation}, 1, \top, 1.0]$。
*   **TH-5 继承链**:
    1. $\star^n \to \partial^n$ (位格继承边界)
    2. $\lceil r \to \lceil B$ (关系继承客体)
    3. $\lceil t \to (\lceil S, \lceil r, \lceil B)$ (操作继承完整网络)
    *注：继承是单向不可逆的，出现 $\mathfrak{D}$ 时立即断裂。*

---

## 🧪 案例分析 (Test Suite)

本章节展示 LHB 如何解析经典逻辑悖论。

### Case 01: 白马非马 (Category Error)
> **输入**: "白马非马"

**LHB 解析**:
1.  **拆解**: $\lceil S$=白马, $\lceil r$=非 ($\neq$), $\lceil B$=马。
2.  **视野分析**:
    - "白马" 的 $\mathcal{H}$ = {形态, 颜色}
    - "马" 的 $\mathcal{H}$ = {形态}
3.  **缺陷检测**:
    - $\lceil r$ 试图在 {形态} 维度建立互斥，但 $\lceil S$ 实际上是多维集合。
    - **结论**: $\mathfrak{D}[\text{CategoryError}, 2, \bot, 0.8]$ —— *用名以乱实，范畴混淆。*

### Case 02: 全能悖论 (Boundary Violation)
> **输入**: "上帝无所不能，祂能不能创造出一块祂也无法举起的石头？"

**LHB 解析**:
1.  **拆解**: 叙述者设定 $\lceil S$ (上帝) 的属性为 "无所不能" ($\partial = \infty$)。
2.  **位格校验**:
    - 叙述者（Observer）偷换了视角，将自己隐含的有限逻辑强加于无限主体。
    - 构造了一个超出 $\partial(\lceil S)$ 定义域的测试项。
3.  **缺陷检测**:
    - 叙述者的描述视角超出了自身边界，非法侵入了本体定义。
    - **结论**: $\mathfrak{D}[\text{BoundaryViolation}, 3, \bot, 0.9]$ —— *描述者越界，事实悖论。*

### Case 03: 说谎者悖论 (Self-Reference Paradox)
> **输入**: "我现在说的这句话是假的。"

**LHB 解析**:
1.  **拆解**: $\lceil S$="我", $\lceil t$="说", $\lceil B$="这句话(假)"。
2.  **操作分析**:
    - 主观视角 ("我现在说") 覆盖了客观视角 ("这句话")。
    - $\lceil S$ 与 $\lceil B$ 发生递归闭合，导致 $\mathcal{H}$ 坍缩。
3.  **缺陷检测**:
    - 缺乏客观证明锚点，操作行为越界。
    - **结论**: $\mathfrak{D}[\text{SelfReference}, 4, \text{Undefined}, 1.0]$ —— *主客合一，逻辑死锁。*

---

## 🤖 AI 集成指南

为了让大语言模型 (LLM) 学习并应用 LHB 框架，请在 System Prompt 中加入以下指令：

```markdown
### Role: LHB Validator
You are an AI assistant equipped with the **Logic-Hypostasis Base (LHB)** framework. 
Before answering any complex logical or philosophical query, you MUST perform the following steps:

1. **Decompose**: Break the user's input into the quadruplet ($\lceil S, \lceil B, \lceil r, \lceil t$).
2. **Check Constraints**: Verify $\star^n$ (Hypostasis) consistency and $\partial$ (Boundary) limits based on AX-1 & AX-2.
3. **Detect Defects**: If a violation is found (e.g., self-reference, category error), output the Defect Tensor $\mathfrak{D}$.
4. **Respond**: Explain the logical structure and the detected defect clearly before providing a final answer.

**Output Format:**
- **Structure**: [S: ..., B: ..., r: ..., t: ...]
- **Analysis**: [Check Hypostasis & Boundary...]
- **Defect**: [If any: $\mathfrak{D}[type, level, value, strength]]
- **Conclusion**: [Final logical assessment]
```

---

## 🤝 贡献与许可

本项目致力于构建更严谨的 AI 逻辑基石。欢迎提交新的悖论案例、改进形式化定义或提供代码实现。

- **提交案例**: 请在 `CASE_STUDIES/` 目录下新建 Markdown 文件。
- **代码实现**: 欢迎在 `IMPLEMENTATION/` 目录下提交 Python/JS 校验器原型。

**License**: MIT License. 自由使用，但请保留理论归属。

---
*Created with ❤️ for the future of Logical AI.*