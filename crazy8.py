import take_input as inp
import random
import time
from abc import ABC, abstractmethod
from card import Card, Deck

class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.hand = Deck()

    @abstractmethod
    def choose_card(self, top: Card, draw_pile: Deck):
        pass

    def draw_card(self, deck: Deck):
        self.hand.add(deck.take())

    def play_card(self, index: int):
        return self.hand.take(index)

    def __str__(self):
        return f'{self.name} hand is:\n{self.hand}'

    def is_win(self):
        return len(self.hand) == 0

    def is_playable(self, top: Card, chosen: Card):
        if chosen is not None:
            return chosen.suit == top.suit or chosen.rank == top.rank or chosen.rank == 8

        return False

    def get_playable_cards(self, top: Card):
        return [card for card in self.hand.cards if self.is_playable(top, card)]

class Human(Player):
    def choose_card(self, top: Card, draw_pile: Deck):
        print(self)
        if self.get_playable_cards(top):
            card_index = int(inp.take_input(f"{self.name}, choose a card (1-{len(self.hand)}): ", rule_error="That card is unplayable, it has a different suit and rank compared to the top card", rule=lambda x: 0 < int(x) <= len(self.hand) and self.is_playable(top, self.hand.get(int(x) - 1)))) - 1
            card = self.play_card(card_index)
            if card.rank == 8:
                suit_change = inp.take_input("Crazy 8!\nchoose the suit: ", choices=['spade', 'heart', 'diamond', 'club'])
                return [card, Card(suit=suit_change, rank=8)]
            else:
                print(f"{self.name} plays {card}")
            return card

        # No playable cards
        print(f"{self.name} has no playable cards")
        self.draw_card(draw_pile)
        drawn_card = self.hand.top

        if self.is_playable(top, drawn_card):
            card = self.hand.take()
            print(f"{self.name} draws and plays {card}")
            self.warn_user()
            return card

        print(f"{self.name} draw, but cannot play the drawn card [{drawn_card}]")
        self.warn_user()
        return None
    
    @staticmethod
    def warn_user(msg = "\nEnter to continue: "):
        inp.take_input(msg)


class Bot(Player):
    def __init__(self, name, log=False):
        super().__init__(name)
        self.log = log

    def choose_card(self, top: Card, draw_pile: Deck):
        if self.log:
            print(self)
        playable_cards = self.get_playable_cards(top)

        if playable_cards:
            chosen_card = random.choice(playable_cards)
            card_index = self.hand.cards.index(chosen_card)
            card = self.play_card(card_index)
            print(f"{self.name} plays {card}")
            return card

        print(f"{self.name} has no playable cards")
        self.draw_card(draw_pile)
        drawn_card = self.hand.top

        if self.is_playable(top, drawn_card):
            card = self.hand.take()
            print(f"{self.name} draws and plays {card}")
            return card

        print(f"{self.name} draw {drawn_card if self.log else ""} but cannot play the drawn card")
        return None


class Game:
    def __init__(self, players, cards_per_player=5, pause_duration=0.5):
        self.pause_duration = pause_duration
        self.cards_per_player = cards_per_player
        self.players = players
        self.draw_pile = Deck.standard_deck()
        self.discard_pile = Deck()
        self.turn = 0
        self.suit_change = None

    def setup(self):
        self.draw_pile.shuffle()

        for _ in range(self.cards_per_player):
            for player in self.players:
                player.draw_card(self.draw_pile)

        self.discard_pile.add(self.draw_pile.take())

    def next_turn(self):
        self.turn = (self.turn + 1 if self.turn < len(self.players) - 1 else 0)

    def run(self):
        self.setup()

        while True:
            player = self.players[self.turn]
            if self.suit_change is not None:
                top_card = Card(suit=self.suit_change, rank=8)
            else:
                top_card = self.discard_pile.top

            print(f"TOP [{top_card}]")
            time.sleep(self.pause_duration)
            played_card = player.choose_card(top_card, self.draw_pile)
            print("===========================")
            if played_card is not None:
                if isinstance(played_card, list):
                    for card in range(len(played_card)-1):
                        self.discard_pile.add(played_card[card])
                    if played_card[-1].rank == 8:
                        self.suit_change = played_card[-1].suit
                    else:
                        self.discard_pile.add(played_card[-1])
                else:
                    self.discard_pile.add(played_card)
                    self.suit_change = None


            if player.is_win():
                print(f"\n {player.name} wins!")
                break

            self.next_turn()
            time.sleep(self.pause_duration)


def main():
    players = [
        Human("Player"),
        Bot("Alex",log=True),
        Bot("Bale", log=True)
    ]

    game = Game(players, cards_per_player = 5, pause_duration = 1)
    game.run()


if __name__ == '__main__':
    main()