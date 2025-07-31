# Mood-Based Playlist Generator 🎵
# A fun way to get music suggestions based on how you feel

# Define mood-based playlists using a dictionary
playlists = {
    "happy": [
        "🎶 Happy – Pharrell Williams",
        "🎶 Can't Stop the Feeling – Justin Timberlake",
        "🎶 Uptown Funk – Bruno Mars"
    ],
    "sad": [
        "🎶 Someone Like You – Adele",
        "🎶 Fix You – Coldplay",
        "🎶 Let Her Go – Passenger"
    ],
    "angry": [
        "🎶 Breaking the Habit – Linkin Park",
        "🎶 Smells Like Teen Spirit – Nirvana",
        "🎶 Killing In The Name – Rage Against The Machine"
    ],
    "chill": [
        "🎶 Lose It – Oh Wonder",
        "🎶 Sunday Morning – Maroon 5",
        "🎶 Better Together – Jack Johnson"
    ],
    "romantic": [
        "🎶 Perfect – Ed Sheeran",
        "🎶 All of Me – John Legend",
        "🎶 Thinking Out Loud – Ed Sheeran"
    ]
}

# Ask user how they feel
print("🎧 Mood-Based Playlist Generator 🎧")
print("How are you feeling today?")
print("Options: happy, sad, angry, chill, romantic")

# Take user input and make it lowercase to match dictionary keys
mood = input("Enter your mood: ").strip().lower()

# Check if the mood is valid
if mood in playlists:
    print(f"\nHere’s a playlist for when you're feeling {mood}:\n")
    for song in playlists[mood]:
        print(song)
else:
    print("\nOops! I don’t have a playlist for that mood 😢")
    print("Try moods like: happy, sad, angry, chill, romantic.")

# End with a smile!
print("\nEnjoy your music! 🎶😄")
