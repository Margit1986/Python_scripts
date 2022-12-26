#Codecademy homework: Sal's Shipping (okt 2022):
#Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers. Sal’s Shippers has several different options for a customer to ship their package:
#Ground Shipping, which is a small flat charge plus a rate based on the weight of your package. See the price table.
#Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight. Flat charge: $125.00
#Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping. See the price table. 
#Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 4.8 #input

#Ground Shipping - need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table:
if weight <=2: 
  cost_ground = weight * 1.5 + 20 #Price per Pound $1.5 and Flat Charge $20.00
elif weight > 2 and weight <= 6: 
  cost_ground = weight * 3.0 + 20 #Price per Pound $3.0 and Flat Charge $20.00
elif weight > 6 and weight <= 10: 
  cost_ground = weight * 4.0 + 20 #Price per Pound $4.0 and Flat Charge $20.00
elif weight > 10: 
  cost_ground = weight * 4.75 + 20 #Price per Pound $4.75 and Flat Charge $20.00

#testing:
print(f'Ground Shipping $: {cost_ground}')

#Ground Shipping Premium - greating a variable for the cost of premium ground shipping. The price of premium ground shipping does not change with the weight of the package. Flat charge: $125.00
cost_ground_prem = 125
print("Ground Shipping Premium $:", cost_ground_prem)

#Drone Shipping - 
if weight <=2: 
  cost_drone = weight * 4.5 #Price per Pound $4.5 and Flat Charge $0.00
elif weight > 2 and weight <= 6: 
  cost_drone = weight * 9 #Price per Pound $9.0 and Flat Charge $0.00
elif weight > 6 and weight <= 10: 
  cost_drone = weight * 12 #Price per Pound $12.0 and Flat Charge $0.00
elif weight > 10: 
  cost_drone = weight * 14.25 #Price per Pound $14.25 and Flat Charge $0.00

#testing:
print("Drone Shipping $:", cost_drone)