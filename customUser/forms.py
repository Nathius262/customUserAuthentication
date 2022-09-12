from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
	"""docstring for CustomSignupForm"""
	first_name = forms.CharField(max_length=60, label="Fast name", widget=forms.TextInput(attrs={'placeholder':'First name'}))
	last_name = forms.CharField(max_length=60, label="Last name", widget=forms.TextInput(attrs={'placeholder':'Last name'}))

	class Meta:
		model = User
		fields = ("email", "username", "first_name", "last_name", "password1", "password2")


	def save(self, request):
		user = super(CustomSignupForm, self).save(request)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.is_active = True
		user.save()

		return user