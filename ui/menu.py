from rich.console import Console
from services.show_menu import show_menu
from context.context import file
from services.import_data import import_data
from modules.quick_analysis.qa_menu import qa_menu

console = Console()

def main():
    import_data()
    while True:

        #extracting file name from context
        file_text = file.get() if file.get() else "No file loaded"
        
        #menu loaded
        show_menu(file_text)

        choice = console.input("\nSelect an option: ")

        if choice == "1":
            console.print("\nInventory selected")
            console.input("Press ENTER to continue")

        elif choice == "2":

            qa_menu()

        elif choice == "3":
            console.print("\nDeath Report selected")
            console.input("Press ENTER to continue")
        
        elif choice == "4" or choice.lower() == "x":
            console.print("\nExiting...")
            break

        else:
            console.print("[red]\nInvalid option\n[/red]")
            console.input("Press ENTER to continue")

