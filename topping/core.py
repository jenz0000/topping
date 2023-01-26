from topping.model import ToppingModel


class Topping:
    def __init__(self, func) -> None:
        self.func = func
        self.model = ToppingModel()

    def __call__(self, *args: any, **kwargs: any):
        return self.model.observe(self.func, *args, **kwargs)


topping = Topping
