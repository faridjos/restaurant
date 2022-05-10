from django.shortcuts import render
from django.views import View

# Create your views here.


class MainImage(View):
    def get(self, request):
        return render(
            request,
            'index.html',
        )


class Contact(View):
    def get(self, request):
        return render(
            request,
            'contact.html',
        )