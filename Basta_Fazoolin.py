# Codecademy homework (dec 2022): Basta Fazoolin'
# You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

# Restaurant has four different menus: brunch, early-bird, dinner, and kids. Creating a Menu class and giving Menu a constructor with the five parameters self, name, items, start_time, and end_time.
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  # Giving the Menu class a string representation method that will tell the name of the menu. Indicating in this representation when the menu is available.
  def __repr__(self):
    return "{} menu available from {}am to {}pm".format(self.name, self.start_time, self.end_time)
  
  # Giving Menu a method calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items. Calculate_bill will return the total price of a purchase consisting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    bill = 0 # how much they owe us
    for purchased_item in purchased_items:
      if purchased_item in self.items: # to make sure the item is in the menu
        bill += self.items[purchased_item]
    return bill

# Restaurant has decided to create more than one restaurant to offer their food. Creating a class Franchise. Giving the Franchise class a constructor. Taking in an address and assigning it to self.address. Also taking in a list of menus and assigning it to self.menus.
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

# Giving the Franchises a string representation so that we’ll be able to tell them apart. Printing out a Franchise it should tell us the address of the restaurant.
  def __repr__(self):
    return self.address

# Telling the customers what they can order. Giving Franchise an available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
  def available_menus(self, time):
    available_menus = [] # finally returning the array of available menus on time
    for menu in self.menus: 
      if time >= menu.start_time and time<=menu.end_time:
        available_menus.append(menu)

    return available_menus

# Going to create a restaurant that sells arepas. Defining a Business class. Giving Business a constructor. A Business needs a name and a list of franchises.
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Creating the first menu "brunch" and it items. Brunch is served from 11am to 4pm. 
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50,
}
brunch = Menu("brunch", brunch_items, 1100, 1600)
#print(brunch.name)
# testing:
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Creating the second menu "early_bird" and it items. Early-bird Dinners are served from 3pm to 6pm.
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'coffee': 1.50, 'mushroom ravioli (vegan)': 13.50, 'coffe': 1.50, 'espresso': 3.00
}
early_bird = Menu("early_bird", early_bird_items, 1500, 1800)
#print(early_bird.name)
# testing:
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating the third menu "dinner" and its items. Dinner is served from 5pm to 11pm. 
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'coffee': 1.50, 'mushroom ravioli (vegan)': 13.50, 'coffe': 2.00, 'espresso': 3.00
}
dinner = Menu("dinner", dinner_items, 1700, 2300)
#print(dinner.name)

# Creating the last menu "kids" and its items. The kids menu is available from 11am until 9pm. 
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", kids_items, 1100, 2100)
#print(kids.name)

print(brunch)

# Creating the first two franchises. Flagship store is located at "1232 West End Road" and new installment is located at "12 East Mulberry Street". Passing in all four menus along with these addresses to define flagship_store and new_installment.
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# Creating the first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Before creating the new business, will need a Franchise and before Franchise will need a menu. The items for Take a’ Arepa available from 10am until 8pm are the following. Saving this to a variable called arepas_menu.
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

# Creating the first Take a’ Arepa franchise. The new restaurant is located at "189 Fitzgerald Avenue". Saving the Franchise object to a variable called arepas_place.
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Creating the new Business. The business is called "Take a' Arepa". 
arepa = Business("Take a' Arepa", [arepas_place])

# testing:
print(flagship_store)
# Testing out available_menus() method. Calling it with 12 noon as an argument and printing out the results.
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# testing arepas:
print(arepa.franchises[0].menus[0])