from .models import Customer, Booking
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username')


class BookingForm(forms.ModelForm):
    booking_time = forms.DateTimeField (
        widget=forms.DateTimeInput (
            attrs={
                'type': 'datetime-local',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ('party_size', 'booking_time')
