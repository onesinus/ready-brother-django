from django.db import models
from django.urls import reverse


# Create your models here.
class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse('contactme-list')