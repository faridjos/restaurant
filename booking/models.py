from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, blank=True, null=True,
                                unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="name", blank=True,
        null=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return str(self.last_name)


class Table(models.Model):
    number_of_seats = models.IntegerField()

    class Meta:
        ordering = ['number_of_seats']

    def __str__(self):
        return str(self.number_of_seats)


class Booking(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="bookings")
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="bookings")
    party_size = models.IntegerField()
    booking_time = models.DateTimeField()
    time_of_booking = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['booking_time']
