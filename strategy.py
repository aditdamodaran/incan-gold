# This strategy performed the best out of 
# (leaveAfterEight, leaveAfterTwoHazards),
# in 10000 games with four players, winning
# 47.9% of the time
def leaveAfterFivePoints(player, stage):
  if (player.treasure >= 5):
    return True
  else:
    return False

# This strategy performs well if
# no one else does it
def leaveAfterTwoHazards(player, stage):
  if(len(stage.hazards)==2 and player.treasure > 0):
    return True
  else:
    return False

# Loses to leaveAfterTwoHazards consistently
def leaveAfterThreeHazards(player, stage):
  if(len(stage.hazards)==3 and player.treasure > 0):
    return True
  else:
    return False

# This strategy performs reasonably well
# winning about 50% of the time against
# (leaveAfterFive)
def leaveAfterEightPoints(player, stage):
  if (player.treasure >= 8):
    return True
  else:
    return False

def calcTreasureRemaining(cards):
  total = 0
  for card in cards:
    if card > 0:
      if card > 20:
        total += (card/10)
      else:
        total += card
  return total

def calcExpectedReturn(player, stage):
  numHazards = len(stage.hazards)
  numCardsRemaining = len(stage.deck.cards)
  totalTreasureRemaining = calcTreasureRemaining(stage.deck.cards)
  removedHazards = stage.removedHazards
  # UNFINISHED


def goBigOrGoHome(player, stage):
  if (player.treasure >= 10 and stage.numPlayers*stage.remainder > 6):
    return True
  elif (player.treasure >= 8 and len(stage.hazards) > 1):
    return True
  else:
    return False