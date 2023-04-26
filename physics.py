#!/bin/python3

# Fahrenheit to Celsius conversion
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Celsius to Fahrenheit conversion
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Calculate force
def get_force(mass, acceleration):
    return mass * acceleration

# Calculate energy
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Calculate work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Test f_to_c function
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Test c_to_f function
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Test get_force function
train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Test get_energy function
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# Test get_work function
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

# Print output strings
print("The GE train supplies {} Newtons of force.".format(train_force))
print("A 1kg bomb supplies {} Joules.".format(bomb_energy))
print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))
