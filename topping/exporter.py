# built-in
from collections.abc import Generator

# rich
from rich.text import Text
from rich.panel import Panel
from rich.console import group
from rich.padding import Padding
from rich import print as rich_print

# topping
from topping.field import ToppingField
from topping.model import ToppingModel


class ToppingExporter:
    @group()
    def get_panels(self, model: ToppingModel) -> Generator:
        yield self.get_path_panel(model)
        yield self.get_padding()
        yield self.get_fields_panel(model)

        if model.error.updated:
            yield self.get_padding()
            yield self.get_error_panel(model)

    def get_padding(self) -> Padding:
        return Padding("")

    def get_path_panel(self, model: ToppingModel) -> Panel:
        text = [
            (f" <function '{model.name.value}'", "yellow1"),
            (f" at {model.path.value}> ", "dark_orange"),
        ]

        panel_text = Text.assemble(*text, justify="center")

        return Panel(panel_text, title="path", style="spring_green2")

    def get_fields_panel(self, model: ToppingModel) -> Panel:
        text = [
            ("\n args: ", "gold1"),
            (f"{model.args.value}\n", "spring_green2"),
            ("\n kwargs: ", "gold1"),
            (f"{model.kwargs.value}\n", "spring_green2"),
            ("\n runtime: ", "gold1"),
            (f"{model.runtime.value:.20f}\n", "spring_green2"),
            ("\n return: ", "gold1"),
            (f"{model.returns.value}\n", "spring_green2"),
        ]

        panel_text = Text.assemble(*text)

        return Panel(panel_text, title="fields", style="steel_blue1")

    def get_error_panel(self, model: ToppingModel) -> Panel:
        error_text = Text(f"\n{model.error.value}", style="light_salmon1")

        return Panel(error_text, title="error", style="bright_red")

    def export(self, model: ToppingModel) -> None:
        panel = Panel(self.get_panels(model), expand=False)

        rich_print(panel)
