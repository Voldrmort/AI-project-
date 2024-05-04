import requests

def geocode_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latitude = data['result']['latitude']
        longitude = data['result']['longitude']
        return latitude, longitude
    else:
        print(f"Failed to geocode postcode {postcode}")
        return None, None
'''
# Example usage:
postcode = "SW1A 1AA"  # Example postcode
latitude, longitude = geocode_postcode(postcode)
print("Latitude:", latitude)
print("Longitude:", longitude)
'''
'''
# Example usage:
postcode = "E16 2GW"  # Example postcode
latitude, longitude = geocode_postcode(postcode)
print("Latitude:", latitude)
print("Longitude:", longitude)
'''