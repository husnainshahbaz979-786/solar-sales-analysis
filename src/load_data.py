import pandas as pd
import numpy as np
import os

def main():
    np.random.seed(42)
    n = 500
    data = {
        'order_id': range(1, n+1),
        'date': pd.date_range(start='2024-01-01', periods=n, freq='D'),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n),
        'product': np.random.choice(['Solar Panel 400W', 'Solar Panel 550W', 'Inverter 5kW', 'Battery 10kWh'], n),
        'quantity': np.random.randint(1, 20, n),
        'unit_price': np.random.randint(150, 900, n),
        'sales_rep': np.random.choice(['Ahmed', 'Sara', 'Ali', 'Ayesha'], n),
    }
    df = pd.DataFrame(data)
    df['total_sales'] = df['quantity'] * df['unit_price']
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    os.makedirs("data", exist_ok=True)
    df.head(100).to_csv("data/cleaned_preview.csv", index=False)
    print(f"Total rows: {len(df)}")
    print("Saved: data/cleaned_preview.csv")
    print(df.head())

if __name__ == "__main__":
    main()