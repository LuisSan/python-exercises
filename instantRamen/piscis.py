# >_ ..introvert/piscis.py
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return(c_temp)

f100_in_celsius = f_to_c(35)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (5/9) + 32
  return(f_temp)

# >_ ..introvert/piscis.py
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return(c_temp)

f100_in_celsius = f_to_c(35)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (5/9) + 32
  return(f_temp)

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)
