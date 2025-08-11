import random
from datetime import date

# ---------------------------
# Mission: Generate a random funny excuse
# Audience: Boss, teacher, or suspicious family member
# Warning: Do NOT actually send this to your boss unless your boss has a sense of humor!
# ---------------------------

# Step 1: List of potential reasons (some more believable than others)
reasons = [
    "my goldfish learned how to moonwalk and I had to record it",
    "my phone auto-corrected my alarm to PM instead of AM",
    "I accidentally joined a flash mob on my way to work",
    "I was abducted by friendly aliens who love pizza",
    "I spilled coffee on my teleportation device",
    "my neighbour's pet llama blocked my driveway"
]

# Step 2: List of consequences (because a reason without drama is boring)
consequences = [
    "so I couldn't leave the house on time.",
    "and it completely ruined my schedule.",
    "which caused me to miss the bus by exactly 3.2 seconds.",
    "so I had to rethink my entire life choices.",
    "and the universe just didn’t want me to work today."
]

# Step 3: Generate today's date (to look official)
today = date.today().strftime("%B %d, %Y")

# Step 4: Pick a random reason and consequence
chosen_reason = random.choice(reasons)
chosen_consequence = random.choice(consequences)

# Step 5: Combine into a full excuse note
excuse_note = f"""
Date: {today}

Dear Sir/Madam,

I regret to inform you that I was unable to attend today because {chosen_reason} {chosen_consequence}

Thank you for your understanding.

Sincerely,
[Your Name]
"""

# Step 6: Print the note (print it with pride)
print(excuse_note)
