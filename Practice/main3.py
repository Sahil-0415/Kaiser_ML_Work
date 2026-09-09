class Account:
    def __init__(self, Acc_id, Holder_name, Balance):
        self.Acc_id = Acc_id
        self.Holder_name = Holder_name
        self.Balance = Balance

    # Added 'self' parameter to access instance variables
    def Show_Account_Details(self):
        # Added 'f' prefix to enable string formatting
        print(f"Account Holder name: {self.Holder_name}")
        print(f"Account ID : {self.Acc_id}")
        print(f"Account Balance : {self.Balance}")
        print("-" * 30) # Visual separator
    
    def Deposit(self, Amount):
        self.Balance += Amount
        print(f"Deposited: {Amount}. New Balance: {self.Balance}")

    def Withdraw(self, Amount):
        # Optional check: prevent withdrawing more than the available balance
        if Amount <= self.Balance:
            self.Balance -= Amount
            print(f"Withdrew: {Amount}. New Balance: {self.Balance}")
        else:
            print("Insufficient balance!")

# Execution code (Moved outside the class definition)
A1 = Account(1, "Sahil Bhoye", 10000)

# Test the methods
A1.Show_Account_Details()
A1.Deposit(10000)
A1.Withdraw(1000)
