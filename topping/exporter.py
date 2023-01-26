# rich
from rich import print
from rich.text import Text
from rich.panel import Panel
from rich.console import group
from rich.padding import Padding
from rich.console import Console
from rich.pretty import pprint

# topping
from topping.field import ToppingField
from topping.model import ToppingModel


class ToppingExporter:
    def __init__(self) -> None:
        self.console = Console()

    @group()
    def get_panels(self, model):
        path = [
            (" <function 'sum'", "yellow1"),
            (" at /mnt/d/project/topping/main.py> ", "dark_orange"),
        ]

        path_text = Text.assemble(*path, justify="center")

        fields = [
            ("\n args: ", "gold1"),
            (f"{model.args.value}\n", "spring_green2"),
            ("\n kwargs: ", "gold1"),
            (f"{model.kwargs.value}\n", "spring_green2"),
            ("\n runtime: ", "gold1"),
            (f"{model.runtime.value}\n", "spring_green2"),
            ("\n return: ", "gold1"),
            (f"{model.returns.value}\n", "spring_green2"),
        ]

        fields_text = Text.assemble(*fields)

        yield Panel(
            path_text,
            title="path",
            style="spring_green2",
        )

        yield Padding("")

        yield Panel(
            fields_text,
            title="fields",
            style="steel_blue1",
        )

        yield Padding("")

        if model.error.updated:
            error_text = Text(f"\n{model.error.value}", style="light_salmon1")

            yield Panel(
                error_text,
                title="error",
                style="bright_red",
            )

    def export(self, model: ToppingModel) -> None:

        print(Panel(self.get_panels(model), expand=False))
