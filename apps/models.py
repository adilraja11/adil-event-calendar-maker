from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    LOCATION_CHOICES = [
        ('online', 'Online'),
        ('jakarta', 'Jakarta'),
        ('bandung', 'Bandung'),
        ('surabaya', 'Surabaya'),
        ('yogyakarta', 'Yogyakarta'),
        ('bali', 'Bali'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name