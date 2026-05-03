import unittest
from strategy.compute_salary_budget import computeSalaryBudget
from strategy.strategy import Employee, hourly_strategy, commission_strategy

class TestSalaryBudget(unittest.TestCase):
    def test_single_employee_commission(self):
        # Сотрудник со стажем ~4 года (с 2022 по 2026)
        # Параметры: wage=110, comm=0.5%
        emp = Employee(
            name="Ivan", 
            id="1", 
            hire_date="2022-05-03", 
            basic_salary=50000, 
            salary_Strategy=commission_strategy
        )
        
        hours = {"1": 10}
        sales = 100000
        
        # Ожидаемо: 50000 (basic) + 10 * 110 (hourly) + 100000 * 0.5 / 100 (comm)
        # 50000 + 1100 + 500 = 51600
        result = computeSalaryBudget([emp], hours, sales)
        self.assertEqual(result, 51600.0)

    def test_no_hours_entry(self):
        # Проверка implied zero hours
        emp = Employee(
            name="Anna", 
            id="2", 
            hire_date="2025-05-03", # < 3 лет: wage 100, comm 0.1%
            basic_salary=30000, 
            salary_Strategy=hourly_strategy
        )
        
        result = computeSalaryBudget([emp], {}, 0)
        # 30000 + 0 * 100 = 30000
        self.assertEqual(result, 30000.0)

    def test_senior_experience(self):
        # Стаж > 10 лет: wage 200, comm 2.0%
        emp = Employee(
            name="Oldman", 
            id="99", 
            hire_date="2010-01-01", 
            basic_salary=100000, 
            salary_Strategy=commission_strategy
        )
        
        hours = {"99": 20}
        sales = 1000000
        # 100000 + 20*200 + 1000000*0.02 = 100000 + 4000 + 20000 = 124000
        result = computeSalaryBudget([emp], hours, sales)
        self.assertEqual(result, 124000.0)

if __name__ == "__main__":
    unittest.main()