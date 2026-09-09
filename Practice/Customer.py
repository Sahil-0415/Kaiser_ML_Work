from Bank_Management_System import *
from Saving_Account import *
from Current_Account import *
from Address import *
class Customer :
    CustID = 1000
    #address class withstreet city pincode
    def __init__(self, cust_name , address):
        self.CustID = self.CustID+1
        self.cust_name = cust_name
        self.address = address
    
    
    def get_customer_details(self):
        return f"Customer name : {self.cust_name}| Customer_Addresss : {self.address.show_address_details()}"    