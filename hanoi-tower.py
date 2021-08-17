#!/usr/bin/env python
#-*- coding: utf-8 -*-

from os import name, system

# Const.
TOTAL_DISCS = 3
TOTAL_TOWERS = 3
ROWS, COLUMNS = 'rows','columns'
DEFAULT_VISUAL = COLUMNS

# Declarations
towers = list()
moves = dict()
total_moves = 0

# Init.
towers = [[x for x in range(TOTAL_DISCS,0,-1)],[],[]]
welcome_msg = '''Welcome to CLI Hanoi Tower.
Hanoi Tower is a CLI puzzle, the goal is to move all the "discs" from the first "tower" to the last "tower".

How to play:
  -      |     |   
 ---     |     |   
-----    |     |   
*******************
   1     2     3
Select a tower to take the first element.
Select another tower to put the element.
Note that you can't move an element over a smaller one.

Enter to start the CLI game.
'''

# Modules.
def clrscr():
   ''' Clear Screen, tested on Linux & Windows '''
   # for mac and linux.
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfroms.
      _ = system('cls')

def display(visual = DEFAULT_VISUAL):
    if visual == ROWS:
        display_rows()
    elif visual == COLUMNS:
        display_columns()
    else:
        print('No Idea whay do you mean bro.')

def display_rows():
    for tower in range(len(towers)):
        print(f'{tower}) ' ,end='')
        for disc in range(TOTAL_DISCS):
            if disc < len(towers[tower]):
                print(towers[tower][disc], end = ' ')
            else:
                print(chr(8212), end=' ')
        print('\n')

def display_columns():
    for disc in range(TOTAL_DISCS,0,-1):
        for tower in range(TOTAL_TOWERS):
            if disc <= len(towers[tower]):
                print(str(towers[tower][disc-1]).center(TOTAL_DISCS+2), end = '')
            else:
                print('.'.center(TOTAL_DISCS+2),end='')
        print()
    print('*' * TOTAL_DISCS*TOTAL_TOWERS + '*'*(TOTAL_TOWERS+2) + '*')
    for i in range(TOTAL_TOWERS):
        print(str(i).center(TOTAL_DISCS+2),end='')
    print()


def move():
    global towers
    x = -1
    y = -1
    def validate(msg):
        value = -1
        while (0 > value) or (value > TOTAL_TOWERS):
            value = input(msg)
            if not value.isdigit(): value = -1
            else: value = int(value)
        return value - 1
    x = validate("Select any tower to take a disc from: ")
    y = validate("Select any tower to put this disc to: ")
    
    if len(towers[x]) != 0:
        if len(towers[y]) == 0 or towers[x][-1] < towers[y][-1]:
            towers[y].append(towers[x].pop())
            moves[len(moves)+1] = [x,y]
        elif towers[x][-1] == towers[y][-1]:
            print('LOL, moved to the same place!')
        else:
            input('Not possible')
    else:
        print(NotImplemented)

def check():
    if len(towers[-1]) == TOTAL_DISCS:
        return True
    return False

def main():
    clrscr()
    if not check():
        display()
        move()
        main()
        return None
    display()
    total_moves = len(moves)
    print('You won!')
    print(f'Total moves: {total_moves}')
    shortest_with = lambda n: 2**n-1
    if shortest_with(TOTAL_DISCS)==total_moves:
        print("Congrats!\nYou found the shortest way to solve the game!")
if __name__ == "__main__":
    clrscr()
    easterEgg = input(welcome_msg)
    if easterEgg.isdigit():
        easterEgg = int(easterEgg)
        if 9 > easterEgg > 3:
            TOTAL_DISCS = easterEgg
            towers = [[x for x in range(TOTAL_DISCS,0,-1)],[],[]]
    else:
        if easterEgg.lower() == 'beta':
            clrscr()
            print('Welcome to the betatester hidden menu.')
            TOTAL_DISCS = int(input('New value for the total amount of discs: '))
            TOTAL_TOWERS = int(input('New value for the total amount of towers: '))
            DEFAULT_VISUAL = input("type 'rows' or 'columns': ")
    main()
    input('Press "Enter" to quit.')