import os
import pandas as pd

# Kaggle dataset: berkerisen/sungrid-solar-sales
# Kaggle needs login/API, so we first try to download,
# if download fails we generate same-structure synthetic data as fallback
KAGGLE_URL = "https://www.kaggle.com/datasets/berkerisen/sungrid-solar-sales"

def load_data():
    os.makedirs("data", exist_ok=True)
    try:
        # Try Kaggle download via kagglehub
        import kagglehub
        path = kagglehub.dataset_download("berkerisen/sungrid-solar-sales")
        print(f"Downloaded from Kaggle: {path}")
        # Find first csv in downloaded folder
        for f in os.listdir(path):
            if f.endswith(".csv"):
                df = pd.read_csv(os.path.join(path, f))
                break
    except Exception as e:
        print(f"Kaggle download failed ({e}), generating synthetic data with same structure...")
        print(f"Source: {KAGGLE_URL}")
        import random
        from datetime import datetime, timedelta
        random.seed(42)
        reps = ["Sara", "Ayesha", "Ahmed", "Ali"]
        regions = ["North", "South", "East", "West"]
        rows = []
        for i in range(200):
            rows.append({
                "Date": (datetime(2024,1,1) + timedelta(days=random.randint(0,365))).date(),
                "Region": random.choice(regions),
                "Sales_Rep": random.choice(reps),
                "Sales_Amount": random.randint(500, 2000)
            })
        df = pd.DataFrame(rows)

    # Clean data
    df = df.dropna()
    df.to_csv("data/cleaned_preview.csv", index=False)
    print(f"Saved: data/cleaned_preview.csv, rows: {len(df)}")
    print(df.head())
    return df

if __name__ == "__main__":
    load_data()