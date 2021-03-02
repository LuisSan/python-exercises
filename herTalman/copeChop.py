# Define your functions

def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  print('Alright that\'s a {} {}!'.format(size, drink_type))
  name = input('Can I get your name please?')
  print('Thanks, {}! Your {} will be ready shortly.'.format(name, drink_type))

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a' or res == 'A':
    return 'latte'
  elif res == 'b' or res == 'B':
    return 'non-fat latte'
  elif res == 'c' or res == 'C':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
# Call coffee_bot()!
  if res == 'a' or res == 'A':
    return 'small'
  elif res == 'b' or res == 'B':
    return 'medium'
  elif res == 'c' or res == 'C':
    return 'large'
  else:
    #return 'Something went wrong...'
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a' or res == 'A':
    return 'brewed coffee'
  elif res == 'b' or res == 'B':
    return 'mocha'
  elif res == 'c' or res == 'C':
    return order_latte()
  else:
    print_message()
    #return get_drink_type()

coffee_bot()

'''Try adding some additional functionality to the chatbot. For example, how can we ask the user if they would like a plastic cup or to use
their own reusable cup? How about if they’d like their drink hot or iced? Or maybe if they’d want to order an additional drink?
Feel free to get creative!'''
