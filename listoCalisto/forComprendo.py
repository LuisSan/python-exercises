heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)

print(usernames)

usernames = [word for word in words if word[0] == '@']

#Note the use of round in the list comprenhension. Otherwise you get an TypeError:
#"TypeError: type list doesn't define __round__ method"

usernames = [word for word in words]

celsius = [0, 10, 15, 32, -5, 27, 3, -34]

fahrenheit = [round(f * 9/5 +32) for f in celsius]

print(fahrenheit)

#For loop of one and only list
#comprenhension list on that list

single_digits = range(0, 10)

squares = []

for single in single_digits:
  print(single)
  squares.append(single ** 2)
print(squares)

cubes = [cube ** 3 for cube in single_digits]

print(cubes)
