import random
import string

def generate_password(length=12):
    # Define the characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask user how long the password should be
try:
    user_length = int(input("Enter password length (default is 12): "))
except ValueError:
    user_length = 12  # Default value if invalid input

# Generate and display the password
password = generate_password(user_length)
print(f"🔐 Your secure password is: {password}")
