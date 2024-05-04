# api_requests.py
import requests

def fetch_house_prices(api_key, postcode, bedrooms):
    url = f"https://api.propertydata.co.uk/prices?key={api_key}&postcode={postcode}&bedrooms={bedrooms}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch house prices:", response.status_code)
        return None

def fetch_postcode_key_stats(api_key, region):
    url = f"https://api.propertydata.co.uk/postcode-key-stats?key={api_key}&region={region}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def fetch_population(api_key, postcode):
    url = f"https://api.propertydata.co.uk/population?key={api_key}&postcode={postcode}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch population data:", response.status_code)
        return None

def fetch_crime_rate(api_key, postcode):
    url =f"https://api.propertydata.co.uk/crime?key={api_key}&postcode={postcode}"
    response = requests.get(url)  # Make the API request

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


