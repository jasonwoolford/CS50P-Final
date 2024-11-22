#CS50P Final Project - Jason Woolford

from pyfiglet import Figlet
import random

def main():
    f = Figlet(font='slant')
    print(f.renderText('Rock, Paper, Scissors!'))
    name = input("Hello!  Welcome to Rock, Paper, Scissors!  We'll be keeping score, so what's your name? ")
    count = int(input(f"Good luck, {name}!  How many games would you like to play? "))
    gauntlet(count)

def gauntlet(count):
    user_score: 0
    comp_score: 0
    count = count
    print(f"We'll now play {count} games!")
    i = 0

    while i < count:
        while True:
            try:
                usr_move = input("Select your move: Rock, Paper, or Scissors: ").lower().strip()

                if usr_move == "rock":
                    usr_move == 1
                elif usr_move == "paper":
                    usr_move == 2
                elif usr_move == "scissors":
                    usr_move == 3
                else:
                    raise ValueError

                cpu_move = random.randrange(1,3)
                compare(usr_move,cpu_move)

                if compare() == 1:
                    user_score += 1
                elif compare() == 2:
                    comp_score += 1
                
            except ValueError:
                print("Try that again, and please choose rock, paper, or scissors")
                continue

def compare(usr_move, cpu_move):
    usr_move = usr_move
    cpu_move = cpu_move

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
    

def finish(name, usr_score, cpu_score):
    print("FINISH!")

    if usr_score > cpu_score:
        print(f"Congratulations, {name}, you win with a score of {usr_score}, overtaking the computer who scored in at {cpu_score}")
    elif usr_score < cpu_score:
        print(f"The computer wins the game with a score of {cpu_score}.  You score {usr_score}, better luck next time!")
    else:
        print(f"Both you and the computer scored {usr_score}.  It's a tie!")

    decide = input("Would you like to try again? ").lower().strip()

    if decide == "yes":
        main()
    else:
        print(f"Final scores: {name} : {usr_score}, CPU: {cpu_score}")


main()