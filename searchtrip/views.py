import json
import os
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import SearchFilter
from .forms import SearchFilterForm, ContactForm

# =============================
#        VIEW FUNCTIONS
# =============================

def home(request):
    """Render the home page of the application."""
    return render(request, "search/index.html")


@login_required(login_url='/accounts/login/')
def search_filter(request):
    """Display saved flight searches for the logged-in user."""
    saved_searches = SearchFilter.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "search/flight_search.html", {
        'saved_searches': saved_searches
    })


@login_required
def get_saved_searches(request):
    """Return all saved flight search filters for the logged-in user in JSON format."""
    searches = SearchFilter.objects.filter(user=request.user).order_by('-created_at')
    data = [
        {
            "id": s.id,
            "departureCity": s.departure_city,
            "arrivalCity": s.arrival_city,
            "departureAirport": s.departure_airport,
            "arrivalAirport": s.arrival_airport,
            "departureAirportCode": s.departure_airport_code,
            "arrivalAirportCode": s.arrival_airport_code,
            "departureDate": s.departure_date,
            "returnDate": s.return_date,
        }
        for s in searches
    ]
    return JsonResponse(data, safe=False)


@csrf_exempt
@login_required
def edit_search(request, search_id):
    """Edit and update an existing saved flight search for the logged-in user."""
    search = get_object_or_404(SearchFilter, id=search_id, user=request.user)
    try:
        data = json.loads(request.body.decode('utf-8'))
        form = SearchFilterForm(data, instance=search)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Search updated successfully.',
                'data': {
                    'id': search.id,
                    'departure_city': search.departure_city,
                    'arrival_city': search.arrival_city,
                    'departure_airport': search.departure_airport,
                    'arrival_airport': search.arrival_airport,
                    'departure_date': str(search.departure_date) if search.departure_date else None,
                    'return_date': str(search.return_date) if search.return_date else None,
                }
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid data.',
                'errors': form.errors
            }, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)


@login_required
def search_cities(request):
    """Search for city names using the GeoDB Cities API (RapidAPI)."""
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
    simplified = [
        {"id": city["id"], "name": city["city"], "country": city["country"]}
        for city in data
    ]
    return JsonResponse(simplified, safe=False)


@login_required
def save_filter(request):
    """Save a new flight search filter to the user's account."""
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        filter_obj = SearchFilter.objects.create(
            user=request.user,
            departure_city=data.get("departure_city"),
            arrival_city=data.get("arrival_city"),
            departure_airport_code=data.get("departure_airport_code") or None,
            arrival_airport_code=data.get("arrival_airport_code") or None,
            departure_airport=data.get("dep_airportName") or None,
            arrival_airport=data.get("arr_airportName") or None,
            departure_date=data.get("departure_date"),
            return_date=data.get("return_date") or None
        )
        return JsonResponse({"message": "Filter saved successfully!", "id": filter_obj.id})

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def get_airports_by_city(request):
    """Fetch a list of airports based on a given city using Booking.com API."""
    query = request.GET.get("city", "")
    if not query:
        return JsonResponse({"error": "Missing city parameter"}, status=400)

    url = "https://booking-com-api5.p.rapidapi.com/flight/find-airport"
    api_key = os.getenv("BOOKINGRAPIDAPI_KEY")
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
            {"name": a.get("name"), "code": a.get("code")}
            for a in airports_data if isinstance(a, dict)
        ]
        return JsonResponse({"airports": results})
    else:
        return JsonResponse({"error": response.text}, status=500)


@login_required
def search_flights(request):
    """Search available roundtrip flights between two airports using Booking.com API."""
    api_key = os.getenv("BOOKINGRAPIDAPI_KEY")
    url = "https://booking-com-api5.p.rapidapi.com/flight/find-roundtrip"

    dep_code = request.GET.get("dep")
    arr_code = request.GET.get("arr")
    dep_date = request.GET.get("dep_date")
    return_date = request.GET.get("return_date")
    adults = request.GET.get("adults", 1)
    children = request.GET.get("children", "")
    cabin_class = request.GET.get("cabin_class", "ECONOMY")

    querystring = {
        "languagecode": "en",
        "children": children,
        "cabin_class": cabin_class,
        "adults": adults,
        "page": "1",
        "depart": dep_date,
        "return": return_date,
        "from": dep_code,
        "to": arr_code,
        "currency": "GBP"
    }
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "booking-com-api5.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            try:
                data = response.json()
                return JsonResponse(data)
            except ValueError:
                return JsonResponse({
                    "success": False,
                    "code": response.status_code,
                    "message": response.text or "Invalid response from API"
                }, status=response.status_code)

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


@login_required
def delete_search(request, search_id):
    """Delete a saved flight search from the user's account."""
    if request.method == "DELETE":
        search = SearchFilter.objects.filter(id=search_id, user=request.user).first()
        if search:
            search.delete()
            return JsonResponse({"message": "Deleted successfully"})
        else:
            return JsonResponse({"error": "Search not found"}, status=404)
    return JsonResponse({"error": "Invalid method"}, status=405)


@login_required
def flight_search(request):
    """Return flight search details for selected departure and arrival cities."""
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


def contact_view(request):
    """Handle the Contact Us form submission and display confirmation messages."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            messages.success(request, f"Thank you {name}! We’ll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def custom_404(request, exception):
    """Render a custom 404 error page when a route is not found."""
    return render(request, "404.html", status=404)


def get_exchange_rate(request):
    """Fetch real-time currency exchange rate using the ExchangeRate API."""
    base = request.GET.get('base', 'USD')
    target = request.GET.get('target', 'GBP')

    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch exchange rate'}, status=500)

    data = response.json()
    rate = data['rates'].get(target)

    return JsonResponse({
        'base': base,
        'target': target,
        'rate': rate,
    })
