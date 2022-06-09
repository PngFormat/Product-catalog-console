import time
from Balance import Balance
from Database import DataItems
from NumbeItems import Number


class Catalog(object):
    def __init__(self):

        self.id = 0
        self.cart = []
        self.summa = 0
        self.man_cloth = {'Рубашка клетчатая': 250,
                          'Кроссовки Adidas': 899,
                          'Футболка': 430,
                          'Костюм классический': 1499,
                          'Кепка': 299}  # Название : цена

        self.man_cloth_code = [2322, 2533, 2323, 1533, 4222]

        self.women_cloth = {'Блузка': 299,
                            'Пижама': 1110,
                            'Платье': 600,
                            'Рюкзак ': 780,
                            'Каблуки': 679}  # Название : цена
        self.women_cloth_code = [5343, 5132, 5666, 5777, 5656]

        self.accessories_jewelry = {'Золотая цепочка': 2500,
                                    'Серебрянное кольцо': 1450,
                                    'Браслет': 750,
                                    'Перстень с позолотой ': 1900,
                                    'Серьги': 1800}  # Название : цена
        self.accessories_code = [1311, 1312, 1313, 1354, 1231]

        self.casual_accessories = {'Пояс кожаный': 699,
                                   'Панама белая': 390,
                                   'Солнцезащитные очки': 650,
                                   'Чехол для телефона ': 340,
                                   'Шарф клетчатый': 699}  # Название : цена
        self.accessories_casual_code = [3313, 3456, 3133, 3154, 3645]

    def print_sum_of_bILL(self):

        print(f"Общая сумма к оплате составляет: {self.summa}")

    def clearing(self):
        for num in range(1, 100):
            print("\n")

    def exit_appplication(self):
        print(f"Возврат в меню...")
        return self.load()

    def input_balance(self):
        obj = Balance()


    def money(self):
        obj = Balance()
        number = obj.get_balance()
        change = number - int(self.summa)
        print("--------------------------")
        print(f"Оставшийся баланс для покупки: {change} ")
        print(f"Товар в корзине стоимостью на :{self.summa}")
        print("--------------------------")

    def itemsManCloth(self,code, number):
        num = Number()
        for goods in num.storeManCloth[code]:
            total_quantity_3 = goods['quantity']
            total_quantity_3 = total_quantity_3 - number
            if total_quantity_3 < 0:
                print("Товар закончился.Выберите меньшее кол-во...")

    def itemsWomenCloth(self,code, number):
        num = Number()
        for goods in num.storeWomenCloth[code]:
            total_quantity_3 = goods['quantity']
            total_quantity_3 = total_quantity_3 - number
            if total_quantity_3 < 0:
                print("Товар закончился.Выберите меньшее кол-во...")

    def itemsJewelry(self,code, number):
        num = Number()
        for goods in num.storeJewerly[code]:
            total_quantity_3 = goods['quantity']
            total_quantity_3 = total_quantity_3 - number
            if total_quantity_3 < 0:
                print("Товар закончился.Выберите меньшее кол-во...")

    def itemsCasual(self,code, number):
        num = Number()
        for goods in num.storeJewerly[code]:
            total_quantity_3 = goods['quantity']
            total_quantity_3 = total_quantity_3 - number
            if total_quantity_3 < 0:
                print("Товар закончился.Выберите меньшее кол-во...")
    def buy_product(self, value):
        num = Number()

        try:
            obj = Balance()
            number = obj.get_balance()

            if number >= self.summa:

                if value == 1:

                    key_list = [*self.man_cloth]

                    self.money()
                    valuesList_1 = [self.man_cloth[key] for key in self.man_cloth]

                    for i in range(5):
                        print(f"{key_list[i]}|||| Добавить в корзину--> {i + 1}  {valuesList_1[i]} $ ")

                    print(f"|||| Выйти--> 0 ||||  ")

                    buy = int(input())

                    if buy == 0:
                        self.clearing()
                        self.exit_appplication()

                    number = int(input("Введите кол-во товара: \n"))

                    if buy == 1:
                        self.itemsManCloth('2322', number)

                    if buy == 2:
                        self.itemsManCloth('2533', number)

                    if buy == 3:
                        self.itemsManCloth('1533', number)

                    if buy == 4:
                        self.itemsManCloth('2323', number)
                    if buy == 5:
                        self.itemsManCloth('4222', number)

                    self.summa += number * valuesList_1[buy - 1]
                    # сумма чека

                if value == 2:
                    key = [*self.women_cloth]
                    self.money()
                    valuesList = [self.women_cloth[key] for key in self.women_cloth]
                    for i in range(5):
                        print(f"{key[i]}|||| Добавить в корзину--> {i + 1}  {valuesList[i]} $ ")
                    print(f"|||| Выйти--> 0 ||||  ")
                    buy = int(input())
                    if buy == 0:
                        self.clearing()
                        self.exit_appplication()

                    number = int(input("Введите кол-во товара: \n"))

                    if buy == 1:
                        self.itemsWomenCloth('5343', number)
                    if buy == 2:
                        self.itemsWomenCloth('5132', number)
                    if buy == 3:
                        self.itemsWomenCloth('5666', number)
                    if buy == 4:
                        self.itemsWomenCloth('5777', number)
                    if buy == 5:
                        self.itemsWomenCloth('5656', number)

                    self.summa += number * valuesList[buy - 1]
                    print(self.summa)

                if value == 3:
                    key = [*self.accessories_jewelry]
                    self.money()
                    valuesList = [self.accessories_jewelry[key] for key in self.accessories_jewelry]
                    for i in range(5):
                        print(f"{key[i]}|||| Добавить в корзину--> {i + 1}  {valuesList[i]} $ ")
                    print(f"|||| Выйти--> 0 ||||  ")
                    buy = int(input())
                    if buy == 0:
                        self.clearing()
                        self.exit_appplication()

                    number = int(input("Введите кол-во товара: \n"))

                    if buy == 1:
                        self.itemsJewelry('1311', number)

                    if buy == 2:
                        self.itemsJewelry('1312', number)
                    if buy == 3:
                        self.itemsJewelry('1313', number)
                    if buy == 4:
                        self.itemsJewelry('1354', number)
                    if buy == 5:
                        self.itemsJewelry('1231', number)

                    self.summa += number * valuesList[buy - 1]
                    print(self.summa)

                if value == 4:
                    key = [*self.casual_accessories]
                    self.money()
                    valuesList = [self.casual_accessories[key] for key in self.casual_accessories]
                    for i in range(5):
                        print(f"{key[i]}|||| Добавить в корзину--> {i + 1}  {valuesList[i]} $ ")
                    print(f"|||| Выйти--> 0 ||||  ")
                    buy = int(input())
                    if buy == 0:
                        self.clearing()
                        self.exit_appplication()

                    number = int(input("Введите кол-во товара: \n"))

                    if buy == 1:
                        self.itemsCasual('3313', number)

                    if buy == 2:
                        self.itemsCasual('3456', number)

                    if buy == 3:
                        self.itemsCasual('3133', number)

                    if buy == 4:
                        self.itemsCasual('3354', number)

                    if buy == 5:
                        self.itemsCasual('3645', number)

                    self.summa += number * valuesList[buy - 1]
                    print(self.summa)

            else:
                print("Недостаточно денег для покупки...")
                time.sleep(2)
                self.exit_appplication()

            if value == 0:
                self.clearing()
                self.exit_appplication()

        except IndexError:
            print("Неверное значение...")
            self.buy_product(value)

    def add_category_product(self):
        num = Number()
        self.choose_category_product()

        choosen = int(input("Выберите подкатегорию:"))
        if choosen == 1:
            self.clearing()
            name_product = str(input("Введите название товара: "))
            price_product = int(input("Введите цену: "))
            code_product = int(input("Код товара: "))
            numberIt = int(input("Введите кол-во:"))

            num.man_cloth[name_product] = price_product

            d = {'price':price_product,'quantity':numberIt}
            num.storeManCloth[code_product] = d
            print(num.storeManCloth)


            print(d)

            self.man_cloth[name_product] = price_product
            print(f"Товар {name_product} добавлен...")
            self.exit_appplication()
        if choosen == 0:
            self.exit_appplication()

        if choosen == 2:
            self.clearing()
            name_product = str(input("Введите название товара: "))
            price_product = int(input("Введите цену: "))
            code_product = int(input("Код товара: "))
            numberIt = int(input("Введите кол-во:"))

            num.women_cloth[name_product] = price_product

            d = {'price': price_product, 'quantity': numberIt}
            num.storeWomenCloth[code_product] = d
            print(num.storeWomenCloth)

            self.women_cloth[name_product] = price_product
            print(f"Товар {name_product} добавлен...")

        if choosen == 3:
            self.clearing()
            name_product = str(input("Введите название товара: "))
            price_product = int(input("Введите цену: "))
            code_product = int(input("Код товара: "))
            numberIt = int(input("Введите кол-во:"))

            num.accessories_jewerly[name_product] = price_product

            d = {'price': price_product, 'quantity': numberIt}
            num.storeJewerly[code_product] = d
            print(num.storeJewerly)

            self.accessories_jewelry[name_product] = price_product
            print(f"Товар {name_product} добавлен...")

        if choosen == 4:
            self.clearing()
            name_product = str(input("Введите название товара: "))
            price_product = int(input("Введите цену: "))
            code_product = int(input("Код товара: "))
            numberIt = int(input("Введите кол-во:"))

            num.casual_accessories[name_product] = price_product

            d = {'price': price_product, 'quantity': numberIt}
            num.storeCasual[code_product] = d
            print(num.storeWomenCloth)

            self.casual_accessories[name_product] = price_product
            print(f"Товар {name_product} добавлен...")

    def load(self):
        "" "Запустить приложение" ""
        print("||||Добро пожаловать в электронный каталог товаров||||\n")

        while True:
            variant = int(input(print("1 - Выбрать категорию товаров(Purchase) \n"
                                      "2 - Добавления товара(Edit)\n"
                                      "3 - Удаление товара(Delete)\n"
                                      "4 - Поиск товара по коду\n"
                                      "5 - Сумма чека\n"
                                      "0 - Выход")))

            if variant == 1:
                self.clearing()

                self.choose_category_product()
                self.input_balance()
                choosen = int(input("Выберите подкатегорию:"))

                if choosen == 1:
                    self.clearing()
                    print(self.man_cloth)
                    print("1 - Добавить товар в корзину\n")
                    add_to_cart = int(input())
                    # Добавление в корзину

                    if add_to_cart == 1:
                        while choosen != 0:
                            self.buy_product(add_to_cart)
                    if choosen == 0:
                        self.exit_appplication()

                if choosen == 2:
                    self.clearing()
                    print(self.women_cloth)
                    print("2 - Добавить товар в корзину\n")
                    add_to_cart = int(input())

                    if add_to_cart == 2:
                        while choosen != 0:
                            self.buy_product(add_to_cart)

                if choosen == 3:
                    self.clearing()
                    print(self.accessories_jewelry)
                    print("3 - Добавить товар в корзину\n")
                    add_to_cart = int(input())
                    if add_to_cart == 3:
                        while choosen != 0:
                            self.buy_product(add_to_cart)

                # Повседневные украшения

                if choosen == 4:
                    self.clearing()
                    print(self.casual_accessories)
                    print("4 - Добавить товар в корзину\n")
                    add_to_cart = int(input())
                    if add_to_cart == 4:

                        while choosen != 0:
                            self.buy_product(add_to_cart)

            if variant == 2:
                self.add_category_product()
            if variant == 3:
                self.delete_product()
            if variant == 4:
                self.find_product_code()
            if variant == 5:
                self.print_sum_of_bILL()
            if variant == 0:
                quit()

    def choose_category_product(self):
        category = ['1-Одежда', '2-Аксессуары']
        subcategory_cloth = ['Мужская одежда', 'Женская одежда']
        print(category)
        choice = str(input("Выберите категорию:\n")).lower()

        if choice == '1':
            self.clearing()

            print("1 - Мужская одежда \n"
                  "2 - Женская одежда\n"
                  "0 - Выход(главное меню)")

        if choice == '2':
            print("3 - Ювелирные украшения \n"
                  "4 - Повседневные украшения\n"
                  "0 - Выход(главное меню)")
        if choice == 0:
            self.exit_appplication()

    def delete_product(self):
        self.clearing()
        self.choose_category_product()

        choosen = int(input("Выберите подкатегорию:"))
        if choosen == 1:
            self.clearing()
            print(self.man_cloth)
            name_product = str(input("Введите название товара: "))
            del self.man_cloth[name_product]
            print(f"Товар {name_product} удален...")
            self.exit_appplication()
        if choosen == 0:
            self.exit_appplication()

        if choosen == 2:
            self.clearing()
            name_product = str(input("Введите название товара: "))
            del self.women_cloth[name_product]
            print(f"Товар {name_product} удален...")

    def find_product_code(self):
        self.clearing()
        datab = DataItems()

        while True:

            print(f"Мужская одежда: {self.man_cloth_code}")
            print(f"Женская одежда: {self.women_cloth_code}")
            print(f"Ювелирные украшения: {self.accessories_code}")
            print(f"Повседневные аксессуары: {self.accessories_casual_code}")
            input_code = int(input("Введите код товара:\n "
                                   "0-Выйти в главное меню\n"))
            self.clearing()
            code = datab.items_code_database
            print("----------------------------------")
            fkey = next((k for k in code if code[k] == input_code), None)
            print(f"Товар под кодом {input_code} : {fkey}")
            print("----------------------------------")

            if input_code == 0:
                self.exit_appplication()
                self.clearing()


shop = Catalog()

shop.load()
