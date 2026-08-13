import take_input as inp
import random, time
from abc import ABC, abstractmethod
from card import Card, Deck
from dataclasses import dataclass, field

@dataclass
class Player(ABC):
    name: str
    hand: Deck = field(default_factory=Deck)

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
            return self.resolve_play(card)

        # No playable cards
        print(f"{self.name} has no playable cards")
        self.draw_card(draw_pile)
        drawn_card = self.hand.top

        if self.is_playable(top, drawn_card):
            card = self.hand.take()
            result = self.resolve_play(card)
            self.warn_user()
            return result

        print(f"{self.name} draw, but cannot play the drawn card [{drawn_card}]")
        self.warn_user()
        return None
    
    @staticmethod
    def warn_user(msg = "\nEnter to continue: "):
        inp.take_input(msg)

    def resolve_play(self, card):
        if card.rank == 8:
            suit_active = inp.take_input("Crazy 8! choose the suit: ", choices=Card.SUIT)
            print(f"{self.name} plays {card} and active suit is now {suit_active}")
            return (card, Card(suit=suit_active, rank=8))
        
        print(f"{self.name} plays {card}")
        return card

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
            return self.resolve_play(card)

        print(f"{self.name} has no playable cards")
        self.draw_card(draw_pile)
        drawn_card = self.hand.top

        if self.is_playable(top, drawn_card):
            card = self.hand.take()
            return self.resolve_play(card)

        print(f"{self.name} draw {drawn_card if self.log else ''} but cannot play the drawn card")
        return None

    def resolve_play(self, card):
        if card.rank == 8:
            suit_active = random.choice(card.SUIT)
            print(f"{self.name} plays {card} and active suit is now {suit_active}")
            return (card, Card(suit=suit_active, rank=8))
        
        print(f"{self.name} plays {card}")
        return card


class Game:
    def __init__(self, players, cards_per_player=5, pause_duration=0.5):
        self.pause_duration = pause_duration
        self.cards_per_player = cards_per_player
        self.players = players
        self.draw_pile = Deck.standard_deck()
        self.discard_pile = Deck()
        self.turn = 0
        self.suit_active = None

    def setup(self):
        self.draw_pile.shuffle()

        for _ in range(self.cards_per_player):
            for player in self.players:
                player.draw_card(self.draw_pile)

        self.discard_pile.add(self.draw_pile.take())

    def next_turn(self):
        self.turn = self.turn + 1 if self.turn < len(self.players) - 1 else 0

    def run(self):
        self.setup()

        while True:
            player = self.players[self.turn]
            if self.suit_active is not None:
                top_card = Card(suit=self.suit_active, rank=8)
            else:
                top_card = self.discard_pile.top

            print(f"TOP [{top_card}]")
            time.sleep(self.pause_duration)
            played_card = player.choose_card(top_card, self.draw_pile)
            print("===========================")
            if played_card is not None:
                if isinstance(played_card, tuple):
                    self.discard_pile.add(played_card[0])
                    self.suit_active = played_card[-1].suit
                else:
                    self.discard_pile.add(played_card)
                    self.suit_active = None

            if player.is_win():
                print(f"\n{player.name} wins!")
                break

            if len(self.draw_pile) <= 0:
                curr_top = self.discard_pile.take()
                self.draw_pile = Deck(self.discard_pile.cards)
                self.discard_pile = Deck([curr_top])
                self.draw_pile.shuffle()
                print("\nThe draw pile runs out of card, so it will take the discard pile from bottom to top -1 then huffle it and make it the new draw pile ")

            self.next_turn()
            time.sleep(self.pause_duration)

def main():
    print(" == Welcome to Crazy 8! == ")
    how_many_bots = inp.take_input("How many bots do you want to play with: ", allow_type=int, rule=lambda x: 0 < x <= 8, rule_error="Bot must be 1-8!")
    players = [Human("Player")]
    for bot in range(how_many_bots):
        name = inp.take_input(f"Name bot # {bot + 1}: ", rule=lambda x: len(x) > 0, rule_error="Name the bot correctly!")
        players.append(Bot(name, log=True))

    game = Game(players, cards_per_player = 5, pause_duration = 2)
    game.run()


if __name__ == '__main__':
    main()