import os

def get_excel_files():
    os.chdir(r"C:\Users\cesar\OneDrive\Documentos")
    files = [f for f in os.listdir() if f.endswith((".xlsx", ".xls", ".xlsm"))]
    return [
    f for f in files
    if "inventory" in f.lower() or "placements" in f.lower()
]