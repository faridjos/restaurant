from datetime import datetime, timedelta
from .models import Customer, Table, Booking

def validate_form(self, party_size, booking_time):
    if party_size not in range(1, 5):
        return False
    day = booking_time.strftime("%A")
    if day in ("Saturday", "Sunday"):
        if booking_time.hour in range(1, 10):
            return False
    else:
        if booking_time.hour in range(0, 10):
            return False
    return True

def round_datetime(self, date_time):
    dt = date_time
    minutes = date_time.minute
    round_minutes = round(minutes/30.0)*30
    dt = dt - timedelta(minutes=minutes) + timedelta(minutes=round_minutes)
    return dt

def found_table(self, number_of_seats, party_size, booking_time):

    if not Table.objects.filter(number_of_seats=number_of_seats).exists():
        return [False, 0]
    else:
        tables = Table.objects.filter(number_of_seats=number_of_seats)

    for table in tables:
        found_empty_table = True
        if table.bookings.exists():
            for booking in table.bookings.all():
                if (booking.booking_time - timedelta(hours=2)) <= booking_time < (booking.booking_time + timedelta(hours=2)):
                    found_empty_table = False
                    break
        if found_empty_table:
            return [True, table.id]

    if not found_empty_table:
        for table in tables:
            found_seats = True
            if table.bookings.exists():
                for booking in table.bookings.all():
                    if (booking.booking_time - timedelta(hours=2)) <= booking_time < (booking.booking_time + timedelta(hours=2)):
                        if party_size > number_of_seats - booking.party_size:
                            found_seats = False
                            break
            if found_seats:
                return [True, table.id]

    return [False, 0]

def found_any_table(self, party_size, booking_time):

    if party_size in (3, 4):
        [found, table_id] = found_table(self, 4, party_size, booking_time)
        if found:
            return [found, table_id]
        return [False, 0]

    if party_size in (1, 2):
        [found, table_id] = found_table(self, 2, party_size, booking_time)
        if found:
            return [found, table_id]
        [found, table_id] = found_table(self, 4, party_size, booking_time)
        if found:
            return [found, table_id]
        return [False, 0]
