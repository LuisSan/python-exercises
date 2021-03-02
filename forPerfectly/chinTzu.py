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

#--- Fyu repetition
# Write your sum_even_keys function here:

def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary[key]
  return(total)

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#--- fyu integration

# Write your add_ten function here:

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return (my_dictionary)
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#--- fuy gratification

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
      if value in my_dictionary:
        value_keys.append(value)
  return value_keys
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
