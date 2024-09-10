# Arden Boettcher
# 9/10
# if-else practice

please = 'I would really like to have python installed on my computer for CTC.'
reasons = 'Without python I cannot debug/run any code using visual studio which would make it impossible to do check my work.'
extra_reasons = 'I am caught up with all of my work and I want it for purely school related reasons.'
# I don't have Python installed on my school computer and I am not able to install it myself because I need permission

while True:
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
                break
            elif check3 == 'yes':
                print('THANK YOU SO MUCH')
                break
            else:
                print('yes or no')
        elif check2 == 'yes':
            print('thank you')
            break
        else:
            print('yes or no')
    elif check1 == 'yes':
        print('thank you')
        break
    else:
        print('yes or no')
