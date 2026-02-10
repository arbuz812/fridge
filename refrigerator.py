from datetime import datetime
from product import Product
from user import User
from door import Door


class Refrigerator:
    def __init__(self, capacity_main, capacity_freezer, owner_name):
        if (not isinstance(capacity_main, int) or capacity_main <= 0) + \
                (not isinstance(capacity_freezer, int) or capacity_freezer <= 0) >= 1:
            raise ValueError("Вместимость должна быть положительным числом!")
        self._capacity_main = capacity_main
        self._capacity_freezer = capacity_freezer
        self._main_products = []
        self._freezer_products = []
        self._owner = User(owner_name, is_owner=True)
        self._current_user = None
        self._doors = {
            "основная": Door("основная"),
            "морозилка": Door("морозилка")
        }

    def __str__(self):
        names_main = [p.name for p in self._main_products]
        names_freezer = [p.name for p in self._freezer_products]
        return f"""Основная камера ({len(self._main_products)}/{self._capacity_main}): {', '.join(names_main) if names_main else 'пуст'}
Морозильная камера ({len(self._freezer_products)}/{self._capacity_freezer}): {', '.join(names_freezer) if names_freezer else 'пуст'}"""

    def add(self, product, zone):
        if self._current_user is None:
            print("Сначала авторизуйтесь")
            return False
        if not self._current_user.is_owner:
            print("У вас нет прав для этого действия")
            return False
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты.")
        if zone == 'основная':
            if len(self._main_products) < self._capacity_main:
                self._main_products.append(product)
                print("Продукт успешно добавлен в холодильник")
                return True
            else:
                print("Холодильник полон.Нельзя добавить продукт.")
                return False
        elif zone == 'морозилка':
            if len(self._freezer_products) < self._capacity_freezer:
                self._freezer_products.append(product)
                print("Продукт успешно добавлен в холодильник")
                return True
            else:
                print("Холодильник полон.Нельзя добавить продукт.")
                return False
        else:
            raise ValueError(
                "Вы можете использовать только основную и морозильную камеры.")

    def remove(self, name, zone):
        if self._current_user is None:
            print("Сначала авторизуйтесь")
            return False
        if not self._current_user.is_owner:
            print("У вас нет прав для этого действия")
            return False
        if zone == 'основная':
            for i, product in enumerate(self._main_products):
                if name == product.name:
                    del self._main_products[i]
                    print(f"Продукт '{name}' успешно удален.")
                    return True

            print(f"Продукт '{name}' не найден.")
            return False
        elif zone == 'морозилка':
            for i, product in enumerate(self._freezer_products):
                if name == product.name:
                    del self._freezer_products[i]
                    print(f"Продукт '{name}' успешно удален.")
                    return True

            print(f"Продукт '{name}' не найден.")
            return False

        else:
            raise ValueError(
                "Вы можете использовать только основную и морозильную камеры.")

    def get_expired(self, today, zone):
        if not isinstance(today, datetime):
            raise TypeError("Параметр 'today' должен быть типа datetime")
        if zone == 'основная':
            expire = [
                product.name for product in self._main_products if product.is_expired(today)]
            print(f"Просроченные: {', '.join(expire)}")
        elif zone == 'морозилка':
            expire = [
                product.name for product in self._freezer_products if product.is_expired(today)]
            print(f"Просроченные: {', '.join(expire)}")
        else:
            raise ValueError(
                "Вы можете использовать только основную и морозильную камеры.")

    def is_full(self, zone):
        if zone == 'основная':
            return len(self._main_products) == self._capacity_main
        elif zone == 'морозилка':
            return len(self._freezer_products) == self._capacity_freezer
        else:
            raise ValueError(
                "Вы можете использовать только основную и морозильную камеры.")

    def login(self, name):
        if name == self._owner.name:
            self._current_user = self._owner
        else:
            self._current_user = User(name, is_owner=False)

    def open_door(self, door_name):
        door = self._doors.get(door_name)
        if door is None:
            print(f"Дверь '{door_name}' не существует.")
            return False
        door.open()

    def close_door(self, door_name):
        door = self._doors.get(door_name)
        if door is None:
            print(f"Дверь '{door_name}' не существует.")
            return False
        door.close()

    def get_current_user_info(self):
        if self._current_user is None:
            return "Не авторизован"
        role = "владелец" if self._current_user.is_owner else "гость"
        return f"{self._current_user.name} ({role})"
