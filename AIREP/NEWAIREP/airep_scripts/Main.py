import folium
from NEWAIREP.airep_scripts.geocoding import geocode_postcode
from NEWAIREP.airep_scripts.API_requests import fetch_house_prices, fetch_crime_rate, fetch_population
from NEWAIREP.airep_scripts.data_preprocessing import preprocess_house_prices_data, preprocess_population_data, preprocess_crime_data


def main():
    # Hardcoded API key and region
    api_key = "RBTHF0AXJL"  # Replace with your actual API key
    region = "greater_london"  # Replace with your actual region

    # Get user input
    postcode = input("Enter the postcode: ")

    # Fetch data from APIs
    house_prices_data = fetch_house_prices(api_key, postcode, 3)
    crime_data = fetch_crime_rate(api_key, postcode)
    population_data = fetch_population(api_key, postcode)

    # Preprocess the fetched data
    preprocessed_house_prices_data = preprocess_house_prices_data(house_prices_data)
    preprocessed_crime_data = preprocess_crime_data(crime_data)
    preprocessed_population_data = preprocess_population_data(population_data)

    # Create map and display
    if preprocessed_house_prices_data and preprocessed_population_data and preprocessed_crime_data:
        map = create_map(preprocessed_house_prices_data, preprocessed_population_data, preprocessed_crime_data, api_key, postcode)
        map.save("interactive_map.html")  # Save map to HTML file
        print("Map saved as interactive_map.html")

def create_map(house_prices_data, population_data, crime_data, api_key, postcode):
    # Create Folium map object
    map = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

    # Get latitude and longitude for the postcode
    latitude, longitude = geocode_postcode(postcode)

    # Plot house prices data on map
    house_prices_layer = folium.FeatureGroup(name="House Prices")
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Average 3 bed: {house_prices_data['average_price']}",
        icon=folium.Icon(color="green"),
    ).add_to(house_prices_layer)
    house_prices_layer.add_to(map)

    # Plot population data on map
    population_layer = folium.FeatureGroup(name="Population")
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Population in radius: {population_data['population']}",
        icon=folium.Icon(color="blue"),
    ).add_to(population_layer)
    population_layer.add_to(map)

    # Plot crime data on map
    crime_layer = folium.FeatureGroup(name="Crime")
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Crimes: {crime_data['crime_rating']}",
        icon=folium.Icon(color="red"),
    ).add_to(crime_layer)
    crime_layer.add_to(map)

    # Add layer control to toggle layers
    folium.LayerControl().add_to(map)

    return map

if __name__ == "__main__":
    main()