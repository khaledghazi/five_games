import random

def guess_the_number(x):
    print("Let's play Guess the numbers")


    random_number = random.randint(0, x)


    num_guesses = 0
    while True:
        guess= int(input(f'Guess a number between zero and {x}:'))
        num_guesses += 1
        if guess == random_number:
            print(f'Congrats the number is {random_number}')
            break
        elif guess < random_number:
            print('Too low !')
        else:
            print('Too High!')

print()
print()
print()