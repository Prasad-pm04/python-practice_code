import datetime
import random

# 💡 Smart Room Light Automation
# This simulates a smart system that decides whether to turn lights ON or OFF
# based on time of day and human presence in the room.

# Step 1: Simulate presence detection (True means someone is in the room)
presence_detected = random.choice([True, False])  # Simulating sensor input

# Step 2: Get current hour of the day (0 to 23)
current_hour = datetime.datetime.now().hour

# Step 3: Define logic to turn the light on or off
# Lights should be ON only if someone is in the room AND it's evening/night
if presence_detected and (current_hour >= 18 or current_hour <= 6):
    print("🔆 Motion detected in the evening/night. Turning lights ON.")
elif presence_detected:
    print("🔅 Motion detected during daytime. Natural light is enough. Lights OFF.")
else:
    print("🌑 No one in the room. Lights OFF to save energy.")

# Step 4: Status log
print(f"\n🕒 Time: {current_hour}:00")
print(f"🚶 Presence Detected: {'Yes' if presence_detected else 'No'}")
