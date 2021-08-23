# importing modules
import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14),
                              ["Spade (\U00002660)", "Heart(\U00002665)", "Diamond (\U00002666)", "Club (\U00002663)"]))

# Shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got: ")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
