# Write your max_key function here:

def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

##---

# Write your word_length_dictionary function here:

def word_length_dictionary(words):
  lanagramaDelRey =  {}
  for word in words:
    lanagramaDelRey[word] = len(word)
  return lanagramaDelRey

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
print(word_length_dictionary(["You", "are", "my", "everything", "!"]))

##---- EOF
