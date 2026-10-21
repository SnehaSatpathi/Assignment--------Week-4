# COVID-19 Data Tracker
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (replace with actual file path)
df = pd.read_csv("covid_data.csv")

# 1. Top 5 countries by total cases
top5 = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(5)
print("Top 5 countries by total cases:\n", top5)

# 2. Plot bar chart
top5.plot(kind="bar", color="red")
plt.title("Top 5 Countries by COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.show()
