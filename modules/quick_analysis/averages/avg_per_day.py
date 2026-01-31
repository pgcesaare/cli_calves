from modules.panel_template import panel_template
from rich.console import Console, Group
from utils.get_avg import get_avg_per_day
from modules.table_template import df_to_rich_table
from rich.text import Text
from utils.output_file import output_file

def avg_per_day():
        
        console = Console()

        while True:

            df, avg = get_avg_per_day()
            
            table = df_to_rich_table(df=df.tail(), caption="Table - Avg. Per Day")
            caption = Text("\n\nShowing only 5 most recent days from last 2 weeks.")
            avg_text = Text(f"\n\nAvg. per day: {avg}")

            content = Group(
                  table,
                  caption,
                  avg_text
            )

            panel_template(
                title="Avg. per day",
                subtitle="[O] to output table",
                content=content
            )

            choice = console.input("Select an option: ").strip().lower()

            if choice == "o":

                output_file(df, "avg_per_day")
                break
            
            if choice == "x":
                exit()
            if choice == "m":
                break
            
