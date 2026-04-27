from datetime import date, timedelta
from typing import Iterable
from collections import defaultdict
from sortedcontainers import SortedList

from company import Company
from employee import Employee
from exceptions import EmployeeAlreadyExistsError, EmployeeNotFoundError

class CompanyImpl(Company):
    def __init__(self):
        # Основное хранилище сотрудников: O(1) доступ
        self._employees: dict[str, Employee] = {}
        
        # Индекс департаментов: dict[название, set[ID_сотрудников]]
        # Это решает сразу две задачи: быстрый поиск O(1) и отслеживание "живых" департаментов
        self._dept_index: defaultdict[str, set[str]] = defaultdict(set)
        
        # Отдельный set для списка департаментов (согласно ТЗ)
        self._departments: set[str] = set()

        # Индексы для диапазонов O(log n)
        # Храним кортежи (salary, employee_id) и (birthdate, employee_id)
        self._by_salary = SortedList()
        self._by_birthdate = SortedList()

    def hire_employee(self, employee: Employee) -> None:
        if employee.id in self._employees:
            raise EmployeeAlreadyExistsError(f"Employee ID {employee.id} already exists.")
        
        self._employees[employee.id] = employee
        
        # 1. Обновляем департаменты
        dept = employee.department
        self._dept_index[dept].add(employee.id)
        self._departments.add(dept)
        
        # 2. Обновляем индексы диапазонов
        self._by_salary.add((employee.salary, employee.id))
        self._by_birthdate.add((employee.birthdate, employee.id))

    def fire_employee(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID {employee_id} not found.")
        
        emp = self._employees.pop(employee_id)
        
        # 1. Удаляем из департамента
        dept = emp.department
        self._dept_index[dept].remove(employee_id)
        # Если департамент опустел — удаляем его полностью
        if not self._dept_index[dept]:
            del self._dept_index[dept]
            self._departments.remove(dept)
            
        # 2. Удаляем из индексов диапазонов
        self._by_salary.remove((emp.salary, emp.id))
        self._by_birthdate.remove((emp.birthdate, emp.id))
        
        return emp

    def get_employee(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise EmployeeNotFoundError(f"Employee ID {employee_id} not found.")
        return self._employees[employee_id]

    def get_all_employees(self) -> Iterable[Employee]:
        return self._employees.values()

    def get_employees_by_department(self, department: str) -> Iterable[Employee]:
        # Поиск ускорился с O(n) до O(1)
        if department not in self._dept_index:
            return []
        return [self._employees[emp_id] for emp_id in self._dept_index[department]]

    def get_employees_by_salary(self, from_salary: int, to_salary: int) -> Iterable[Employee]:
        # Пустая строка "" меньше любого ID, а символ "\uffff" больше любого обычного текста.
        # Это позволяет точно захватить границы диапазона.
        start = self._by_salary.bisect_left((from_salary, ""))
        end = self._by_salary.bisect_right((to_salary, "\uffff"))
        
        return [self._employees[emp_id] for _, emp_id in self._by_salary.islice(start, end)]

    def get_employees_by_age(self, from_age: int, to_age: int) -> Iterable[Employee]:
        today = date.today()
        
        # Вспомогательная функция для безопасного вычитания лет (учитывая високосные года)
        def subtract_years(dt: date, years: int) -> date:
            try:
                return dt.replace(year=dt.year - years)
            except ValueError:
                # Если 29 февраля, а год не високосный, откатываемся на 28 февраля
                return dt.replace(year=dt.year - years, day=28)

        # Переводим возраст в даты.
        # Максимальная дата (самые молодые)
        max_birthdate = subtract_years(today, from_age)
        
        # Минимальная дата (самые старые)
        # Тот, кому сегодня 40, мог родиться ровно 41 год назад минус 1 день
        min_birthdate = subtract_years(today, to_age + 1) + timedelta(days=1)
        
        # Ищем в индексе дат (min_birthdate будет раньше в календаре, поэтому она "слева")
        start = self._by_birthdate.bisect_left((min_birthdate, ""))
        end = self._by_birthdate.bisect_right((max_birthdate, "\uffff"))
        
        return [self._employees[emp_id] for _, emp_id in self._by_birthdate.islice(start, end)]