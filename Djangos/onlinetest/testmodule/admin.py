from django.contrib import admin


from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class Profile_Admin(UserAdmin):
    list_display = ("username", )
    # add_fieldsets = (
    #     (None, {
    #         'fields': ('identification'), }
    #      ),

    # )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('idcode','identification',)}),

    )


class Subject_Admin(models.Model):
    pass


class Course_Admin(models.Model):
    pass

class Teacher_Admin(models.Model):
    pass

class CourseTaken_Admin(models.Model):
    pass

class ChoiceQuestions_Admin(models.Model):
    pass

class Choices_Admin(models.Model):
    pass
class FillQuestions_Admin(models.Model):
    pass

class TextQuestions_Admin(models.Model):
    pass

class TestInfo_Admin(models.Model):
    pass

class StudentAnswer_Admin(models.Model):
    pass

class StudentAnswer_Admin(models.Model):
    pass

class StudentAnswer_Admin(models.Model):
    pass

class StudentAnswer_Admin(models.Model):
    pass
# list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')


# admin.site.register(Profile, Profile_Admin)
