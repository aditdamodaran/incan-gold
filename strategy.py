def leaveAfterFivePoints(player, stage):
  if (player.treasure >= 5):
    return True
  else:
    return False

def leaveAfterTwoHazards(player, stage):
  if(len(stage.hazards)==2 and player.treasure > 0):
    return True
  else:
    return False

def leaveAfterEightPoints(player, stage):
  if (player.treasure >= 8):
    return True
  else:
    return False