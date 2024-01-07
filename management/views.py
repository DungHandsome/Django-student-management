from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
@login_required
def home(request):
	student_announce = Announcement.objects.all().order_by('-date')
	teacher_announce = TeacherAnnouncement.objects.all().order_by('-date')
	
	user = request.user
	if user.student.name == "Student":
		return render(request, 'homepage/student_home.html', {'announcement': student_announce})
	else:
		return render(request, 'homepage/teacher_home.html', {'announcement': teacher_announce})

	#if request.user.is_authenticated:
	#	announce = Announcement.objects.all().order_by('-date')
	#    return render(request, 'homepage/home.html',)
	#else:
	#	pass


@login_required
def classpage(request, id):
	data = Class.objects.get(id=id)
	student = mystudent.objects.filter(student_class = data)
	user = request.user
	if user.student.name == "Student":
		return render(request, 'homepage/student_class.html', {'class': data})
	else:
		return render(request, 'homepage/teacher_class.html', {'class': data,'student': student},)
	

def signup_request(request):
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				messages.success(request, "Registration successful." )
				return redirect("home")
			messages.error(request, "Unsuccessful registration. Invalid information.")
		form = NewUserForm()
		return render (request=request, template_name="user/signup.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="user/login.html", context={"login_form":form})


@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

@login_required
def student_details(request, id):
	data = {
		mystudent.objects.get(id=id)
	}