import random
from board import Board
from strategy import *
from statistics import mean 
import operator
from collections import Counter

# NUMBER OF STRATEGIES BE AT LEAST AS LONG AS THE
# NUMBER OF PLAYERS
numberOfPlayers = 4
strategyMap = {
  "Player1": goBigOrGoHome,
  "Player2": leaveAfterEightPoints,
  "Player3": leaveAfterTwoHazards,
  "Player4": leaveAfterFivePoints,
  # "Player5": leaveAfterFivePoints,
  # "Player6": leaveAfterFivePoints,
  # "Player7": leaveAfterFivePoints,
  # "Player8": leaveAfterFivePoints,
}
results = {
  "Player1": [],
  "Player2": [],
  "Player3": [],
  "Player4": []
}

winners = []

# array = [-1, 13, -2, 50, -2, 7, 5, 17, -5, -3, 3, -3, 4, 5, 7, 9, -5, -5, -1, 11, 2, -4, -2, 15, -3, -4, 1, -4, 14, -1, 11]

# numHazards = 0
# total = 0
# for card in array:
#   if card > 0:
#     if card > 20:
#       total += (card/10)
#     else:
#       total += card
#   else:
#     numHazards += 1

# # Total = total treasure remaining
# # numHazards = Number of Hazards Remaining
# # array = cards remaining

# print(total, numHazards, len(array))
# print("Chance of drawing a hazard: ", numHazards/len(array))
# print("Expected Value of Treasure Cards Remaining: ", total/(len(array)-numHazards))


def runGame(numberOfPlayers, strategyMap, times, results, printDetail):
  # RUN GAME
  for i in range(0, times):
    game = Board(numberOfPlayers, strategyMap, printDetail)
    updatedDeck = game.stage1()
    updatedDeck = game.stage2()
    updatedDeck = game.stage3()
    updatedDeck = game.stage4()
    updatedDeck = game.stage5()

    # GET FINAL RESULTS
    for player in game.players:
      # print(player.name, "has: ",sum(player.tent))
      score = sum(player.tent)
      results[player.name].append(score)
    
    # DETERMINE WHO WON (OR A TIE WIN)
    winner = max(results.keys(), key=(lambda k: results[k][i]))
    winners.append(winner)

def main(numberOfPlayers, strategyMap, times, results, printDetail, printIndividualGames):
  runGame(numberOfPlayers, strategyMap, times, results, printDetail)
  
  print("\n")

  if(printIndividualGames):
    for key in results:
      print(key, results[key])

  for key in results:
    print(key, "averaged", mean(results[key]),"in", str(times), "games, using", str(strategyMap[key].__name__))

  print('\nWIN COUNT: ')
  print(Counter(winners))
  print("\n")


main(numberOfPlayers, strategyMap, 10000, results, False, False)
