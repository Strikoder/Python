from art import logo, vs
from Game_data import data
from random import randint
"""
{'name': 'Instagram', 'follower_count': 346, 
 'description': 'Social media platform', 'country': 'United States'}
"""

score = 0

print(logo)

print("\n\nWelcome to our program. Please try to guess who has more followers.\n")
while True:
    guessing = randint(0, 49)
    print(f"So here we have \"{data[guessing]['name']}\" which is from \"{data[guessing]['country']}\" which works as \"{data[guessing]['description']}\"")
    followers_first = data[guessing]['follower_count']

    print(vs)

    guessing = randint(0, 50)
    print(f"And here we have \"{data[guessing]['name']}\" which is from \"{data[guessing]['country']}\" which works as \"{data[guessing]['description']}\"")
    followers_second = data[guessing]['follower_count']

    entered_value = int(input("Please enter 1 if you think the first choice has more followers than the second one, or 2 if you think it's the other way around: "))

    if entered_value == 1:
        if followers_first < followers_second:
            print("You lose.")
            print(f"The first has \"{followers_first}\" followers, while the second one has \"{followers_second}\"")
            break
        else:
            score += 1
    elif entered_value == 2:
        if followers_first > followers_second:
            print("You lose.\n")
            print(f"The first choice has \"{followers_second}\" followers, while the second one has \"{followers_first}\"")
            break

        else:
            score += 1
    else:
        print("Please enter a valid value.")

print(f"\nYou scored {score} points.")
