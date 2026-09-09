from Department import *
from main5 import *
from Address import *

deptobj = Department("IT" , "Nashik")
address = Address("Kate Coluny" , "Pune")
empobj = Employee(1 , "Sahil",100000 ,deptobj ,address)
print(empobj.get_details())
print(empobj.get_showdetails())

print("**************************************8")
print(empobj.get_details())
print(empobj.get_address_details())