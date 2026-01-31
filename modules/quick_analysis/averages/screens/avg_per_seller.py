from modules.panel_template import panel_template
from rich.console import Console, Group
from utils.get_avg import get_avg_per_seller, get_avg_per_seller_per_day
from modules.table_template import df_to_rich_table
from rich.text import Text
from utils.output_file import output_file

def avg_per_seller():
        
        console = Console()

        while True:

            df, avg = get_avg_per_seller()
            
            table = df_to_rich_table(df=df, caption="Table - Placements Per Seller Two Weeks")
            avg_caption = Text("\nAverage per seller\n", style="bold")
            avg_table = df_to_rich_table(df=avg, caption="Table - Avg. Per Seller")

            content = Group(
                  table,
                  avg_caption,
                  avg_table
            )

            panel_template(
                title="Avg. per Seller",
                subtitle="[O] to output table",
                content=content
            )

            choice = console.input("Select an option: ").strip().lower()

            if choice == "o":

                output_file(avg, "avg_per_seller")
                break
            
            if choice == "x":
                exit()
            if choice == "m":
                break

def avg_per_seller_per_day():
        
        console = Console()

        while True:

            df, avg = get_avg_per_seller_per_day()
            
            avg_table = df_to_rich_table(df=avg, caption="Table - Avg. Per Seller, data from last 2 weeks")

            content = Group(
                  avg_table
            )

            panel_template(
                title="Avg. per Seller Per Day",
                subtitle="[O] to output table",
                content=content
            )

            choice = console.input("Select an option: ").strip().lower()

            if choice == "o":

                output_file(avg, "avg_per_seller_per_day")
                break
            
            if choice == "x":
                exit()
            if choice == "m":
                break
            
