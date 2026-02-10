class User:
    def __init__(self, name, is_owner=False):
        self._name = name
        self._is_owner = is_owner

    @property
    def name(self):
        return self._name

    @property
    def is_owner(self):
        return self._is_owner
