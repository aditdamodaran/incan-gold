# Incan Gold Game Simulator

[Incan Gold](https://en.wikipedia.org/wiki/Diamant_(board_game)) is a simple card game featuring 3-8 players. The game has 5 stages. In each stage, cards are drawn from a shuffled deck. The deck contains:

* 15 hazard cards (3 of each of the 5 hazards)
* 15 treasure cards (with point values of 1,2,3,4,5,5,7,7,9,11,11,13,14,15,17)
* 5 artifacts (with point values of 5,7,8,10,12), each inserted into the deck at the respective stage.
  * Stage 1: all 15 hazards, 15 treasures, and the 5 point artifact

Players have the option to "stay" or "leave" following each draw from the deck.

* If a treasure card is drawn, the treasure is split evenly among those players remaining in the game. If an odd number of treasure appears, the remainder is left on the board. (i.e. if there are 3 players remaining and an 11 is drawn, each player gets 3 points and 2 points remain on the board)

* If two hazard cards are drawn the stage ends, and any remaining players lose all accumulated treasure. One of the three hazard cards for the hazard that ended the stage is removed from the deck. 
* If a player leaves before two hazards are drawn, they keep whatever treasure they have accumulated in the game, plus their share of whatever treasure remains on the board. So if two players leave at the same time, they take their treasure and split that which remains on the board.
* If all players have left, the stage ends.
* If an artifact card is drawn, a player must leave alone to claim its points. If two players leave when an artifact card is on the board, neither obtain it.



When the stage ends, players put their accumulated treasure points into their tents. An artifact card is inserted into the deck. If a hazard ended the stage, one of its three cards is removed from the deck. The deck is reshuffled and the following round begins.







