from django.urls import path
from .views import search_cities, my_trip, city_selector_page, get_weather,flight_search,get_airports_by_city

urlpatterns = [
    path("autocomplete/", search_cities, name="city_autocomplete"),
    path('trip/', my_trip, name='trip'),        
    path("select/", city_selector_page, name="city_selector"),
    path("weather/", get_weather, name="get_weather"),
    path("flights/", flight_search, name="flight_search"),
    path('get-airports/', get_airports_by_city, name='get_airports'),
]