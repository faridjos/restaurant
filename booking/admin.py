from django.contrib import admin
from .models import Customer, Table
#, Booking

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname')
    search_fields = ['lname']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number_of_seats',)

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#    list_display = ('customer', 'party_size', 'booking_time', 'time_of_booking')
#    list_filter = ('booking_time',)
#    search_fields = ['customer']
