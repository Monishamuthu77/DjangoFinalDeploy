from django.db import models

# Create your models here.
class Screen(models.Model):
    theatre_name = models.CharField(max_length=250)
    screen_name = models.CharField(max_length=100)
    golden_seats = models.IntegerField()
    silver_seats = models.IntegerField()
    is_mvp = models.BooleanField(default=False)
    screen_photo = models.ImageField(upload_to="photos/%Y/%m/%d")

    def __str__(self):
        return self.screen_name


