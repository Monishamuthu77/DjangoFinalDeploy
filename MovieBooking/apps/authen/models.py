from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=(('1', 'Male'), ('2', 'Female'), ('3', 'Other')))
    dob = models.DateField()
    phone = models.CharField(unique=True, max_length=10)
    image = models.ImageField(upload_to='images', default='plants-grow.jpg')

    def get_absolute_url(self):
        return reverse('home', kwargs={'profile_id':self.id})



