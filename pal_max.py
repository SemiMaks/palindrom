a1 = input("Ваше число:\n")


def palindrom(a1):
    a1 = int(a1)
    a3 = a1
    a2 = 0
    while a1 > 0:
        digit = a1 % 10
        a1 = a1 // 10
        a2 = a2 * 10 + digit

    print(a3 + a2)
    x = a3 + a2
    x = str(x)
    if x == x[::-1]:
        print('Палиндром!\n')
        a1 = input("Ваше число:\n")
    else:
        print('Не палиндром!\n')
        a1 = input("Ваше число:\n")
    palindrom(a1)


while a1 != 'q':
    palindrom(a1)
