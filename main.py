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


#main brain
print("***************************************")
print("*Welcome to my python maths calculator*")
print("***************************************")
math_sign=input("D = Division, M = Multiplication, A = Addition, S = Subtraction ")
num1=input("Enter first number ")
num2=input("Enter second number ")
print("Your final answer is") 
print(my_math_function(int(num1),
int(num2), math_sign))