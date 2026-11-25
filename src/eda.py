import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.cells = [
    nbf.v4.new_markdown_cell("# Task 2: Exploratory Data Analysis - SunGrid Solar Sales\nData Source: data/cleaned_preview.csv (Real Plant 1 Generation Data)\nSales = DC_POWER, Revenue = AC_POWER, Product = SOURCE_KEY"),
    nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/cleaned_preview.csv")
print(df.shape)
print(df.describe())
print("Missing Values:")
print(df.isnull().sum())
df.head()"""),
    nbf.v4.new_markdown_cell("### Chart 1: Monthly Sales Trend (Line Chart)\nMay me sab se zyada generation / sales hui. Growth upar ja rahi hai."),
    nbf.v4.new_code_cell("""df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
df['MONTH'] = df['DATE_TIME'].dt.to_period('M').astype(str)
monthly = df.groupby('MONTH')['DC_POWER'].sum()
monthly.plot(kind='line', marker='o', figsize=(10,4))
plt.title("Monthly Sales Trend - DC Power Generated")
plt.ylabel("Sales Volume (DC_POWER)")
plt.show()"""),
    nbf.v4.new_markdown_cell("### Chart 2: Top 5 Products (Bar Chart)\nKaunse 5 inverters ne sab se zyada bijli / sales di. In par focus karo."),
    nbf.v4.new_code_cell("""top5 = df.groupby('SOURCE_KEY')['DC_POWER'].sum().sort_values(ascending=False).head(5)
top5.plot(kind='bar', figsize=(10,4))
plt.title("Top 5 Products (Inverters) by Sales")
plt.ylabel("DC_POWER")
plt.show()"""),
    nbf.v4.new_markdown_cell("### Chart 3: Sales by Region / Time (Heatmap)\nDin ke kis time zyada sales hui. Dopahar 11-2 baje peak hai."),
    nbf.v4.new_code_cell("""df['HOUR'] = pd.to_datetime(df['DATE_TIME']).dt.hour
df['DAY'] = pd.to_datetime(df['DATE_TIME']).dt.day
pivot = df.pivot_table(index='HOUR', columns='DAY', values='DC_POWER', aggfunc='mean')
plt.figure(figsize=(12,5))
sns.heatmap(pivot, cmap='YlOrRd')
plt.title("Sales Heatmap - Hour vs Day")
plt.show()"""),
    nbf.v4.new_markdown_cell("### Chart 4: Revenue vs Installation Size (Scatter)\nJitni DC Power zyada, utni AC Power (Revenue) zyada. Seedha relation hai."),
    nbf.v4.new_code_cell("""plt.figure(figsize=(8,5))
plt.scatter(df['DC_POWER'], df['AC_POWER'], alpha=0.3)
plt.title("Revenue vs Installation Size (AC vs DC Power)")
plt.xlabel("DC_POWER - Installation Size")
plt.ylabel("AC_POWER - Revenue")
plt.show()"""),
]

with open("eda.ipynb", "w") as f:
    nbf.write(nb, f)
print("eda.ipynb ban gayi!")