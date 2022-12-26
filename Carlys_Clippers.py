# Codecademy homework (nov 2022): Carly's Clippers: 
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
# You have been provided with three lists:
# 1.hairstyles: the names of the cuts offered at Carly’s Clippers.
# 2.prices: the price of each hairstyle in the hairstyles list.
# 3.last_week: the number of purchases for each hairstyle type in the last week.
# Each index in hairstyles corresponds to an associated index in prices and last_week.
# For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

# Summing up all the prices of haircuts. Creating a variable total_price:
total_price = 0
# Looping through the prices list and adding each price to the variable total_price.
for price in prices:
  total_price += price
# Creating a variable called average_price that is the total_price divided by the number of price. Getting the number of prices by using the len() function:
average_price = total_price / len(prices)
print("Average Haircut Price:" , average_price)

# 2. That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

# Using a list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices = [p - 5 for p in prices]
print(new_prices)

# 3. Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

# Creating a variable called total_revenue. Using a for loop to create a variable i that goes from 0 to len(hairstyles). Adding the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:" ,total_revenue)

# Finding the average daily revenue by dividing total_revenue by 7:
average_daily_revenue = total_revenue / 7
print("Average daily revenue:" , average_daily_revenue)

# 4. Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

# Using a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print("Haircuts under 30 dollars:" ,cuts_under_30)
