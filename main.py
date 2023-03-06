#what the calculator will output
def my_math_function(x, y, z):
  if z=="M":
    return x*y
  if z=="D":
    return x/y
  if z=="A":
    return x+y
  if z=="S":
    return x-y


#the main code for the calculator
print("-----------------------------------")
print("= Welcome to my python calculator =")
print("-----------------------------------")
math_sign=input("What equation would you like mo to complete. D = Division, M = Multiplication, A = Addition or S = Subtraction? ")
num1=input("Enter first number ")
num2=input("Enter second number ")
print("Your final answer is") 
print(my_math_function(int(num1),
int(num2), math_sign))