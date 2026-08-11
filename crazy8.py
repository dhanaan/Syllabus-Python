import take_input as inp
import random
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
            return chosen.suit == top.suit or chosen.rank == top.rank

        return False

    def is_something_playable(self, top: Card):
        for card in self.hand.cards:
            if self.is_playable(top, card):
                return True

        return False

    def get_playable_cards(self, top: Card):
        return [
            card
            for card in self.hand.cards
            if self.is_playable(top, card)
        ]


class Human(Player):
    def choose_card(self, top: Card, draw_pile: Deck):
        print(self)
        if self.is_something_playable(top):
            card_index = int(
                inp.take_input(f"{self.name}, choose a card (1-{len(self.hand)}): ",
                    rule_error=(
                        "That card is unplayable, it has a different "
                        "suit and rank compared to the top card"
                    ),
                    rule=lambda x: 0 < int(x) <= len(self.hand) and self.is_playable(top, self.hand.get(int(x) - 1)))) - 1

            card = self.play_card(card_index)
            print(f"{self.name} plays: {card}")

            return card

        # No playable cards, so draw one.
        print(f"{self.name} has no playable cards.")
        print(f"{self.name} draws a card.")

        self.draw_card(draw_pile)

        drawn_card = self.hand.top

        # Automatically play the drawn card if possible.
        if self.is_playable(top, drawn_card):
            card = self.hand.take()
            print(f"{self.name} draws and plays: {card}")
            return card

        print(f"{self.name} cannot play the drawn card.")
        return None


class Bot(Player):
    def choose_card(self, top: Card, draw_pile: Deck):
        print(self)

        playable_cards = self.get_playable_cards(top)

        # If the bot has playable cards, randomly choose one.
        if playable_cards:
            chosen_card = random.choice(playable_cards)

            card_index = self.hand.cards.index(chosen_card)
            card = self.play_card(card_index)
            print(f"{self.name} plays: {card}")
            return card

        # Otherwise draw one card.
        print(f"{self.name} has no playable cards.")
        print(f"{self.name} draws a card.")

        self.draw_card(draw_pile)

        drawn_card = self.hand.top

        # Automatically play the drawn card if possible.
        if self.is_playable(top, drawn_card):
            card = self.hand.take()

            print(f"{self.name} draws and plays: {card}")

            return card

        print(f"{self.name} cannot play the drawn card.")
        return None


class Game:
    def __init__(self, players):
        self.players = players
        self.draw_pile = Deck.standard_deck()
        self.discard_pile = Deck()
        self.turn = 0

    def setup(self):
        self.draw_pile.shuffle()

        # Deal 5 cards to each player.
        for _ in range(5):
            for player in self.players:
                player.draw_card(self.draw_pile)

        # Start the discard pile.
        self.discard_pile.add(self.draw_pile.take())

    def next_turn(self):
        self.turn = (
            self.turn + 1
            if self.turn < len(self.players) - 1
            else 0
        )

    def run(self):
        self.setup()

        while True:
            player = self.players[self.turn]
            top_card = self.discard_pile.top
            print(f"Top card is: {top_card}")
            print(f"{player.name} turn")

            played_card = player.choose_card(
                top_card,
                self.draw_pile
            )

            if played_card is not None:
                self.discard_pile.add(played_card)


            if player.is_win():
                print(f"\n {player.name} wins!")
                break

            self.next_turn()


def main():
    players = [
        Human("you"),
        Bot("a"),
        Bot("b")
    ]

    game = Game(players)
    game.run()


if __name__ == '__main__':
    main()