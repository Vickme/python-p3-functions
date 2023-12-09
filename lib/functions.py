#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()




def greet(name):
    print("Hello, {}!".format(name))

greet("Kelvin")



def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))
    
greet_with_default() 



def add(num1, num2):
    return num1 + num2

result = add(45, 55)
print("Sum:", result) 



def halve(number):
    return number / 2

result = halve(8)
print("Half:", result)