from django import forms
from .models import SearchFilter  # import your model

class SearchFilterForm(forms.ModelForm):
    class Meta:
        model = SearchFilter
        fields = [
            'departure_city',
            'arrival_city',
            'departure_airport',
            'arrival_airport',
            'departure_airport_code',
            'arrival_airport_code',
            'departure_date',
            'return_date',
        ]