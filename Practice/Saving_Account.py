# --- Savings Account Class ---
from Bank_Management_System import *
class SavingsAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, min_balance=1000.0):
        # Inherit base guardrails
        super().__init__(account_no, holder_name, balance)
        self.set_min_balance(min_balance)
                
    def set_min_balance(self, min_balance):
        if min_balance < 0:
            raise ValidationError("Minimum balance threshold constraint cannot be negative!")
        self.min_balance = float(min_balance)    

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Deposit value (₹{amount}) must be greater than zero!")
            self.balance += amount
            return f"Successfully deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Deposit operation rejected! Amount input must be a numeric value.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Withdrawal value (₹{amount}) must be greater than zero!")
            if self.balance - amount < self.min_balance:
                raise InsufficientFundsError(
                    f"Transaction Denied! Savings balance must stay above ₹{self.min_balance:.2f}."
                )
            self.balance -= amount
            return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Withdrawal operation rejected! Amount input must be a numeric value.")

    def show_details(self):
        # Nested execution catches base class format errors and layers custom details on top safely
        try:
            base_details = super().show_details()
            return f"[Savings] {base_details} | Min Balance Req: ₹{self.min_balance:.2f}"
        except BankingException as e:
            raise BankingException(f"Savings Account details generation failed: {e}")