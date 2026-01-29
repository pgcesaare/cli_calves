from modules.menu_builder import build_menu
from rich.console import Console
console = Console()
def qa_menu():

    options = {
    "1": "Averages",
    }

    
    result = build_menu(
        title="Quick Analysis",
        subtitle="Summary Statistics",
        options=options,
    )

    print(result)
    console.input("Press ENTER to continue")
    if result == "exit":
        exit()