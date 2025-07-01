import requests

# This function fetches the current exchange rate between two currencies
def get_exchange_rate(from_currency, to_currency):
    # API URL from exchangerate.host (free and no API key required)
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"

    # Make the request to the exchange rate API
    response = requests.get(url)

    # Parse the response as JSON
    data = response.json()

    # Extract the conversion rate from the response
    rate = data['info']['rate']
    
    return rate

# This function performs the currency conversion
def convert_currency(amount, from_currency, to_currency):
    # Get the current exchange rate
    rate = get_exchange_rate(from_currency, to_currency)

    # Calculate the converted amount
    converted_amount = amount * rate

    # Display the result with a readable message
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

# Example usage:
# Convert 100 USD to INR
convert_currency(100, "USD", "INR")
