from player import Player
from deck import Deck
from stage import Stage, formatCard

class Board:
  def __init__(self, numPlayers, strategyMap, printDetail):
    self.stages = [1,2,3,4,5]
    self.hazardsRemoved = []
    self.players = []
    self.numPlayers = numPlayers
    self.deck = Deck()
    self.strategyMap = strategyMap
    self.printDetail = printDetail
    self.hazardsRemoved = []
  
  def initPlayers(self, numPlayers):
    for i in range(1,numPlayers+1):
      player = Player('Player' + str(i))
      self.players.append(player)
  
  def stage1(self):
    self.initPlayers(self.numPlayers)
    self.deck.shuffle()
    stage1 = Stage(self.deck, self.players, self.printDetail, self.hazardsRemoved)
    self.hazardsRemoved = stage1.runStage(self.deck, self.strategyMap)
    # print(list(map(formatCard,self.hazardsRemoved)))
    return self.deck
  
  def stage2(self):
    for player in self.players:
      player.respawn()
    self.deck.shuffle()
    self.deck.cards += [70]
    stage2 = Stage(self.deck, self.players, self.printDetail, self.hazardsRemoved)
    self.hazardsRemoved = stage2.runStage(self.deck, self.strategyMap)
    return self.deck
  
  def stage3(self):
    for player in self.players:
      player.respawn()
    self.deck.shuffle()
    self.deck.cards += [80]
    stage3 = Stage(self.deck, self.players, self.printDetail, self.hazardsRemoved)
    self.hazardsRemoved = stage3.runStage(self.deck, self.strategyMap)
    return self.deck
  
  def stage4(self):
    for player in self.players:
      player.respawn()
    self.deck.shuffle()
    self.deck.cards += [100]
    stage4 = Stage(self.deck, self.players, self.printDetail, self.hazardsRemoved)
    self.hazardsRemoved = stage4.runStage(self.deck, self.strategyMap)
    return self.deck
  
  def stage5(self):
    for player in self.players:
      player.respawn()
    self.deck.shuffle()
    self.deck.cards += [120]
    stage5 = Stage(self.deck, self.players, self.printDetail, self.hazardsRemoved)
    self.hazardsRemoved = stage5.runStage(self.deck, self.strategyMap)
    if (self.printDetail):
      print("Removed Hazards: ", list(map(formatCard,self.hazardsRemoved)))
    return self.deck