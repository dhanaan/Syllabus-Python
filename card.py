import random

class Card:
    def __init__(self, suit: str, rank: int):
        self.suit = suit
        self.rank = rank

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


class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else []

    @classmethod
    def standard_deck(cls):
        deck = cls()

        for suit in ['spade', 'heart', 'diamond', 'club']:
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

