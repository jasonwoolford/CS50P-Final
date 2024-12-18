#CS50P Final Project - Jason Woolford

from pyfiglet import Figlet
from os import get_terminal_size
import random
import colorama

def main():
    #Initialize colorama
    colorama.init()

    #Initialize the Figlet library with f, then print the game title with it
    f = Figlet(font='slant')
    colored_title = (colorama.Fore.RED + f.renderText('Rock, ') + colorama.Fore.WHITE + f.renderText('Paper, ') + colorama.Fore.BLUE + f.renderText('Scissors!') + colorama.Style.RESET_ALL)
    print(colored_title)

    #Get user's name for the sake of score keeping
    name = input("Hello!  Welcome to Rock, Paper, Scissors!  We'll be keeping score, so what's your name? ")

    #Get number of game rounds to play from the user
    count = int(input(f"Good luck, {name}! How many games would you like to play? "))

    scores = [0,0] #Storing scores in a list for the sake of keeping everything properly accounted for during the game.

    gauntlet(count, scores) #Call upon gauntlet to run the user-specified number of rounds
    finish(name, scores[0], scores[1]) #Once the number of rounds are finished, call upon finish() to call the winner of the game

def gauntlet(count, scores):
    usr_score = scores[0]
    cpu_score = scores[1]
    print(f"We'll now play {count} games!")

    #Initialize for loop that handles the user-defined number of rounds of RPS
    for _ in range(count):
        while True: #This is for handling ValueErrors
            try:
                #User makes a move
                usr_move = input("Select your move: Rock, Paper, or Scissors: ").lower().strip()

                #Handles unacceptable inputs
                if usr_move not in ["rock","paper","scissors"]:
                    raise ValueError("Try that again, and please choose rock, paper, or scissors!")
                break

            except ValueError as error:
                print(error)
                    
        #Computer makes a randomized move after the user
        cpu_move = random.choice(["rock","paper","scissors"])
        print(f"Computer chose: {cpu_move}"),

        #Run compare() to determine the winner for the round, store the result in the result variable
        result = compare(usr_move,cpu_move)

        #If the user wins, add one point to usr_score, and print a confirmation message for visual feedback
        if result == 1:
            usr_score += 1
            print(f"{usr_move.capitalize()} beats {cpu_move}, you win this round!")
        #If the computer wins, add on point to cpu_score, and print a confrimation message for visual feedback
        elif result == -1:
            cpu_score += 1
            print(f"{cpu_move.capitalize()} beats {usr_move}, the computer wins this round!")
        #If both players make the same move, confirm that the round is a tie and leave the scores unaltered
        else:
            print(f"You both played {usr_move}, this round is a tie!")

    scores[0] = usr_score
    scores[1] = cpu_score

def compare(usr_move, cpu_move):
    #Tie conditions
    if usr_move == cpu_move:
        return 0
    #User win conditions
    elif (usr_move == "rock" and cpu_move == "scissors") or \
         (usr_move == "paper" and cpu_move == "rock") or \
         (usr_move == "scissors" and cpu_move == "paper"):
         return 1
    #If neither a tie or user win occurs, signal a computer win     
    else:
        return -1

def finish(name, usr_score, cpu_score):
    print("FINISH!")
    #If the user wins...
    if usr_score > cpu_score:
        print(f"Nice! {name} beats the computer with a score of {usr_score} over the computer's score of {cpu_score}!")
    #If the computer wins...
    elif usr_score < cpu_score:
        print(f"The computer wins the game with a score of {cpu_score}.  You scored {usr_score} winning rounds.  Better luck next time!")
    #If the computer and the user score equally...
    else:
        print(f"It's a tie!  Both {name} and the computer scored {usr_score}.")
    
    #Ask the user if they'd like to play again, restarting the program by recalling main()
    retry = input("Would you like to play again? Y/N ").lower().strip()

    if retry == "y" or retry == "yes":
        main()
    else:
        print(f"Very well, here's your final scores! \n{name}: {usr_score}, CPU: {cpu_score}")

main()