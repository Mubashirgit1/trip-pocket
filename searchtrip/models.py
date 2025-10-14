from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SearchFilter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_filters')
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.departure_city} to {self.arrival_city}"