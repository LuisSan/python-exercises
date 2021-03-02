from utils import print_message, get_size, get_drink_type, order_latte, order_mocha

def coffee_bot():
  print('Welcome to the cafe Sepoy!')

  order_drink = 'y'
  drinks = []
  while order_drink == 'y':
    size = get_size()
    drink_type = get_drink_type()
    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      order_drink = input('Would you like to order another drink? (y/n)\n')
      if order_drink in ['y', 'n']:
        break
    print('Okay, so I have:\n')

    for drink in drinks:
      print('-{}'.format(drink))

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your {} will be ready shortly.'.format(name, drink_type))

coffee_bot()

### Improvements:
#[] Add an additional type of drink or an additional option to an existing drink
#[] Allow the chatbot to recognize additional inputs besides 'y' and 'n' – such as 'yes', 'sure', or 'nah' – when it asks the user if they would like another drink
#[] Allow the chatbot to recognize key exit words such as 'stop' or 'bye' that can terminate the order at any step
#[X] Break down the main code so allt the functions are in the utils
