#!/bin/python3

#1. Creating the trip_planner_welcome() function:
def trip_planner_welcome(name):
    print(f"Welcome to Trip Planner v1.0 {name}")
    
#Call the function by passing your name as an argument:
trip_planner_welcome("Justin")
#Output:"Welcome to Trip Planner v1.0 {name}"

#2. Creating the estimated_time_rounded() function:
def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time
#Call the function by passing a decimal argument:
estimate = estimated_time_rounded(2.5)
print(estimate)
#Output: 3

#3. Creating the destination_setup() function:
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    pass

#4. Adding print statements inside the destination_setup() function:
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print(f"Your trip starts off in {origin}")
    print(f"And you are traveling to {destination}")
    print(f"You will be traveling by {mode_of_transport}")
    print(f"It will take approximately {str(estimated_time)} hours")
#Call the function with different arguments:
destination_setup("New York", "Los Angeles", 8)
destination_setup("New York", "Los Angeles", 8, "Plane")




