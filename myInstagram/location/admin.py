from django.contrib import admin
from .models import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_state_name', 'get_country_name')
admin.site.register(City, CityAdmin)
admin.site.register(State)
admin.site.register(Country)

