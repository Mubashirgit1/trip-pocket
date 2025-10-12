import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def my_trip(request):
    return render(request, "search/index.html")
# Create your views here.

def city_selector_page(request):
    return render(request, "search/city_selector.html")

def search_cities(request):
    query = request.GET.get("q", "")
    if not query:
        return JsonResponse({"data": []})

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
    }
    params = {"namePrefix": query, "limit": 10}
    res = requests.get(url, headers=headers, params=params)

    data = res.json().get("data", [])
    # simplify data for frontend
    simplified = [
        {"id": city["id"], "name": city["city"], "country": city["country"]}
        for city in data
    ]

    return JsonResponse(simplified, safe=False)



def get_weather(request):
    city = request.GET.get("city", "London")
    api_key = os.getenv("OPENWEATHER_API_KEY")  # store your key in .env
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url)
    data = res.json()

    return JsonResponse(data)



def get_flight_info(flight_iata):
    """Fetch flight data by IATA code, e.g. 'AF123'"""
    api_key = os.getenv("AVIATIONSTACK_API_KEY")  # store your key in .env
    url = f"http://api.aviationstack.com/v1/flights"
    params = {"access_key": api_key, "flight_iata": flight_iata}

    res = requests.get(url, params=params)
    return res.json()


def get_airports_by_city(request):
    city_name = request.GET.get("city")

    if not city_name:
        return JsonResponse({"error": "Missing city parameter"}, status=400)

    url = "http://autocomplete.travelpayouts.com/places2"
    params = {
        "term": city_name,
        "locale": "en",
        "types[]": "airport"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        airports = response.json()
        results = [
            {"name": a["name"], "code": a["code"]}
            for a in airports
        ]
        return JsonResponse({"airports": results})
    else:
        return JsonResponse({"error": "API request failed"}, status=500)

# ✅ Django view
def flight_search(request):
    departure_city = request.GET.get("departure", "New York")
    arrival_city = request.GET.get("arrival", "London")

    dep_code = fetch_airport_code(departure_city)
    arr_code = fetch_airport_code(arrival_city)

    res = {
        "departure_city": departure_city,
        "arrival_city": arrival_city,
        "departure_code": dep_code,
        "arrival_code": arr_code
    }

    print(res)
    return JsonResponse(res)