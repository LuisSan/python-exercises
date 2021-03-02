#simple parameter

def mult_two_add_three(number):
  print(number*2 + 3)

# Call mult_two_add_three() here:
mult_two_add_three(0)

def mult_x_add_y(number, x, y):
  print(number* x + y)

mult_x_add_y(1, 3 , 1)

#Default parameter vs keyword argument

# Define create_spreadsheet():
def create_spreadsheet(title, row_count=10):
  print("Creating a spreadsheet called " + title + "with " +  str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications ")

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
my_age = calculate_age(2049, 1993)

dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age)  + " years old ")
