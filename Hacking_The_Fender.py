# Codecademy homework (dec 2022): Hacking The Fender. 
# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat. Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

# Reading In The Passwords. Writting a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv". 
# First importing the CSV module, because need it to parse the data. Then need to create a list of users whose passwords have been compromised, creating a new list and saving it to the variable compromised_users.
import csv 
compromised_users = []

# Opening the file passwords.csv and storing it in a file object called password_file. Passing the password_file object holder to  CSV reader for parsing. Saving the parsed csv.DictReader object as password_csv. Then iterating through each of the lines in the CSV. Creating a for loop and adding each username to the list of compromised_users. 
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    print(row['Username'])
    compromised_users.append(row['Username'])

print("--------------")

# Opening a file called compromised_users.txt (in write-mode), saving the file object as compromised_user_file. Iterating over each of the compromised_users. Writing the username of each compromised_user in compromised_users to compromised_user_file
with open('compromised_users.txt', 'w') as compromised_user_file:
  for users in compromised_users:
    compromised_user_file.write(users)

# Notifying the Boss. Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.

# Importing the json module. Opening a new JSON file in write-mode called boss_message.json. Saving the file object to the variable boss_message. Creating a Python dictionary object, calling this boss_message_dict. Giving it a "recipient" key with a value "The Boss" and "message" key with the value "Mission Success". Writing out boss_message_dict to boss_message using json.dump().
import json
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss", 
    "message": "Mission Success"
    }
  json.dump(boss_message_dict, boss_message)

with open("boss_message.json") as read_json:
    message = json.load(read_json)
print(message)

# Scrambling the Password. Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
# Creating a new with block and opening "new_passwords.csv" in write-mode. Saving the file object to a variable called new_passwords_obj. Saving a multiline string to the variable slash_null_sig. Writing slash_null_sig to new_passwords_obj. Now there is a file to replace passwords.csv with. 
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   ___  __    __   __   
 / __)/  \  /  \ (  )  
( (__(  O )(  O )/ (_/\
 \___)\__/  \__/ \____/

  """
  output = csv.DictWriter(new_passwords_obj, fieldnames=slash_null_sig)
