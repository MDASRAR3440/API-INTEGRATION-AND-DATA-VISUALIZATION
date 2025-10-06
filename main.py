# main.py
"""
API Integration and Data Visualization
--------------------------------------
This script fetches weather data from the OpenWeatherMap API
and visualizes temperature variations using Matplotlib.
"""

import requests
import matplotlib.pyplot as plt

# Replace this with your own API key from https://openweathermap.org/
API_KEY = "demo"  # For demonstration; replace with a valid key
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
print("Fetching weather data...")
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    forecasts = data['list'][:10]  # Take first 10 entries for simplicity

    times = [item['dt_txt'] for item in forecasts]
    temps = [item['main']['temp'] for item in forecasts]

    # Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("Error fetching data! Please check your API key or city name.")
