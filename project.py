#CS50P Final Project - Jason Woolford

from pyfiglet import Figlet
import random

def main():
    f = Figlet(font='slant')
    print(f.renderText('Rock, Paper, Scissors!'))
    name = input("Hello!  Welcome to Rock, Paper, Scissors!  We'll be keeping score, so what's your name? ")
    count = input(f"Good luck, {name}!  How many games would you like to play?")
    gauntlet(count)

def gauntlet(count):
    user_score: 0
    comp_score: 0
    count = count
    print(f"We'll now play {count} games!")

    i = 0
    while i < count:
        game()
        if game() == 1:
            user_score += 1
        elif game() == 2:
            comp_score += 1
        else:
            continue
    
    if i == count:
        finish(user_score, comp_score)
    

def game():
    usr_move = input("Select your move: Rock, Paper, or Scissors: ").lower().strip()
        if usr_move == "rock":
            usr_move == 1
        elif usr_move == "paper":
            usr_move == 2
        elif usr_move == "scissors":
            usr_move == 3
        else:
            raise ValueError("Try again, and please type either rock, paper, or scissors")
            game()

    cpu_move = random.randrange(1,3)
    

    if usr_move == 1 and cpu_move == 3:
        print("Rock beats scissors!  You win the round!")
        return 1
    elif usr_move == 2 and cpu_move == 1:
        print("Paper beats rock!  You win the round!")
        return 1
    elif usr_move == 3 and cpu_move == 2:
        print("Scissors beats paper!  You win the round!")
        return 1
    elif usr_move == cpu_move:
        print("Draw!  Neither player scores this round!")
        return 3
    elif cpu_move == 1 and usr_move == 3:
        print("Rock beats scissors!  The computer wins this round!")
        return 2 
    elif cpu_move == 2 and usr_move == 1:
        print("Paper beats rock!  The computer wins this round!")
        return 2
    elif cpu_move == 3 and usr_move == 2:
        print("Scissors beats paper!  The computer wins this round!")
        return 2

'''
def func3():
    ...
'''

main()