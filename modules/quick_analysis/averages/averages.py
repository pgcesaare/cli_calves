from modules.menu_builder import build_menu
from rich.console import Console

#calculations
from modules.quick_analysis.averages.avg_per_week import avg_per_week 
from modules.quick_analysis.averages.avg_per_day import avg_per_day


console = Console()

def averages_menu():

    options = {
        "1": "Avg. Calves Per Week",
        "2": "Avg. Calves Per Day"
    }

    
    result = build_menu(
        title="Averages",
        options=options,
        subtitle="Calculate average statistics",
    )

    if result == "1":
            avg_per_week()
            

    if result == "2":
            avg_per_day()

    if result == "exit":
        exit()