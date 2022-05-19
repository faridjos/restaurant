from django.contrib import admin
from .models import Customer, Booking, Table

# Register your models here.
# From Code Institute Django3blog


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['last_name']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number_of_seats',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party_size', 'table', 'booking_time',
                    'time_of_booking')
    list_filter = ('booking_time',)
    search_fields = ['customer']
