import time
import sys

# Digital Hourglass Timer ⏳
# Imagine flipping a real hourglass — this code simulates that countdown using text animation.

def hourglass_timer(seconds):
    """
    Countdown timer with a falling sand animation using dots.
    """
    print(f"\n⏳ Flipping the hourglass for {seconds} seconds...\n")

    for remaining in range(seconds, 0, -1):
        sand = '.' * (seconds - remaining + 1)  # Add one dot each second
        sys.stdout.write(f"\rTime left: {remaining:2d}s | Falling sand: {sand}")
        sys.stdout.flush()
        time.sleep(1)

    print("\n\n🟢 Time's up! The sand has fully fallen.\n")

# 👋 Let the user interact like a real timer
try:
    user_input = int(input("Enter number of seconds for your hourglass: "))
    if user_input > 0:
        hourglass_timer(user_input)
    else:
        print("⚠️ Please enter a positive number!")
except ValueError:
    print("❌ That's not a number! Try again.")
