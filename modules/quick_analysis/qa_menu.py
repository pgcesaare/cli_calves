from modules.menu_builder import build_menu
from modules.quick_analysis.averages.averages_main_menu import averages_menu
from rich.console import Console
console = Console()

def qa_menu():

    options = {
    "1": "Totals",
    "2": "Averages",
    }

    
    result = build_menu(
        title="Quick Analysis",
        subtitle="Summary Statistics",
        options=options,
    )

    if result == "2":
        averages_menu()

    if result == "exit":
        exit()