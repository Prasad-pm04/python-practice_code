# Import the required library
import yfinance as yf
import time

# Function to fetch the current stock price
def get_stock_price(ticker_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch the latest market price
    todays_data = ticker.history(period='1d')
    
    # Return the last closing price
    return todays_data['Close'].iloc[-1]

# Main code starts here
if __name__ == "__main__":
    stock = "AAPL"  # You can change this to "GOOG", "MSFT", etc.
    
    print(f"📈 Tracking live stock price for: {stock}")
    
    # Run this in a loop (like every 5 seconds)
    while True:
        try:
            price = get_stock_price(stock)
            print(f"🔄 Current price of {stock}: ${round(price, 2)}")
            
            # Wait for 5 seconds before checking again
            time.sleep(5)
        
        except Exception as e:
            print(f"❌ Error fetching price: {e}")
            break
