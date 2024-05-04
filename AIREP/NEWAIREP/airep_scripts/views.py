from django.shortcuts import render
# AIREP/scripts/views.py

from API_requests import fetch_house_prices, fetch_crime_rate, fetch_population
from NEWAIREP.airep_scripts.data_preprocessing import preprocess_house_prices_data, preprocess_population_data, preprocess_crime_data
from Main import create_map

def index(request):
    if request.method == 'POST':
        postcode = request.POST.get('postcode')
        api_key = "RBTHF0AXJL"
        region = "greater_london"

        house_prices_data = fetch_house_prices(api_key, postcode, 3)
        crime_data = fetch_crime_rate(api_key, postcode)
        population_data = fetch_population(api_key, postcode)

        house_prices = preprocess_house_prices_data(house_prices_data)
        crime = preprocess_crime_data(crime_data)
        population = preprocess_population_data(population_data)

        map_ = create_map(house_prices_data, population_data, crime_data, api_key, postcode)
        map_html = map_._repr_html_()

        context = {
            'house_prices': house_prices,
            'crime': crime,
            'population': population,
            'map': map_html,
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html')
# Create your views here.
