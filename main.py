from art import logo
import random


def welcome_user():
    """This function will check if user want to play game."""
    return input("\nWelcome in our casino do you want to try your luck (yes/no): ")


def encourage_user(win, u_cards, c_cards):
    """This function will encourage user to play more game."""
    if win and sum(u_cards) == sum(c_cards):
        endure = input("\nWow you are such a good player no one draw, maybe"
                       " you will want to try your luck more time (yes/no): ")
        return endure
    elif win:
        endure = input("\nWow you are such a good player maybe"
                       " you will want to try your luck more time (yes/no): ")
        return endure
    else:
        endure = input("\nSometimes everyone must defeat, but I think you can try"
                       " one more time, I think that you can win (yes/no): ")
        return endure


def fill_hands(u_cards, c_cards, deck):
    """This function will fill players hands."""
    for i in range(2):
        u_cards.append(random.choice(deck))
        c_cards.append(random.choice(deck))


def check_result_c(c_cards, deck):
    """This function will check if computer has got cards
     of value at least 17, if not then append more."""
    while sum(c_cards) < 17:
        c_cards.append(random.choice(deck))
        if_as(c_cards)


def print_result(u_cards, c_cards, deck):
    """This function will show first result after random choices."""
    print(f"\nYour card is: {u_cards} and your current score is {sum(u_cards)}")
    print(f"Computer first card is: {c_cards[0]}")
    drawing = input("\nDo you want to draw one more card (yes/no): ")
    if drawing == "yes":
        append_u_card(u_cards, c_cards, deck)


def append_u_card(u_cards, c_cards, deck):
    """This function will append one more card into user hand,
    then print result and prompt if user want to draw more card."""
    u_cards.append(random.choice(deck))
    if_as(u_cards)
    sum_u_hand = sum(u_cards)
    if sum_u_hand > 21:
        print(f"\nSum of your cards is above 21, it's {sum_u_hand}.")
    else:
        print_result(u_cards, c_cards, deck)


def if_as(deck_card):
    """This function will check if there is as in hands and score
    is above 21 then change the value of as to 1 not 11"""
    if 11 in deck_card and sum(deck_card) > 21:
        deck_card.remove(11)
        deck_card.append(1)


def check_winner(u_cards, c_cards):
    """This function will check who is the winner."""
    u_sum = sum(u_cards)
    c_sum = sum(c_cards)
    print(f"\nYour cards are {u_cards} and computer cards are {c_cards}.")
    if c_sum == u_sum:
        print(f"No one is winner it's a draw. You've got the same scores {u_sum}, {c_sum}")
    if c_sum > 21 and c_sum > u_sum:
        print(f"Computer went over his score is: {c_sum}. You win this round!")
        return True
    elif u_sum > 21 and u_sum > c_sum:
        print(f"You went over, your score is: {c_sum}. You loose this round!")
        return False
    elif u_sum > c_sum:
        print(f"You are the winner, your score is {u_sum},"
              f" while computer is only {c_sum}!")
        return True
    else:
        print(f"You are not the winner, your score is only {u_sum},"
              f" while computer is {c_sum}. You can try your luck next time")
        return False


print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

start = welcome_user()

while start:
    fill_hands(user_cards, computer_cards, cards)
    check_result_c(computer_cards, cards)
    print_result(user_cards, computer_cards, cards)
    winner = check_winner(user_cards, computer_cards)

    start_stop = encourage_user(winner, user_cards, computer_cards)

    if start_stop == "no":
        break

    user_cards = []
    computer_cards = []
