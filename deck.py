import random

class Deck:
  # The game starts off with:
  # 15 treasure cards 
  #     represented by their point values,
  # 15 hazards (3 for each type) 
  #     represented by negative numbers
  # 1 artifact (worth 5 points) in the deck
  def __init__(self):
    self.cards = [1,2,3,4,5,5,7,7,9,11,11,13,14,15,17] \
      + ([-1]*3) \
      + ([-2]*3) \
      + ([-3]*3) \
      + ([-4]*3) \
      + ([-5]*3) \
      + [50]
  
  # Shuffles the deck
  def shuffle(self):
    random.shuffle(self.cards)
  
  # Removes a card from the deck
  def remove(self, value):
    # print('removing')
    counter = 0
    for i, card in enumerate(self.cards):
      if (card == value and counter == 0):
        # print('popping', card)
        self.cards.pop(i)
        counter+=1
  
  # Draws a card
  def draw(self):
    drawn = self.cards[0]
    self.cards = self.cards[1:len(self.cards)]
    return drawn