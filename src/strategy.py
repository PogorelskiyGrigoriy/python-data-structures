from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Employee:
    name: str
    id: str
    hire_date: str  # ISO format YYYY-MM-DD
    basic_salary: int
    salary_Strategy: "SalaryStrategy"


@dataclass(frozen=True)
class EmployeePayment:
    wage: float  # 1 hour wage
    hours_worked: int
    commission: float  # percent from sales
    sales: int  # total sales


SalaryStrategy = Callable[[Employee, EmployeePayment], float]


def calculate_basic_salary(employee: Employee, payment: EmployeePayment) -> float:
    return employee.basic_salary


def hourly_strategy(employee: Employee, payment: EmployeePayment) -> float:
    return (
        calculate_basic_salary(employee, payment) + payment.wage * payment.hours_worked
    )


def commission_strategy(employee: Employee, payment: EmployeePayment) -> float:
    return hourly_strategy(employee, payment) + payment.sales * payment.commission / 100
