# This is a functional calculator
from math import pi
from logo import logo
print(logo)
print("""
Welcome to Calcuflex.
Here are some Guidelines and functions:
Functions -
multiply = *
subtract = -
Add = +
divide = /
pi = pi 
""")
user_input = input("Your INPUT Here_\n")

def calc(inputs):
    ans = eval(inputs)
    print(ans)

calc(user_input)