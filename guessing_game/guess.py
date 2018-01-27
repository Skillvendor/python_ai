import random

def generate_code():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def guess(num, code):
    hints = []
    if len(num) != len(code):
        hints.append('Not a valid input')
        return hints

    for pos in range(len(code)):
        if code[pos] == num[pos]:
            hints.append('Match')
        elif num[pos] in code:
            hints.append('Close')

    if len(hints) == 0:
        hints.append('None')

    return hints

code = generate_code()
print('Code generated and is: {}'.format(code))

wrong_guess = True

while wrong_guess:
    num = list(input("What is your guess? "))
    num = list(map(int, num))

    if num == code:
        print('YOU ARE RIGHT!!!')
        wrong_guess = False
    else:
        hints = guess(num, code)
        print(hints)
