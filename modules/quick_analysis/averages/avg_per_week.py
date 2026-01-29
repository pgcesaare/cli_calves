from modules.panel_template import panel_template
from rich.console import Console, Group
from utils.get_avg import get_avg_per_week
from modules.table_template import df_to_rich_table
from rich.text import Text
import os

def avg_per_week():
        
        console = Console()

        while True:

            df, avg = get_avg_per_week()
                  
            table = df_to_rich_table(df=df, caption="Table - Avg. Per Week")
            avg_text = Text(f"\n\nAvg. per week: {avg}")

            content = Group(
                  table,
                  avg_text
            )

            panel_template(
                title="Avg. per week",
                subtitle="[O] to output table",
                content=content
            )

            choice = console.input("Select an option: ").strip().lower()

            if choice == "o":

                output_dir = "output"
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, "avg_per_week.csv")
                df.to_csv(output_path, index=False)
                console.print(f"[green]Table exported successfully to {output_path}[/green]")
                console.input("Press Enter to continue...")
                break
            
            if choice == "x":
                 exit()
            if choice == "m":
                break
            
