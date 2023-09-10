#!/usr/bin/env python3

######################################################################
import random

message = "Hello World"
print(message)
SUIT_TUPLE = ('Spades','Hearts','Clubs','Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10',)
NCARDS     = 8

#Pass in a deck and this function return a random card from the deck
def getCard(deckListIn):
   thisCard = deckListIn.pop()
   return thisCard

#Pretty much self explanatory
def shuffle(deckListIn):
   deckListOut = deckListIn.copy()
   random.shuffle(deckListOut)
   return deckListOut

print("Weclome to Higher or Lower")
print("You have to choose whether the next card to be shown")
print("is higher or lower than the current card.")
print("Correctly guessing adds 20 point, incorrectly guessing loses")
print("15 points.\nYou have 50 points to start.\n\n")

startingDeckList = []
for suit in SUIT_TUPLE:
   for thisValue, rank in enumerate(RANK_TUPLE):
      cardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
      startingDeckList.append(cardDict)

score = 50

while True:
   print()
   gameDeckList = shuffle(startingDeckList)
   currentCardDict = getCard(gameDeckList)
   currentCardRank = currentCardDict['rank']
   currentCardValue = currentCardDict['value']
   currentCardSuit = currentCardDict['suit']
   print(currentCardRank+" of "+currentCardSuit)
   print(str(currentCardValue))
   print()
   for cardNumber in range(0,NCARDS):
      answer = input('Will the next card be higher (h) or lower (l)'+
                     ' than the '+currentCardRank+" of "+
                      currentCardSuit+"?")
      answer = answer.casefold()
      nextCardDict = getCard(gameDeckList)
      nextCardRank = nextCardDict['rank']
      nextCardSuit = nextCardDict['suit']
      nextCardValue= nextCardDict['value']

      if answer == 'h':
         if nextCardValue > currentCardValue:
            print("You guessed correct")
            score = score + 20
         else:
            print("You guessed incorrect")
            score = score - 15
      elif answer == 'l':
         if nextCardValue < currentCardValue:
            print("You guessed correct")
            score = score + 20
         else:
            print("You guessed incorrect")
            score = score - 15
      print("Your Score is: ",score)
      print()
      currentCardRank = nextCardRank
      currentCardValue = nextCardValue

   goAgain = input("Press 'q' to quit: ")
   if goAgain == 'q':
      break

print('Bye-Bye')

######################################################################
