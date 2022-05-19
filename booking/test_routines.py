"""Test the four subroutines in routines.py"""
from django.test import TestCase
from datetime import datetime, timedelta
from .routines import validate_form, round_datetime
from .routines import found_table, found_any_table
from .models import Customer, Table, Booking
import pytz
# Create your tests here.


class TestRoutines(TestCase):

    def test_validate_booking_time1(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        self.assertTrue(validate_form(self, 2, date_time))

    def test_validate_booking_time2(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(hours=2)
        self.assertFalse(validate_form(self, 2, date_time))

    def test_validate_booking_time3(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(days=5, hours=2)
        self.assertTrue(validate_form(self, 2, date_time))

    def test_validate_booking_time4(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(days=6, hours=2)
        self.assertTrue(validate_form(self, 2, date_time))

    def test_round_datetime(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        self.assertEqual(round_datetime(self, date_time).minute, 0)
        self.assertEqual(round_datetime(self, date_time).hour, 23)

    def test_round_datetime2(self):
        date_time = datetime(2022, 5, 15, 23, 10)
        self.assertEqual(round_datetime(self, date_time).minute, 0)
        self.assertEqual(round_datetime(self, date_time).hour, 23)

    def test_round_datetime3(self):
        date_time = datetime(2022, 5, 15, 23, 20)
        self.assertEqual(round_datetime(self, date_time).minute, 30)
        self.assertEqual(round_datetime(self, date_time).hour, 23)

    def test_round_datetime4(self):
        date_time = datetime(2022, 5, 15, 23, 40)
        self.assertEqual(round_datetime(self, date_time).minute, 30)
        self.assertEqual(round_datetime(self, date_time).hour, 23)

    def test_found_table1(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table = Table.objects.create(number_of_seats=2)
        booking_time = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table, party_size=2,
            booking_time=booking_time, time_of_booking=time_of_booking)
        found = found_table(
            self, 2, 2, datetime(2022, 5, 20, 14, 00, tzinfo=pytz.UTC))[0]
        self.assertTrue(found)

    def test_found_table2(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table = Table.objects.create(number_of_seats=2)
        booking_time = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table, party_size=2,
            booking_time=booking_time, time_of_booking=time_of_booking)
        found = found_table(
            self, 2, 2, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertFalse(found)

    def test_found_table3(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table1 = Table.objects.create(number_of_seats=2)
        table2 = Table.objects.create(number_of_seats=2)
        booking_time1 = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        booking_time2 = datetime(2022, 5, 21, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table1, party_size=2,
            booking_time=booking_time1, time_of_booking=time_of_booking)
        Booking.objects.create(
            customer=customer, table=table2, party_size=2,
            booking_time=booking_time2, time_of_booking=time_of_booking)
        found = found_table(
            self, 2, 2, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertTrue(found)

    def test_found_table4(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table = Table.objects.create(number_of_seats=4)
        booking_time = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table, party_size=2,
            booking_time=booking_time, time_of_booking=time_of_booking)
        found = found_table(
            self, 4, 2, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertTrue(found)

    def test_found_table5(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table = Table.objects.create(number_of_seats=4)
        booking_time = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table, party_size=3,
            booking_time=booking_time, time_of_booking=time_of_booking)
        found = found_table(
            self, 4, 2, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertFalse(found)

    def test_found_any_table1(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table1 = Table.objects.create(number_of_seats=2)
        table2 = Table.objects.create(number_of_seats=4)
        booking_time1 = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        booking_time2 = datetime(2022, 5, 21, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table1, party_size=2,
            booking_time=booking_time1, time_of_booking=time_of_booking)
        Booking.objects.create(
            customer=customer, table=table2, party_size=2,
            booking_time=booking_time2, time_of_booking=time_of_booking)
        found = found_any_table(
            self, 2, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertTrue(found)

    def test_found_any_table2(self):
        customer = Customer.objects.create(first_name="Tom", last_name="Jerry")
        table1 = Table.objects.create(number_of_seats=2)
        table2 = Table.objects.create(number_of_seats=4)
        booking_time1 = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        booking_time2 = datetime(2022, 5, 20, 12, 00, tzinfo=pytz.UTC)
        time_of_booking = datetime.now()
        Booking.objects.create(
            customer=customer, table=table1, party_size=2,
            booking_time=booking_time1, time_of_booking=time_of_booking)
        Booking.objects.create(
            customer=customer, table=table2, party_size=2,
            booking_time=booking_time2, time_of_booking=time_of_booking)
        found = found_any_table(
            self, 3, datetime(2022, 5, 20, 13, 00, tzinfo=pytz.UTC))[0]
        self.assertFalse(found)
