import pandas as pd
import os

def load_data():
    # Asli dataset ka path
    file_path = "Plant_1_Generation_Data.xlsx"
    if not os.path.exists(file_path):
        file_path = "data/Plant_1_Generation_Data.xlsx"

    print(f"Loading real dataset from: {file_path}")
    df = pd.read_excel(file_path, engine="openpyxl")
    print(f"Total Rows: {len(df)}")

    # --- Cleaning ---
    # DATE ko date banao, HOUR nikalo
    df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
    df['DATE'] = df['DATE_TIME'].dt.date
    df['HOUR'] = df['DATE_TIME'].dt.hour

    # Khali values hatado
    df = df.dropna()

    # --- Cleaned Preview File Banana (Yehi Supervisor maang raha hai) ---
    os.makedirs("data", exist_ok=True)

    # Preview = pehli 1000 saaf ki hui rows
    preview = df.head(1000)
    preview.to_csv("data/cleaned_preview.csv", index=False)
    print("Saved: data/cleaned_preview.csv - Rows:", len(preview))

    # Poora saaf data bhi save kar do
    df.to_csv("data/cleaned_data.csv", index=False)
    print("Saved: data/cleaned_data.csv - Rows:", len(df))

    return df

if __name__ == "__main__":
    df = load_data()