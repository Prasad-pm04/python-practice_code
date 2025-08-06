import time
import random

# A simple Plant class to represent the virtual plant
class Plant:
    def __init__(self, name):
        self.name = name
        self.water_level = 5      # Water level ranges from 0 to 10
        self.sunlight_level = 5   # Sunlight level ranges from 0 to 10
        self.nutrients = 5        # Nutrients level ranges from 0 to 10
        self.health = 100         # Health out of 100

    # Method to display current plant status
    def status(self):
        print(f"\n🌿 Status of {self.name}:")
        print(f"   💧 Water: {self.water_level}/10")
        print(f"   ☀️  Sunlight: {self.sunlight_level}/10")
        print(f"   🌱 Nutrients: {self.nutrients}/10")
        print(f"   ❤️ Health: {self.health}/100\n")

    # Method to simulate passage of time (plant getting thirsty, etc.)
    def time_passes(self):
        # Over time, the plant's needs go down randomly
        self.water_level = max(0, self.water_level - random.randint(1, 3))
        self.sunlight_level = max(0, self.sunlight_level - random.randint(1, 2))
        self.nutrients = max(0, self.nutrients - random.randint(0, 2))

        # Health deteriorates if any level is too low
        if self.water_level < 3 or self.sunlight_level < 3 or self.nutrients < 3:
            self.health -= random.randint(5, 10)
        else:
            self.health = min(100, self.health + random.randint(1, 5))  # reward for good care

    # Methods to care for the plant
    def water(self):
        self.water_level = min(10, self.water_level + 3)
        print("💧 You watered the plant!")

    def give_sunlight(self):
        self.sunlight_level = min(10, self.sunlight_level + 2)
        print("☀️  You placed the plant in sunlight!")

    def fertilize(self):
        self.nutrients = min(10, self.nutrients + 2)
        print("🌱 You added some nutrients!")

# Let's create a plant and take care of it
my_plant = Plant("Lily")

print("🌼 Welcome to your virtual plant caretaker!")
my_plant.status()

# Simple simulation loop
for day in range(1, 6):  # 5 days simulation
    print(f"📅 Day {day}: What would you like to do?")
    action = input("Options: water / sun / fertilize / skip: ").strip().lower()

    if action == "water":
        my_plant.water()
    elif action == "sun":
        my_plant.give_sunlight()
    elif action == "fertilize":
        my_plant.fertilize()
    else:
        print("⏩ You skipped caring today.")

    my_plant.time_passes()
    my_plant.status()
    time.sleep(1)  # adds a slight pause for realism

# Final report
if my_plant.health >= 80:
    print("🎉 Your plant is thriving! Great job!")
elif my_plant.health >= 50:
    print("🙂 Your plant survived, but it could use more care.")
else:
    print("😢 Your plant didn't make it. Try again and give it more love!")
