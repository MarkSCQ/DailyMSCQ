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
        (None, {'fields': ('idcode', 'identification',)}),

    )


class Subject_Admin(models.Model):
    list_display = ("SubjectName", "SubjectID", "SubjectDescriptio",)
    ordering = ("SubjectName",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Subject.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Course_Admin(models.Model):
    list_display = ("CourseID", "CousrseName", "CourseSubject",
                    "CourseTimeStart", "CourseTimeEnd",)
    ordering = ("CourseID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Course.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Teacher_Admin(models.Model):
    list_display = ("idcode", "TeacherBaseInfo", "identification",)
    ordering = ("idcode",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Teacher.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Student_Admin(models.Model):
    list_display = ("idcode", "StudentBaseInfo", "identification",)
    ordering = ("idcode",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Student.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class CourseTaken_Admin(models.Model):
    list_display = ("Student", "Crouse", "TestTimeStart", "TestTimeEnd",)
    ordering = ("Student",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=CourseTaken.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class ChoiceQuestions_Admin(models.Model):
    list_display = ("QuestionContent", "ChoiceAnswer", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=ChoiceQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Choices_Admin(models.Model):
    list_display = ("ChoiceQues", "ChoiceCorrect",)
    ordering = ("ChoiceQues",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Choices.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class FillQuestions_Admin(models.Model):
    list_display = ("QuestionContent", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=FillQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TextQuestions_Admin(models.Model):
    list_display = ("QuestionContent", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TextQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TestInfo_Admin(models.Model):
    list_display = ("TestID", "TestCourse", "TestSubject",
                    "TestTimeStart", "TestTimeEnd",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TestInfo.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TestContent_Admin(models.Model):
    list_display = ("TestID",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TestContent.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class ChoiceQues_StudentAnswer_Admin(models.Model):
    list_display = ("TestID", "ChoiceQues", "ChoiceAns",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=ChoiceQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class FillQues_StudentAnswer_Admin(models.Model):
    list_display = ("TestID", "FilleQues",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=FillQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TextQues_StudentAnswer_Admin(models.Model):
    list_display = ("TestID", "TextQues",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TextQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class StudentAnswers_Admin(models.Model):
    list_display = ("StudentID", "Test",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=StudentAnswers.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Grades_Admin(models.Model):
    list_display = ("TestID", "TextQues",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Grades.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"
# list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')




admin.site.register(Profile, Profile_Admin)

# admin.site.register(Subject, Subject_Admin)
# admin.site.register(Course, Course_Admin)
# admin.site.register(Teacher, Teacher_Admin)
# admin.site.register(Student, Student_Admin)
# admin.site.register(Profile, CourseTaken_Admin)
# admin.site.register(Profile, ChoiceQuestions_Admin)
# admin.site.register(Profile, FillQuestions_Admin)
# admin.site.register(Profile, TextQuestions_Admin)
# admin.site.register(Profile, TestContent_Admin)
# admin.site.register(Profile, ChoiceQues_StudentAnswer_Admin)
# admin.site.register(Profile, FillQues_StudentAnswer_Admin)
# admin.site.register(Profile, TextQues_StudentAnswer_Admin)
# admin.site.register(Profile, StudentAnswers_Admin)
# admin.site.register(Profile, Grades_Admin)
