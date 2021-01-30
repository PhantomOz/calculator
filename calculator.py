# This is a functional calculator
from math import pi

user_input = input("Your INPUT Here_\n")

def calc(inputs):
    ans = eval(inputs)
    print(ans)

calc(user_input)