from PIL import Image, ImageFilter

def z1():
    i = Image.open('3.jpg')
    i.show()

    print('Размер', i.size, 'Формат', i.format , 'Цветовая модель', i.mode)

def z2():
    i = Image.open('3.jpg')

    i1 = i.reduce(3)
    i1.save('3_1.jpg')

    i2 = i.transpose(Image.FLIP_TOP_BOTTOM)
    i2.save('3_2.jpg')

    i3 = i.transpose(Image.FLIP_LEFT_RIGHT)
    i3.save('3_3.jpg')

def z3():
    for i in range(1, 6):
        k = Image.open(str(i) + '.jpg')
        k = k.filter(ImageFilter.SHARPEN)
        k.save('z3/' + str(i) + '.jpg')
        k.show()

def z4():
    i = Image.open('watermark.png')
    f = Image.open('1.jpg')

    f.paste(i, (50, 50), i)

    f.save('vodznak.jpg')
    f.show()

z4()