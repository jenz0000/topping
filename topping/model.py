# built-in
import time
import traceback


# topping
from topping.field import ToppingField


class ToppingModel:
    def __init__(self) -> None:
        self.func = ToppingField("func")
        self.args = ToppingField("args")
        self.kwargs = ToppingField("kwargs")
        self.runtime = ToppingField("runtime")
        self.returns = ToppingField("returns")
        self.error = ToppingField("error")

    def observe(self, func: callable, *args: any, **kwargs: any) -> None:
        try:
            start_time = time.time()

            self.func.update(func.__name__)
            self.args.update(args)
            self.kwargs.update(kwargs)
            self.returns.update(func(*args, **kwargs))
            self.runtime.update(time.time() - start_time)

        except:
            error = traceback.format_exc()
            error = error.split("\n")

            del error[1:3]

            error = "\n".join(error)

            error = "".join(error)

            self.error.update(error)
            self.returns.update(None)

    def get_return(self) -> any:
        return self.returns.value
