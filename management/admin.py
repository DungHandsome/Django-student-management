from django.contrib import admin
from .models import *
# Register your models here.
class CourseAd(admin.ModelAdmin):
    list_display = ['course_name']
    list_filter = ['course_name']
    search_fields = ['course_name']
class ClassAd(admin.ModelAdmin):
    list_display = ['class_name']
    list_filter = ['class_name']
    search_fields = ['class_name']
class AssignmentAd(admin.ModelAdmin):
    list_display = ['assignment_name']
    list_filter = ['assignment_name']
    search_fields = ['assignment_name']
class StudentAd(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']


admin.site.register(Grade, CourseAd)
admin.site.register(Class, ClassAd)
admin.site.register(Assignment, AssignmentAd)
admin.site.register(mystudent, StudentAd)