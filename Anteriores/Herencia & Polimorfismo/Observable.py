class Observable:
    def __init__(self, value=None):
        self._subs = []
        self._value = value

    def subscribe(self, callback):
        self._subs.append(callback)
        if self._value is not None:
            callback(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for cb in self._subs:
            cb(new_value)