from django.db import models
from django.utils import timezone

# Create your models here.


class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=255)
    booking_date = models.DateField(default=timezone.now)
    bay_number = models.IntegerField()

    def __str__(self):
        return self.customer_name
