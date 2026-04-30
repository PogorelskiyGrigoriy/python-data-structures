from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Iterable, Set

@dataclass(frozen=True)
class Employee:
    name: str
    id: str

class Company(ABC):
    @abstractmethod
    def get_employees(self) -> Iterable[Employee]:
        pass
    
    @abstractmethod
    def add_employee(self, employee: Employee) -> None:
        pass

class CompanySet(Company):
    def __init__(self):
        # Типизация приватных полей через аннотации внутри __init__ или в классе
        self.__employees: Set[Employee] = set()
        
    def get_employees(self) -> Iterable[Employee]:
        return self.__employees
    
    def add_employee(self, employee: Employee) -> None:
        self.__employees.add(employee)

class NetworkProtocol(ABC):
    @abstractmethod
    def send(self, *args, **kwargs) -> None:
        pass

class HttpNetworkProtocol(NetworkProtocol):
    def __init__(self, base_url: str):
        self.__base_url = base_url
        
    def send(self, *args, **kwargs) -> None:
        print(f"Sending data to {self.__base_url} with args: {args} and kwargs: {kwargs}")
        
class CompanyNetworkProxy(Company):
    def __init__(self, company: Company, network_protocol: NetworkProtocol):
        self.__company = company
        self.__network_protocol = network_protocol
        
    def get_employees(self) -> Iterable[Employee]:
        employees = self.__company.get_employees()
        self.__network_protocol.send(action="get_employees", count=len(employees))
        return employees
    
    def add_employee(self, employee: Employee) -> None:
        self.__company.add_employee(employee)
        self.__network_protocol.send(action="add_employee", employee=employee)       