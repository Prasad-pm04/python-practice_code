import time

# Define a function to simulate a traffic light
def traffic_light_simulator(cycles=3):
    # List of lights in the order they appear
    lights = [("Red", 5), ("Green", 3), ("Yellow", 2)]

    print("🚦 Traffic Light Simulation Started 🚦\n")
    
    # Run the simulation for a specific number of cycles
    for i in range(cycles):
        print(f"Cycle {i + 1} begins...")
        
        # Loop through each light and display its state
        for color, duration in lights:
            print(f"{color} light is ON for {duration} seconds.")
            time.sleep(duration)  # Pause for the light duration

        print(f"Cycle {i + 1} completed.\n")

    print("Simulation ended. Drive safe! 🚗")

# Call the function to run the simulation
traffic_light_simulator()
