from context.context import data as data_file

def normalize_headers():
    df = data_file.get()
    df.columns = (
            df.columns.str.strip().str.lower().str.replace(" ", "_")
        )

    return df