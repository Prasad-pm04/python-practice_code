# Simple ATM Program in Python

# Let's assume this is the user's account balance
account_balance = 10000  

# Function to display the ATM menu
def display_menu():
    print("\nWelcome to the Python Bank ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Main loop to keep the ATM running until user chooses to exit
while True:
    display_menu()  # Show the menu options

    # Ask user to choose an option
    choice = input("Please enter your choice (1-4): ")

    # Check balance
    if choice == '1':
        print(f"Your current balance is ₹{account_balance}")

    # Deposit money
    elif choice == '2':
        deposit_amount = float(input("Enter amount to deposit: ₹"))
        if deposit_amount > 0:
            account_balance += deposit_amount
            print(f"₹{deposit_amount} deposited successfully!")
        else:
            print("Invalid amount. Please try again.")

    # Withdraw money
    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: ₹"))
        if 0 < withdraw_amount <= account_balance:
            account_balance -= withdraw_amount
            print(f"₹{withdraw_amount} withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount.")

    # Exit the program
    elif choice == '4':
        print("Thank you for using Python Bank ATM. Goodbye!")
        break

    # Handle invalid input
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
