import datetime

# 👋 Hey, welcome to your personal habit tracker!
# Let’s help you stay consistent and motivated.

# Sample habit list (feel free to customize)
habits = {
    "Read 10 pages": [],
    "Meditate": [],
    "Exercise": [],
}

# Get today's date
today = datetime.date.today().isoformat()

# Ask about each habit
print(f"\n📅 Today is {today}")
print("Let’s check off your habits for today!\n")

for habit in habits:
    answer = input(f"✅ Did you {habit.lower()} today? (yes/no): ").strip().lower()
    if answer == "yes":
        habits[habit].append(today)
        print("🎉 Great job! Keep it up!\n")
    else:
        print("🕒 No worries. Tomorrow is a new chance!\n")

# Summary
print("📊 Your Habit History:")
for habit, dates in habits.items():
    print(f"• {habit}: done {len(dates)} day(s) -> {dates}")

# Motivation boost
total = sum(len(dates) for dates in habits.values())
if total > 0:
    print("\n🚀 You’ve completed", total, "habits so far! That’s awesome!")
else:
    print("\nLet’s get started — one small step at a time! 🌱")
