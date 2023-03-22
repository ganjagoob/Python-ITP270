#!/bin/python3

#1. Create variables for name, age, degree program
name = ""
age = 0
degree_program = ""

#2. Take user input for all three variables
name = input("Please enter your name ")
age = int(input("Please enter your age "))
degree_program = input("Please enter your degree program ")

#3. Calculate remaining age
remaining_age = (age * 3) % 2

# 4. Print message with string concatenation
print("Hi my name is "+ name + ". My remaining age is "+ str(remaining_age) + " and I am majoring in " + degree_program + " at NOVA.")
