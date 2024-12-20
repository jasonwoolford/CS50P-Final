#Pytest for project.py for CS50P Final - Jason Woolford

#Importing libraries and relevant functions
import pytest
from project import main, gauntlet, compare, finish

def test_main():
    assert scores == [0,0]

def test_gauntlet(count):
    assert count > 1

def test_compare():
    assert compare('rock', 'scissors') == 1
    assert compare('paper', 'rock') == 1
    assert compare('scissors', 'paper') == 1
    assert compare('rock', 'paper') == -1
    assert compare('paper', 'scissors') == -1
    assert compare('scissors', 'rock') == -1
    assert compare('rock', 'rock') == 0
    assert compare('paper', 'paper') == 0
    assert compare('scissors', 'scissors') == 0

def test_finish(usr_score, cpu_score):
    assert finish(1,0) == print(f"Nice! {name} beats the computer!")
    assert finish(0,1) == print(f"The computer wins the game. Better luck next time!")
    assert finish(0,0) == print(f"It's a tie! Both {name} and the computer scored {usr_score}")