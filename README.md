# ============================================================
# 🌦️ API Integration and Data Visualization
# Author: Mohammed Asrar Uddin
# Description: Fetches real-time weather data using OpenWeatherMap API
#              and visualizes it using Matplotlib and Seaborn.
# ============================================================

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# 🔑 Enter your OpenWeatherMap API Key here
# ----------------------------------------
API_KEY = "YOUR_API_KEY"  # ← Replace this with your actual key

# 🏙️ List of cities to fetch weather data for
cities = ["London", "New York", "Tokyo", "Paris", "Delhi", "Sydney"]

# 🌐 Base URL for OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 🧭 Function to fetch weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Pressure (hPa)": data["main"]["pressure"],
            "Weather": data["weather"][0]["main"],
        }
    else:
        print(f"⚠️ Failed to fetch data for {city}")
        return None

# 📊 Fetch data for all cities
weather_data = [get_weather(city) for city in cities]
weather_data = [d for d in weather_data if d is not None]  # Remove failed entries

# Convert to DataFrame
df = pd.DataFrame(weather_data)
print("\n✅ Weather Data Fetched Successfully!\n")
print(df)

# ----------------------------------------
# 🎨 Data Visualization
# ----------------------------------------

sns.set(style="whitegrid")

# 1️⃣ Temperature Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm")
plt.title("🌡️ Temperature Comparison by City", fontsize=14)
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("temperature_chart.png")
plt.show()

# 2️⃣ Humidity Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Humidity (%)", data=df, palette="Blues")
plt.title("💧 Humidity Comparison by City", fontsize=14)
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("humidity_chart.png")
plt.show()

# 3️⃣ Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]].corr(), annot=True, cmap="viridis")
plt.title("📊 Correlation Heatmap", fontsize=13)
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

print("\n📁 Charts saved as: temperature_chart.png, humidity_chart.png, correlation_heatmap.png")

