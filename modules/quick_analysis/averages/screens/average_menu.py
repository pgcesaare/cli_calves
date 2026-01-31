from modules.menu_builder import build_menu
from rich.console import Console

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
            console.print("Avg. Calves")
    if result == "2":
            console.print("Avg. Calves Per Seller")

    if result == "3":
            console.print("Avg. Calves Per Breed")

    if result == "4":
            console.print("Calves Per Seller Per Breed")

    if result == "exit":
        exit()