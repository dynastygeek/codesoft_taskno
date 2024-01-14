a = float(input("Enter the first number: ")) 
b = float(input("Enter the second number: "))

print("Enter 1 :for addition of two numbers")
print("Enter 2 :for substraction of two numbers")
print("Enter 3 :for multiplication of two numbers")
print("Enter 4 :for divison of two numbers")
print("Enter 5 :for modulus of two numbers")
print("Enter 6 :for floor divison of two numbers")
print("Enter 7 :for exponents of two numbers")

enter_operator_num = int(input("Enter the operator number:"))
if enter_operator_num == 1:
  print("The sum of two numbers is : ",a+b)
if enter_operator_num == 2:
  print("The substractio of two numbers is : ",a-b)
if enter_operator_num == 3:
  print("The multiplication of two numbers is : ",a*b)
if enter_operator_num == 4:
  print("The division of two numbers is : ",a/b)
if enter_operator_num == 5:
  print("The modulus of two numbers is : ",a%b)
if enter_operator_num == 6:
  print("The floor division of two numbers is : ",a//b)
if enter_operator_num == 7:
  print("The exponents of two numbers is : ",a**b)