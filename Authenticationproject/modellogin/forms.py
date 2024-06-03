from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm ,UserChangeForm

class signUpForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Confirm Password' }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Password' }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 py-2 text-sm w-1/2 mr-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 py-2 text-sm w-1/2 ml-2', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Email Address'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Password'}))


class changepassForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'New Password'}))
    
    
class editUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 py-2 text-sm w-1/2 mr-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 py-2 text-sm w-1/2 ml-2', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class':'border-b border-black focus:outline-none focus:border-blue-600 text-sm w-full py-2', 'placeholder': 'Email Address'}),
        }