from collections import deque
import take_input as inp
import random

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number


class Player:
    def __init__(self, hand):
        self.hand = hand

    def print_card(self):
        for cards in self.hand:
            print(f'[{cards.color} {cards.number}]', end=' ')

    def is_playable(self, top):
        cards = []
        for i, card in enumerate(self.hand):
            if card.number == top.number or card.color == top.color:
                cards.append(str(i))
        return cards

    def add(self, card):
        self.hand.append(card)
    
    

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def add(self, card):
        self.cards.append(card)

    def top_card(self):
        return self.cards[-1]

def fill_deck(deck, card, numbers, colors):
    for num in numbers:
        deck.append(card(color = colors, number = num))

def main():
    ALL_COLORS = ("red", "green", "yellow", "blue")
    draw_deck = []
    for color in ALL_COLORS:
        fill_deck(draw_deck, Card, range(10), color)
    draw_deck = Deck(draw_deck)
    draw_deck.shuffle()
    player_user = Player([draw_deck.draw() for _ in range(8)])
    player_bot = Player([draw_deck.draw() for _ in range(8)])
    top = draw_deck.draw()


    turn = 0
    uno = False
    while not uno:
        print(f'Top Card: [{top.color} {top.number}]')
        if turn == 0:
            player_user.print_card()
            print()
            playable_card = player_user.is_playable(top)
            if playable_card:
                picked_option = inp.take_input(f"Pick card index. available: {", ".join(playable_card)} >> ", choices=playable_card)
            else:
                print("you have no card you can use so you have to draw")
                player_user.add(draw_deck.draw())
            
            turn = 1
        else:
            turn = 0


if __name__ == '__main__':
    main()
