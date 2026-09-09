# --- Current Account Class ---
from Bank_Management_System import *
class CurrentAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_no, holder_name, balance)
        self.set_overdraft_limit(overdraft_limit)
        
    def set_overdraft_limit(self, overdraft_limit):
        if overdraft_limit < 0:
            raise ValidationError("Overdraft protection ceiling limit cannot be negative!")
        self.overdraft_limit = float(overdraft_limit)
        
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
            if self.balance - amount < -self.overdraft_limit:
                raise InsufficientFundsError(
                    f"Transaction Denied! Balance cannot fall lower than overdraft limit (-₹{self.overdraft_limit:.2f})."
                )
            self.balance -= amount
            return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Withdrawal operation rejected! Amount input must be a numeric value.")

    def show_details(self):
        try:
            base_details = super().show_details()
            return f"[Current] {base_details} | Overdraft Limit: ₹{self.overdraft_limit:.2f}"
        except BankingException as e:
            raise BankingException(f"Current Account details generation failed: {e}")

