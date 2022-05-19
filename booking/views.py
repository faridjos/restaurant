from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CustomerForm, BookingForm
from .models import Customer, Booking, Table
from datetime import datetime
from .routines import validate_form, round_datetime, found_any_table
from django.contrib import messages


# Create your views here.


class MainImage(View):
    """Render the home page"""
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
    """Render the contact page"""
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
    """Render and submit form. Make a booking and display message
    if it was successful or not"""
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
        if booking_form.is_valid():
            if request.user.is_authenticated:
                customer_form.instance.user = request.user
                customer_form.instance.username = request.user.username
                username = customer_form.instance.username
            else:
                username = request.POST.get('username')
            if username is not None:
                if not username.isspace():
                    # Do not create customer object if it already exists.
                    # A customer is identified by his username.
                    if Customer.objects.filter(username=username).exists():
                        customer = get_object_or_404(
                            Customer, username=username)
                    else:
                        customer = customer_form.save()
                # If the customer does not write his username (it is optional)
                # there is no way of knowing if the customer has a record or
                # not.
                else:
                    customer = customer_form.save()
            else:
                customer = customer_form.save()
            booking = booking_form.save(commit=False)
            # Validate form
            if validate_form(self, booking.party_size, booking.booking_time):
                booking.customer = customer
                round_booking_time = round_datetime(self, booking.booking_time)
                booking.booking_time = round_booking_time
                [found, table_id] = found_any_table(
                    self, booking.party_size, booking.booking_time)
                # Store booking if table is found
                if found:
                    table = get_object_or_404(Table, id=table_id)
                    booking.table = table
                    booking = booking_form.save()
                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your booking was sucessful!')
                    # Show booking
                    return redirect('booking', booking.id)
                else:
                    messages.add_message(
                        request, messages.ERROR, 'No available table')
                    return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(instance=customer),
                        }
                    )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Error in party size (0-4) or booking time (see opening hours)')
                return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(instance=customer),
                        }
                )
        else:
            messages.add_message(
                        request, messages.ERROR, 'Error in booking form')
            return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(),
                            'customer_form': CustomerForm(),
                        }
            )


class ShowBooking(View):
    """Show booking if it was successful"""
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        # Format time for printing on booking card
        booking_time = booking.booking_time.astimezone().strftime(
            "%d/%m/%Y %H:%M")
        time_of_booking = booking.time_of_booking.astimezone().strftime(
            "%d/%m/%Y %H:%M")
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
    """Show booking if any"""
    def get(self, request):
        if Customer.objects.filter(username=request.user.username).exists():
            customer = get_object_or_404(
                Customer, username=request.user.username)
            if customer.bookings.exists():
                bookings = customer.bookings.all().order_by('booking_time')
                dt = datetime.now().astimezone()
                for booking in bookings:
                    if booking.booking_time >= dt:
                        # Show first booking if several
                        return redirect('booking', booking.id)
                    else:
                        messages.add_message(
                            request, messages.ERROR, 'You have no booking')
                        return redirect('home')
            else:
                messages.add_message(
                    request, messages.ERROR, 'You have no booking')
                return redirect('home')
        else:
            messages.add_message(
                    request, messages.ERROR, 'You have no booking')
            return redirect('home')


class CancelBooking(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'You successfully cancelled your booking!')
        return redirect('home')


class EditForm(View):
    def get(self, request, booking_id):
        # Render prepopulated booking form
        booking = get_object_or_404(Booking, id=booking_id)
        customer = booking.customer
        return render(
            request,
            'form.html',
            {
                'booking_form': BookingForm(instance=booking),
                'customer_form': CustomerForm(instance=customer),
            }
        )

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        customer = booking.customer
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            # Validate form
            if validate_form(self, booking.party_size, booking.booking_time):
                round_booking_time = round_datetime(self, booking.booking_time)
                booking.booking_time = round_booking_time
                [found, table_id] = found_any_table(
                    self, booking.party_size, booking.booking_time)
                # Store booking if table is found
                if found:
                    table = get_object_or_404(Table, id=table_id)
                    booking.table = table
                    booking = booking_form.save()
                    messages.add_message(
                        request, messages.SUCCESS,
                        'Your booking was sucessful!')
                    return redirect('booking', booking.id)
                else:
                    messages.add_message(
                        request, messages.ERROR, 'No available table')
                    return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(instance=booking),
                            'customer_form': CustomerForm(instance=customer),
                        }
                    )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Error in party size (0-4) or booking time (see opening hours)')
                return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(instance=booking),
                            'customer_form': CustomerForm(instance=customer),
                        }
                )
        else:
            messages.add_message(
                        request, messages.ERROR, 'Error in booking form')
            return render(
                        request,
                        'form.html', {
                            'booking_form': BookingForm(instance=booking),
                            'customer_form': CustomerForm(instance=customer),
                        }
            )
