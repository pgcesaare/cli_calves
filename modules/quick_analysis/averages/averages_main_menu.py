from modules.menu_builder import build_menu
from rich.console import Console

from modules.quick_analysis.averages.utils.period_menu import period_menu
from modules.quick_analysis.averages.utils.average_controller import average_controller
from modules.quick_analysis.averages.utils.sellers_controller import sellers_controller

console = Console()

def averages_menu():

    options = {
          
        "1": "Avg. Calves",
        "2": "Avg. Calves Per Seller",
        "3": "Avg. Calves Per Breed",
        "4": "Avg. Calves Per Seller Per Breed"

    }

    
    result = build_menu(
        title="Averages",
        options=options,
        subtitle="Calculate average statistics",
    ) 

    #options logic
    if result == "1": 
        period = period_menu("Select Period for Avg. Calves", "Choose the time frame")
        average_controller(period)

    elif result == "2":
        period = period_menu("Select Period for Avg. Calves Per Seller", "Choose the time frame")
        sellers_controller(period)

    elif result == "3":
        console.print("Avg. Calves Per Breed")

    elif result == "4":
        console.print("Calves Per Seller Per Breed")
        
    elif result == "exit":
        exit()