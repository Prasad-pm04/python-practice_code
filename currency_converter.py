import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Error fetching exchange rate data."

    data = response.json()

    if to_currency.upper() not in data['rates']:
        return "Target currency not available."

    rate = data['rates'][to_currency.upper()]
    converted_amount = amount * rate

    return f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}"

# Example usage:
from_currency = "USD"
to_currency = "INR"
amount = 10

print(convert_currency(from_currency, to_currency, amount))
