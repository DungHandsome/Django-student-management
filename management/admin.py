from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
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
    list_display = ['assignment_title']
    list_filter = ['assignment_title']
    search_fields = ['assignment_title']
class StudentAd(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']
class AnnouncementAd(admin.ModelAdmin):
    list_display = ['tittle']
    list_filter = ['tittle']
    search_fields = ['tittle']
class accAd(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Grade, CourseAd)
admin.site.register(Class, ClassAd)
admin.site.register(Assignment, AssignmentAd)
admin.site.register(mystudent, UserAdmin)
admin.site.register(Announcement, AnnouncementAd)
admin.site.register(TeacherAnnouncement, AnnouncementAd)
admin.site.register(accFilter, accAd)