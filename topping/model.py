import time
import traceback


class ToppingModel:
    def __init__(self) -> None:
        self.args = ToppingField("args")
        self.kwargs = ToppingField("kwargs")
        self.runtime = ToppingField("runtime")
        self.returns = ToppingField("returns")
        self.error = ToppingField("error")

    def observe(self, func: callable, *args: any, **kwargs: any) -> any:
        try:
            start_time = time.time()

            self.args.update(args)
            self.kwargs.update(kwargs)
            self.returns.update(func(*args, **kwargs))
            self.runtime.update(time.time() - start_time)

        except:
            self.error.update(traceback.format_exc())
            self.returns.update(None)

        print(f"args: {self.args.value}")
        print(f"kwargs: {self.kwargs.value}")
        print(f"runtime: {self.runtime.value}")
        print(f"returns: {self.returns.value}")
        print(f"error: {self.error.value}")

        return self.returns


class ToppingField:
    def __init__(self, name, value=None) -> None:
        self.name = name
        self.value = value
        self.updated = False

    def update(self, value) -> None:
        self.value = value
        self.updated = True
