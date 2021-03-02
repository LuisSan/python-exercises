all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", 
"Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0
while index < 6:
  students_in_poetry.append(all_students.pop())
  index += 1
  print(students_in_poetry)
