from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainImage.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('form/', views.Form.as_view(), name='form'),
    path('booking/<booking_id>', views.ShowBooking.as_view(), name='booking'),
    path('booking_btn', views.BookingButton.as_view(), name='booking_btn'),
    ]
