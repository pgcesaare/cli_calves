from rich.console import Console
from rich.table import Table
from rich.box import SIMPLE, MINIMAL, ROUNDED
import pandas as pd
from ui.styles import PRIMARY_COLOR 

def df_to_rich_table(
    df: pd.DataFrame,
    caption: str = None,
    show_index: bool = False,
    header_style: str = PRIMARY_COLOR,
    border_style: str = "dim",
    box_style = ROUNDED,
    max_rows: int = None,
    show_lines: bool = True,
    padding: tuple = (0,1)
) -> Table:
    """
    Convierte un DataFrame de pandas a una tabla Rich minimalista.
    
    Args:
        df: DataFrame a convertir
        show_index: Mostrar índice del DataFrame
        header_style: Estilo de los encabezados
        border_style: Estilo de los bordes
        box_style: Estilo de caja (SIMPLE, MINIMAL, etc.)
        max_rows: Número máximo de filas a mostrar
    """
    table = Table(
        caption=caption,
        show_header=True,
        header_style=header_style,
        border_style=border_style,
        box=box_style,
        show_lines = show_lines,
        padding=padding
    )
    
    # Agregar índice si se solicita
    if show_index:
        table.add_column("Index", style="dim", width=8)
    
    # Agregar columnas
    for column in df.columns:
        table.add_column(str(column))
    
    # Agregar filas (limitadas si se especifica max_rows)
    df_display = df.head(max_rows) if max_rows else df
    
    for idx, row in df_display.iterrows():
        row_data = [str(idx)] if show_index else []
        row_data.extend([str(val) for val in row])
        table.add_row(*row_data)
    
    # Agregar nota si hay más filas
    if max_rows and len(df) > max_rows:
        remaining = len(df) - max_rows
        table.caption = f"[dim]...y {remaining} filas más[/dim]"
    
    return table


