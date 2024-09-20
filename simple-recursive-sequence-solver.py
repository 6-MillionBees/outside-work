# Arden Boettcher
# 9/18/24
# Simple Recursive Sequence Solver

import math
import string

superscript_map = { # This whole thing is because I want the powers and square roots to be in superscript
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"} # I literally just stole this from a guy on stack overflow

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))

main = input('\nput 3 numbers in a sequence THEY MUST BE SEPARATED WITH A SPACE:\n\n')

listmain = main.split() # This whole thing makes the variable main a functioning tuple
tuplemain = tuple(listmain) # I also stole this from a guy on stack overflow

tuple0 = float(tuplemain[0])
tuple1 = float(tuplemain[1])
tuple2 = float(tuplemain[2])
num3c1 = tuple1 - tuple0 # This may look complicated but it's just defining variables
num3c2 = tuple2 - tuple1
num3c3 = tuple1 / tuple0
num3c4 = tuple2 / tuple1
num = tuple1
num2 = tuple0
power = 0
root = 0

while num > 1: # This decides if it's to the power of anything and then counts how many powers
    num /= tuple0
    power += 1 

while num2 > 1: # This is for square roots
    num2 /= tuple1
    root += 1 

if num3c1 == num3c2: # This is where the output is decided and finally printed
    print(f'\nUn = Un-1 + ({num3c1})\n')
elif num3c3 == num3c4:
    print(f'\nUn = Un-1 (*{num3c3})\n')
elif num == 1:
    print(f'\nUn = Un-1 ({str(power).translate(trans)})\n')
elif num2 == 1:
    print(f'\nUn = ({str(root).translate(trans)}√)Un-1\n')
else:
    print('\nyou did not math correctly\n')
