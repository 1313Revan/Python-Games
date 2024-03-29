# A terminal-based Rock Paper Scissors I made while taking a Python course
# Author: Revan

import random
import rps_art as art


print('\nWelcome to the ROCK PAPER SCISSORS terminal game!\nYou\'ll be placed against the computer to see which of you comes out on top.\n')
print('\nMake your choice!\n')
print('1. Rock\n2. Paper\n3. Scissors\n')

player = input('>> ').lower()
if player == 'rock' or player == '1':
    p_choice = art.rock
elif player == 'paper' or player == '2':
    p_choice = art.paper
else:
    p_choice = art.scissors

computer = random.randint(1,3)
if computer == 1:
    c_choice = art.rock
elif computer == 2:
    c_choice = art.paper
else:
    c_choice = art.scissors

print('\n********************')
print('\nYou chose:\n',p_choice,'\n')
print('\nComputer chose:\n',c_choice)
print('\n********************')

if p_choice == art.rock:
    if c_choice == art.rock:
        print('\nDRAW\n')
    elif c_choice == art.paper:
        print('\nYOU LOSE\n')
    else:
        print('\nYOU WIN\n')
elif p_choice == art.paper:
    if c_choice == art.rock:
        print('\nYOU WIN\n')
    elif c_choice == art.paper:
        print('\nDRAW\n')
    else:
        print('\nYOU LOSE')
else:
    if c_choice == art.rock:
        print('\nYOU LOSE')
    elif c_choice == art.paper:
        print('\nYOU WIN\n')
    else:
        print('\nDRAW\n')
