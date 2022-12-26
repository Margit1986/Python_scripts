# Codecademy homework (detc 2022): Scrabble. In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points. You have been provided you with two lists, letters and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using a list comprehension and zip, creating a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {key: value for key, value in zip(letters, points)}
#print(letter_to_points)

# Adding an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0
print(letter_to_points)
print("-----------")

# Creating a function that will take in a word and return how many points that word is worth. Defining a function called score_word that takes in a parameter word. Inside score_word, creating a variable called point_total and set it to 0. Create a for loop that goes through the letters in word and adds the point value of each letter to point_total. Will be getting the point value from the letter_to_points dictionary. If the letter is not in letter_to_points, adding 0 to the point_total.
def score_word(word):
  point_total = 0
  for letters in word: 
    point_total += letter_to_points.get(letters, 0)
  return point_total

# Creating a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE". The word BROWNIE will earn 15 points. 
brownie_points = score_word("BROWNIE")
print(brownie_points)
print("-----------")

# Creating a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary: player1" = "BLUE", "TENNIS", "EXIT"; "wordNerd" = ""EARTH", "EYES", "MACHINE"; "Lexi Con" = "ERASER", "BELLY", "HUSKY"; "Prof Reader" = "ZAP", "COMA", "PERIOD".
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}



# Creating an empty dictionary called player_to_points.
player_to_points = {}

# Iterating through the items in player_to_words. Call each player player and each list of words words. Within the loop, creating a variable called player_points and setting it to 0. Within the loop, creating another loop that goes through each word in words and adds the value of score_word() with word as an input. After the inner loop ends, setting the current player value to be a key of player_to_points, with a value of player_points.
for player, words in player_to_words.items():
  player_points = 0
  for word in words: 
    player_points += score_word(word)
  player_to_points[player] = player_points #

# Printing player_to_points out to see the current standings for this game. wordNerd is winning by 1 point.
print(player_to_points)

