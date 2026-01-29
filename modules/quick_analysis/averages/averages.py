from modules.menu_builder import build_menu
from rich.console import Console

#calculations
from modules.quick_analysis.averages.avg_per_week import avg_per_week
console = Console()

def averages_menu():

    options = {
        "1": "Avg. Calves per Week",
    }

    
    result = build_menu(
        title="Averages",
        options=options,
        subtitle="Calculate average statistics",
    )

    if result == "1":
            avg_per_week()
            

    if result == "exit":
        exit()