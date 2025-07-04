import time

test_sentence = "Python is a powerful and easy-to-learn language."
print("Type the following sentence as fast as you can:")
print(f"\n👉 {test_sentence}\n")

input("Press Enter when you're ready...")

start_time = time.time()  # Start the timer
typed_sentence = input("Start typing: ")
end_time = time.time()    # End the timer

# Calculate typing time
time_taken = end_time - start_time
words = len(test_sentence.split())
speed_wpm = (words / time_taken) * 60  # Words per minute

# Check accuracy
accuracy = (len(set(typed_sentence.split()) & set(test_sentence.split())) / words) * 100

print(f"\n⏱ Time taken: {time_taken:.2f} seconds")
print(f"💬 Typing speed: {speed_wpm:.2f} words per minute")
print(f"✅ Accuracy: {accuracy:.2f}%")
