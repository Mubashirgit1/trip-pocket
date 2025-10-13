import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    return render(request, "search/index.html")
# Create your views here.

def search_filter(request):
    return render(request, "search/flight_search.html")

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





def get_airports_by_city(request):
    query = request.GET.get("city", "")
    if not query:
        return JsonResponse({"error": "Missing city parameter"}, status=400)

    url = "https://booking-com-api5.p.rapidapi.com/flight/find-airport"
    api_key = os.getenv("BOOKINGRAPIDAPI_KEY")  # store your key in .env

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "booking-com-api5.p.rapidapi.com"
    }
    params = {"query": query, "languagecode": "en"}
   
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        airports_data = data.get("data", [])
        results = [
                {
                    "name": a.get("name"),
                    "code": a.get("code")
                }
                for a in airports_data
                if isinstance(a, dict)
            ]
        return JsonResponse({"airports": results})
    else:
        return JsonResponse({"error": "API request failed"}, status=500)



# ✅ Django view


# i try aviation apis but need paid version
# def get_flight_info(flight_iata):
#     """Fetch flight data by IATA code, e.g. 'AF123'"""
#     api_key = os.getenv("AVIATIONSTACK_API_KEY")  # store your key in .env
#     url = f"http://api.aviationstack.com/v1/flights"
#     params = {"access_key": api_key, "flight_iata": flight_iata}

#     res = requests.get(url, params=params)
#     return res.json()


def search_flights(request):
    api_key = os.getenv("BOOKINGRAPIDAPI_KEY")  # store your key in .env

    url = "https://booking-com-api5.p.rapidapi.com/flight/find-roundtrip"

    # Get parameters from GET request
    dep_code = request.GET.get("dep")
    arr_code = request.GET.get("arr")
    dep_date = request.GET.get("dep_date")
    return_date = request.GET.get("return_date")  # optional
    adults = request.GET.get("adults", 1)
    children = request.GET.get("children", "")  # e.g., "4,12"
    cabin_class = request.GET.get("cabin_class", "ECONOMY")


    querystring = {"languagecode":"en","children":"","cabin_class":"PREMIUM_ECONOMY","adults":"1","page":"1","depart":dep_date,"return":return_date,"from":dep_code,"to":arr_code,"currency":"GBP"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "booking-com-api5.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        # ✅ Handle Booking.com API error messages
        if response.status_code != 200:
            try:
                data = response.json()
                response.raise_for_status()
                data = response.json()
                return JsonResponse(data)  # return as JSON to frontend
            except ValueError:
                # Non-JSON response (like HTML error page)
                return JsonResponse({
                    "success": False,
                    "code": response.status_code,
                    "message": response.text or "Invalid response from API"
                }, status=response.status_code)

        # ✅ Parse successful responses
        data = response.json()
        if not data.get("data"):
            return JsonResponse({
                "success": False,
                "code": 404,
                "message": "No Flight Found"
            }, status=404)

        return JsonResponse({
            "success": True,
            "data": data["data"]
        })

    except requests.RequestException as e:
        return JsonResponse({
            "success": False,
            "code": 500,
            "message": str(e)
        }, status=500)



def flight_search(request):
    departure_city = request.GET.get("departure", "New York")
    arrival_city = request.GET.get("arrival", "London")

    dep_code = get_airports_by_city(departure_city)
    arr_code = get_airports_by_city(arrival_city)

    res = {
        "departure_city": departure_city,
        "arrival_city": arrival_city,
        "departure_code": dep_code,
        "arrival_code": arr_code
    }

    print(res)
    return JsonResponse(res)