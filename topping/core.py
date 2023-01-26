from topping.model import ToppingModel
from topping.exporter import ToppingExporter


class Topping:
    def __init__(self, func) -> None:
        self.func = func

        self.model = ToppingModel()
        self.exporter = ToppingExporter()

    def __call__(self, *args: any, **kwargs: any):
        self.model.observe(self.func, *args, **kwargs)
        self.exporter.export(self.model)

        return self.model.get_return()


topping = Topping
