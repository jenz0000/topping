class Topping:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        print("hi i am topping!")
        return self.func(*args, **kwargs)


topping = Topping
