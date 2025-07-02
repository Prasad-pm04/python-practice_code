import requests

# This function fetches top headlines from NewsAPI based on the country code
def get_top_news(country='in'):
    # NewsAPI key (Get yours for free at https://newsapi.org/)
    api_key = "your_newsapi_key_here"  # Replace with your actual API key

    # URL to get top headlines for a country (e.g., 'in' for India, 'us' for USA)
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"

    try:
        # Make the API request to fetch news
        response = requests.get(url)
        data = response.json()  # Convert JSON string to Python dictionary

        # Check if the request was successful
        if data["status"] == "ok":
            print(f"\n📰 Top Headlines for country code '{country.upper()}':\n")

            # Loop through the top 5 articles
            for i, article in enumerate(data["articles"][:5], 1):
                print(f"{i}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   Link: {article['url']}\n")
        else:
            # If API call failed
            print("Failed to fetch news:", data.get("message", "Unknown error"))

    except Exception as e:
        # Handle unexpected errors (e.g., no internet)
        print("Error occurred while fetching news:", e)

# ---- Main Program ----

# Ask user for a country code (default is 'in' for India)
country_code = input("Enter a 2-letter country code (e.g., in, us, gb): ").lower()
get_top_news(country_code if country_code else 'in')
