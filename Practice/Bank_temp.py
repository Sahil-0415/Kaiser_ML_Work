from Bank_Management_System import *
from Saving_Account import *
from Current_Account import *
from Customer import *
from Address import *


BankObj = Account(1,"sahil" ,10000)
print(BankObj.show_details())
AddObj = Address("Punavle" , "Pune")
print(AddObj.show_address_details())
custObj = Customer("Sahil" , "NAshik")