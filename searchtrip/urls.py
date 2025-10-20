from django.urls import path
from .views import search_cities, home,flight_search,get_airports_by_city,search_flights,search_filter,save_filter,get_saved_searches,edit_search,delete_search,contact_view,get_exchange_rate

urlpatterns = [
    path("autocomplete/", search_cities, name="city_autocomplete"),
    path('', home, name='home'),        
    path("search/", search_filter, name="search_filter"),
    path("flights/", flight_search, name="flight_search"),
    path('search-flights/', search_flights, name='search_flights'),
    path('get-airports/', get_airports_by_city, name='get_airports'),
    path("save-filter/", save_filter, name="save_filter"),
    path("get-saved-searches/", get_saved_searches, name="get_saved_searches"),
    path('edit-search/<int:search_id>/', edit_search, name='edit_search'),
    path('delete-search/<int:search_id>/', delete_search, name='delete_search'),
    path('contact/', contact_view, name='contact'),
    path('api/exchange-rate/', get_exchange_rate, name='exchange_rate'),
]