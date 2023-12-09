from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Grade(models.Model):
    course_name = models.CharField(max_length=1000)
    def __str__(self):
        return (self.course_name)

class Class(models.Model):
    course = models.ForeignKey(Grade, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=1000)
    def __str__(self):
        return (self.class_name)

class Assignment(models.Model):
    assignment_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    assignment_name = models.CharField(max_length=1000)
    file = models.FileField(upload_to ='uploads/')
    def __str__(self):
        return (self.assignment_name)

class mystudent(AbstractUser):
    student_class = models.ManyToManyField(Class, null=True)
    fullname = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    sex_choices = ((0, 'Nam'), (1, 'Nữ'), (2, 'Không xác định'))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choices, default=0)
    country = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    avatar = models.ImageField(null=True)


