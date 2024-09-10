# Arden Boettcher
# 9/10
# if-else practice


# I don't have Python installed on my school computer and I am not able to install it myself because I need permission
please = 'I would like to have Python installed on my computer for CTC.'
reasons = 'Without Python I cannot debug/run any code using Visual Studio which would make it impossible to check my work.'
extra_reasons = 'I am caught up with all of my work and want it for purely school-related reasons.'

print(please) 
print('do you agree?')

check1 = input()

if check1 == 'no': # I have absolutely no clue if this works or not bc I haven't been able to bug-test it
    print(reasons)
    print('please say yes')
    check2 = input()

    if check2 == 'no':
        print(extra_reasons)
        print('please :(')
        check3 = input()

        if check3 == 'no':
            print(':(')
        elif check3 == 'yes':
            print('THANK YOU SO MUCH')
        else:
            print('yes or no')

    elif check2 == 'yes':
        print('thank you')
    else:
        print('yes or no')

elif check1 == 'yes':
    print('thank you')
else:
    print('yes or no')
