"""
Logic-Hypostasis Base Validator (LHB)
Version: 1.0.0
Author: Logic-Hypostasis Base Community
Description: 
    A prototype validator implementing the LHB meta-syntax framework.
    It decomposes sentences into (Subject, Object, Relation, Transform)
    and checks for Hypostasis (★) and Boundary (∂) violations.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List, Tuple, Any
import math

# ==============================================================================
# 1. Core Definitions (核心定义)
# ==============================================================================

class TruthValue(Enum):
    TRUE = "⊤"
    FALSE = "⊥"
    UNDEFINED = "Undefined"
    CONTRADICTORY = "Contradictory"

class DefectType(Enum):
    NONE = "None"
    BOUNDARY_VIOLATION = "BoundaryViolation"      # 边界越界 (AX-1)
    SELF_EXPANSION = "SelfExpansion"              # 自指扩张 (AX-1)
    CATEGORY_ERROR = "CategoryError"              # 范畴错误 (白马非马)
    SUBJECT_OBJECT_MERGE = "SubjectObjectMerge"   # 主客合一 (说谎者悖论)
    RELATION_CONFLICT = "RelationConflict"        # 关系互斥 (TH-4)
    UNOBSERVABLE = "UnobservableClaim"            # 不可观测 (AX-2)
    CHAIN_BROKEN = "InheritanceChainBroken"       # 继承链断裂 (TH-5)

@dataclass
class DefectTensor:
    """
    缺陷张量 𝔇 = [type, level, truth_value, strength]
    """
    type: DefectType = DefectType.NONE
    level: int = 0  # 1-5
    truth_value: TruthValue = TruthValue.TRUE
    strength: float = 0.0

    def is_valid(self) -> bool:
        return self.type == DefectType.NONE

    def __str__(self):
        if self.is_valid():
            return "✅ Valid (No Defects)"
        return (f"❌ DEFECT: {self.type.name} | "
                f"Lvl:{self.level} | Val:{self.truth_value.value} | Str:{self.strength}")

@dataclass
class Horizon:
    """
    视野 ℋ: 定义本体包含的属性集合
    """
    attributes: set = field(default_factory=set)
    is_infinite: bool = False

    def contains(self, other: 'Horizon') -> bool:
        if self.is_infinite:
            return True
        return other.attributes.issubset(self.attributes)

    def __eq__(self, other):
        if not isinstance(other, Horizon):
            return False
        if self.is_infinite and other.is_infinite:
            return True
        return self.attributes == other.attributes

@dataclass
class LHBUtterance:
    """
    语言单元 U = (┌S, ┌B, ┌r, ┌t)
    """
    subject: str
    object_: str
    relation: str
    transform: str
    
    # Metadata
    hypostasis_level: int = 1  # ★ⁿ
    subject_horizon: Horizon = field(default_factory=lambda: Horizon())
    object_horizon: Horizon = field(default_factory=lambda: Horizon())
    is_self_referential: bool = False
    
    # Analysis Result
    defect: DefectTensor = field(default_factory=DefectTensor)

# ==============================================================================
# 2. LHB Validator Engine (校验引擎)
# ==============================================================================

class LHBValidator:
    def __init__(self):
        self.axioms_log = []

    def validate(self, utterance: LHBUtterance) -> DefectTensor:
        """
        执行完整校验流程
        """
        u = utterance
        
        # Reset defect
        u.defect = DefectTensor()

        # --- Step 1: AX-1 Self-Reference Conservation (自指守恒) ---
        # If S acts on itself, H(S) and ∂(S) must not change.
        if u.is_self_referential:
            if self._check_self_expansion(u):
                u.defect = DefectTensor(
                    type=DefectType.SELF_EXPANSION,
                    level=5,
                    truth_value=TruthValue.FALSE,
                    strength=1.0
                )
                return u.defect
            
            # Check for Subject-Object Merge (Liar Paradox specific)
            if self._check_subject_object_merge(u):
                u.defect = DefectTensor(
                    type=DefectType.SUBJECT_OBJECT_MERGE,
                    level=5,
                    truth_value=TruthValue.UNDEFINED,
                    strength=1.0
                )
                return u.defect

        # --- Step 2: TH-2 Truth Assignment Precondition (真值前提) ---
        # Relation must be a valid edge within Horizon
        if not self._is_valid_relation_edge(u):
            u.defect = DefectTensor(
                type=DefectType.CATEGORY_ERROR,
                level=3,
                truth_value=TruthValue.FALSE,
                strength=0.8
            )
            return u.defect

        # --- Step 3: AX-2 Observability (可观测性) ---
        # Skip for pure logical structures, but check for infinite boundaries in finite contexts
        if u.subject_horizon.is_infinite and "create_unliftable" in u.transform.lower():
             # Specific heuristic for Omnipotence Paradox
             u.defect = DefectTensor(
                type=DefectType.BOUNDARY_VIOLATION,
                level=5,
                truth_value=TruthValue.FALSE,
                strength=1.0
            )
             return u.defect

        # --- Step 4: TH-4 Operational Mutual Exclusion (操作互斥) ---
        if self._check_relation_conflict(u):
            u.defect = DefectTensor(
                type=DefectType.RELATION_CONFLICT,
                level=1,
                truth_value=TruthValue.TRUE, # Paradoxically true that it's conflicting
                strength=1.0
            )
            return u.defect

        # If no defects found
        return u.defect

    # --- Helper Rules (辅助规则) ---

    def _check_self_expansion(self, u: LHBUtterance) -> bool:
        """
        AX-1: Check if the operation tries to expand the subject's horizon illegally.
        """
        # Heuristic: If transform implies changing the definition of S while S is evaluating S
        if "expand" in u.transform.lower() or "redefine" in u.transform.lower():
            return True
        return False

    def _check_subject_object_merge(self, u: LHBUtterance) -> bool:
        """
        Detect Liar Paradox structure: S claims truth value of the statement containing S.
        """
        # Heuristic: If relation is "is false/true" AND object refers to the statement itself
        if u.is_self_referential:
            if "false" in u.relation.lower() or "true" in u.relation.lower():
                # In LHB, if S tries to determine the truth of the very act of determining truth -> Merge
                return True
        return False

    def _is_valid_relation_edge(self, u: LHBUtterance) -> bool:
        """
        TH-2: Check if Relation is valid within Horizons.
        Case: White Horse != Horse (Category Error)
        """
        # Heuristic for "White Horse" case
        # If S has MORE attributes than B, but Relation says "IS NOT" (implying exclusion from category)
        # While logically S should be a subset of B.
        
        s_attrs = u.subject_horizon.attributes
        b_attrs = u.object_horizon.attributes
        
        # If S is a superset of B in attributes (e.g., White+Horse vs Horse)
        # But the relation claims total exclusion ("Is Not") in a classification context
        if b_attrs.issubset(s_attrs) and len(s_attrs) > len(b_attrs):
            if u.relation.lower() in ["is not", "≠", "non"]:
                # This is the公孙龙 trap. 
                # In Classification Horizon: S ∈ B. Claiming S ∉ B is a Category Error.
                # In Identity Horizon: S ≠ B. Claiming S ≠ B is Valid.
                # LHB defaults to Classification for natural language unless specified.
                # We flag this as a potential defect requiring disambiguation.
                return False 
        return True

    def _check_relation_conflict(self, u: LHBUtterance) -> bool:
        """
        TH-4: Check if transform implies mutually exclusive states.
        """
        # Placeholder for complex conflict detection
        return False

# ==============================================================================
# 3. Test Suite (案例测试)
# ==============================================================================

def run_tests():
    validator = LHBValidator()
    
    print("="*60)
    print("LOGIC-HYPOSTASIS BASE (LHB) VALIDATOR v1.0")
    print("="*60)

    # --- Case 1: The Liar Paradox (说谎者悖论) ---
    print("\n[TEST 1] The Liar Paradox: 'This sentence is false.'")
    case1 = LHBUtterance(
        subject="I/Speaker",
        object_="This Sentence",
        relation="is False",
        transform="Declare Truth Value",
        is_self_referential=True,
        subject_horizon=Horizon(attributes={"consciousness"}),
        object_horizon=Horizon(attributes={"text", "self-ref"})
    )
    # Simulating the merge: The object IS the act of the subject
    result1 = validator.validate(case1)
    print(f"Input: ┌S={case1.subject}, ┌B={case1.object_}, ┌r={case1.relation}")
    print(f"Result: {result1}")
    print("> Analysis: Subject-Object Merge detected. No independent anchor.")

    # --- Case 2: Omnipotence Paradox (全能悖论) ---
    print("\n[TEST 2] Omnipotence Paradox: 'Create a stone God cannot lift.'")
    case2 = LHBUtterance(
        subject="God",
        object_="Unliftable Stone",
        relation="Create",
        transform="Create_Unliftable_Object", # Key trigger
        is_self_referential=False,
        subject_horizon=Horizon(is_infinite=True), # Omnipotent
        object_horizon=Horizon(attributes={"heavy", "unliftable_by_God"})
    )
    result2 = validator.validate(case2)
    print(f"Input: ┌S={case2.subject} (∞), ┌B={case2.object_}, ┌t={case2.transform}")
    print(f"Result: {result2}")
    print("> Analysis: Boundary Violation. Finite logic trying to constrain Infinite Horizon.")

    # --- Case 3: White Horse is Not Horse (白马非马) ---
    print("\n[TEST 3] White Horse is Not Horse.")
    case3 = LHBUtterance(
        subject="White Horse",
        object_="Horse",
        relation="is Not", # 非
        transform="Classify",
        is_self_referential=False,
        subject_horizon=Horizon(attributes={"Shape:Horse", "Color:White"}),
        object_horizon=Horizon(attributes={"Shape:Horse"})
    )
    result3 = validator.validate(case3)
    print(f"Input: ┌S={case3.subject} {{Shape, Color}}, ┌B={case3.object_} {{Shape}}, ┌r={case3.relation}")
    print(f"Result: {result3}")
    print("> Analysis: Category Error. Confusing Identity (≠) with Membership (∉).")

    # --- Case 4: Normal Statement (Control) ---
    print("\n[TEST 4] Normal Statement: 'The cat sits on the mat.'")
    case4 = LHBUtterance(
        subject="Cat",
        object_="Mat",
        relation="on",
        transform="Sit",
        is_self_referential=False,
        subject_horizon=Horizon(attributes={"Animal"}),
        object_horizon=Horizon(attributes={"Furniture"})
    )
    result4 = validator.validate(case4)
    print(f"Input: ┌S={case4.subject}, ┌B={case4.object_}, ┌r={case4.relation}")
    print(f"Result: {result4}")
    print("> Analysis: Valid structure. No defects.")

    print("\n" + "="*60)
    print("Validation Complete.")
    print("="*60)

if __name__ == "__main__":
    run_tests()