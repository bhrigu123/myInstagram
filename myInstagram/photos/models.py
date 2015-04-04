from django.db import models
from account.models import MyUser

# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length = 100)
    count = models.IntegerField(default = 0)
    def __str__(self):
        return '#' + self.name

class Photo(models.Model):
    image = models.ImageField(upload_to = 'uploads/')
    by = models.ForeignKey(MyUser, related_name = 'photos_uploaded')
    on = models.DateTimeField(auto_now_add = True)
    description = models.TextField(max_length = 1000, null = True)
    likers = models.ManyToManyField(MyUser, related_name = 'photos_liked', null = True)
    user_tags = models.ManyToManyField(MyUser, related_name = 'photos_tagged_in', null = True)
    hash_tags = models.ManyToManyField(HashTag, null = True)

class Comment(models.Model):
    by = models.ForeignKey(MyUser)
    photo = models.ForeignKey(Photo)
    on = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length = 100)

    def __str__(self):
        return self.text



