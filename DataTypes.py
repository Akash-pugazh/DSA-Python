# Data Types

from typing import List, Tuple, Dict, Set, Any

e, f, g = 12, 13, 14  # same line assignment

x: int = 12
# type annotations
y: float = 12.0
z: str = "Hello"
x1: bool = True
x2: None = None

# custom types
Vector2d = List[List[int]]

a: Vector2d = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
# Any data type within List

b: Tuple[int, int, int] = (12, 13, 14)
# Tuple must mention datatype for every variable

c: Dict[str, Dict[str, int]] = {
    "details": {"age": 12},
}
# Dict with straigh frwd str represent key Datatype
# and dict[str, int] mentions value type


d: Set[int] = {12, 13, 12, 13}
# Set simple as list
