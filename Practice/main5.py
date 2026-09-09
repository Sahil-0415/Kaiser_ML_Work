# Parent Class
import random
from abc import ABC , abstractmethod
from Department import *
from Address import *
class Employee(ABC):
   
    def __init__(self, emp_id, name, salary , deptobj ,address):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        
        self.department = deptobj
        self.address = address
    
    def get_address_details(self ):
        self.address.show_address_details()

    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Salary: ₹{self.salary}"
    
    def get_showdetails(self):
        self.department.show_dept_details()
    
    # @abstractmethod
    # def passs(self):
    #     pass

# Child Class inheriting from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        # super() calls the __init__ of the parent class (Employee)
        super().__init__(emp_id, name, salary)
        # Initialize the unique attribute for Manager
        self.department = department

    # Overriding the parent method to include department info
    def get_details(self):
        # super() calls the get_details method from Employee
        base_details = super().get_details()
        return f"{base_details} | Dept: {self.department}"
    
    # @property
    # def passs(self):
    #     return " manger ka Passss"

class Clerk(Employee):
    def __init__(self, emp_id, name, salary, overTime , Overtime_pay):
        # super() calls the __init__ of the parent class (Employee)
        super().__init__(emp_id, name, salary)
        # Initialize the unique attribute for Clerk
        self.overTime = overTime
        self.Overtime_pay = Overtime_pay

    # Overriding the parent method to include department info
    def get_details(self):
        # super() calls the get_details method from Employee
        base_details = super().get_details()
        return f"{base_details} | Overtime: {self.overTime} | OverTime_Pay: {self.Overtime_pay}"
    
    # @property
    # def passs(self):
    #     return "clerk ka Passss"
    
    
class SalesMan(Employee):
    def __init__(self, emp_id, name, salary, commsion):
        # super() calls the __init__ of the parent class (Employee)
        super().__init__(emp_id, name, salary)
        # Initialize the unique attribute for SalesMan
        self.commsion = commsion

    # Overriding the parent method to include department info
    def get_details(self):
        # super() calls the get_details method from Employee
        base_details = super().get_details()
        return f"{base_details} | Commision: {self.commsion}"
    # @property
    # def passs(self):
    #     return "Salesman ka passsss"

#Its a Polymorphic Behaviour Function which is Show what is it.
def process_Emp_details(empObj):
    print(type(empObj))
    print(empObj.get_details())
# --- Execution Code ---

# 1. Create a regular Employee object  - No EMp object
# emp1 = Employee(101, "Amit Sharma", 50000)
# print("Employee Details:")
# print(emp1.get_details())
# print("-" * 40)

# 2. Create a Manager object (inherits from Employee)
# Id_Man = random.randint(1,10)
# mgr1 = Manager(Id_Man, "Sahil Bhoye", 95000, "IT Operations")
# process_Emp_details(mgr1)
# print("Manager Details:")
# print(mgr1.get_details())
# print(mgr1.passs)

# # 3. Create a SalesMan object (inherits from Employee)
# Id_Sal = random.randint(21,30)
# Sal = SalesMan(Id_Sal, "Shivam Bhoye", 105000, 10000)
# process_Emp_details(Sal)
# print("SalesMan Details:")
# print(Sal.get_details())
# print(Sal.passs)

# # 4. Create a Clerk object (inherits from Employee)
# Id_Cle = random.randint(31,40)
# Cle = Clerk(Id_Cle, "Sai Bhoye", 50000, 5 , 10000)
# process_Emp_details(Cle)
# print("Clerk Details:")
# print(Cle.get_details())
# print(Cle.passs)
