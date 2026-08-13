import random
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Card:
    suit: str
    rank: int

    SUIT: ClassVar[list] = ['spade', 'heart', 'diamond', 'club']

    def __str__(self):
        suit_emoji = {
            'spade': '♠️',
            'heart': '♥️',
            'diamond': '♦️',
            'club': '♣️',
            '?': '?'
        }

        rank_alias = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }

        suit = suit_emoji.get(self.suit, '?')
        rank = rank_alias.get(self.rank, self.rank)
        return f'{suit}  {rank}'

@dataclass
class Deck:
    cards: list = field(default_factory=list)

    @classmethod
    def standard_deck(cls):
        deck = cls()

        for suit in Card.SUIT:
            for rank in range(1, 14):
                deck.add(Card(suit, rank))

        return deck

    def add(self, card):
        if card is not None:
            self.cards.append(card)

    def take(self, idx=-1):
        return self.cards.pop(idx)

    @property
    def top(self):
        return self.cards[-1]

    def get(self, idx):
        if 0 <= idx < len(self.cards):
            return self.cards[idx]

        return None

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return " ".join(str(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)

