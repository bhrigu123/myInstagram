from django.contrib import admin
from .models import *

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    raw_id_fields = ('likers', 'user_tags', 'hash_tags', 'by')
    autocomplete_lookup_fields = {
        'fk' : ['by'],
        'm2m' : ['likers', 'user_tags']
    }

admin.site.register(Photo, PhotoAdmin)
admin.site.register(HashTag)
admin.site.register(Comment)

