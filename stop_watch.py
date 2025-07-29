# ⏰ This is a simple stopwatch timer
# You can start and stop the timer manually and see how much time has passed

import time  # We need this to track the current time

def stopwatch():
    input("▶️ Press ENTER to start the stopwatch")
    start_time = time.time()  # Record the start time

    input("⏹️ Press ENTER to stop the stopwatch")
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the difference
    print(f"\n⏳ Time elapsed: {round(elapsed_time, 2)} seconds")

# Call the stopwatch function
stopwatch()
