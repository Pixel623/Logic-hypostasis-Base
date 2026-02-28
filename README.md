# Logic-Hypostasis Base (LHB)

> **A Meta-Syntax Framework for Validating "Dialogical Hypostasis" and "Horizon Boundaries" in Language Units**
>
> **LHB** does not judge semantic truth directly. Instead, it provides a formalized rule set to decompose language structures and verify whether the **Hypostasis (Role/Person)** and **Boundary (Scope)** of an utterance are logically consistent. It is designed to detect and flag logical defects—such as self-referential paradoxes, perspective overreach, and category errors—providing explainable logical self-check capabilities for Artificial Intelligence.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Experimental](https://img.shields.io/badge/Status-Experimental-orange)]()
[🇯🇵 日本語](./README_JA.md) | [🇨🇳 中文](./README_CN.md)

---

## 📖 Table of Contents

- [Core Philosophy](#-core-philosophy)
- [Formal Definitions](#-formal-definitions)
  - [Primitives](#primitives)
  - [Role Decomposition](#role-decomposition)
  - [Defect Detection](#defect-detection)
- [Axioms & Theorems](#-axioms--theorems)
- [Case Studies](#-case-studies)
- [AI Integration Guide](#-ai-integration-guide)
- [Terminology Map](#-terminology-map)
- [Contributing & License](#-contributing--license)

---

## 💡 Core Philosophy

In Natural Language Processing (NLP) and Large Language Model (LLM) generation, many logical fallacies stem from **"Hypostasis Confusion"** (Who is speaking?) and **"Boundary Violations"** (What can be said?).

While Western formal logic focuses on syntactic validity, and Eastern dialectics (like the School of Names or Zen Koans) explore contextual fluidity, **LHB** bridges these traditions. It ensures logical robustness through two key steps:

1.  **Structural Decomposition**: Uniquely decomposing any sentence into **Subject ($\lceil S$)**, **Object ($\lceil B$)**, **Relation ($\lceil r$)**, and **Transform ($\lceil t$)**.
2.  **Boundary Validation**: Ensuring every unit operates within its assigned **Hypostasis ($\star^n$)** and **Boundary ($\partial_\alpha$)**. Violations are immediately flagged as a **Defect Tensor $\mathfrak{D}$**.

---

## 🧮 Formal Definitions

### Primitives

| Symbol | Name | Definition |
| :---: | :--- | :--- |
| $\mathcal{L}$ | **Noumenon** | The ontological base; the emptiness ready to be filled with meaning. |
| $\mathcal{H}$ | **Horizon** | The指向 domain (scope) of meaning once the Noumenon is filled. |
| $\star$ | **Hypostasis** | The hierarchical level of the dialogical role (e.g., God, Human, Observer). |
| $\partial$ | **Boundary** | The threshold of meaning quantity that cannot be arbitrarily expanded. |

### Role Decomposition

Any language unit $U$ must be mapped to a quadruplet $\Psi$:
$$ U \mapsto (\lceil S, \lceil B, \lceil r, \lceil t) $$

- $\lceil S$ (**Subject**): The active agent; the initiator of action or state.
- $\lceil B$ (**Object**): The passive recipient; the target of action or state.
- $\lceil r$ (**Relation**): The structural carrier; the logical link between Subject and Object.
- $\lceil t$ (**Transform**): The dynamic operation; the process of state change.

### Defect Detection

When an unit violates axioms or theorems, a **Defect Tensor $\mathfrak{D}$** is generated:
$$ \mathfrak{D} = [\text{type}, \text{level}, \text{truth\_value}, \text{strength}] $$
- `type`: Error category (e.g., `BoundaryViolation`).
- `level`: Severity level (1-5).
- `truth_value`: Truth status ($\top$ / $\bot$ / $\text{Undefined}$).
- `strength`: Defect intensity (0.0 - 1.0).

---

## 📜 Axioms & Theorems

### Axioms

*   **AX-1 Law of Self-Reference Conservation**: A Subject $\lceil S$ may act upon itself, but its Horizon $\mathcal{H}(\lceil S)$ and Boundary $\partial(\lceil S)$ must remain invariant. Forcible expansion results in the invalidation of the original $\lceil S$.
*   **AX-2 Principle of Observability**: Any description set $D$ must contain at least one observable item $O$ that is recordable and falsifiable:
    $$ \exists O \in D \land \text{recordable}(O) \land \text{falsifiable}(O) $$

### Theorems

*   **TH-1 Default Hypostasis**: If $\star^n(\lceil S)$ is not explicitly declared, then $\star^1(\lceil S) = \text{"I (Observer)"}$.
*   **TH-2 Truth Assignment Precondition**: Truth values ($\top/\bot$) can only be assigned if the relation $\lceil r$ is confirmed as a valid edge within the Horizon $\mathcal{H}$.
*   **TH-3 Ternary Logic of Operations**: For any $\lceil t$, its semantic state $\in \{ \text{Deterministic}, \text{Indeterminate}, \text{Contradictory} \}$.
*   **TH-5 Unidirectional Inheritance**: Hypostasis inherits Boundary; Relation inherits Object. This chain is单向 (unidirectional) and breaks immediately upon encountering a $\mathfrak{D}$.

---

## 🧪 Case Studies

How LHB analyzes classic logical paradoxes.

### Case 1: White Horse is Not Horse (School of Names, China)
> **Input**: "A white horse is not a horse."

**LHB Analysis**:
- **Structure**: $\lceil S$=White Horse (Form+Color), $\lceil B$=Horse (Form only), $\lceil r$=Is Not ($\neq$).
- **Defect**: The argument conflates **Identity** ($=$) with **Membership** ($\in$).
- **Result**: $\mathfrak{D}[\text{CategoryError}, 3, \bot, 0.8]$.
  - *Insight*: A category error caused by shifting the definition domain of the Horizon $\mathcal{H}$.

### Case 2: The Omnipotence Paradox
> **Input**: "Can God create a stone so heavy that He cannot lift it?"

**LHB Analysis**:
- **Structure**: The Narrator (Finite) attempts to define the Boundary $\partial$ of God (Infinite).
- **Defect**: The narrator's perspective illegally exceeds their own boundary to constrain the subject (Boundary Violation).
- **Result**: $\mathfrak{D}[\text{BoundaryViolation}, 5, \bot, 1.0]$.
  - *Insight*: This is not a contradiction in God, but a logical overreach by the narrator.

### Case 3: The Liar Paradox
> **Input**: "This sentence is false."

**LHB Analysis**:
- **Structure**: Subject ($\lceil S$) and Object ($\lceil B$) merge completely; the observational anchor is lost.
- **Defect**: Subject-Object Merge leads to an infinite recursion loop.
- **Result**: $\mathfrak{D}[\text{SubjectObjectMerge}, 5, \text{Undefined}, 1.0]$.
  - *Insight*: A structural defect. No truth value should be assigned.

---

## 🤖 AI Integration Guide

To equip Large Language Models (LLMs) with LHB capabilities, add the following instructions to your System Prompt:

```markdown
### Role: LHB Validator
You are an AI assistant equipped with the **Logic-Hypostasis Base (LHB)** framework.
Before answering complex logical or philosophical queries, you MUST:

1. **Decompose**: Break the input into the quadruplet ($\lceil S, \lceil B, \lceil r, \lceil t$).
2. **Check Constraints**: Verify $\star^n$ (Hypostasis) consistency and $\partial$ (Boundary) limits per AX-1 & AX-2.
3. **Detect Defects**: If a violation is found (e.g., self-reference, category error), output the Defect Tensor $\mathfrak{D}$.
4. **Respond**: Explain the logical structure and detected defects clearly before providing a final answer.

**Output Format**:
- **Structure**: [S: ..., B: ..., r: ..., t: ...]
- **Analysis**: [Check Hypostasis & Boundary...]
- **Defect**: [If any: $\mathfrak{D}[type, level, value, strength]]
- **Conclusion**: [Final logical assessment]
```

---

## 📚 Terminology Map

| English | Chinese (简体) | Japanese (日本語) | Symbol |
| :--- | :--- | :--- | :---: |
| Logic-Hypostasis Base | 格式基 | 論理実体基盤 | LHB |
| Noumenon | 本体 | 本体 | $\mathcal{L}$ |
| Horizon | 视野 | 視野 | $\mathcal{H}$ |
| Hypostasis | 位格 | 位格 | $\star$ |
| Boundary | 边界 | 境界 | $\partial$ |
| Subject | 主体 | 主体 | $\lceil S$ |
| Object | 客体 | 客体 | $\lceil B$ |
| Relation | 关系 | 関係 | $\lceil r$ |
| Transform | 操作 | 操作 | $\lceil t$ |
| Defect Tensor | 缺陷张量 | 欠陥テンソル | $\mathfrak{D}$ |

---

## 🤝 Contributing & License

This project aims to build a more rigorous logical foundation for AI. We welcome contributions including new paradox case studies, improvements to formal definitions, or code implementations.

- **Submit Cases**: Create a Markdown file in the `CASE_STUDIES/` directory.
- **Code Implementation**: Submit Python/JS prototypes in the `IMPLEMENTATION/` directory.

**License**: MIT License. Free to use, but please retain attribution to the theoretical framework.

---
*Created with ❤️ for the future of Logical AI.*