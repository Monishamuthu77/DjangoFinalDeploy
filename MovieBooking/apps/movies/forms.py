from django import forms
from .models import BookingTickets

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(widgets = forms.DateTimeInput(attrs={'class': 'datetime-input'}))
    class Meta:
        model = BookingTickets
        fields = '__all__'
