from django.contrib import admin
from .models import *

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
            ('None', {'fields': ('image', 'description', 'user_tags', 'hash_tags')}),
    )
    raw_id_fields = ('user_tags', 'hash_tags')
    autocomplete_lookup_fields = {
        'm2m' : ['user_tags', 'hash_tags']
    }
    def save_model(self, request, obj, form, change):
        obj.by = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(PhotoAdmin, self).get_queryset(request)

       # if request.user.is_superuser:
        #    return qs
        return qs.filter(by=request.user)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(HashTag)
admin.site.register(Comment)

