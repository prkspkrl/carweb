from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField(blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    customer_need = models.CharField(max_length=200)
    car_title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email

