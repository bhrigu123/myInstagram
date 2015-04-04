from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from location.models import City

# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    dob = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(unique = True, null=True, blank=True)
    street_address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    pincode = models.CharField(max_length=8, default="0000000")
    following = models.ManyToManyField("self", symmetrical = False, related_name = "followers")

    def image_tag(self):
        if self.profile_pic:
            return '<img height="40px" width="40px" src="/media/%s">' % self.profile_pic
        else:
            return ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = 'True'
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "username__icontains", "first_name__icontains", "last_name__icontains")

