# Let's create a simple countdown timer in Python!
# It will count down from the number of seconds you give.

import time  # We'll use the time module to make the program wait

# Step 1: Ask the user how long the timer should run
seconds = int(input("⏲️ Enter time in seconds: "))

print(f"Starting countdown for {seconds} seconds...\n")

# Step 2: Start the countdown using a loop
while seconds:
    mins, secs = divmod(seconds, 60)  # Convert total seconds into minutes and seconds
    timer_format = '{:02d}:{:02d}'.format(mins, secs)  # Format as MM:SS
    print(timer_format, end='\r')  # Print on the same line using carriage return
    time.sleep(1)  # Wait for 1 second
    seconds -= 1  # Decrease the timer

# Step 3: Timer ends
print("⏰ Time's up!               ")
