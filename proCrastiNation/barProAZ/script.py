letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {alpha:number for alpha,number in zip(letters, points)}

letter_to_points[" "] = 0

#.get() takes the value out of a dictionary pair
print(letter_to_points.get("A"))

#print(letter_to_points)

def score_word(word):
  point_total = 0
  for char in word:
    if char in word:
      point_total += letter_to_points.get(char)
    else:
      point_total += letter_to_points.get(char, 0)
  return point_total

'''TESTING
brownie_points = score_word("BROWNIE")

print(brownie_points)
'''

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT", "BULL"], "wordNerd": ["EARTH", "EYES", "MACHINE", "XMAS"], "Lexi Con": ["ERASER", "BELLY","HUSKY", "JUICE"], "Reader": ["ZAP", "COMA", "PERICO", "SODA"]}

print(player_to_words)

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

'''
ROOM FY IMPOROVEMENTS
[ ] play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
[ ] update_point_totals() — turn your nested loops into a function that you can call any time a word is played
[ ] make your letter_to_points dictionary able to handle lowercase inputs as wel
'''

