# Daily Mood Tracker - keeps track of how your mood changes day by day

from datetime import datetime  # to get current date and time

# Step 1: Ask the user how they are feeling today
mood = input("How are you feeling today? 😊: ")

# Step 2: Get the current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Format the mood entry
entry = f"{timestamp} - Mood: {mood}\n"

# Step 4: Save this entry to a file
with open("mood_log.txt", "a") as file:
    file.write(entry)

# Step 5: Let the user know it was saved
print("✅ Your mood has been saved. Have a great day!")

# Extra feature (Optional): Show past 3 mood entries
print("\nHere are your last 3 mood logs:")
try:
    with open("mood_log.txt", "r") as file:
        lines = file.readlines()
        for line in lines[-3:]:
            print(line.strip())
except FileNotFoundError:
    print("No previous mood logs found.")
