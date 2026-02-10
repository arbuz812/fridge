from datetime import datetime, timedelta


class Product:
    def __init__(self, name, price, shelf_life, production_date):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if shelf_life <= 0:
            raise ValueError("Срок годности должен быть положительным")
        if not isinstance(production_date, datetime):
            raise TypeError("Дата производства должна быть datetime")

        self._name = name
        self._price = price
        self._shelf_life = shelf_life
        self._production_date = production_date
        self._expiration_date = production_date + timedelta(days=shelf_life)

    def __str__(self):
        return f"Продукт: {self.name}, цена: {self.price}$, срок годности: {self.shelf_life} дней, дата производства: {self.production_date}, дата окончания срока годности:{self.expiration_date}"

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def shelf_life(self):
        return self._shelf_life

    @property
    def production_date(self):
        return self._production_date

    @property
    def expiration_date(self):
        return self._expiration_date

    def is_expired(self, today):
        if not isinstance(today, datetime):
            raise TypeError("Параметр 'today' должен быть типа datetime")
        return today > self.expiration_date
