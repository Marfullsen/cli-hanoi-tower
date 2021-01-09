#-*- coding: utf-8 -*-
from os import name, system

def clrscr():
   ''' Clear Screen, tested on Linux & Windows '''
   # for mac and linux.
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfroms.
      _ = system('cls')