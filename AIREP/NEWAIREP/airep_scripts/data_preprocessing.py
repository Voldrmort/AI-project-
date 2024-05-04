# data_preprocessing.py
#from NEWAIREP.airep_scripts.API_requests import fetch_house_prices, fetch_crime_rate, fetch_population


def preprocess_postcode_key_stats(fetch_postcode_key_stats_data):
    try:
        # Extract relevant information from the API response
        postcode = fetch_postcode_key_stats_data['data'][0]['outcode']  # Extract 'outcode'
        avg_price = fetch_postcode_key_stats_data['data'][0]['avg_price']
        avg_rent = fetch_postcode_key_stats_data['data'][0]['avg_rent']
        growth_1y = fetch_postcode_key_stats_data['data'][0]['growth_1y']
        growth_3y = fetch_postcode_key_stats_data['data'][0]['growth_3y']
        sales_per_month = fetch_postcode_key_stats_data['data'][0]['sales_per_month']

        # Return the preprocessed data as a dictionary
        preprocessed_data = {
            'postcode': postcode,  # Use 'postcode' as the key
            'avg_price': avg_price,
            'avg_rent': avg_rent,
            'growth_1y': growth_1y,
            'growth_3y': growth_3y,
            'sales_per_month': sales_per_month
        }
        return [preprocessed_data]  # Return the preprocessed data as a list of dictionaries
    except (KeyError, IndexError) as e:
        print(f"Error occurred while preprocessing data: {e}")
        return None
def preprocess_house_prices_data(fetch_house_prices):
    try:
        # Extract relevant information from the API response
        average_price = fetch_house_prices['data']['average']
        range_70pc = fetch_house_prices['data']['70pc_range']
        range_80pc = fetch_house_prices['data']['80pc_range']
        range_90pc = fetch_house_prices['data']['90pc_range']
        range_100pc = fetch_house_prices['data']['100pc_range']
        points_analysed = fetch_house_prices['data']['points_analysed']

        # Return the preprocessed data as a dictionary
        preprocessed_data = {
            'average_price': average_price,
            'range_70pc': range_70pc,
            'range_80pc': range_80pc,
            'range_90pc': range_90pc,
            'range_100pc': range_100pc,
            'points_analysed': points_analysed
        }
        return preprocessed_data
    except (KeyError, IndexError) as e:
        print(f"Error occurred while preprocessing house prices data: {e}")
        return None
def preprocess_population_data(population_data):
    try:
        # Extract relevant information from the API response
        population = int(population_data['result']['population'].replace(',', ''))
        households = int(population_data['result']['households'].replace(',', ''))
        density = int(population_data['result']['density'].replace(',', ''))

        # Return the preprocessed data as a dictionary
        preprocessed_data = {
            'population': population,
            'households': households,
            'density': density
        }
        return preprocessed_data
    except (KeyError, ValueError) as e:
        print(f"Error occurred while preprocessing population data: {e}")
        return None
def preprocess_crime_data(fetch_crime_rate_data):
    try:
        # Extract relevant information from the API response
        crimes_last_12m = fetch_crime_rate_data.get('crimes_last_12m', None)
        crimes_per_thousand = fetch_crime_rate_data.get('crimes_per_thousand', None)
        crime_rating = fetch_crime_rate_data.get('crime_rating', None)
        crime_types = fetch_crime_rate_data.get('types', None)

        # Return the preprocessed data as a dictionary
        preprocessed_data = {
            'crimes_last_12m': crimes_last_12m,
            'crimes_per_thousand': crimes_per_thousand,
            'crime_rating': crime_rating,
            'crime_types': crime_types
        }
        return preprocessed_data
    except (KeyError, ValueError) as e:
        print(f"Error occurred while preprocessing crime data: {e}")
        return None
# Example usage
'''
api_response = {
    'status': 'success',
    'radius': '0.41',
    'population': 24364,
    'crimes_last_12m': 2853,
    'crimes_per_thousand': 117,
    'crime_rating': 'Low crime',
    'types': {
        'Anti-social behaviour': 935,
        'Violence and sexual offences': 597,
        'Other theft': 280,
        # Other crime types...
    }
    
   }
'''



 # Example postcode
#fetch_postcode_key_stats_data = fetch_postcode_key_stats(api_key, region)

# Pass the API data to the preprocess_data function for preprocessing
# preprocessed_postcode_data = preprocess_data(fetch_postcode_key_stats_data)

'''
if __name__ == "__main__":
    # Example usage
    api_key = "RBTHF0AXJL"  # Replace with your actual API key
    postcode = input("Enter the postcode: ")
    region = "greater_london"  # Replace with your actual region

    # Fetch data from APIs
    house_prices_data = fetch_house_prices(api_key, postcode, 3)
    crime_data = fetch_crime_rate(api_key, postcode)
    population_data = fetch_population(api_key, postcode)

    # Preprocess the fetched data
    preprocessed_house_prices_data = preprocess_house_prices_data(house_prices_data)
    preprocessed_crime_data = preprocess_crime_data(crime_data)
    preprocessed_population_data = preprocess_population_data(population_data)

    # Print the preprocessed data
    print("Preprocessed House Prices Data:", preprocessed_house_prices_data)
    print("Preprocessed Crime Data:", preprocessed_crime_data)
    print("Preprocessed Population Data:", preprocessed_population_data)

'''