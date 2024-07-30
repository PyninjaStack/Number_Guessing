from random import randint
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def check_answer(guess,answer,turns):
    if guess > answer:
        print("To High.")
        return turns - 1
    elif guess < answer:
        print("To Low.")
        return turns - 1
    else:
        print(f"You got it! The Answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN
    
def game():
    print(logo)
    print("Welcome To The Number Gussing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"The correct Answer is: {answer}")

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a Guess: "))

        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again.")

game()
