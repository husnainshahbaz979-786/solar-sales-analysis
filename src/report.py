import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

# Roz ka total
daily = df.groupby('DATE')['DAILY_YIELD'].max()

print("=== FINAL REPORT NUMBERS ===")
print("Total Days:", len(daily))
print("Total Rows:", len(df))
print("Sab se zyada 1 din ki Yield:", daily.max())
print("Sab se kam 1 din ki Yield:", daily.min())
print("Average Roz ki Yield:", round(daily.mean(), 2))
print("Sab se zyada DC Power:", df['DC_POWER'].max())
print("Sab se zyada AC Power:", df['AC_POWER'].max())
print("\nBest 5 Din:")
print(daily.sort_values(ascending=False).head(5))
print("\nWorst 5 Din:")
print(daily.sort_values().head(5))