'''          ASSIGNMENT 1
Write a program that takes 2 inputs from the user in variable a and b.
Based on these inputs find the output of following expressions:
1. Floor Division
2. a power b
3. Find out whether two variables have equal value or not - if yes then print True if they are not equal then print False'''

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

flr_div = a // b

power= a ** b

chk = a == b

print("1. Floor Division:", flr_div)
print("2. a power b:", power)
print("3. Are a and b equal?" :, chk)
