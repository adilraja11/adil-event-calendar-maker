from django.contrib.auth.models import User
from django.db import models

from .utils import generate_id


# Create your models here.
class Event(models.Model):
    LOCATION_CHOICES = [
        ("online", "Online"),
        ("jakarta", "Jakarta"),
        ("bandung", "Bandung"),
        ("surabaya", "Surabaya"),
        ("yogyakarta", "Yogyakarta"),
        ("bali", "Bali"),
    ]

    id = models.CharField(
        primary_key=True, max_length=24, default=generate_id, editable=False
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
