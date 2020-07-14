class Player:
  def __init__(self, name):
    self.name = name
    self.tent = []
    self.token = 1
    self.treasure = 0
    self.left = 0
  
  # Player drops their token to leave
  def leave(self):
    self.token = 0
  
  def respawn(self):
    self.token = 1
    self.treasure = 0
    self.left = 0
  
  def strategy(self, stage, strategyMap):
    # print(self.treasure, stage.remainder)
    # Decide whether to leave or stay (Boolean)
    leave = strategyMap[self.name](self, stage)
    if (leave):
      self.leave()
    else:
      return


player = Player('Player1')
player.strategy