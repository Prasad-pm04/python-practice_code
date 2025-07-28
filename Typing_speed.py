import time
import random

# List of sample sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing fast requires a lot of practice and focus.",
    "Artificial intelligence is shaping the future.",
    "Data science is a blend of math, coding, and business."
]

# Select a random sentence
sentence = random.choice(sentences)
print("\n--- Typing Speed Test ---")
print("\nType the following sentence exactly as shown:\n")
print(f"👉 {sentence}")

# Wait for user to get ready
input("\nPress Enter when you're ready...")

# Record start time
start_time = time.time()

# Take user input
typed = input("\nStart typing: ")

# Record end time
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time
time_taken = round(time_taken, 2)

# Calculate words per minute
word_count = len(sentence.split())
wpm = round((word_count / time_taken) * 60)

# Check accuracy
accuracy = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        accuracy += 1
accuracy = (accuracy / len(sentence)) * 100
accuracy = round(accuracy, 2)

# Show results
print("\n--- Results ---")
print(f"🕒 Time Taken: {time_taken} seconds")
print(f"⌨️  Words Per Minute: {wpm}")
print(f"🎯 Accuracy: {accuracy}%")
