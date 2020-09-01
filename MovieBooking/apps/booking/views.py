from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Booking

# Create your views here.

def index(request):
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def list(request):
    return render(request, 'movies/listings.html')

        

