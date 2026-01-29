from modules.panel_template import panel_template
from rich.text import Text
from rich.console import Console

console = Console()

def build_menu(title: str, subtitle: str, options: dict, callbacks: dict = None):
    """
    Constructor de menú genérico
    
    Args:
        title: Título del menú
        subtitle: Subtítulo del menú
        options: Dict con {key: label} ej: {"1": "Averages", "2": "Totals"}
        callbacks: Dict opcional con {key: function} para ejecutar
    
    Returns:
        La opción seleccionada
    """
    # Construir texto del menú
    menu_text = Text()

    for key, label in options.items():
        menu_text.append(f"\n{key}) {label}\n")
    
    while True:

        panel_template(title, subtitle, menu_text)
        
        choice = console.input("\nSelect an option: ").strip().lower()
        
        # Opciones especiales
        if choice == "m":
            return "back"
        if choice == "x":
            return "exit"
        
        # Validar opción
        if choice in options:
            # Si hay callback, ejecutarlo
            if callbacks and choice in callbacks:
                callbacks[choice]()
            else:
                choice
            
            return choice
        else:
            console.print("[red]Invalid option[/red]")
            console.input("Press ENTER to continue")