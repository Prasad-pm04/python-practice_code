import random
import time

# Dictionary to display dice faces as text
dice_faces = {
    1: (
        "---------",
        "|       |",
        "|   o   |",
        "|       |",
        "---------"
    ),
    2: (
        "---------",
        "| o     |",
        "|       |",
        "|     o |",
        "---------"
    ),
    3: (
        "---------",
        "| o     |",
        "|   o   |",
        "|     o |",
        "---------"
    ),
    4: (
        "---------",
        "| o   o |",
        "|       |",
        "| o   o |",
        "---------"
    ),
    5: (
        "---------",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "---------"
    ),
    6: (
        "---------",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "---------"
    )
}

# Main program loop
while True:
    input("\nPress Enter to roll the dice...")

    print("Rolling", end="")
    for _ in range(3):  # Simple loading animation
        print(".", end="", flush=True)
        time.sleep(0.3)

    rolled = random.randint(1, 6)  # Random number between 1 and 6
    print(f"\nYou rolled a {rolled}!\n")
    
    # Print the dice face
    for line in dice_faces[rolled]:
        print(line)
    
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! 🎉")
        break
