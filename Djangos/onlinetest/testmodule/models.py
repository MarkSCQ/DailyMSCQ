from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import uuid
import datetime


# Create your models here.


IDENTIFICATION = (("STU", "Student"),
                  ("STA", "Staff"),
                  ("TEA", "Teacher"))


# ! subjects and Courses Models

class Subject(models.Model):
    SubjectID = models.CharField(
        verbose_name='Subject ID', max_length=20, default=None, null=True, blank=True)
    SubjectName = models.CharField(
        verbose_name="Subject Name", max_length=100, default=None, null=True, blank=True)
    SubjectDescription = models.TextField(verbose_name="Subject Description")


class Course(models.Model):
    CourseID = models.CharField(
        verbose_name='Course ID', max_length=20, default=None, null=True, blank=True)
    CourseSubject = models.ForeignKey(
        Subject, verbose_name='Course Subject', null=True, on_delete=models.SET_NULL, blank=True)
    CousrseName = models.CharField(
        verbose_name="Course Name", max_length=100, default=None, null=True, blank=True)
    CourseTimeStart = models.DateTimeField(verbose_name="Start Date")
    CourseTimeEnd = models.DateTimeField(verbose_name="End Date")
    CourseDescription = models.TextField(verbose_name="Course Description")

# * ----------------------------------


# ! Teacher and Student Models

class Profile(AbstractUser):
    pass


class Teacher(models.Model):
    TeacherBaseInfo = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Name')
    identification = models.CharField(
        verbose_name='Identification', max_length=20, choices=IDENTIFICATION, default=None, null=True, blank=True)
    idcode = models.CharField(
        verbose_name='ID Code', max_length=20, default=None, null=True, blank=True)


class Student(models.Model):
    StudentBaseInfo = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,   null=True, blank=True, verbose_name='Name')
    identification = models.CharField(
        verbose_name='Identification', max_length=20, choices=IDENTIFICATION, default=None, null=True, blank=True)
    idcode = models.CharField(
        verbose_name='ID Code', max_length=20, default=None, null=True, blank=True)


class CourseTaken(models.Model):
    Student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Name')
    Crouse = models.ManyToManyField(Course)
# * ----------------------------------


# ! Test Informations


class ChoiceQuestions(models.Model):
    QuestionID = models.UUIDField()
    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20, default=None, null=True, blank=True)

    ChoiceAnswer = models.CharField(
        verbose_name="Correct Answer", max_length=4, default=None, null=True, blank=True)
    QuestionMark = models.IntegerField(verbose_name="Mark")


class Choices(models.Model):
    
    ChoiceQues = models.ForeignKey(
        ChoiceQuestions, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name='Choice Question')
    ChoiceIndex = models.CharField(
        verbose_name='Choice Index', max_length=4, default=None, null=True, blank=True)
    ChoiceContent = models.CharField(
        verbose_name='Choice Content', max_length=100, default=None, null=True, blank=True)
    

class FillQuestions(models.Model):
    QuestionID = models.UUIDField()

    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20, default=None, null=True, blank=True)
    QuestionAnswer = models.CharField(
        verbose_name='Question Answer', max_length=20, default=None, null=True, blank=True)
    QuestionMark = models.IntegerField(verbose_name="Mark")


class TextQuestions(models.Model):
    QuestionID = models.UUIDField()

    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20, default=None, null=True, blank=True)
    QuestionAnswer = models.CharField(
        verbose_name='Question Answer', max_length=20, default=None, null=True, blank=True)
    QuestionMark = models.IntegerField(verbose_name="Mark")


class TestInfo(models.Model):
    TestID = models.CharField(
        verbose_name='Test ID', max_length=20, default=None, null=True, blank=True)
    TestCourse = models.ForeignKey(Course, verbose_name="Test Course",
                                   on_delete=models.CASCADE,   null=True, blank=True)

    TestSubject = models.ForeignKey(Subject, verbose_name="Subject Course",
                                    on_delete=models.CASCADE, null=True, blank=True)
    TestDescription = models.TextField(verbose_name="Test Description")
    TestTimeStart = models.DateTimeField(verbose_name="Start Time")
    TestTimeEnd = models.DateTimeField(verbose_name="End Time")


class TestContent(models.Model):
    TestID = models.ForeignKey(TestInfo, verbose_name="Test ID",
                               on_delete=models.CASCADE, null=True, blank=True)
    TestChoiceQues = models.ManyToManyField(ChoiceQuestions)
    TestFillQues = models.ManyToManyField(FillQuestions)
    TestTextQues = models.ManyToManyField(TextQuestions)
    pass
# * ----------------------------------


# ! Grades Models

class ChoiceQues_StudentAnswer(models.Model):
    ChoiceQues = models.ForeignKey(ChoiceQuestions)
    Choice = models.CharField()
    
class FillQues_StudentAnswer(models.Model):
    ChoiceQues = models.ForeignKey(FillQuestions)
    Choice = models.CharField()

class TextQues_StudentAnswer(models.Model):
    ChoiceQues = models.ForeignKey(TextQuestions)
    Choice = models.CharField()



class Grades(models.Model):
    StudentID = models.ForeignKey(Student, verbose_name="Student",
                                  on_delete=models.SET_NULL,  null=True, blank=True)
    TestID = models.CharField(
        verbose_name='Test ID', max_length=20, default=None, null=True, blank=True)

    Grade = models.FloatField(verbose_name="Grade")

# * ----------------------------------
