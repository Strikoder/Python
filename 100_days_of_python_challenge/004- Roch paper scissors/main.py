rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import  random
Game=[rock,paper,scissors]
user_c=int(input("what do you choose? please type 0 for rock, 1 for paper and 2 for scissors\n"))
print(f"\nYou have chosen{Game[user_c]}")
computer_c=random.randint(0,2)
print(f"The computer has chosen {Game[computer_c]}")

if user_c > 2 or user_c < 0:
    print("Pick a number between 0 and 2 -.-!")
elif user_c==computer_c:
    print("Draw")
elif user_c==2 and computer_c==0:
    print("You lose")
elif user_c == 0 and computer_c == 2:
    print("You win")
elif user_c>computer_c:
    print("You win")
elif user_c < computer_c:
    print("You lose")
else:
    print("Undefined")