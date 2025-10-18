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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label='Your Message'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label