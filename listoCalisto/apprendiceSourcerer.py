#Write your function here

def append_size(lst):
  append_len = len(lst)
  print(lst.append(append_len))
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here

def every_three_nums(start):
#the hard way
  '''if start < 100:
    list_to_hundred = list(range(start, 101, 3))
    return list_to_hundred
  else:
    list_to_hundred = []
    return list_to_hundred'''
#the cool way
  return list(range(start, 10001, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
