print("TOTAL EXERCISES")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112,
"lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)

print(lessons)

for lesson in lessons:
  print(lesson)


for user in user_ids.keys():
  print(user)

##for-lopp for values in dictionary

print("NUMBER EXERCISES")

num_exercises = {"functions": 20, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for total in num_exercises.values():
  total_exercises += total

print(total_exercises)


##.items() method to get key and values in a tuple fashion

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")


##--------------

print("RELATION WOMAN-OCCUPATION")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percent in pct_women_in_occupation.items():
  print("*Women make up " + str(percent) + " percent of " + occupation +"s")

#-------------------

##Tarot

pinrt("TAROT")

tarot = { 1: "The Magician", 2:	"The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16: "The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for destiny, card in spread.items():
  print("Your " + destiny + " is the " + card + " card.")
