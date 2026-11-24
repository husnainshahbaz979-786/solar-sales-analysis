import pandas as pd
import os

def load_data():
    # Asli dataset ka path
    file_path = "Plant_1_Generation_Data.xlsx"

    # Agar file root me na ho to data folder me check karo
    if not os.path.exists(file_path):
        file_path = "data/Plant_1_Generation_Data.xlsx"

    print(f"Loading real dataset from: {file_path}")

    # Asli dataset fetch karo - koi fake data nahi
    df = pd.read_excel(file_path, engine="openpyxl")

    print(f"Total Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(df.head())

    return df

if __name__ == "__main__":
    df = load_data()