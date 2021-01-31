# This is a functional calculator
from math import pi, sin, sqrt, log10, cos, tan
from logo import logo
print(logo)
print("""


WELCOME TO CALCUFLEX.

Here are some Guidelines and functions:
Functions -
multiply = *
subtract = -
Add = +
divide = /
pi = pi 
sn = sin
rt = sqrt
lg = log10
cs = cos
tn = tan
""")
# Global Variable
sn = sin
rt = sqrt
lg = log10
cs = cos
tn = tan
user_input = input("Your INPUT Here_\n")

def calc(inputs):
    """This is to calculate everything from the user_input"""
    ans = eval(inputs)
    print(ans)

calc(user_input)