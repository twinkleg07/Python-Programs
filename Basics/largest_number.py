# Program: Largest Number among Three Numbers
# Author: Twinkle Gupta
# Description: This program takes three numbers from the user and prints the largest one. It also handles cases where numbers are equal.

print("Enter three numbers one by one to get the largest among them:")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x == y and y == z:
  print("Numbers are the same.")
  
elif x >= y and x >= z:
  print(x, "is the largest number")
  
elif y >= x and y >= z:
  print(y, "is the largest number")
  
else:
  print(z, "is the largest number")
