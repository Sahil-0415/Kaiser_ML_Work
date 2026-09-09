str = '*'
print(str*60)
print(str*60)
print("********* Hospital Bill Validation ****************")
print(str*60)
print(str*60)



id = int(input("Enter Patient Id :"))
name = input("Enter Patient Name :")
age = int(input("Enter Patient Age :"))
gender = input("Enter Patient Gender :")
address = input("Enter Patient Address :")
weight = int(input("Enter Patient Weight :"))


# From here the hospital Predecied Value

conslutent_Fee = 1000
thyroid_test = 1000
blood_test = 500
urine_test = 600
# Its a Kideny fuction test
Kft = 4000 
cbc = 3000
lab_chargese = thyroid_test+blood_test+urine_test;
total_bill = lab_chargese+conslutent_Fee;
discount = total_bill * 0.9
final_total_bill = round(discount,2)

# Print all the things ::  Inaurence part need to include.
print(str*60)
print("******************Patient Details************************")
print("Patient Name :", name)
print("Patient id :" , id)
print("Patient Age :" , age)
print("Patient Gender :",gender)
print("Patient Address :", address)
print("Patient Weight :",weight)

print("Consultant Fee :",conslutent_Fee)
print("Lab Chargese (Tyroid test | Blood Test | Urine Test)",lab_chargese)
print("Total bill Before Discount :",total_bill)
print("Final Bill with Discount :" , final_total_bill)

print(str*60)