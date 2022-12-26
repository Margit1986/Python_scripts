# import codecademylib3_seaborn

# Below import codecademylib3_seaborn, import pyplot from the module matplotlib with the alias plt.
from matplotlib import pyplot as plt
# Import random 
import random
# Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive).
numbers_a = range(1,13)
# Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).
numbers_b = random.sample(range(1000), 12)
print(numbers_b)
# Now let’s plot these number sets against each other using plt. Call plt.plot() with your two variables as its arguments.
plt.plot(numbers_a, numbers_b)
# Now call plt.show() and run your code! You should see a graph of random numbers displayed. You’ve used two Python modules to accomplish this (random and matplotlib).
plt.show()

