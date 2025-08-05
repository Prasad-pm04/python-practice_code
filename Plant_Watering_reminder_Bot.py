import json
import datetime

# File to store plant data
DATA_FILE = "my_plants.json"

# Load existing plant data from the file
def load_plants():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save updated plant data back to the file
def save_plants(plants):
    with open(DATA_FILE, "w") as file:
        json.dump(plants, file, indent=4)

# Add a new plant to the list
def add_plant(name, watering_days):
    plants = load_plants()
    plants[name] = {
        "last_watered": str(datetime.date.today()),
        "frequency_days": watering_days
    }
    save_plants(plants)
    print(f"✅ Added {name} to your plant list!")

# Update the watering date when you water the plant
def water_plant(name):
    plants = load_plants()
    if name in plants:
        plants[name]["last_watered"] = str(datetime.date.today())
        save_plants(plants)
        print(f"💧 {name} has been watered today!")
    else:
        print("⚠️ Plant not found!")

# Check which plants need watering today
def check_water_reminders():
    plants = load_plants()
    today = datetime.date.today()
    print("\n🪴 Watering Reminder:")
    for plant, info in plants.items():
        last_watered = datetime.date.fromisoformat(info["last_watered"])
        freq = info["frequency_days"]
        if (today - last_watered).days >= freq:
            print(f"🌱 {plant} needs watering today! 💧")
        else:
            print(f"😊 {plant} is fine for now!")

# -----------------------------
# 👇 Example usage (you can modify this part later with input prompts)
# -----------------------------
if __name__ == "__main__":
    # Add a new plant (run only once per new plant)
    # add_plant("Snake Plant", 7)
    # add_plant("Aloe Vera", 5)

    # Uncomment to water a plant
    # water_plant("Aloe Vera")

    # Daily check
    check_water_reminders()
