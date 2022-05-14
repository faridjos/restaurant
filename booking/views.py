from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerForm
# BookingForm, 

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
                # 'booking_form': BookingForm(),
                'customer_form': CustomerForm(),
            }
        )
    
    def post(self, request):
        # booking_form = BookingForm(request.POST)
        customer_form = CustomerForm(request.POST)
    # booking_form.is_valid() and    
        if customer_form.is_valid():
            # booking_form.save()
            customer_form.save()
            return redirect('booking')


class Booking(View):
    def get(self, request):
        return render(
            request,
            'booking.html',
        )
