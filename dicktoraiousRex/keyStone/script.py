zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", 
"Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", 
"Aquarius"]}

print(zodiac_elements["earth"])

print(zodiac_elements["fire"])

print(zodiac_elements["water"])

print(zodiac_elements["air"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo","Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

##Unpacking and packing dictionaries

for score_list in test_scores.values():
  print(score_list)

print(list(test_scores))
print(list(test_scores.values()))
print(list(zip(test_scores, test_scores.values())))
