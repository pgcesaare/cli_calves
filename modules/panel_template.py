from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from ui.styles import PRIMARY_COLOR

def panel_template(title, subtitle, content):
    from rich.console import Console
    from rich.panel import Panel
    from rich.align import Align
    from ui.styles import PRIMARY_COLOR

    console = Console()
    console.clear()

    panel = Panel(
        Align.center(content),
        title=f"[bold {PRIMARY_COLOR}]{title}[/bold {PRIMARY_COLOR}]",
        subtitle=f"[{PRIMARY_COLOR}]{subtitle}, [X] to exit, [M] to main menu[/{PRIMARY_COLOR}]",
        border_style=PRIMARY_COLOR,
        padding=(1, 2),
    )

    console.print(panel)