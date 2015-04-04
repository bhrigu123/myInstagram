from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    code = models.CharField(max_length = 5, unique = True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

class State(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length = 5)
    def __str__(self):
        return self.country.name + " > " + self.name

    class Meta:
        db_table = 'state'

class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.state.country.name + " > " +  self.state.name + " > " + self.name
    
    class Meta:
        db_table = 'city'
