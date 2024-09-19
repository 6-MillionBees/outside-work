# Arden Boettcher
# 9/18/24
# Recursive Sequence Finder

main = input('\nput 3 numbers in a sequence THEY MUST BE SEPARATED WITH A SPACE:\n\n')

listmain = main.split() # this whole thing makes the variable main a functioning tuple
tuplemain = tuple(listmain)


num3c1 = float(tuplemain[1]) - float(tuplemain[0]) # this may look complicated but it's just defining variables
num3c2 = float(tuplemain[2]) - float(tuplemain[1])
num3c3 = float(tuplemain[1]) / float(tuplemain[0])
num3c4 = float(tuplemain[2]) / float(tuplemain[1])


if num3c1 == num3c2: # the BEEF of the operation, this is where the output is decided and printed
    print(f'\nUn = Un-1(+{num3c1})\n')
elif num3c3 == num3c4:
    print(f'\nUn = Un-1(*{num3c3})\n')
else:
    print('you did not math correctly\n')
