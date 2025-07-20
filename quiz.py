# 🎉 Welcome to the Simple Quiz Game!
# This game will ask you a few general knowledge questions.
# Let's test how much you know!

score = 0  # This variable will keep track of your score

# Asking the first question
print("Q1: What is the capital of India?")
answer1 = input("Your answer: ")

if answer1.lower() == "new delhi":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Oops! The correct answer is New Delhi.")

# Asking the second question
print("\nQ2: What is the largest planet in our solar system?")
answer2 = input("Your answer: ")

if answer2.lower() == "jupiter":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Nope! It's Jupiter.")

# Asking the third question
print("\nQ3: Who wrote the Harry Potter series?")
answer3 = input("Your answer: ")

if answer3.lower() == "j.k. rowling" or answer3.lower() == "jk rowling":
    print("✅ Well done!")
    score += 1
else:
    print("❌ The correct answer is J.K. Rowling.")

# Final score
print("\n🎯 You've completed the quiz!")
print(f"Your final score is: {score}/3")

# Bonus message based on performance
if score == 3:
    print("🏆 Excellent! You're a quiz master!")
elif score == 2:
    print("👍 Good job! You're almost there.")
else:
    print("📚 Keep learning! You can do better next time.")
