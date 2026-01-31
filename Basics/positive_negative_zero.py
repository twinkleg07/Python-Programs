# Program: Positive / Negative / Zero
# Author: Twinkle Gupta
# Description: This program checks if a given number is positive, negative or zero using if else statement.

x = float(input("Enter a number:"))

if x > 0:
  print(x, "is a positive number")
  
elif x < 0:
  print(x, "is a negative number")
  
else:
  print(x, "is zero")
