import math

def formatCard(card):
  if card == (-1):
    return 'Mummy Girl'
  elif card == (-2):
    return 'Fire'
  elif card == (-3):
    return 'Rocks'
  elif card == (-4):
    return 'Spiders'
  elif card == (-5):
    return 'Snakes'
  elif card == (50):
    return 'Artifact (5)'
  elif card == (70):
    return 'Artifact (7)'
  elif card == (80):
    return 'Artifact (8)'
  elif card == (100):
    return 'Artifact (10)'
  elif card == (120):
    return 'Artifact (12)'
  else: 
    return card

class Stage:
  def __init__(self, deck, players):
    self.hazards = []
    self.treasure = []
    self.players = players
    self.numPlayers = len(self.players)
    self.endedByHazards = False
    self.deck = deck
    self.drawnCards = []
    self.remainder = 0
    self.playersLeaving = []
    self.artifactsAvailable = False
    self.artifacts = []
  
  def addHazard(self, hazard):
    self.hazards = self.hazards + [hazard]
   
  
  def turn(self, deck):
    # Draw a Card from the Deck
    card = deck.draw()
    print(formatCard(card))
    self.drawnCards.append(card)

    # Check if it's a hazard (and would end the round)
    if (card < 0):
      if card in self.hazards:
        self.endedByHazards = True 
      self.addHazard(card)
    # Check if it's an artifact (and thus would not be divied up)
    elif (card > 20):
      self.artifactsAvailable = True
      artifactValue = int(card / 10)
      self.artifacts.append(artifactValue)
      return
    else:
      # Else divy up the treasure
      shareOfTreasure = math.floor(card/self.numPlayers)
      for i in range(0, len(self.players)):
        self.players[i].treasure += shareOfTreasure
      remainder = card%self.numPlayers
      self.remainder += remainder
      # print(shareOfTreasure, remainder)
  
  def runStage(self, deck, strategyMap):
    print(deck.cards)
    
    while (self.numPlayers != 0) and (not self.endedByHazards):
      # Draw from the deck, and appropriate points accordingly
      self.turn(self.deck)

      # Leave or Stay
      for i, player in enumerate(self.players):
        player.strategy(self, strategyMap)
        # IF PLAYER STRATEGY CHOOSES TO LEAVE
        if (player.token == 0 and player.left == 0):
          self.playersLeaving.append(i)
          player.left = 1
          # PUT ACCUMULATED TREASURE IN TENT (DOESN'T INCLUDE REMAINDER OR ARTIFACT)
          self.players[i].tent.append(player.treasure)
      
      # Update the Number of Remaining Players
      # Handle Artifacts and Remainders
      if (self.playersLeaving):
        print(self.playersLeaving, "are leaving")
        self.numPlayers -= len(self.playersLeaving)
      
      # Divy up the remaining treasure for those leaving
      numLeaving = len(self.playersLeaving)

      # If a player leaves on their own
      if numLeaving == 1:
        # print("One Player is leaving. The remainder is", self.remainder)
        idx = self.playersLeaving[0]
        # They get all the remaining treasure on the board
        self.players[idx].tent.append(self.remainder)
        # And all the artifacts
        if (self.artifactsAvailable):
          self.players[idx].tent.append(sum(self.artifacts))
          self.artifactsAvailable = False
          for artifact in self.artifacts:
            value = artifact*10
            self.drawnCards.remove(value)
          self.artifacts = []
        self.remainder = 0
      if numLeaving > 1:
        share = math.floor(self.remainder/numLeaving)
        # print(numLeaving,"players are leaving. They each get", share)
        for idx in self.playersLeaving:
          self.players[idx].tent.append(share)
        self.remainder = self.remainder - (share*numLeaving)

      self.playersLeaving = []
    
    
    self.deck.cards = self.deck.cards + (self.drawnCards)
    # If ended by hazards:
    # Players lose accumulated treasure (unless they've left)
    # Hazard is removed from the deck for future rounds
    if (self.endedByHazards):
      hazardToRemove = self.hazards[-1]
      self.deck.remove(hazardToRemove)

    for player in self.players:
      print(player.name, player.tent)
  
    
    