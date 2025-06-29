import random
import time

# Define a WeatherStation class
class WeatherStation:
    def __init__(self, location, threshold):
        self.location = location
        self.threshold = threshold

    def get_temperature(self):
        # Simulate temperature in °C
        return round(random.uniform(25.0, 45.0), 2)

    def check_alert(self, temp):
        if temp > self.threshold:
            print(f"🔥 ALERT! Temperature in {self.location} is {temp}°C, which is above the threshold!")
        else:
            print(f"✅ Temperature in {self.location} is normal: {temp}°C")

# Create object
station = WeatherStation("Pune", 40.0)

# Simulate real-time monitoring
for i in range(5):
    current_temp = station.get_temperature()
    station.check_alert(current_temp)
    time.sleep(2)  # Wait for 2 seconds before next reading
