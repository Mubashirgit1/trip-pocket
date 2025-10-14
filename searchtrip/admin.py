from django.contrib import admin

# Register your models here.
from .models import SearchFilter

admin.site.register(SearchFilter)
class SearchFilterAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'departure_city', 
        'departure_airport_code',
        'arrival_city', 
        'arrival_airport_code',
        'departure_date', 
        'return_date',
        'created_at'
    )
    search_fields = (
        'departure_city', 
        'arrival_city', 
        'departure_airport_code',
        'arrival_airport_code',
        'user__username'
    )