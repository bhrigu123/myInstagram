from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from location.models import City

# Create your models here.
class MyUser(AbstractUser):
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    dob = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(unique = True, null=True, blank=True)
    street_address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    pincode = models.CharField(max_length=8, default="0000000")
    following = models.ManyToManyField("self", symmetrical = False, related_name = "followers")



