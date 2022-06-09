class Number(object):

    man_cloth = {
        'Рубашка клетчатая': '2322',
        'Кроссовки Adidas': '2533',
        'Футболка': '2323',
        'Костюм классический': '1533',
        'Кепка': '4222' # Название : код
    }

    storeManCloth = {
        '2322': [
            {
                'quantity': 10,
                'price': 250,
            },
        ],
        '2533': [
            {
                'quantity': 5,
                'price': 899,
            },
        ],
        '2323': [
            {
                'quantity': 2,
                'price': 430,
            },

        ],
        '1533': [
            {
                'quantity': 11,
                'price': 1499,
            },

        ],
        '4222': [
            {
                'quantity': 15,
                'price': 299,
            },

        ],
    }

    women_cloth = {
        'Блузка': '5343',
        'Пижама': '5132',
        'Платье': '5666',
        'Рюкзак ': '5777',
        'Каблуки':  '5656'


    }

    storeWomenCloth = {
        '5343': [
            {
                'quantity': 15,
                'price': 299,
            },
        ],
        '5132': [
            {
                'quantity': 5,
                'price': 1110,
            },
        ],
        '5666': [
            {
                'quantity': 2,
                'price': 600,
            },

        ],
        '5777': [
            {
                'quantity': 9,
                'price': 780,
            },

        ],
        '5656': [
            {
                'quantity': 4,
                'price': 679,
            },

        ],
    }

    accessories_jewerly ={
        'Золотая цепочка': '1311',
        'Серебрянное кольцо': '1312',
        'Браслет': '1313',
        'Перстень с позолотой ': '1354',
        'Серьги': '1231'

    }

    storeJewerly = {
        '1311': [
            {
                'quantity': 13,
                'price': 299,
            },
        ],
        '1312': [
            {
                'quantity': 5,
                'price': 1110,
            },
        ],
        '1313': [
            {
                'quantity': 11,
                'price': 600,
            },

        ],
        '1354': [
            {
                'quantity': 7,
                'price': 780,
            },

        ],
        '1231': [
            {
                'quantity': 5,
                'price': 679,
            },

        ],
    }

    casual_accessories = {
        'Пояс кожаный': '3313',
        'Панама белая':  '3456',
        'Солнцезащитные очки':  '3133',
        'Чехол для телефона ': '3154',
        'Шарф клетчатый':'3645'
    }

    storeCasual = {
        '3313': [
            {
                'quantity': 27,
                'price': 299,
            },
        ],
        '3456': [
            {
                'quantity': 5,
                'price': 1110,
            },
        ],
        '3133': [
            {
                'quantity': 2,
                'price': 600,
            },

        ],
        '3154': [
            {
                'quantity': 8,
                'price': 780,
            },

        ],
        '3645': [
            {
                'quantity': 13,
                'price': 679,
            },

        ],
    }

    for title, code in man_cloth.items():
        total_quantity = 0
        total_cost = 0
        for goods in storeManCloth[code]:
            total_quantity += goods['quantity']

        print(title, " - ", total_quantity, " шт")