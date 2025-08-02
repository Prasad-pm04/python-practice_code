# Dream Job Predictor 🧑‍🚀
# Created by: Prasad Mangade

import random

# Lists of fun job predictions based on interests and traits
dream_jobs = [
    "AI Whisperer 🤖",
    "Professional Netflix Critic 🍿",
    "Dragon Trainer 🐉",
    "Virtual Reality Chef 👨‍🍳",
    "Time Traveler Historian ⏳",
    "Alien Translator 👽",
    "Emoji Analyst 😎",
    "Cloud Architect (literally builds clouds) ☁️",
    "Pet Psychologist 🐶",
    "Head Meme Curator at NASA 🚀"
]

# Welcome user
print("✨ Welcome to the Dream Job Predictor ✨")
print("Answer the following questions honestly, or have some fun!")

# Collecting quirky user data
fav_subject = input("\n📚 What was your favorite subject in school? ")
spirit_animal = input("🦄 What’s your spirit animal? ")
hobby = input("🎨 What's a hobby you enjoy the most? ")
fav_color = input("🌈 What's your favorite color? ")

# Adding some human-like humor and randomness
print("\n🔮 Analyzing your answers with AI-powered cosmic algorithms... 🤯")
print("Loading personality matrix...")
print("Connecting with the Dream Dimension...\n")

# Wait a moment for drama
import time
time.sleep(2)

# Randomly select a dream job
predicted_job = random.choice(dream_jobs)

# Fun result message
print(f"🚀 Based on your love for {fav_subject}, your connection with {spirit_animal}s,")
print(f"and your passion for {hobby} in the realm of {fav_color},")
print(f"your future dream job is: **{predicted_job}** 💼")

# Friendly outro
print("\nThanks for playing! Keep dreaming big. 🌟")
