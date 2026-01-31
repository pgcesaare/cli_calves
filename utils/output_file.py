import os
from datetime import datetime
import pandas as pd
from rich.console import Console

def output_file(df, filename_prefix):
        console = Console()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{filename_prefix}_{timestamp}.csv")
        df.to_csv(output_path, index=False)
        console.print(f"[green]Table exported successfully to {output_path}[/green]")
        console.input("Press Enter to continue...")