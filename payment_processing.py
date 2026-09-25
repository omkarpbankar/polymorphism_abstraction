from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount:.2f}")

class UPIPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Processing UPI payment of ${amount:.2f}")

class NetBankingPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Processing Net Banking payment of ${amount:.2f}")

def process_payment(payment_method: Payment, amount: float) -> None:
    # Demonstrating runtime polymorphism
    # The exact pay() method called depends on the object passed at runtime
    payment_method.pay(amount)

if __name__ == "__main__":
    # Create different payment objects
    cc_payment = CreditCardPayment()
    upi_payment = UPIPayment()
    net_payment = NetBankingPayment()

    amount_to_pay = 150.00

    print("--- Payment Processing ---")
    process_payment(cc_payment, amount_to_pay)
    process_payment(upi_payment, amount_to_pay)
    process_payment(net_payment, amount_to_pay)
