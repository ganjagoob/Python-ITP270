#!/bin/python3

# Define the three lists of data we will be working with
hairstyles = ["Hipster", "Side Parting", "Buzz", "Cornrows", "Slicked", "Caesar", "Long Hair", "Mullet"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Step 1: Calculate the average price of a haircut
total_price = 0 # Initialize a variable to hold the total price of all haircuts

# Step 2: Loop through the prices list and add each price to the total price
for price in prices:
    total_price += price

# Step 3: Calculate the average price of a haircut by dividing the total price by the number of haircuts
average_price = total_price / len(prices)

# Step 4: Print the average price of a haircut
print("Average Haircut Price: " + str(average_price))

# Step 5: Reduce all prices by $5 using a list comprehension
new_prices = [price - 5 for price in prices]

# Step 6: Print the new prices list
print(new_prices)

# Step 7: Calculate the total revenue from last week's haircuts
total_revenue = 0 # Initialize a variable to hold the total revenue

# Step 8: Loop through the hairstyles list using the range() function
for i in range(len(hairstyles)):
    # Step 9: Calculate the revenue from the current haircut and add it to the total revenue
    total_revenue += prices[i] * last_week[i]

# Step 10: Print the total revenue from last week's haircuts
print("Total Revenue: " + str(total_revenue))

# Step 11: Calculate the average daily revenue
average_daily_revenue = total_revenue / 7

# Step 12: Create a list of haircuts that cost less than $30 using a list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Step 13: Print the list of haircuts that cost less than $30
print(cuts_under_30)

