from datetime import date
from typing import Iterable
from company import Company
from employee import Employee
from exceptions import EmployeeAlreadyExistsError, EmployeeNotFoundError

class CompanyImpl(Company):
    def __init__(self):
        # Professional standard: use a leading underscore for internal attributes
        self._employees: dict[str, Employee] = {}

    def hire_employee(self, employee: Employee) -> None:
        if employee.id in self._employees:
            raise EmployeeAlreadyExistsError(f"Employee ID {employee.id} already exists.")
        self._employees[employee.id] = employee

    def fire_employee(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID {employee_id} not found.")
        return self._employees.pop(employee_id)

    def get_employee(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID {employee_id} not found.")
        return self._employees[employee_id]

    def get_all_employees(self) -> Iterable[Employee]:
        return self._employees.values()

    def get_employees_by_department(self, department: str) -> Iterable[Employee]:
        return [emp for emp in self._employees.values() if emp.department == department]

    def get_employees_by_salary(self, from_salary: int, to_salary: int) -> Iterable[Employee]:
        return [
            emp for emp in self._employees.values() 
            if from_salary <= emp.salary <= to_salary
        ]

    def get_employees_by_age(self, from_age: int, to_age: int) -> Iterable[Employee]:
        today = date.today()
        result = []
        for emp in self._employees.values():
            # Robust age calculation
            age = today.year - emp.birthdate.year - (
                (today.month, today.day) < (emp.birthdate.month, emp.birthdate.day)
            )
            if from_age <= age <= to_age:
                result.append(emp)
        return result