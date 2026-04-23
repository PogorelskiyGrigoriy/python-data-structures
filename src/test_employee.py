from unittest import TestCase
from employee import Employee
class TestEmployee(TestCase):
    empl: Employee = Employee(salary=10000, name="Vasya",department="QA",
                                  id="123", birthdate="2000-01-01")
    empl1: Employee = Employee(salary=10000, name="Vasya",department="QA",
                                  id="123", birthdate="2000-01-01")
    empl2: Employee = Employee(salary=10000, name="David",department="QA",
                                  id="120", birthdate="2001-01-01")
    empl3: Employee = Employee(salary=20000, name="Kolya",department="QA",
                                  id="125", birthdate="1990-01-01")
    def test_creating_dict(self):
        
        self.assertEqual(self.empl, self.empl1)
        self.assertFalse(self.empl is self.empl1)
        self.assertEqual("123", self.empl.__dict__["id"])
    def test_sorting_comparing(self) :
        employees: list[Employee] = [self.empl1, self.empl2, self.empl3]
        expectedById = [self.empl2, self.empl1, self.empl3] # sorted by id
        self.assertEqual(expectedById,sorted(employees))
        expectedByBirthdate = [self.empl3, self.empl1, self.empl2]
        self.assertEqual(expectedByBirthdate,sorted(employees, key=lambda e: e.birthdate))
    def test_string_convertion(self) :
        self.assertTrue("Vasya" in str(self.empl))   
        
       
        
       