def z1():
    if int(input()) % 3 == 0:
        print('Да')
    else:
        print('Нет')

def z2():
    try:
        a = int(input())
        s = 100/a
    except ValueError:
        print('ошибка не число')
    except ZeroDivisionError:
        print('ошибка равно 0')
    else:
        print('равно ', s)

def z3():
    s = input('Впишите дату в виде 02.11.2022 ').split('.')
    if int(s[0]) * int(s[1]) == int(s[2][2:]):
        print('МАГИЯ')
    else:
        print('НЕ МАГИЯ')

def z4():
    s = input('Билет: ')
    if len(s) % 2 == 0:
        g = int(len(s)/2)
        s1 = 0
        s2 = 0
        for i in range(g):
            s1 += int(s[i])

        for i in range(g, len(s)):
            s2 += int(s[i])

        if s1 == s2:
            print('СЧАСТЛИВЫЙ')
        else:
            print('НЕСЧАСТНЫЙ')
    else:
        print('нечетное количество')

print(z1(), z2(), z3(), z4())