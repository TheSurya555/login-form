from django.shortcuts import render, HttpResponseRedirect
from .forms import signUpForm, UserLoginForm ,changepassForm ,editUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'modellogin/home.html')

def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully !')
            form.save()
            form = signUpForm()
        else:
            messages.error(request, 'Account creation failed. Please check the form.')
    else:
        form = signUpForm()
        
    return render(request, 'modellogin/signUp.html', {'form': form})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserLoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/about/')
            else:
                messages.error(request, 'Bad credentials !!')
        else:
            fm = UserLoginForm()
        return render(request, 'modellogin/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/about/')


def about_user(request):
    if request.user.is_authenticated:
        return render(request , 'modellogin/about.html')
    
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def changepass(request):
    if request.method == 'POST':
        fm = changepassForm(user=request.user ,data=request.POST )
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request , fm.user)
            return HttpResponseRedirect('/login/')
    else:
        fm = changepassForm(user=request.user)    
    return render(request, 'modellogin/changepass.html' ,{'form' : fm})


@login_required
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = editUserForm(instance = user)
        if request.method == 'POST':
            form = editUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return HttpResponseRedirect('/profile/')  # Redirect to the profile page after editing        
        context = {
            'user' : user,
            'edit' : form
        }
        return render(request, 'modellogin/profile.html', context)
    else:
        return HttpResponseRedirect('/login/')
