from abc import ABC, abstractmethod
import random

# here These are the custom exception which check the user perspective Exception so i made it by my Self.
class BankingException(Exception):
    """Base exception for all errors inside the Banking System."""
    pass

class InsufficientFundsError(BankingException):
    """Raised when an account cannot fulfill a withdrawal constraint."""
    pass

class InvalidTransactionError(BankingException):
    """Raised when deposit or withdrawal rules are violated."""
    pass

class ValidationError(BankingException):
    """Raised when initializing or setting data values incorrectly."""
    pass


# --- Base Abstract Class ---
class Account(ABC):
    def __init__(self, account_no, holder_name, balance=0.0):
        # Every step in initialization is safely guarded by methods throwing custom exceptions
        self.set_account_no(account_no)
        self.set_holder_name(holder_name)
        self.set_balance(balance)
        
    def set_holder_name(self, holder_name):
        # Strict checking for empty, null, or blank strings
        if not holder_name or not str(holder_name).strip():
            raise ValidationError("Account holder name cannot be empty or blank!")
        self.holder_name = str(holder_name).strip()   
        
    def get_name(self):
        return self.holder_name;    
         
    def set_account_no(self, account_no):
        # Prevent numbers below or equal to zero, and non-integers
        if not isinstance(account_no, int) or account_no <= 0:
            raise ValidationError(f"Invalid Account No ({account_no}). Must be an integer greater than 0!")
        self.account_no = account_no
        
    def set_balance(self, balance):
        # Secure the data layer against negative injections
        if balance < 0:
            raise ValidationError(f"Initial balance (₹{balance}) cannot be negative!")
        self.balance = float(balance)        

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_details(self):
        # Inner try-catch protects string formatting failures if attributes ever get corrupted
        try:
            return f"Acc No: {self.account_no} | Holder: {self.holder_name} | Balance: ₹{self.balance:.2f}"
        except Exception as e:
            raise BankingException(f"Failed to compile account details display: {e}")






# --- Runtime Flow UI and Interface Engine ---
