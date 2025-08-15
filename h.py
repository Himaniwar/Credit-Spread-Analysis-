import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="M"),
    "Corporate_Bond_Yield": [5.2, 5.3, 5.5, 5.6, 5.4, 5.8, 5.9, 6.0, 6.1, 6.2],
    "Govt_Bond_Yield": [4.5, 4.6, 4.7, 4.8, 4.7, 4.9, 5.0, 5.1, 5.0, 5.2]
}

df = pd.DataFrame(data)

# Calculate credit spread
df["Credit_Spread"] = df["Corporate_Bond_Yield"] - df["Govt_Bond_Yield"]

# Display stats
print("Average Spread:", df["Credit_Spread"].mean())
print("Max Spread:", df["Credit_Spread"].max())
print("Min Spread:", df["Credit_Spread"].min())

# Plot
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Credit_Spread"], marker="o", label="Credit Spread")
plt.title("Credit Spread Over Time")
plt.xlabel("Date")
plt.ylabel("Spread (%)")
plt.grid(True)
plt.legend()
plt.show()
