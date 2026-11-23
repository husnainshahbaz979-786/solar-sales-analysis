import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    df = pd.read_csv("data/cleaned_preview.csv")
    print(f"Total Rows: {len(df)}")
    print(f"Total Sales: Rs {df['total_sales'].sum():,}")
    print("\n--- Sales by Region ---")
    print(df.groupby('region')['total_sales'].sum().sort_values(ascending=False))
    print("\n--- Sales by Product ---")
    print(df.groupby('product')['total_sales'].sum().sort_values(ascending=False))
    print("\n--- Sales by Sales Rep ---")
    print(df.groupby('sales_rep')['total_sales'].sum().sort_values(ascending=False))

    # Chart 1: Region wise sales
    region_sales = df.groupby('region')['total_sales'].sum()
    plt.figure(figsize=(8, 5))
    region_sales.plot(kind='bar', color='orange')
    plt.title('Sales by Region')
    plt.ylabel('Total Sales (Rs)')
    plt.tight_layout()
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/sales_by_region.png")
    print("\nSaved: outputs/sales_by_region.png")

if __name__ == "__main__":
    main()