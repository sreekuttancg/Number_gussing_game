import random
from art import logo
game_mode=10
# def game():
print(logo)
print("Welcome to NUmber gussing Game!")
print("I'm thinking of a number between 1 and 100.")
random_num=random.randint(1,100)

game_over=False
difficulty=input("Choose a Difficluty. Type 'easy' or 'hard':")
if difficulty=="easy":

    game_mode=10

else:
    game_mode=5

while not game_over:
    print(f"You have {game_mode} attempts remaining to guess the number. ")

    guess=int(input("Make a guess"))
    if guess==random_num:
        print(f"You got it! The answer is {random_num}")
        game_over=True
    elif guess>random_num:
        print("Too high")
        game_mode-=1
    else:
        print("Too low")
        game_mode -= 1









