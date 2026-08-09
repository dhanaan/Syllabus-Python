from collections import deque
import take_input as inp
import random
import time

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
    
    def out(self, idx):
        return self.hand.pop(idx)
    
    
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
    garbage_deck = Deck([])
    draw_deck.shuffle()
    player_user = Player([draw_deck.draw() for _ in range(8)])
    player_bot = Player([draw_deck.draw() for _ in range(8)])
    top = draw_deck.draw()

    turn = 0
    win = False

    while not win:
        if turn % 2 == 0:
            player_operate(top, player_user, draw_deck, garbage_deck)
        else:
            bot_operate(top, player_bot, draw_deck, garbage_deck)
        turn += 1

def player_operate(top, player_user, draw_deck, garbage_deck):
    playable_card = player_user.is_playable(top)
    playable_method = player_user.
    if playable_card:
        while playable_card:
            print(f'Top Card: [{top.color} {top.number}]')
            player_user.print_card()
            option = int(inp.take_input(f"\n\nPick card index. available: {", ".join(playable_card)} >> ", choices=playable_card))
            garbage_deck.add(player_user.out(option))
            top = garbage_deck.top_card()
            playable_card = player_user.is_playable(top)
        print("You Have no more card that can be out")
        time.sleep(1)
    else:
        print(f'Top Card: [{top.color} {top.number}]')
        player_user.print_card()
        print("you have no card you can use so you have to draw..")
        time.sleep(1)
        new_card = player_user.add(draw_deck.draw())
        top = garbage_deck.top_card()
        playable_card = player_user.is_playable(top)
        if playable_card:
            garbage_deck.add(player_user.out(playable_card[0]))
            print(f"You got a {new_card} which is playable so it is out")
        else:
            print(f"You got {new_card}")

def bot_operate(top, player_bot, draw_deck, garbage_deck):
    time.sleep(2)
    top = garbage_deck.top_card()
    print("BOT ==========================")
    bot_playable = player_bot.is_playable(top)
    if bot_playable:
        while bot_playable:
            print(f'Top Card: [{top.color} {top.number}]')
            player_bot.print_card()
            bot_option = int(random.choice(bot_playable))
            print(f'\n\nBOT PLAYABLE: {bot_playable}')
            print(f'BOT OPTION: {bot_option}')
            garbage_deck.add(player_bot.out(bot_option))
            top = garbage_deck.top_card()
            bot_playable = player_bot.is_playable(top)
    else:
        print(f'Top Card: [{top.color} {top.number}]')
        player_bot.print_card()
        print("you have no card you can use so you have to draw..")
        new_card = player_bot.add(draw_deck.draw())
        top = garbage_deck.top_card()
        bot_playable = player_bot.is_playable(top)
        if bot_playable:
            garbage_deck.add(player_user.out(playable_card[0]))
            print(f"You got a {new_card} which is playable so it is out")
        else:
            print(f"You got {new_card}")
    print("BOT ==========================")

if __name__ == '__main__':
    main()
