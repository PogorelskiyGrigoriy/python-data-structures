from logger_config import setup_logging
from abc import ABC, abstractmethod


logger = setup_logging()

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass
    
class PayPalPayment(Payment):
    def pay(self, amount):
        logger.info(f"Processing PayPal payment of ${amount}")
        
class CreditCardPayment(Payment):
    def pay(self, amount):
        logger.info(f"Processing Credit Card payment of ${amount}")
        
    #abstrack risk
class Risk(ABC):
    @abstractmethod
    def score(self) -> float:
        pass
    
class PayPalRisk(Risk):
    def score(self) -> float:
        logger.info("Calculating PayPal risk score")
        return 0.2  # Dummy risk score for PayPal
    
class CreditCardRisk(Risk):
    def score(self) -> float:
        logger.info("Calculating Credit Card risk score")
        return 0.5  # Dummy risk score for Credit Card
    
    #abstract factory   
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass
    
    @abstractmethod
    def create_risk(self) -> Risk:
        pass
    
class PayPalFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return PayPalPayment()
    
    def create_risk(self) -> Risk:
        return PayPalRisk()
    
class CreditCardFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return CreditCardPayment()
    
    def create_risk(self) -> Risk:
        return CreditCardRisk()