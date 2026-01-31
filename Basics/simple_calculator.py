# Program: Simple Calculator 
# Author: Twinkle Gupta
# Description: This program creates a simple calculator using if-else statements and performs operations on two numbers.

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print("Choose one Operator")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

opr = input("Enter the operator:")

if opr == "+":
  print("Result:", num1+num2)
  
elif opr == "-":
  print("Result: ", num1-num2)
  
elif opr == "*":
  print("Result: ", num1*num2)
  
elif opr == "/":
  if num2 != 0:
    print("Result: ", num1/num2)
  else:
    print("Error: Can't divide by zero")
    
else:
  print("Invalid operator.Try again.")
  
           
