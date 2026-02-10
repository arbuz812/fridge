class Door:
    def __init__(self, name):
        self._name = name
        self._is_open = False

    def open(self):
        self._is_open = True
        print(f"Дверь {self._name} открыта")

    def close(self):
        self._is_open = False
        print(f"Дверь {self._name} закрыта")
