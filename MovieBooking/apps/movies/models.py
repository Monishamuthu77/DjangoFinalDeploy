from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from apps.theatres.models import Screen
# Create your models here.
class Listing(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.DO_NOTHING)
    branch = models.CharField(max_length=100)
    desc = models.TextField(max_length=10000, default='A very good movie')
    movie_name = models.CharField(max_length=150)
    golden_price = models.DecimalField(max_digits=6, decimal_places=2)
    silver_price = models.DecimalField(max_digits=6, decimal_places=2)
    released_date = models.DateField(default=datetime.now)
    video = EmbedVideoField()
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    is_published = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.movie_name


class BookingTickets(models.Model):
    morning = '10AM-1PM'
    afternoon = '2PM-5PM'
    evening = '7PM-10PM'
    night = '11PM-3AM'
    showtime_choices = [
        (morning, "Morning"),
        (afternoon, "Afternoon"),
        (evening, "Evening"),
        (night, "Night")
    ]
    username = models.CharField(max_length=250)
    phone = models.CharField(max_length=10, unique=True)
    gold_seats = models.IntegerField()
    silver_seats = models.IntegerField()
    show_time = models.CharField(max_length=30, choices=showtime_choices)
    booking_date = models.DateField()

    def __str__(self):
        return self.phone


