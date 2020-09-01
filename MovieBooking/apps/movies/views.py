from django.shortcuts import render, get_object_or_404
from .models import Listing, BookingTickets
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

def index(request):
    listing = Listing.objects.all()
    print(listing)
    paginator = Paginator(listing, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    listings = {"listings": page_obj}
    return render(request, 'movies/listings.html', context=listings)
def search(request):
    return render(request, 'movies/search.html')
def listings(request):
    return render(request, 'movies/singlemovie.html', )
def booking(request, listing_id):
  booking = get_object_or_404(Listing, pk=listing_id)

  context = {
    'booking': booking
  }
  return render(request, 'movies/aboutmovies.html', context)

class BookingCreate(CreateView):
    model = BookingTickets
    fields = '__all__'
    success_url = '/list/'

class BookingUpdate(UpdateView):
    model = BookingTickets
    fields = '__all__'
    success_url = '/list/'


class BookingDelete(DeleteView):
    model = BookingTickets
    fields = '__all__'
    success_url = '/list/'


class BookingList(ListView):
        model = BookingTickets
        fields = '__all__'




