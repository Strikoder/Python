from random import randint
from art import logo


#Function to check user's guess against actual answer.
def check(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""

  if guess == answer:
    print(f"It's right, the answer is: {answer}")
    return

  elif guess > answer:
    print("Too high, try a smaller number.")

  else:
    print("Too low, try a larger one.")

  return turns - 1




#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return 10
  else:
    return 5



def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining, try to guess the number again.")

    #Let the user guess a number.
    guess = int(input("Make a guess^^: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check(guess, answer, turns)
    if turns == 0:
      print(f"You've run out of guesses, you lose, the correct answer is: {answer}")
      return
    elif guess != answer:
      print("Guess again.")



game()

