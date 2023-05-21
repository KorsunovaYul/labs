from tkinter import *

def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Морожка", 'кафе', ['ваниль', 'клубника', 'шоколад'])
    s.ice_flavors()
def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')


    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors, place, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def ice_flavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

        def plusflav(self):
            self.flavors.append(input('Введите новый сорт '))

        def minusflav(self):
            self.flavors.remove(input('Введите сорт, который хотите удалить '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('Такой есть')
            else:
                print('Нет в наличии')

    class Napalochke(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, material):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.material = material

        def palochka(self):
            print('Материал палочки: ', self.material)

    class Vstakane(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, sale):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.sale = sale

        def stakan(self):
            print('Размер стакана:', self.sale, 'ml')



    s = IceCreamStand("Морожка", 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Садовая', '6:00-18:00')
    s.describe_restaurant()
    s.plusflav()
    s.ice_flavors()
    s.minusflav()
    s.ice_flavors()
    s.poisk()

    s = Vstakane('Морожка', 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Садовая', '6:00-18:00', '400')
    s.stakan()

    s = Napalochke('Морожка', 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Садовая', '6:00-18:00', 'красное дерево')
    s.palochka()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Морожка", 'кафе', ['ваниль', 'клубника', 'шоколад'])


    root = Tk()
    root['bg'] = 'lightgreen'
    root.title('Морожка')
    root.geometry('250x250')
    root.resizable(width=False, height=False)

    frame1 = Frame(root, bg='white', bd=1)
    frame1.place(relx=0.1, rely= 0.1, relwidth=0.8, relheight=0.1)

    title1 = Label(frame1, text='Виды мороженного:', bg='white', font=30)
    title1.pack()

    frame2 = Frame(root, bg='white', bd=1)
    frame2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    for i in s.flavors:
        title2 = Label(frame2, text=i, bg='white', font=30 )
        title2.pack()

    root.mainloop()


z1()
z2()
z3()

