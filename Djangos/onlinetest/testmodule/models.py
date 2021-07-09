from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import uuid
import datetime


# Create your models here.


IDENTIFICATION = (("STU", "Student"),
                  ("STA", "Staff"),
                  ("TEA", "Teacher"))

ANSWERSELECT = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

TEST_STATE = (
    ("OPEN", "OPEN"),
    ("CLOSE", "CLOSE")
)

DONE_STATE = {
    ('FINISHED', 'FINISHED'),
    ('UNFINISHED', 'UNFINISHED')
}


# ! subjects and Courses Models

class Subject(models.Model):
    SubjectUUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    SubjectID = models.CharField(
        verbose_name='Subject ID', max_length=20, default="XXXXX")
    SubjectName = models.CharField(
        verbose_name="Subject Name", max_length=100,  default="XXXXX")
    SubjectDescription = models.TextField(
        verbose_name="Subject Description",  default="XXXXX")

    def __str__(self):
        return self.SubjectName

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = verbose_name


class Course(models.Model):
    CourseUUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    CourseID = models.CharField(
        verbose_name='Course ID', max_length=20,  default="")
    CourseSubject = models.ForeignKey(
        Subject, verbose_name='Course Subject', null=True, on_delete=models.SET_NULL, blank=True)
    CourseeName = models.CharField(
        verbose_name="Course Name", max_length=100,  default="")
    CourseTimeStart = models.DateTimeField(verbose_name="Start Date")
    CourseTimeEnd = models.DateTimeField(verbose_name="End Date")
    CourseDescription = models.TextField(verbose_name="Course Description")

    def __str__(self):
        return self.CousrseName

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = verbose_name

# * ----------------------------------


# ! Teacher and Student Models

class Profile(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    TeacherBaseInfo = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Teacher Name')
    identification = models.CharField(
        verbose_name='Identification', max_length=20, choices=IDENTIFICATION, default="Teacher",)
    idcode = models.CharField(
        verbose_name='ID Code', max_length=20, default="")

    def __str__(self):
        return self.TeacherBaseInfo.username

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = verbose_name


class Student(models.Model):
    StudentBaseInfo = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,   null=True, blank=True, verbose_name='Student Name')
    identification = models.CharField(
        verbose_name='Identification', max_length=20, choices=IDENTIFICATION,  default="Student",)
    idcode = models.CharField(
        verbose_name='ID Code', max_length=20, default="")

    def __str__(self):
        return self.StudentBaseInfo.username

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = verbose_name


class CourseTaken(models.Model):
    Student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Student Name')
    Crouse = models.ForeignKey(
        Course,  on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Course Name")

    TestTimeStart = models.DateTimeField(
        verbose_name="Start Time", default=None, null=True, blank=True)
    TestTimeEnd = models.DateTimeField(
        verbose_name="End Time", default=None, null=True, blank=True)

    def __str__(self):
        return self.Student.StudentBaseInfo.username

    class Meta:
        verbose_name = "Course Taken"
        verbose_name_plural = verbose_name

# * ----------------------------------


# ! Test Informations

class ChoiceQuestions(models.Model):
    QuestionID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20,  default="")
    ChoiceAnswer = models.CharField(
        verbose_name="Correct Answer", max_length=4,  default="")
    QuestionMark = models.IntegerField(verbose_name="Question Mark")

    def __str__(self):
        return self.QuestionContent

    class Meta:
        verbose_name = "Choice Question Content"
        verbose_name_plural = verbose_name


class Choices(models.Model):
    ChoiceQues = models.ForeignKey(
        ChoiceQuestions, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name='Choice Question')

    ChoiceAnswerA = models.CharField(default="aaa",
                                     max_length=200, verbose_name="A")

    ChoiceAnswerB = models.CharField(default="bbb",
                                     max_length=200, verbose_name="B")

    ChoiceAnswerC = models.CharField(default="ccc",
                                     max_length=200, verbose_name="C")

    ChoiceAnswerD = models.CharField(default="ddd",
                                     max_length=200, verbose_name="D")
    ChoiceCorrect = models.CharField(
        verbose_name="Single Choice True Answer", max_length=20, choices=ANSWERSELECT, default="")
    ChoiceExplanation = models.TextField(
        default="Explanation is ...;", verbose_name="Choice Explanation")
    # ChoiceIndex = models.CharField(
    #     verbose_name='Choice Index', max_length=4, default=None, null=True, blank=True)
    # ChoiceContent = models.CharField(
    #     verbose_name='Choice Content', max_length=100, default=None, null=True, blank=True)

    def __str__(self):
        return self.ChoiceQues.QuestionContent

    class Meta:
        verbose_name = "Choices Content"
        verbose_name_plural = verbose_name


class FillQuestions(models.Model):
    QuestionID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20,  default="")
    QuestionAnswer = models.CharField(
        verbose_name='Question Answer', max_length=20,  default="")
    QuestionMark = models.IntegerField(verbose_name="Mark")

    FillExplanation = models.TextField(
        default="Explanation is ...", verbose_name="Fill Explanation")

    def __str__(self):
        return self.ChoiceQues.QuestionContent

    class Meta:
        verbose_name = "Fill Question Content"
        verbose_name_plural = verbose_name


class TextQuestions(models.Model):
    QuestionID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    QuestionContent = models.CharField(
        verbose_name='Question Content', max_length=20,  default="")
    QuestionAnswer = models.CharField(
        verbose_name='Question Answer', max_length=20,  default="")
    QuestionMark = models.IntegerField(verbose_name="Mark")
    QuestionExplanation = models.TextField(
        default="Explanation is ...", verbose_name="Text Explanation")

    def __str__(self):
        return self.ChoiceQues.QuestionContent

    class Meta:
        verbose_name = "Text Question Content"
        verbose_name_plural = verbose_name


class TestInfo(models.Model):
    TestID = models.CharField(
        verbose_name='Test ID', max_length=20,  default="")
    TestCourse = models.ForeignKey(
        Course, verbose_name="Test Course", on_delete=models.SET_NULL,   null=True, blank=True)

    TestSubject = models.ForeignKey(
        Subject, verbose_name="Subject Course", on_delete=models.SET_NULL, null=True, blank=True)
    TestName = models.TextField(
        verbose_name="Test Name", default=None, null=True, blank=True)
    TestTimeStart = models.DateTimeField(
        verbose_name="Start Time", default=None, null=True, blank=True)
    TestTimeEnd = models.DateTimeField(
        verbose_name="End Time", default=None, null=True, blank=True)

    def __str__(self):
        return self.TestID

    class Meta:
        verbose_name = "TestInfo"
        verbose_name_plural = verbose_name


class TestContent(models.Model):
    TestID = models.ForeignKey(TestInfo, verbose_name="Test ID",
                               on_delete=models.SET_NULL, null=True, blank=True)
    TestChoiceQues = models.ManyToManyField(
        ChoiceQuestions, verbose_name="Choice Question")
    TestFillQues = models.ManyToManyField(
        FillQuestions, verbose_name="Fill Question")
    TestTextQues = models.ManyToManyField(
        TextQuestions, verbose_name="Text Question")

    def __str__(self):
        return self.TestID.TestID

    class Meta:
        verbose_name = "Test Information"
        verbose_name_plural = verbose_name
# * ----------------------------------


# ! Grades Models

class ChoiceQues_StudentAnswer(models.Model):
    TestID = models.ForeignKey(TestInfo, verbose_name="Test ID",
                               on_delete=models.SET_NULL, null=True, blank=True)
    ChoiceQues = models.ForeignKey(
        ChoiceQuestions, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Choice Question')
    ChoiceAns = models.CharField(
        max_length=20, choices=ANSWERSELECT, default="A", verbose_name="Choice Ans")

    def __str__(self):
        return self.TestID.TestID

    class Meta:
        verbose_name = "Student Choice Questions Answers"
        verbose_name_plural = verbose_name


class FillQues_StudentAnswer(models.Model):
    TestID = models.ForeignKey(TestInfo, verbose_name="Test ID",
                               on_delete=models.SET_NULL, null=True, blank=True)
    FilleQues = models.ForeignKey(FillQuestions, on_delete=models.SET_NULL,
                                  null=True, blank=True, verbose_name='Fill Question')
    FillAns = models.TextField(verbose_name='Fill Question')

    def __str__(self):
        return self.TestID.TestID

    class Meta:
        verbose_name = "Student Fill Questions Answers"
        verbose_name_plural = verbose_name


class TextQues_StudentAnswer(models.Model):
    TestID = models.ForeignKey(TestInfo, verbose_name="Test ID",
                               on_delete=models.SET_NULL, null=True, blank=True)
    TextQues = models.ForeignKey(TextQuestions, on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name=' Text Question')
    TextAns = models.TextField(verbose_name=' Text Question')

    def __str__(self):
        return self.TestID.TestID

    class Meta:
        verbose_name = "Student Text Questions Answers"
        verbose_name_plural = verbose_name


class StudentAnswers(models.Model):
    StudentID = models.ForeignKey(Student, verbose_name="Student",
                                  on_delete=models.SET_NULL,  null=True, blank=True)
    Test = models.ForeignKey(TestInfo, verbose_name="Test",
                             on_delete=models.SET_NULL,  null=True, blank=True)
    ChoiceQues = models.ManyToManyField(
        ChoiceQues_StudentAnswer, verbose_name="Choice Question")
    FillQues = models.ManyToManyField(
        FillQues_StudentAnswer, verbose_name="Fill Question")
    TextQues = models.ManyToManyField(
        TextQues_StudentAnswer, verbose_name="Text Question")

    def __str__(self):
        return self.StudentID.StudentBaseInfo.username

    class Meta:
        verbose_name = "Student Answers"
        verbose_name_plural = verbose_name


class Grades(models.Model):
    StudentID = models.ForeignKey(Student, verbose_name="Student",
                                  on_delete=models.SET_NULL,  null=True, blank=True)
    TestID = models.ForeignKey(TestInfo,
                               verbose_name='Test ID', null=True, blank=True, on_delete=models.SET_NULL)

    Grade = models.FloatField(verbose_name="Grade")

    DoneState = models.CharField(
        max_length=20, choices=DONE_STATE, default="UNFINISHED", verbose_name="Done State")
    GradeDate = models.DateTimeField(
        null=True, blank=True, default=timezone.now)
    Course = models.ForeignKey(
        Course, null=True, on_delete=models.SET_NULL,  verbose_name="Course")

    Subject = models.ForeignKey(
        Subject, null=True, on_delete=models.SET_NULL,  verbose_name="Subject")

    def __str__(self):
        return self.StudentID.StudentBaseInfo.username+" "+self.TestID.TestID+str(float)

    class Meta:
        verbose_name = "Student Grades"
        verbose_name_plural = verbose_name
