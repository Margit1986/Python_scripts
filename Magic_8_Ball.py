#Codecademy homework: Magic 8-Ball. 
#The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.Write a magic8.py Python program that can answer any Yes or No question with a different fortune each time it executes.
import random #importing random module so we can use its functions like .randint().

name = "Iku"
question = "Am i surrounded by idiots?"
answer = "" #storing the answer of the Magic 8-Ball in this variable

#In order for the answer to be different each time when running the program, I will utilize randomly generated values.
random_number = random.randint(1, 9) #creating a variable to store the randomly generated value which will generate a random number between 1 (inclusive) and 9 (inclusive).
#print(random_number)

#utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value:
if random_number==1:
  answer = "Yes - definitely."
elif random_number==2:
  answer = "It is decidedly so."
elif random_number==3:
  answer = "Without a doubt."
elif random_number==4:
  answer = "Reply hazy, try again."
elif random_number==5:
  answer = "Ask again later."
elif random_number==6:
  answer = "Better not tell you now."
elif random_number==7:
  answer = "My sources say no."
elif random_number==8:
  answer = "Outlook not so good."
elif random_number==9:
  answer ="Very doubtful."
else: 
 print("Error")

#statement to output the asker’s name and their question:
print(name + " asks: " +question)
#statement that will output the Magic 8-Ball’s answer:
print("Magic 8-Ball's answer: " +answer)
