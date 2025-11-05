# import os
# print(os.getenv("password"))
# export password="joy"
# $env:password = "joy"

import sys

def resource(name):  # function definition
    return f"this will be active, {name}!"  # returns a message

message = resource("Vpc,ec2")  # calling the function with input "Alice"

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub =num1 - num2
    return(sub)

def mul(num1, num2):
    mul = num1 * num2
    return(mul)

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)