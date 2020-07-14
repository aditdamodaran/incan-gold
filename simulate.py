import random
from board import Board
from strategy import *

# NUMBER OF STRATEGIES BE AT LEAST AS LONG AS THE
# NUMBER OF PLAYERS
numberOfPlayers = 4
strategyMap = {
  "Player1": leaveAfterTwoHazards,
  "Player2": leaveAfterEightPoints,
  "Player3": leaveAfterTwoHazards,
  "Player4": leaveAfterFivePoints,
  "Player5": leaveAfterFivePoints,
  "Player6": leaveAfterFivePoints,
  "Player7": leaveAfterFivePoints,
  "Player8": leaveAfterFivePoints,
}


# RUN GAME
game = Board(numberOfPlayers, strategyMap)
updatedDeck = game.stage1()
updatedDeck = game.stage2()
updatedDeck = game.stage3()
updatedDeck = game.stage4()
updatedDeck = game.stage5()

# PRINT FINAL RESULTS
for player in game.players:
  print(player.name, "has: ",sum(player.tent))


