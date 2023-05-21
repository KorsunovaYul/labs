def z3_1():
    n = int(input('Сколько слов?'))
    s = ''
    for i in range(n):
        a = input()
        s += a + ' '
    print(s)

def z3_2():
    a = input()
    s = ''
    while a != 'stop':
        s += a + " "
        a = input()
    print(s)

def z3_3():
    a = input()
    while a != 'stop':
        if 'ф' in a or 'Ф' in a:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')
        a = input()

def z3_4():
    import random
    n = 0
    x = 0
    while n < 3:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        ab = str(a) + ' + ' + str(b) + ' = '
        s = int(input(ab))
        if s == a + b:
            print('Правильно!')
            x += 1
        else:
            print('Ответ неверный')
            n += 1
    print('Правильных ответов: ', x)

print(z3_1(), z3_2(), z3_3(), z3_4())