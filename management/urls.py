from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('class/<int:id>/', views.classpage, name='classpage'),
    path('student/<int:id>/', views.student_details, name='studentpage'),
]