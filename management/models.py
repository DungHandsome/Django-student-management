from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Grade(models.Model):
    course_name = models.CharField(max_length=1000)
    def __str__(self):
        return (self.course_name)

class Class(models.Model):
    course = models.ForeignKey(Grade, on_delete=models.CASCADE)
    class_note = models.TextField(null=True)
    class_name = models.CharField(max_length=1000)
    def __str__(self):
        return (self.class_name)

class Assignment(models.Model):
    assignment_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(null=True, default=True)
    due_date = models.DateTimeField(null=True)
    assignment_title = models.CharField(max_length=1000, null=True)
    assignment_file = models.FileField(upload_to='assignment', null=True)
    def __str__(self):
        return (self.assignment_title)

class accFilter(models.Model):
    name = models.CharField(max_length=1000)
    Student = models.BooleanField(default=False, null=True)
    def __str__(self):
        return (self.name)

class mystudent(AbstractUser):
    student = models.ForeignKey(accFilter, on_delete=models.SET_NULL, null=True)
    student_class = models.ManyToManyField(Class, null=True)
    fullname = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, null=True)
    sex_choices = ((0, 'Nam'), (1, 'Nữ'), (2, 'Không xác định'))
    age = models.IntegerField(default=0)
    birthdate = models.DateField(null=True)
    sex = models.IntegerField(choices=sex_choices, default=0)
    country = models.CharField(max_length=200)
    avatar = models.ImageField(null=True)
    bio = models.TextField(null=True)

class Announcement(models.Model):
    
    tittle = models.CharField(max_length=1000)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.tittle)
    
class TeacherAnnouncement(models.Model):
    
    tittle = models.CharField(max_length=1000)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.tittle)
