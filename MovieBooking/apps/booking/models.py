from django.db import models

# Create your models here.
class Booking(models.Model):
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

