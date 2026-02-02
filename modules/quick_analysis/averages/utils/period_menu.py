from modules.menu_builder import build_menu
from rich.console import Console

console = Console()

def period_menu(title, subtitle):

    options = {
          
        "1": "Daily",
        "2": "Weekly",
        "3": "Monthly"

    }
    
    result = build_menu(
        title=title,
        options=options,
        subtitle=subtitle,
    )

    if result == "1":
        return "daily"
    if result == "2":
        return "weekly"
    if result == "3":
        return "monthly"
    