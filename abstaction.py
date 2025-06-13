from abc import ABC, abstractmethod

# Abstract class
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class 1
class CreditCardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

# Concrete class 2
class PayPalPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

# Client code
def make_payment(payment_method, amount):
    payment_method.pay(amount)

