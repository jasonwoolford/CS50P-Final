#This file is for running tests on project.py using pytest

import pytest, project
from project import main, gauntlet, compare, finish

#This must be tested using -s ("pytest test_project.py -s")
def test_compare():
    assert compare("rock", "scissors") == 1
    assert compare("paper", "rock") == 1
    assert compare("scissors", "paper") == 1
    assert compare("rock", "rock") == 0
    assert compare("paper", "paper") == 0
    assert compare("scissors", "scissors") == 0
    assert compare("rock", "paper") == -1
    assert compare("paper", "scissors") == -1
    assert compare("scissors", "rock") == -1

def test_gauntlet():
    scores = [0,0]
    gauntlet(1, scores)
    assert scores[0] in (0,1)
    assert scores[1] in (0,1)

def test_finish():
    with pytest.raises(SystemExit) as e:
        finish("Alice", 3, 2)
    assert e.type is SystemExit and e.value.code == 0

def test_main():
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type is SystemExit and e.value.code == 0

if __name__ == "__main__":
    pytest.main()