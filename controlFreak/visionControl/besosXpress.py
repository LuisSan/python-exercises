#Jeff Besos Xpress Bud

weight = 4.8

#Ground Shipping
cost = weight * 4.45 + 20
if weight <= 2:
  cost = weight * 1.50 + 20
  print("The cost with Ground is $ " + str(round(cost, 2)))
elif weight > 2 and weight <= 6:
  cost = weight * 3.0 + 20
  print("The cost with Ground is $ " + str(round(cost, 2)))
elif weight > 6 and weight <= 10:
  cost = weight * 4.0 + 20
  print("The cost with Ground is $ " + str(round(cost, 2)))
else:
  cost = weight * 4.75 + 20
  print("The cost with Ground is $ " + str(round(cost, 2)))

#Ground Shipping Premium
premium = 125

if premium and weight:
  print("The cost with Premium is $ " + str(round(premium)))

# Drone Shipping
#weight = 1.5

if weight <= 2:
  cost = weight * 4.50
  print("The cost with Drone is $ " + str(round(cost, 2)))
elif weight > 2 and weight <= 6:
  cost = weight * 9.0
  print("The cost with Drone is $ " + str(round(cost, 2)))
elif weight > 6 and weight <= 10:
  cost = weight * 12.0
  print("The cost with Drone is $ " + str(round(cost, 2)))
else:
  cost = weight * 14.25
  print("The cost with Drone is $ " + str(round(cost, 2)))
