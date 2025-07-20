from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.title

class Images(models.Model):
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    carousel = models.ForeignKey('Carousel',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.carousel) if self.carousel else "No Carousel"


class Brane(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.surname} {self.name}"