#CS50P Final Project - Jason Woolford

from pyfiglet import Figlet
import random

def main():
    f = Figlet(font='slant')
    print(f.renderText('Rock, Paper, Scissors!'))
    name = input("Hello!  Welcome to Rock, Paper, Scissors!  We'll be keeping score, so what's your name?")
    count = int(input(f"Good luck, {name}! How many games woudl you like to play? "))
    scores = [0,0] #Storing scores in a list for the sake of keeping everything properly accounted for during the game.
    gauntlet(count, scores) #Call upon gauntlet to run the user-specified number of rounds
    finish(name, scores[0], scores[1])

def gauntlet(count, scores):
    usr_score = scores[0]
    cpu_score = scores[1]
    print(f"We'll now play {count} games!")

    for _ in range(count):
        usr_move = input("Select your move: Rock, Paper, or Scissors: ").lower().strip()

        #Handles unacceptable inputs
        if usr_move not in ["rock","paper","scissors"]:
            raise ValueError("Try that again, and please choose rock, paper, or scissors!")
        
        cpu_move = random.choice(["rock","paper","scissors"])
        print(f"Computer chose: {cpu_move}")

        result = compare(usr_move,cpu_move)
        if result == 1:
            usr_score += 1
            print(f"{usr_move} beats {cpu_move}, you win this round!")
        elif result == -1:
            cpu_score += 1
            print(f"{cpu_move} beats {usr_move}, the computer wins this round!")
        else:
            print(f"You both played {usr_move}, this round is a tie!")

    scores[0] = usr_score
    scores[1] = cpu_score

def compare(usr_move, cpu_move):
    if usr_move == cpu_move:
        return 0
    elif (usr_move == "rock" and cpu_move == "scissors") or \
         (usr_move == "paper" and cpu_move == "rock") or \
         (usr_move == "scissors" and cpu_move == "paper"):
         return 1
    else:
        return -1

main()