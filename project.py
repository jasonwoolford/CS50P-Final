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


main()