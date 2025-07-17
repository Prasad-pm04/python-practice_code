# BMI Calculator in Python
# This program helps users calculate their Body Mass Index and understand their health category.

def calculate_bmi(weight, height):
    """
    BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)
    return bmi

# 👤 Ask the user to input their weight in kilograms
weight = float(input("Enter your weight in kilograms (e.g., 70): "))

# 📏 Ask the user to input their height in meters
height = float(input("Enter your height in meters (e.g., 1.75): "))

# 🔢 Calculate BMI using the function
bmi = calculate_bmi(weight, height)

# 🧾 Print the calculated BMI, rounded to 2 decimal places
print(f"\nYour BMI is: {bmi:.2f}")

# 🧍 Give health feedback based on BMI value
if bmi < 18.5:
    print("You are underweight. Eat healthy and consult a dietician if needed.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight. Keep up the good work!")
elif 25 <= bmi < 29.9:
    print("You are overweight. Consider a balanced diet and regular exercise.")
else:
    print("You are obese. It's advisable to talk to a healthcare provider.")



#Enter your weight in kilograms (e.g., 70): 65
# Enter your height in meters (e.g., 1.75): 1.7

# Your BMI is: 22.49
# You have a normal weight. Keep up the good work!
