# Arden Boettcher
# 9/10
# if-else practice



please = 'I would really like to have python installed on my computer for CTC.'
reasons = 'Without python I cannot debug/run any code using visual studio which would make it impossible to do check my work.'
extra_reasons = 'I am caught up with all of my work and I want it for purely school related reasons.'

print(please)
print('do you agree?')

check1 = input()

if check1 == 'no':
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