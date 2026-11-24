import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

# 15 May ka data - har ghante ka average lo
one_day = df[df['DATE'] == '2020-05-15']
hourly = one_day.groupby('HOUR')['DC_POWER'].mean()

plt.figure(figsize=(10, 5))
plt.plot(hourly.index, hourly.values, marker='o', color='orange')
plt.title("Solar Power - 15 May 2020 (Smooth Graph)")
plt.xlabel("Hour (0-23)")
plt.ylabel("DC Power")
plt.grid(True)
plt.savefig("solar_graph.png")
plt.show()
print("Graph save ho gaya: solar_graph.png")