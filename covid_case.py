import requests

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"COVID-19 Stats for {country}:")
        print(f"🧍 Total Cases: {data['cases']}")
        print(f"💀 Total Deaths: {data['deaths']}")
        print(f"❤️ Recovered: {data['recovered']}")
        print(f"📅 Today's Cases: {data['todayCases']}")
        print(f"📅 Today's Deaths: {data['todayDeaths']}")
    else:
        print("Failed to retrieve data. Please check the country name or try again later.")

# Example usage
get_covid_data("India")
