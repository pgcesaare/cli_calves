from modules.menu_builder import build_menu
from rich.console import Console

console = Console()

def period_menu(title, subtitle):

    options = {
          
        "1": "Monthly",
        "2": "Weekly",
        "3": "Daily",

    }
    
    result = build_menu(
        title=title,
        options=options,
        subtitle=subtitle,
    )
    
    return result