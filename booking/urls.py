from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainImage.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('form/', views.Form.as_view(), name='form'),
    path('booking/<booking_id>', views.Show_booking.as_view(), name='booking'),
    ]