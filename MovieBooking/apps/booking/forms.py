from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['show_time', 'booking_date']
        widgets = {
            'completeDateTime': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }