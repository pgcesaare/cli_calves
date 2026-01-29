from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import pandas as pd

from ui.services.import_data import import_data
from ui.styles import PRIMARY_COLOR

console = Console()


def show_menu():
    console.clear()

    menu = Text()
    
    menu.append("\n1) Inventory\n")
    menu.append("\n2) Quick Analysis\n")
    menu.append("\n3) Death Report\n")

    panel = Panel(
        Align.center(menu),
        title=f"[bold {PRIMARY_COLOR}]MAIN MENU — Gold Star[/bold {PRIMARY_COLOR}]",
        subtitle=f"[{PRIMARY_COLOR}]Select Analysis Option, [X] to exit! [/{PRIMARY_COLOR}]",
        border_style=PRIMARY_COLOR,
        padding=(1, 2),
    )

    console.print(panel)





def main():

    data = import_data()

    while True:
        show_menu()

        choice = console.input("\nSelect an option: ")

        if choice == "1":
            console.print("\nInventory selected")
            console.input("Press ENTER to continue")

        elif choice == "2":
            console.print("\nQuick Analysis selected")
            console.input("Press ENTER to continue")

        elif choice == "3":
            console.print("\nDeath Report selected")
            console.input("Press ENTER to continue")
        
        elif choice == "4" or choice.lower() == "x":
            console.print("\nExiting...")
            break

        else:
            console.print("\nInvalid option")
            console.input("Press ENTER to continue")

