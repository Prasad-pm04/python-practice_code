import datetime
import random

# A list of fun time travel destinations (real or fictional)
destinations = [
    "Ancient Egypt – Build the pyramids 🏺",
    "Future Mars Colony – Red planet adventures 🚀",
    "1980s – Retro vibes and arcade games 👾",
    "Renaissance Italy – Paint with da Vinci 🎨",
    "Dinosaur Era – Careful with the T-Rex! 🦖",
    "Year 3000 – Flying cars and robot pets 🤖",
    "Medieval Castle – Sword fights and feasts ⚔️"
]

# Time Travel Diary storage (in-memory for now)
time_travel_log = []

print("🕰️ Welcome to the Time Travel Diary 🕰️")

# Loop to allow multiple entries
while True:
    # Let the user log a new journey
    input("Press Enter to initiate a random time travel journey...")

    # Choose a random destination
    destination = random.choice(destinations)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log the journey
    time_travel_log.append((timestamp, destination))

    print(f"\n✨ You have arrived at: {destination}")
    print(f"🗓️ Time of travel: {timestamp}\n")

    # Ask if they want to continue or stop
    continue_travel = input("Do you want to take another trip? (yes/no): ").lower()
    if continue_travel != 'yes':
        break

# Show travel history
print("\n🧳 Your Time Travel History:")
for entry in time_travel_log:
    print(f"{entry[0]} – {entry[1]}")

print("\n🌌 Thanks for using the Time Travel Diary. Until next time!")
