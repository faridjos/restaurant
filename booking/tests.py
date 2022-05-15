from django.test import TestCase
from datetime import datetime, timedelta
from .routines import validate_form, round_datetime
# Create your tests here.


class TestRoutines(TestCase):

    def test_validate_booking_time1(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        self.assertTrue(validate_form(self, date_time, 2))

    def test_validate_booking_time2(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(hours=2)
        self.assertFalse(validate_form(self, date_time, 2))

    def test_validate_booking_time3(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(days=5, hours=2)
        self.assertTrue(validate_form(self, date_time, 2))

    def test_validate_booking_time4(self):
        date_time = datetime(2022, 5, 15, 22, 50)
        date_time += timedelta(days=6, hours=2)
        self.assertTrue(validate_form(self, date_time, 2))

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