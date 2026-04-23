from abc import ABC, abstractmethod
from typing import Iterable
from employee import Employee

class Company(ABC):
    @abstractmethod
    def hire_employee(self, employee: Employee) -> None:
        """
        Adds a new employee to the company.
        :raises EmployeeAlreadyExistsError: if ID is already taken.
        """
        pass

    @abstractmethod
    def fire_employee(self, employee_id: str) -> Employee:
        """
        Removes an employee and returns their data.
        :raises EmployeeNotFoundError: if ID does not exist.
        """
        pass

    @abstractmethod
    def get_employee(self, employee_id: str) -> Employee:
        """
        Returns employee data by ID.
        :raises EmployeeNotFoundError: if ID does not exist.
        """
        pass

    @abstractmethod
    def get_all_employees(self) -> Iterable[Employee]:
        """Returns all employees in the company."""
        pass

    @abstractmethod    
    def get_employees_by_department(self, department: str) -> Iterable[Employee]:
        """Returns employees working in a specific department."""
        pass

    @abstractmethod   
    def get_employees_by_salary(self, from_salary: int, to_salary: int) -> Iterable[Employee]: 
        """Returns employees within the specified salary range [from, to]."""
        pass

    @abstractmethod
    def get_employees_by_age(self, from_age: int, to_age: int) -> Iterable[Employee]:
        """Returns employees within the specified age range [from, to]."""
        pass