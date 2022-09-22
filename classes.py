class Storage:
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, quantity: int):  #Увеличивает запас items
        if name in self._items.keys():
            self._items[name] += quantity
        else:
            self._items[name] = quantity

    def remove(self, name: str, quantity: int):  #уменьшает запас items
        if self._items[name] - quantity < 0:
            return False
        else:
            self._items[name] -= quantity

    @property
    def get_free_space(self) -> int:  #Возвращает кол-во свободных мест
        return self._capacity - sum(self._items.values())

    @property
    def get_items(self) -> dict:  #возвращает сожержание склада в словаре {товар: количество}
        return self._items

    @property
    def get_unique_items_count(self):  #возвращает количество уникальных товаров.
        return len(self._items.keys())


class Store(Storage):
    def __init__(self, items: dict, capacity: int=100):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_free_space >= quantity:
            super().add(name,quantity)
            return True


class Shop(Storage):
    def __init__(self, items: dict, capacity: int=20):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_free_space >= quantity:
            super().add(name,quantity)
            return True

class Request:
    def __init__(self, user_from_carry: str, user_to_carry: str, user_amount: int, user_product: str):
        self.from_carry: str = user_from_carry
        self.to_carry: str = user_to_carry
        self.amount: int = user_amount
        self.product: str = user_product

    def __repr__(self):
        return f'{self.amount} {self.product} из {self.from_carry} в {self.to_carry}'
