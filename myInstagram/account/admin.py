from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'get_full_name', 'is_staff', 'gender', 'image_tag', 'phone')
    fieldsets = (
            ('None', {'fields' : ('username', 'password', 'email')}),
            ('Personal Info', {'fields' : ('first_name', 'last_name', 'gender', 'dob','phone', 'profile_pic')}),
            ('Address', {'fields': (('street_address', 'city', 'pincode'),)}),
            ('Permission', {'fields': (('is_staff', 'is_superuser', 'is_active'),'groups', 'user_permissions')}),
            ('Important Dates', {'fields': ('last_login', 'date_joined')})
            )
    add_fieldsets = (
            ('None', {
                'classes' : ('wide',),
                'fields': ('username', 'email', 'first_name', 'last_name', 'gender', 'dob', 'phone', 'passwd1', 'passwd2')
                }),)
    add_form = UserCreationForm
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone')




admin.site.register(MyUser, MyUserAdmin)
