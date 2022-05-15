from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CustomerForm, BookingForm
from .models import Booking, Customer
from datetime import datetime

# Create your views here.


class MainImage(View):
    def get(self, request):
        form = "form"
        return render(
            request,
            'index.html',
            {
                'form': form,
            }
        )


class Contact(View):
    def get(self, request):
        form = "form"
        return render(
            request,
            'contact.html',
            {
                'form': form,
            }
        )


class Form(View):
    def get(self, request):
        return render(
            request,
            'form.html',
            {
                'booking_form': BookingForm(),
                'customer_form': CustomerForm(),
            }
        )
    
    def post(self, request):
        customer_form = CustomerForm(request.POST)
        booking_form = BookingForm(request.POST)
        if customer_form.is_valid() and booking_form.is_valid():
            customer = customer_form.save()
            booking = booking_form.save(commit=False) 
            booking.customer = customer
            booking = booking_form.save()
            return redirect('booking', booking.id)


class Show_booking(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking_time = booking.booking_time.strftime("%d/%m/%Y %H:%M")
        time_of_booking = booking.time_of_booking.strftime("%d/%m/%Y %H:%M")
        return render(
            request,
            'booking.html',
            {
                'booking': booking,
                'booking_time': booking_time,
                'time_of_booking': time_of_booking,
            }
        )
