class ToppingField:
    def __init__(self, name, value=None) -> None:
        self.name = name
        self.value = value
        self.updated = False

    def update(self, value) -> None:
        self.value = value
        self.updated = True
