# Codecademy homework (nov 2022): Getting Ready for Physics Class. You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

# previously defined values:
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# writing function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# creating variable f100_in_celsius and setting it equal to the value of f_to_c with 100 as an input.
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# writing a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit:
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# testing the function with a value of 0 Celsius. creating a variable c0_in_fahrenheit and setting it equal to the value of c_to_f with 0 as an input:
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# defining a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.
def get_force(mass, acceleration):
  mass = mass * acceleration
  return mass

# testing the get_force by calling it with the variables train_mass and train_acceleration. saving the result to a variable called train_force and printing it out.
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print("The GE train supplies", train_force, "Newtons of force")

# defining a function called get_energy that takes in mass and c. C is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Setting c to have a default value of 3*10**8:
def get_energy(mass,c=3*10**8):
  mass = mass * c
  return mass

# testing get_energy by using it on bomb_mass, with the default value of c. saving the result to a variable called bomb_energy:
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules")

# defining a function called get_work that takes in mass, acceleration, and distance. Work is defined as force multiplied by distance. First, getting the force using get_force, then multiplying that by distance. 
def get_work(mass,acceleration,distance):
  work = get_force(mass,acceleration) * distance
  return work

# testing get_work by using it on train_mass, train_acceleration, and train_distance. saving the result to a variable called train_work.
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
