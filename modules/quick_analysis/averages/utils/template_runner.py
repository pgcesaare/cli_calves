from modules.panel_template import panel_template
from rich.console import Console, Group
from modules.table_template import df_to_rich_table
from rich.text import Text
from utils.output_file import output_file
import pandas as pd

def template_runner(title, general_caption, caption, dataframe_caption, dataframe, data_fn, output_name):
        
    console = Console()

    while True:

        df, avg = data_fn()
        content_items = []
        
        if dataframe:
            content_items.append(df_to_rich_table(df=df, caption=dataframe_caption))
                
        content_items.append(Text(f"\n{general_caption}\n", style="bold"))

        if isinstance(avg, pd.DataFrame):
            content_items.append(df_to_rich_table(df=avg, caption=caption))
        else:
            content_items.append(Text(f"{avg}", style="bold green"))

        content = Group(
            *content_items
        )

        panel_template(
            title=title,
            subtitle="[O] to output table",
            content=content
        )

        choice = console.input("Select an option: ").strip().lower()

        if choice == "o":
            output_file(avg, output_name)
            break
        if choice == "x":
            exit()
        if choice == "m":
            break
