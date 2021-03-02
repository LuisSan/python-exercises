dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
#  print(list(dog)) #Print every item in list as a list i.e. ['d', 'a', 'l', 'm', 'a', 't', 'i', 'a', 'n']
  print(dog)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print('They have the dog I want!')
    break #use of the keyword break

#use of the keyword continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age < 21:
   continue
  print(age)

# For loop _a continuation

# Write your sum_values function here:

'''
def greater_than_ten(my_dictionary, number):
  count = 0
  for value in my_dictionary.values():
    if value > number:
      count += 1
  return count
'''

def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
