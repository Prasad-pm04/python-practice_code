# Simple Unit Converter App
# Converts values between different units like km to miles, Celsius to Fahrenheit, etc.

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def show_menu():
    print("\n🔄 Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            km = float(input("Enter kilometers: "))
            miles = km_to_miles(km)
            print(f"🚗 {km} km = {miles:.2f} miles\n")

        elif choice == '2':
            miles = float(input("Enter miles: "))
            km = miles_to_km(miles)
            print(f"🛣️ {miles} miles = {km:.2f} km\n")

        elif choice == '3':
            c = float(input("Enter Celsius temperature: "))
            f = celsius_to_fahrenheit(c)
            print(f"🌡️ {c}°C = {f:.2f}°F\n")

        elif choice == '4':
            f = float(input("Enter Fahrenheit temperature: "))
            c = fahrenheit_to_celsius(f)
            print(f"🌡️ {f}°F = {c:.2f}°C\n")

        elif choice == '5':
            print("👋 Exiting Unit Converter. Stay smart!")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")

# Start the unit converter app
main()
