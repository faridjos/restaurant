from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainImage.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    ]