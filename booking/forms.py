from .models import Customer
#, Booking
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fname', 'lname', 'username')


# class BookingForm(forms.ModelForm):
#     class Meta:
 #       model = Booking
#        fields = ('party_size', 'booking_time')
