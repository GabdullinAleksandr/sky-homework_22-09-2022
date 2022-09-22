from classes import Storage, Shop, Store, Request

def main():
    store_items: dict = {'Печеньки': 20, 'Коробки': 25, 'Конфеты': 5, 'Бутылки': 15, 'Шарики': 10, 'Мячики': 5}
    shop_items: dict = {'Печеньки': 5, 'Конфеты': 5, 'Коробки': 2}
    store = Store(store_items)
    shop = Shop(shop_items)
    while True:
        print(f'Программа: Товары на Складе: {store.get_items}\n'
              f'Программа: Кол-во свободного места на Складе: {store.get_free_space}\n'
              f'Программа: Товары в Магазине: {shop.get_items}\n'
              f'Программа: Кол-во свободного места в Магазине: {shop.get_free_space}\n')
        print('Программа: Введите Ваш запрос, если желаете остановить программу введите "stop"')
        user_from_carry: str = input('Пользователь: Откуда(Склад или Магазин) - ').title()
        user_to_carry: str = input('Пользователь: Куда(Склад или Магазин) - ').title()
        try:
            user_amount: int = int(input('Пользователь: Сколько - '))
        except:
            break
        user_product: str = input('Пользователь: Что(Печеньки, Коробки, Конфеты, Бутылки, Шарики, Мячики) - ').title()
        us_input: str = user_from_carry + user_to_carry + str(user_amount) + user_product
        if 'stop' in us_input:
            break
        request = Request(user_from_carry, user_to_carry, user_amount, user_product)
        print(f'Доставить {request}')
        if user_from_carry == 'Склад':
            if shop.get_free_space < user_amount:
                print('В магазине не хватает места')
                continue
            if shop.get_unique_items_count >= 4:
                print('Превышено кол-во уникальных товаров')
                continue
            if store.remove(user_product, user_amount) == False:
                print('Программа: На складе не хватает товара')
                continue
            else:
                print('Программа: На складе достаточно товара ')
                if shop.add(user_product, user_amount):
                    print(f'Курьер доставляет {request}')
        else:
            if store.get_free_space < user_amount:
                print('На складе не хватает места')
                continue
            if shop.remove(user_product, user_amount) == False:
                print('Программа: В магазине не зватает товара')
            else:
                print('Программа: В магазине достаточно товара ')
                if store.add(user_product, user_amount):
                    print(f'Курьер доставляет {request}')


if __name__ == '__main__':
    main()

