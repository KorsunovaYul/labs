from PIL import Image, ImageFont, ImageDraw

def z1():
    i = Image.open('lab8/8 мар.jpg')
    i.show()

    print('Размер', i.size, 'Формат', i.format , 'Цветовая модель', i.mode)
    i = i.crop((100, 75, 300, 150))
    i.show()
    i.save('lab8/1.0.jpg')

def z2():
    s = {'8 марта': 'lab8/8 мар.jpg', '23 февраля': 'lab8/23 фев.jpg',
        'новый год': 'lab8/нг.jpg', '1 сентября': 'lab8/1сен.jpg'}

    i = input('К какому празднику нужна открытка?')
    k = Image.open(s[i])
    k.show()

def z3():
    i = Image.open('lab8/8 мар.jpg')
    n = input('Имя, кого вы хотите поздравить?')
    font = ImageFont.truetype("lab8/arial_bold.ttf", 35)
    d = ImageDraw.Draw(i)
    d.text((30, 60), n + ", поздравляю!", font = font, fill = 'red')

    i.show()
    i.save('lab8/pozdrav')

z1()
z2()
z3()