# Arden Boettcher
# 9/11
# Math-1-2
# I felt as if I could do my math homework entirely on Python but I gave up on question 3

print('1.)') # question 1

question1a = 150 / 100
print(f'a.) *{question1a} growth')

question1b = 29.375 / 73.4375
print(f'b.) *{question1b} decay')

question1c = 82.40 / 80.00
print(f'c.) *{question1c} growth')

question1d = 191.36 / 208.00
print(f'd.) *{question1d} decay\n')

print('2.)') # question 2

print(f'a. un = u(n-1)*{question1a}')
print(f'b. un = u(n-1)*{question1b}')
print(f'c. un = u(n-1)*{question1c}')
print(f'd. un = u(n-1)*{question1d}\n')

print('3.)')

question3a = 0
num3a = 2000
print('a.', end=' ')

while question3a < 4:
    if question3a == 3:
        print(num3a)
    else:
        print(num3a, end=', ')
    num3a *= 1.05
    question3a += 1


print('b.', end=' ')

question3b = 0
num3b = 5000

while question3b < 4:
    if question3b == 3:
        print(num3b)
    else:
        print(num3b, end=', ')
    num3b *= 0.85
    question3b += 1

print('c.', end=' ')

# this whole thing is overly complex bc I wanted it to work no matter what numbers you put in it (as long as they are in a sequence)
num3c1 = 1350 - 1250
num3c2 = 1458 - 1350
num3c3 = 1350 / 1250
num3c4 = 1458 / 1350

if num3c1 == num3c2:
    print(f'Un = Un-1(+{num3c1})')
elif num3c3 == num3c4:
    print(f'Un = Un-1(*{num3c3})')
else:
    print('didn\'t work :(')