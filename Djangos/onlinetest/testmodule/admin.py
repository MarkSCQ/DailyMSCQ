from django.contrib import admin


from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class Profile_Admin(UserAdmin):
    list_display = ("username", )
    ordering = ("username",)

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Subject.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"



class Subject_Admin(admin.ModelAdmin):
    list_display = ("SubjectName", "SubjectID",)
    ordering = ("SubjectName",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Subject.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Course_Admin(admin.ModelAdmin):
    list_display = ("CourseID", "CourseeName", "CourseSubject",
                    "CourseTimeStart", "CourseTimeEnd",)
    ordering = ("CourseID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Course.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Teacher_Admin(admin.ModelAdmin):
    list_display = ("idcode", "TeacherBaseInfo", "identification",)
    ordering = ("idcode",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Teacher.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Student_Admin(admin.ModelAdmin):
    list_display = ("idcode", "StudentBaseInfo", "identification",)
    ordering = ("idcode",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Student.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class CourseTaken_Admin(admin.ModelAdmin):
    list_display = ("Student", "Crouse", "TestTimeStart", "TestTimeEnd",)
    ordering = ("Student",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=CourseTaken.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class ChoiceQuestions_Admin(admin.ModelAdmin):
    list_display = ("QuestionContent", "ChoiceAnswer", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=ChoiceQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Choices_Admin(admin.ModelAdmin):
    list_display = ("ChoiceQues", "ChoiceCorrect",)
    ordering = ("ChoiceQues",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Choices.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class FillQuestions_Admin(admin.ModelAdmin):
    list_display = ("QuestionContent", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=FillQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TextQuestions_Admin(admin.ModelAdmin):
    list_display = ("QuestionContent", "QuestionMark",)
    ordering = ("QuestionContent",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TextQuestions.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TestInfo_Admin(admin.ModelAdmin):
    list_display = ("TestID", "TestCourse", "TestSubject",
                    "TestTimeStart", "TestTimeEnd",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TestInfo.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TestContent_Admin(admin.ModelAdmin):
    list_display = ("TestID",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TestContent.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class ChoiceQues_StudentAnswer_Admin(admin.ModelAdmin):
    list_display = ("TestID", "ChoiceQues", "ChoiceAns",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=ChoiceQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class FillQues_StudentAnswer_Admin(admin.ModelAdmin):
    list_display = ("TestID", "FilleQues",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=FillQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class TextQues_StudentAnswer_Admin(admin.ModelAdmin):
    list_display = ("TestID", "TextQues",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=TextQues_StudentAnswer.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class StudentAnswers_Admin(admin.ModelAdmin):
    list_display = ("StudentID", "Test",)
    ordering = ("StudentID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=StudentAnswers.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"


class Grades_Admin(admin.ModelAdmin):
    list_display = ("TestID", "StudentID",)
    ordering = ("TestID",)
    actions = ['cancel_orders', ]

    def cancel_orders(self, request, queryset):
        queryset.update(order_status=Grades.CANCELLED)
    cancel_orders.short_description = "Mark selected orders as cancelled"
# list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')


admin.site.register(Profile, Profile_Admin)

admin.site.register(Subject, Subject_Admin)
admin.site.register(Course, Course_Admin)
admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Student, Student_Admin)
admin.site.register(CourseTaken, CourseTaken_Admin)
admin.site.register(ChoiceQuestions, ChoiceQuestions_Admin)
admin.site.register(FillQuestions, FillQuestions_Admin)
admin.site.register(TextQuestions, TextQuestions_Admin)
admin.site.register(TestContent, TestContent_Admin)
admin.site.register(ChoiceQues_StudentAnswer, ChoiceQues_StudentAnswer_Admin)
admin.site.register(FillQues_StudentAnswer, FillQues_StudentAnswer_Admin)
admin.site.register(TextQues_StudentAnswer, TextQues_StudentAnswer_Admin)
admin.site.register(StudentAnswers, StudentAnswers_Admin)
admin.site.register(Grades, Grades_Admin)
