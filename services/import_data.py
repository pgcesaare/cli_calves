from rich.console import Console
from rich.panel import Panel
from context.context import file, data
from ui.styles import PRIMARY_COLOR
from utils.get_files import get_excel_files
import pandas as pd
import os

console = Console()

def import_data():

    while True:
        console.clear()

        files = get_excel_files()

        if not files:
            console.print("[red]No Excel files found[/red]")
            console.input("Press ENTER to exit")
            return None

        files_text = "\n".join(
            f"{i+1}) {os.path.basename(f)}"
            for i, f in enumerate(files)
        )

        panel = Panel(
            files_text,
            title=f"[bold {PRIMARY_COLOR}]Files Available[/bold {PRIMARY_COLOR}]",
            border_style=PRIMARY_COLOR,
            subtitle=f"[{PRIMARY_COLOR}]Select a file by number, [X] to exit![/{PRIMARY_COLOR}]",
            padding=(1, 2),
        )

        console.print(panel)

        choice = console.input("\nSelect file number: ").strip().lower()

        if choice == "0":
            continue

        if choice == "x":
            return exit()

        try:
            index = int(choice) - 1

            if index < 0 or index >= len(files):
                raise IndexError

            file_path = files[index]

            #data for context
            file.set(file_path.split('.')[0])
            data.set(pd.read_excel(file_path))

            console.print(
                f"\n[{PRIMARY_COLOR}]Loaded:[/{PRIMARY_COLOR}] {os.path.basename(file_path)}"
            )

            confirm = console.input(
                "\nPress ENTER to confirm or [0] to go back: "
            )

            if confirm == "0":
                continue

            return data

        except ValueError:
            console.print("[red]Please enter a valid number[/red]")
        except IndexError:
            console.print("[red]Number out of range[/red]")
        except PermissionError:
            console.print("[red]File is open or locked (Excel / OneDrive)[/red]")
        except Exception as e:
            console.print(f"[red]Error loading file: {e}[/red]")

        console.input("\nPress ENTER to try again")