# Simple AI Stylist: Recommends outfit based on weather

def outfit_recommender(temp_celsius, weather):
    """
    Suggests what to wear based on temperature and weather.
    """
    print(f"\n🌡️ Weather Report: {temp_celsius}°C and {weather}")

    # Start with temperature-based recommendation
    if temp_celsius >= 30:
        outfit = "light t-shirt and shorts"
    elif 20 <= temp_celsius < 30:
        outfit = "casual shirt and jeans"
    elif 10 <= temp_celsius < 20:
        outfit = "sweatshirt or light jacket"
    else:
        outfit = "heavy jacket, gloves, and maybe a warm hat"

    # Adjust based on weather condition
    if "rain" in weather.lower():
        outfit += " + carry an umbrella ☔"
    elif "snow" in weather.lower():
        outfit += " + wear boots and gloves ❄️"
    elif "sun" in weather.lower() and temp_celsius > 25:
        outfit += " + sunglasses 😎"

    print(f"\n👕 Recommended Outfit: {outfit}")


# --- User Simulation ---

# Example 1
outfit_recommender(32, "sunny")

# Example 2
outfit_recommender(18, "cloudy")

# Example 3
outfit_recommender(8, "snow")

# Example 4
outfit_recommender(22, "light rain")
