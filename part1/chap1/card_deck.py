from collections import namedtuple 
from dataclasses import dataclass

# How to create a new representation for cards? 
# Method 1: define like a regular class; but this is mutable and not 
# preferred for card class as each card is supposed to be immutable

# class Card: 
# 	def __init__(self, rank, suit): 
# 		self.rank = rank
# 		self.suit = suit
# 
# 	def __repr__(self): 
# 		return repr((self.rank, self.suit))
# 
# Method 2: define the Card class as a namedtuple and given that namedtupled are 
# immutable and hence Card is also mutable. Unfortunately, we don't have the desired representation.
  
# Card = namedtuple('Card', ['rank', 'suit'])

# Method 3: define the Card class as a derived class for namedtuple. This works. 
class Card(namedtuple('Card', ['rank', 'suit'])):
      def __repr__(self):
          return repr((self.rank, self.suit))


# Method 4: define the Card class using dataclass(frozen=True). This also works.
# @dataclass(frozen=True)
# class Card: 
# 	rank: str
# 	suit: str
# 	def __repr__(self): 
# 		return repr((self.rank, self.suit))
# 

class FrenchDeck: 
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()
	suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)	

	def __init__(self): 
		self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
		
	def __len__(self): 
		return len(self._cards)

	def __getitem__(self, position): 
		return self._cards[position]
			
	def spades_high(self, card): 
		rank_value = self.ranks.index(card.rank)
		return rank_value * len(self.suit_values) + self.suit_values[card.suit]


print(FrenchDeck.ranks[0])      			# Able to access ranks class attribute - even initialization is not needed. 

deck = FrenchDeck()
print(deck.spades_high(list(reversed(deck))[0]))	# can reverse deck and access the elements because we have defined __getitem__, which is called for element access
print(deck[3])						# able to access elements. 



# Chapter Notes: 
# When len is called in python, it doesn't actually calculate object count, rather just reads a variable called ob_size 
# stored in C. python is interpreted using a cpython interpreter. 




