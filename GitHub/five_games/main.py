from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle
from connect_four import ConnectFour
while True:
    txt= """Mini Games !!!
    -Guess the number (1)
    - Rock, paper, Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press a number or 'q' to quit):"""
    value= input(txt)
    if value == "1":
        x=int(input('Please enter an upper bound for guessing:'))
        guess_the_number(x)
    elif value == "2":
        rock_paper_scissors()
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        game= ConnectFour()
        game.play()
    elif value == "5":
        pass
    elif value == "q":
        break