# built-in
import os
import time
import inspect
import traceback

# topping
from topping.field import ToppingField


class ToppingModel:
    def __init__(self) -> None:
        self.name = ToppingField("name")
        self.path = ToppingField("path")
        self.args = ToppingField("args")
        self.kwargs = ToppingField("kwargs")
        self.runtime = ToppingField("runtime")
        self.returns = ToppingField("returns")
        self.error = ToppingField("error")

    def observe(self, func: callable, *args: any, **kwargs: any) -> None:
        try:
            # update fields value
            self.name.update(func.__name__)
            self.path.update(os.path.abspath(inspect.getfile(func)))
            self.args.update(args)
            self.kwargs.update(kwargs)

            # set start time
            self.start_time = time.time()

            # call origin function!
            self.returns.update(func(*args, **kwargs))
        except Exception:
            self.update_error()
        finally:
            self.runtime.update(time.time() - self.start_time)

    def update_error(self):
        error = traceback.format_exc().split("\n")

        # Stacks from 1 to 3 are created because of this topping module.
        # So, we delete it.
        del error[1:3]

        error = "\n".join(error)
        self.error.update(error)

    def get_return(self) -> any:
        return self.returns.value
