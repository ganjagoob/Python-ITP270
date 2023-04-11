#!/bin/python3

# Step 1: Create the gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [[subjects[i], grades[i]] for i in range(len(subjects))]

# Step 2: Add the new grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] += 5
gradebook[2][-1] = "Pass"

# Step 3: Combine the two gradebooks
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 89], ["architecture", 75]]
full_gradebook = last_semester_gradebook + gradebook

# Step 4: Format and print the output
print("{:<20} {:<10}".format("Subject", "Grade"))
print("------------------------------------")
for subject, grade in full_gradebook:
    if isinstance(grade, int):
        print("{:<20} {:<10}".format(subject, grade))
    else:
        print("{:<20} {:<10}".format(subject, grade.capitalize()))

