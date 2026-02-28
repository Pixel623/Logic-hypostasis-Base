# Logic-Hypostasis Base Specification (v1.0)

> **文档状态**: Draft / Experimental  
> **适用范围**: NLP 逻辑校验模块、LLM Prompt 工程、形式化语义分析  
> **最后更新**: 2023-10-XX

## 1. 概述 (Overview)

**Logic-Hypostasis Base (LHB)** 是一种元语法框架，旨在解决自然语言处理中的**视角模糊**、**逻辑越界**及**自指悖论**问题。
本规范定义了语言单元的**四元组拆解规则**、**位格（Hypostasis）约束**及**边界（Boundary）校验机制**。
LHB 不直接判定事实真伪（True/False of Facts），而是判定**陈述结构的逻辑合法性（Validity of Structure）**。

---

## 2. 符号系统 (Symbol System)

本规范采用左制表符风格的结构化符号，所有实现必须严格遵循以下定义。

### 2.1 基元 (Primitives)

| 符号 | 名称 | 类型 | 描述 |
| :---: | :--- | :--- | :--- |
| $\mathcal{L}$ | **Noumenon** | `Set` | 本体，可被填充的空性集合。 |
| $\mathcal{H}$ | **Horizon** | `Function` | 视野函数，$\mathcal{H}(x)$ 返回 $x$ 的意义指向域。 |
| $\star$ | **Hypostasis** | `Integer` | 位格层级，$\star^n$ 表示第 $n$ 级对话角色。 |
| $\partial$ | **Boundary** | `Float` | 边界阈值，定义意义量的最大允许范围。 |

### 2.2 角色分解 (Role Decomposition)

任何自然语言句子 $S_{ent}$ 必须被映射为四元组 $\Psi$：
$$ \Psi = (\lceil S, \lceil B, \lceil r, \lceil t) $$

- **$\lceil S$ (Subject)**: 主动方，动作或状态的发起者。
- **$\lceil B$ (Object)**: 被动方，动作或状态的承受者/指向对象。
- **$\lceil r$ (Relation)**: 结构承载项，定义 $\lceil S$ 与 $\lceil B$ 之间的静态逻辑连接。
- **$\lceil t$ (Transform)**: 动态操作项，描述状态变化的过程或动词核心。

### 2.3 异常张量 (Defect Tensor)

当校验失败时，系统必须生成缺陷张量 $\mathfrak{D}$：
$$ \mathfrak{D} = [\tau, \lambda, \nu, \sigma] $$
- $\tau$ (`type`): 错误类型枚举 (见第 5 节)。
- $\lambda$ (`level`): 严重等级 $\in [1, 5]$。
- $\nu$ (`truth`): 真值状态 $\in \{\top, \bot, \text{Undefined}\}$。
- $\sigma$ (`strength`): 缺陷强度 $\in [0.0, 1.0]$。

---

## 3. 公设 (Axioms)

所有 LHB 兼容系统必须硬编码以下公设作为底层约束。

### AX-1: 自指守恒律 (Law of Self-Reference Conservation)
**定义**: 主体 $\lceil S$ 可以对自身进行操作，但其视野 $\mathcal{H}(\lceil S)$ 与边界 $\partial(\lceil S)$ 在操作过程中保持恒定。
**形式化**:
$$ \forall \lceil t: \lceil S \to \lceil S, \quad \mathcal{H}(\lceil S)_{pre} = \mathcal{H}(\lceil S)_{post} \land \partial(\lceil S)_{pre} = \partial(\lceil S)_{post} $$
**违规后果**: 若检测到 $\mathcal{H}$ 或 $\partial$ 强行扩张，原 $\lceil S$ 立即失效，触发 $\mathfrak{D}[\text{SelfExpansion}, 5, \bot, 1.0]$。

### AX-2: 可观测性原则 (Principle of Observability)
**定义**: 任何有效的描述集 $D$ 必须包含至少一个可记录且可证伪的观测项 $O$。
**形式化**:
$$ \text{Valid}(D) \iff \exists O \in D : \text{recordable}(O) \land \text{falsifiable}(O) $$
其中 `recordable` 和 `falsifiable` 为元语言可判定谓词。
**违规后果**: 若 $D$ 全由不可证伪的形而上学断言组成，标记为 $\mathfrak{D}[\text{Unobservable}, 3, \text{Undefined}, 0.7]$。

---

## 4. 定理与推导规则 (Theorems & Derivation Rules)

### TH-1: 默认位格推断 (Default Hypostasis Inference)
**规则**: 若输入中未显式声明位格 $\star^n(\lceil S)$，则系统自动继承默认值。
$$ \neg \exists n, \star^n(\lceil S) \implies \star^1(\lceil S) \leftarrow \text{"Observer/Speaker"} $$

### TH-2: 真值赋值前提 (Truth Assignment Precondition)
**规则**: 仅当关系项 $\lceil r$ 被验证为位于视野 $\mathcal{H}$ 内的合法边时，方可进行真值赋值。
$$ \text{Assign}(\top/\bot) \iff \lceil r \in \text{Edges}(\mathcal{H}) $$
否则，真值状态强制为 `Undefined`。

### TH-3: 操作三值逻辑 (Ternary Logic of Operations)
**规则**: 对任意动态操作 $\lceil t$，其语义状态空间定义为：
$$ \text{State}(\lceil t) \in \{ \text{Deterministic}, \text{Indeterminate}, \text{Contradictory} \} $$

### TH-4: 操作互斥性 (Operational Mutual Exclusion)
**规则**: 同一 $\lceil t$ 不能同时处于两个互斥的关系判定中。
$$ \neg (\text{Judge}(\lceil t, r_1) \land \text{Judge}(\lceil t, r_2)) \quad \text{if } r_1 \perp r_2 $$
**违规后果**: 触发 $\mathfrak{D}[\text{RelationConflict}, 1, \top, 1.0]$。

### TH-5: 单向继承链 (Unidirectional Inheritance Chain)
**规则**: 属性继承遵循严格单向路径，不可逆。
1. **位格继承边界**: $\star^n \xrightarrow{inherits} \partial^n$
2. **关系继承客体**: $\lceil r \xrightarrow{inherits} \lceil B$
3. **操作继承网络**: $\lceil t \xrightarrow{inherits} (\lceil S, \lceil r, \lceil B)$

**断裂机制**: 一旦链路中任意节点产生 $\mathfrak{D}$，后续继承立即断裂，下游节点状态置为 `Invalid`。

---

## 5. 缺陷类型枚举 (Defect Types Enumeration)

实现中需支持以下标准错误类型：

| ID | Type Name | 描述 | 典型场景 |
| :--- | :--- | :--- | :--- |
| `D01` | **BoundaryViolation** | 主体视野超出其位格允许的边界 | 全能悖论、凡人妄断神意 |
| `D02` | **SelfExpansion** | 自指过程中非法扩张本体定义 | 递归定义死循环 |
| `D03` | **CategoryError** | 关系项连接了不同范畴的客体 | 白马非马、颜色有重量 |
| `D04` | **SubjectObjectMerge** | 主客体在操作中非法合一，丧失观测锚点 | 说谎者悖论 |
| `D05` | **UnobservableClaim** | 描述集缺乏可证伪项 | 纯形而上学断言 |

---

## 6. 算法流程参考 (Reference Algorithm)

以下为 LHB 校验器的伪代码实现参考：

```python
class LHBValidator:
    def validate(self, sentence: str) -> Result:
        # 1. 拆解 (Decomposition)
        s, b, r, t = self.parser.decompose(sentence)
        
        # 2. 位格初始化 (Hypostasis Init)
        if not s.hypostasis_declared:
            s.hypostasis = StarLevel(1) # TH-1
        
        # 3. 边界检查 (Boundary Check - AX-1)
        if self.check_boundary_violation(s, t):
            return Defect(type="BoundaryViolation", level=5)
            
        # 4. 自指守恒检查 (Self-Reference Check - AX-1)
        if s == b and self.detect_expansion(s, t):
            return Defect(type="SelfExpansion", level=5)
            
        # 5. 关系合法性检查 (Relation Validity - TH-2)
        if not self.is_valid_edge(r, s.horizon):
            return Defect(type="CategoryError", level=3)
            
        # 6. 操作互斥检查 (Mutual Exclusion - TH-4)
        if self.has_conflicting_relations(t):
            return Defect(type="RelationConflict", level=1)
            
        # 7. 继承链完整性 (Inheritance Chain - TH-5)
        if not self.verify_inheritance_chain(s, r, b, t):
            return Defect(type="ChainBroken", level=4)
            
        return Valid(status="Passed")

    def check_boundary_violation(self, subject, transform):
        # 实现逻辑：判断 transform 是否要求 subject 拥有超出其定义的 horizon
        pass
```

---

## 7. 兼容性说明 (Compliance)

- **LLM Prompt 兼容**: 本规范设计的符号系统（如 $\lceil S$, $\star^n$）可直接嵌入 Large Language Model 的 System Prompt，作为思维链（Chain-of-Thought）的约束指令。
- **形式化验证兼容**: 公设部分可转换为 Coq 或 Isabelle 等证明辅助语言的定理，用于数学层面的逻辑验证。
- **自然语言处理兼容**: 四元组拆解可作为依存句法分析（Dependency Parsing）的后处理层，用于语义纠错。

---

## 8. 版本历史 (Changelog)

- **v1.0**: 初始规范发布。定义核心基元、5 大公设定理及缺陷张量结构。
- **v0.9 (Draft)**: 内部草案，确立“格式基”概念。

---
*本规范由 Logic-Hypostasis Base Community 维护。解释权归所有贡献者共同所有。*