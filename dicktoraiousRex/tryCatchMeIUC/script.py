caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

key_to_check = "matcha"

caffeine_level["matcha"] = 30

try:
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")
