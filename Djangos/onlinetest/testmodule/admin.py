from django.contrib import admin


from .models import *
from django.contrib.auth.admin import UserAdmin
 
# Register your models here.



class Profile_Admin(UserAdmin):
    # list_display = ("identification", )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identification')}
        ),
    )# list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')


admin.site.register(Profile, Profile_Admin)
 
