from dataclasses import dataclass, field
from datetime import date

@dataclass(order=True, frozen=True, slots=True)
class Employee:
    id: str = field(compare=True)
    name: str = field(compare=False)
    birthdate: date = field(compare=False)
    department: str = field(compare=False)
    salary: int = field(compare=False)