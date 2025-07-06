import time
from datetime import datetime

# 🎯 Set your target date and time
event_name = "New Year 2026"
target_date = datetime(2026, 1, 1, 0, 0, 0)  # YYYY, MM, DD, HH, MM, SS

# 💡 Keep updating the time until the event is reached
while True:
    # Get the current date and time
    now = datetime.now()

    # Calculate remaining time
    time_left = target_date - now

    # If time is up, break the loop
    if time_left.total_seconds() <= 0:
        print(f"\n🎉 It's {event_name} time! 🎉")
        break

    # Extract days, hours, minutes, seconds
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Clear and print updated countdown
    print(f"\r⏳ Countdown to {event_name}: {days}d {hours}h {minutes}m {seconds}s", end="")

    # Wait for 1 second before updating again
    time.sleep(1)
