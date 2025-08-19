import time
import psutil

# List of "distracting" apps to monitor (you can customize this)
distracting_apps = ["chrome.exe", "spotify.exe", "instagram.exe", "discord.exe"]

# Track how long the distraction has been open
distraction_timer = 0
warning_limit = 60  # in seconds — you can change this

print("👀 Distraction Detector is now running. Stay focused!")

while True:
    found_distraction = False

    # Check currently running processes
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in distracting_apps:
            found_distraction = True
            distraction_timer += 5
            print(f"⚠️ Detected: {proc.info['name']} running. ({distraction_timer}s distracted)")
            break  # no need to check further if one is already found

    if not found_distraction:
        if distraction_timer > 0:
            print("✅ Back to focus. Nice job!")
        distraction_timer = 0  # reset timer when no distraction is found

    # If distraction time crosses limit, gently remind
    if distraction_timer >= warning_limit:
        print("\n🚨 Hey, you’ve been distracted for a while...")
        print("💡 Take a break, then get back to your goals. You've got this!")
        distraction_timer = 0  # reset after warning

    time.sleep(5)  # Check every 5 seconds
