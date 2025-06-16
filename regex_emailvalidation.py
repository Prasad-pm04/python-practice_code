import re

# Sample email input from user
email = input("Enter your email address: ")

# Define the regex pattern for a valid email
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate using re.match
if re.match(pattern, email):
    print("✅ Valid email address")
else:
    print("❌ Invalid email address")

# #pattern explaination
# ^ and $ → Start and end of the string.

# [\w\.-]+ → One or more word characters, dots, or hyphens (for username).

# @ → The "@" symbol.

# [\w\.-]+ → One or more word characters, dots, or hyphens (for domain name).

# \.\w{2,4} → A dot followed by 2–4 word characters (like .com, .in, .org).

