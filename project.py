#CS50P Final Project - Jason Woolford

from pyfiglet import Figlet

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
        else:
            comp_score += 1
    
    if i == count:
        finish(user_score, comp_score)
    

def game():
    usr_move = input("Select your move: Rock, Paper, or Scissors: ").lower()



'''
def func3():
    ...
'''

main()