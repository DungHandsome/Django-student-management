from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your forms here.

class NewUserForm(UserCreationForm):
	sex_choices = ((0, 'Nam'), (1, 'Nữ'), (2, 'Không xác định'))
	email = forms.EmailField(required=True)


	class Meta:
		model = User
		fields = ( "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user