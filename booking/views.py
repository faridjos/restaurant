from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CustomerForm, BookingForm
from .models import Customer, Booking, Table
from datetime import datetime
from .routines import validate_form, round_datetime, found_table, found_any_table
from django.utils import timezone


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
            print("hej1")
            customer = customer_form.save(commit=False)
            booking = booking_form.save(commit=False)
            print(booking.party_size)
            if validate_form(self, booking.party_size, booking.booking_time):
                print("hej2")
                if request.user.is_authenticated:
                    customer.user = request.user
                    customer.username = request.user.username
                booking.customer = customer
                round_booking_time = round_datetime(self, booking.booking_time)
                booking.booking_time = round_booking_time
                [found, table_id] = found_any_table(self, booking.party_size, booking.booking_time)
                if found:
                    print("hej3")
                    table = get_object_or_404(Table, id=table_id)
                    booking.table = table
                    customer = customer_form.save()
                    booking = booking_form.save()
                    return redirect('booking', booking.id)
                else:
                    return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(),
                        }
                    )
            else:
                return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(),
                        }
                )
        else:
            return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(),
                        }
            )
            


class ShowBooking(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking_time = booking.booking_time.strftime("%d/%m/%Y %H:%M %Z")
        time_of_booking = booking.time_of_booking.strftime("%d/%m/%Y %H:%M %Z")
        return render(
            request,
            'booking.html',
            {
                'booking': booking,
                'booking_time': booking_time,
                'time_of_booking': time_of_booking,
            }
        )


class BookingButton(View):
    def get(self, request):
        if Customer.objects.filter(username=request.user.username).exists():
            customer = get_object_or_404(Customer, username=request.user.username)
            booking = customer.bookings.all()[0]
            dt = datetime.now()
            dt_aware = timezone.make_aware(dt, timezone.get_current_timezone())
            if booking.booking_time >= dt_aware:
                return redirect('booking', booking.id)
            else: 
                return redirect('home')
        else: 
            return redirect('home')
