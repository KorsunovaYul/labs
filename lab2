def z1():
    k1 = input("Введите пароль ")

    if len(k1) < 5:
        print("Пароль слишком короткий")
    else:
        k2 = input("Введите еще раз чтобы подтвердить ")
        if k2 != k1:
            print("Неправильное подтверждение")
        else:
            print("Пароль записан")

def z2():
    n = int(input("Номер? "))

    if n % 2 == 0 and n in range(1, 37):
        print('Верх')
    if n % 2 != 0 and n in range(1, 37):
        print('Низ')

    if n % 2 == 0 and n in range(37, 55):
        print('Верх боковушки')
    if n % 2 != 0 and n in range(37, 55):
        print('Низ боковушки')

    if n > 54:
        print('Неправильный номер')

def z3():
    y = int(input('Введите номер года'))
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print('Год ', y, ' - високосный')
    else:
        print('Это год не високосный')

def z4():
    c1 = input('1 цвет ')
    c2 = input('2 цвет ')

    q = 'желтый'
    w = 'красный'
    e = 'синий'

    if (c1 == w or c2 == w) and (c1 == e or c2 == e):
        print('фиолетовый')
    if (c1 == w or c2 == w) and (c1 == q or c2 == q):
        print('оранжевый')
    if (c1 == e or c2 == e) and (c1 == q or c2 == q):
        print('зеленый')


def z5():
    n = int(input('Сколько слов?'))
    s = ''
    for i in range(n):
        a = input()
        s += a + ' '
    print(s)
