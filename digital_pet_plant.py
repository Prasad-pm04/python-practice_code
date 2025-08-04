import time
import json
from datetime import datetime, timedelta

# A virtual plant that grows with care (sunlight & water)
class DigitalPlant:
    def __init__(self, name):
        self.name = name
        self.watered_at = None
        self.sunlight_at = None
        self.growth = 0  # Growth scale from 0 to 100

    # Water the plant and update last watered time
    def water(self):
        self.watered_at = datetime.now()
        print(f"💧 You watered {self.name} at {self.watered_at.strftime('%H:%M:%S')}")

    # Give sunlight to the plant
    def give_sunlight(self):
        self.sunlight_at = datetime.now()
        print(f"☀️ You gave sunlight to {self.name} at {self.sunlight_at.strftime('%H:%M:%S')}")

    # Update growth if both needs are met within the last 6 hours
    def update_growth(self):
        now = datetime.now()
        if self.watered_at and self.sunlight_at:
            if now - self.watered_at < timedelta(hours=6) and now - self.sunlight_at < timedelta(hours=6):
                self.growth = min(100, self.growth + 10)
                print(f"🌿 {self.name} has grown! Growth level: {self.growth}/100")
            else:
                print(f"⚠️ {self.name} is not happy. Missed water or sunlight.")
        else:
            print(f"⏳ {self.name} needs both water and sunlight to grow.")

    # Save plant status to a file so you can come back later
    def save_status(self):
        data = {
            "name": self.name,
            "growth": self.growth,
            "watered_at": self.watered_at.isoformat() if self.watered_at else None,
            "sunlight_at": self.sunlight_at.isoformat() if self.sunlight_at else None
        }
        with open("plant_status.json", "w") as f:
            json.dump(data, f)
        print("💾 Plant status saved!")

    # Load previous plant status if exists
    @staticmethod
    def load_status():
        try:
            with open("plant_status.json", "r") as f:
                data = json.load(f)
                plant = DigitalPlant(data["name"])
                plant.growth = data["growth"]
                plant.watered_at = datetime.fromisoformat(data["watered_at"]) if data["watered_at"] else None
                plant.sunlight_at = datetime.fromisoformat(data["sunlight_at"]) if data["sunlight_at"] else None
                print(f"🌱 Loaded your plant '{plant.name}' with growth: {plant.growth}/100")
                return plant
        except FileNotFoundError:
            print("🌱 No existing plant found. Let's grow a new one!")
            return None

# --- Simulate interaction ---

# Load existing plant or create new one
plant = DigitalPlant.load_status()
if not plant:
    name = input("Give your plant a name: ")
    plant = DigitalPlant(name)

# Let’s interact with the plant
while True:
    print("\nWhat do you want to do?")
    print("1. Water the plant")
    print("2. Give sunlight")
    print("3. Check growth")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        plant.water()
    elif choice == "2":
        plant.give_sunlight()
    elif choice == "3":
        plant.update_growth()
    elif choice == "4":
        plant.save_status()
        print("👋 See you later!")
        break
    else:
        print("❌ Invalid choice, try again.")

    time.sleep(1)
