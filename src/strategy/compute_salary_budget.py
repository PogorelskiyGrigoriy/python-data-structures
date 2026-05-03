from datetime import datetime
from typing import Iterable, Dict
from .config import get_params_by_experience
from .strategy import Employee, EmployeePayment

def calculate_years_experience(hire_date_str: str) -> float:
    hire_date = datetime.strptime(hire_date_str, "%Y-%m-%d")
    today = datetime(2026, 5, 3)  # Текущая дата по условию
    delta = today - hire_date
    return delta.days / 365.25

def computeSalaryBudget(
    employees: Iterable[Employee], 
    employeesHours: Dict[str, int], 
    sales: int
) -> float:
    total_budget = 0.0
    
    for emp in employees:
        # 1. Считаем опыт
        exp_years = calculate_years_experience(emp.hire_date)
        
        # 2. Получаем параметры из конфига
        wage, commission_percent = get_params_by_experience(exp_years)
        
        # 3. Определяем часы (0 если id нет в словаре)
        hours = employeesHours.get(emp.id, 0)
        
        # 4. Формируем объект платежа
        # Важно: commission в конфиге указан как коэффициент (0.01), 
        # но в базовой стратегии он делится на 100, поэтому умножаем на 100
        payment = EmployeePayment(
            wage=wage,
            hours_worked=hours,
            commission=commission_percent,
            sales=sales
        )
        
        # 5. Вызываем стратегию сотрудника
        total_budget += emp.salary_Strategy(emp, payment)
        
    return total_budget