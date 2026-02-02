from modules.panel_template import panel_template
from rich.console import Console, Group
from utils.get_avg import sellers_day, sellers_week, sellers_month
from modules.table_template import df_to_rich_table
from rich.text import Text
from utils.output_file import output_file

def avg_sellers_day():
        
        console = Console()

        while True:

            df, avg = sellers_day()
            
            avg_caption = Text("\nAverage per seller\n", style="bold")
            avg_table = df_to_rich_table(df=avg, caption="Table - Avg. Per Seller")

            content = Group(
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

def avg_sellers_week():
        
        console = Console()

        while True:

            df, avg = sellers_week()
            
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

def avg_sellers_month():
        
        console = Console()

        while True:

            df, avg = sellers_month()
            
            avg_table = df_to_rich_table(df=avg, caption="Table - Avg. Per Seller, data from last 2 months")

            content = Group(
                  avg_table
            )

            panel_template(
                title="Avg. per Seller Per Month",
                subtitle="[O] to output table",
                content=content
            )

            choice = console.input("Select an option: ").strip().lower()

            if choice == "o":

                output_file(avg, "avg_per_seller_per_month")
                break
            
            if choice == "x":
                exit()
            if choice == "m":
                break
            
