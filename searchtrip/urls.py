from django.urls import path
from .views import search_cities, home, get_weather,flight_search,get_airports_by_city,search_flights,search_filter

urlpatterns = [
    path("autocomplete/", search_cities, name="city_autocomplete"),
    path('', home, name='home'),        
    path("search/", search_filter, name="search_filter"),
    path("weather/", get_weather, name="get_weather"),
    path("flights/", flight_search, name="flight_search"),
    path('search-flights/', search_flights, name='search_flights'),
    path('get-airports/', get_airports_by_city, name='get_airports'),

]