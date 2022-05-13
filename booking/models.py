from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="name", blank=True, null=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    class Meta:
        ordering = ['lname']

    def __str__(self):
        return self.lname


class Table(models.Model):
    number_of_seats = models.IntegerField()

    class Meta:
        ordering = ['number_of_seats']


class Booking(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="bookings")
    tables = models.ManyToManyField(Table, related_name="bookings")
    party_size = models.IntegerField()
    booking_time = models.DateTimeField()
    time_of_booking = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booking_time']
