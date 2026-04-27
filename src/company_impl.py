from datetime import date, timedelta
from typing import Iterable
from collections import defaultdict
from sortedcontainers import SortedList

from company import Company
from employee import Employee
from exceptions import EmployeeAlreadyExistsError, EmployeeNotFoundError

class CompanyImpl(Company):
    def __init__(self):
        # Initialize primary storage and indexing structures
        self._employees: dict[str, Employee] = {}
        
        # Mapping: department_name -> set of employee_ids
        self._dept_index: defaultdict[str, set[str]] = defaultdict(set)

        # Range indices: store tuples (value, employee_id)
        self._by_salary = SortedList()
        self._by_birthdate = SortedList()

    def _get_employee_or_raise(self, employee_id: str) -> Employee:
        # Validate employee existence or raise an exception
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID {employee_id} not found.")
        return self._employees[employee_id]

    def _subtract_years(self, dt: date, years: int) -> date:
        # Calculate a past date safely, handling February 29th
        try:
            return dt.replace(year=dt.year - years)
        except ValueError:
            return dt.replace(year=dt.year - years, day=28)

    def hire_employee(self, employee: Employee) -> None:
        # Register a new employee and update all search indices
        if employee.id in self._employees:
            raise EmployeeAlreadyExistsError(f"Employee ID {employee.id} already exists.")
        
        self._employees[employee.id] = employee
        self._dept_index[employee.department].add(employee.id)
        
        self._by_salary.add((employee.salary, employee.id))
        self._by_birthdate.add((employee.birthdate, employee.id))

    def fire_employee(self, employee_id: str) -> Employee:
        # Remove an employee and purge their data from all indices
        emp = self._get_employee_or_raise(employee_id)
        
        dept = emp.department
        self._dept_index[dept].remove(employee_id)
        if not self._dept_index[dept]:
            del self._dept_index[dept]
            
        self._by_salary.remove((emp.salary, emp.id))
        self._by_birthdate.remove((emp.birthdate, emp.id))
        
        return self._employees.pop(employee_id)

    def get_employee(self, employee_id: str) -> Employee:
        # Retrieve a specific employee by their unique ID
        return self._get_employee_or_raise(employee_id)

    def get_all_employees(self) -> Iterable[Employee]:
        # Return a collection of all employees in the company
        return self._employees.values()

    def get_employees_by_department(self, department: str) -> Iterable[Employee]:
        # Efficiently fetch all employees belonging to a specific department
        ids = self._dept_index.get(department, set())
        return [self._employees[eid] for eid in ids]

    def get_employees_by_salary(self, from_salary: int, to_salary: int) -> Iterable[Employee]:
        # Perform an efficient range search for employees by salary
        start = self._by_salary.bisect_left((from_salary, ""))
        end = self._by_salary.bisect_right((to_salary, "\uffff"))
        
        return [self._employees[eid] for _, eid in self._by_salary.islice(start, end)]

    def get_employees_by_age(self, from_age: int, to_age: int) -> Iterable[Employee]:
        # Filter employees within an age range using birthdate indexing
        today = date.today()
        
        max_date = self._subtract_years(today, from_age)
        min_date = self._subtract_years(today, to_age + 1) + timedelta(days=1)
        
        start = self._by_birthdate.bisect_left((min_date, ""))
        end = self._by_birthdate.bisect_right((max_date, "\uffff"))
        
        return [self._employees[eid] for _, eid in self._by_birthdate.islice(start, end)]

    def get_all_departments(self) -> Iterable[str]:
        # List all departments that currently have active employees
        return self._dept_index.keys()