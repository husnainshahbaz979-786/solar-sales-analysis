import pandas as pd

df = pd.read_excel("Plant_1_Generation_Data.xlsx", engine="openpyxl")

df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'], dayfirst=True)
df['DATE'] = df['DATE_TIME'].dt.date
df['HOUR'] = df['DATE_TIME'].dt.hour

print("Khali values:")
print(df.isnull().sum())

df.to_csv("data/cleaned_data.csv", index=False)
print("\nHo gaya! cleaned_data.csv ban gayi")
print(df.head())