from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from ui.styles import PRIMARY_COLOR


def show_menu(file):
    console = Console()
    console.clear()
    menu = Text()

    #menu options
    menu.append("\n1) Inventory\n")
    menu.append("\n2) Quick Analysis\n")
    menu.append("\n3) Death Report\n")

    panel = Panel(
        Align.center(menu),
        title=f"[bold {PRIMARY_COLOR}]MAIN MENU — {file}[/bold {PRIMARY_COLOR}]",
        subtitle=f"[{PRIMARY_COLOR}]Select Option, [X] to exit! [/{PRIMARY_COLOR}]",
        border_style=PRIMARY_COLOR,
        padding=(1, 2),
    )

    console.print(panel)