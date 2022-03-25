from dataclasses import dataclass
from typing import Dict, Tuple, TypeVar, List, Generic, get_type_hints

T = TypeVar('T')

class Varchar():
    def __init__(self, length):
        self.length = length

@dataclass
class A:
    v1: str
    v2: int
    v3: list[int or float]
    v4: dict
    v5: tuple[int, str] = (12,456)
    v6: Varchar(16) = None

a = A('123', 1, [1,2,3,5.6], {'a': 123})


def first_int(ls: List[T]) -> T:
    return ls[0]

first_int([1,2,3,4])

print(get_type_hints(a))
print(get_type_hints(A))