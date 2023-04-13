#!/bin/python
#jhua
print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = int(input("Enter the planet number: "))

if planet == 1:
    weight *= 0.91
    print("Your weight on Venus would be", weight)
elif planet == 2:
    weight *= 0.38
    print("Your weight on Mars would be", weight)
elif planet == 3:
    weight *= 2.34
    print("Your weight on Jupiter would be", weight)
elif planet == 4:
    weight *= 1.06
    print("Your weight on Saturn would be", weight)
elif planet == 5:
    weight *= 0.92
    print("Your weight on Uranus would be", weight)
elif planet == 6:
    weight *= 1.19
    print("Your weight on Neptune would be", weight)
else:
    print("Invalid planet number. Please enter a number between 1 and 6.")

