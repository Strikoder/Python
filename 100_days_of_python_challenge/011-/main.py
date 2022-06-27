from art import logo
import random

## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_deck = []
bot_deck = []


def sum(l):
    total = 0
    for val in l:
        total = total + val
    return total


def start():
    for i in range(2):
        player_deck.append(cards[random.randint(0, 12)])
        bot_deck.append(cards[random.randint(0, 12)])
    print(f"Your cards are: {player_deck}\nopponent's first card is: {bot_deck[0]}")


def game():
    choice = input("Type 'y' to draw another card or 'n' to pass:").lower()
    player_score = sum(player_deck)
    bot_score = sum(bot_deck)

    while choice == "y":
        player_deck.append(cards[random.randint(0, 12)])
        player_score = sum(player_deck)
        if 11 in bot_deck and sum(bot_deck) > 21:
            player_deck.remove(11)
            player_deck.append(1)

        print(f"\nYour current cards are:{player_deck}")

        print(f"Your current score is:{player_score}")
         
        bot_deck.append(cards[random.randint(0, 12)])
        bot_score = sum(bot_deck)
        if 11 in bot_deck and sum(bot_deck) > 21:
            bot_deck.remove(11)
            bot_deck.append(1)

        if player_score > 21:
            print("Game over, you lost!")
            return
        elif bot_score > 21:
            print("Congratz, you win!")
            print(f"bot's cards were{bot_deck}")
            return

        choice = input("Type 'y' to draw another card or 'n' to pass.").islower()

    if player_score == bot_score:
        print("draw")
    elif player_score > bot_score:
        print("Congratz, you win!")
    else:
        print("Game over, you lost!")
        print(f"bot's cards were{bot_deck}")





print(logo)
start()
game()
