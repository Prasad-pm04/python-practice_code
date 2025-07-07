import time
import os

# Run the clock forever
while True:
    # Clear the screen (Windows: cls, Linux/macOS: clear)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get current time
    current_time = time.strftime('%H:%M:%S')

    # Print it
    print("⏰ Real-Time Clock")
    print("====================")
    print("Current Time:", current_time)

    # Wait for 1 second
    time.sleep(1)
