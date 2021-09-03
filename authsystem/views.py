from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

from .decorators import unauthorizedUsersCanView, authorizedUsersCanView
from .forms import CreateUserForm, SettingsForm

def index(request):
    context = {}
    return render(request, 'authsystem/index.html', context)

@unauthorizedUsersCanView
def register(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authsystem:login')

    context = {'form': form}
    return render(request, 'authsystem/register.html', context)

@unauthorizedUsersCanView
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Successfully logged in as {username}')
            return redirect('posts:homePage')
        else:
            messages.error(request, 'Username or Password is incorrect.')

    context = {}
    return render(request, 'authsystem/login.html', context)

@authorizedUsersCanView
def logout_view(request):
    username = request.user
    logout(request)
    messages.success(request, f'Successfully logged out from {username}')
    return redirect('authsystem:home')


@authorizedUsersCanView
def settings_view(request, pk):
    instance = User.objects.get(id=pk)

    current_user_id = request.user.id
    # print('This is the request.user.id: ', current_user_id)

    url_id = pk
    # print('This is the pk id: ', url_id)

    if current_user_id == url_id:
        form = SettingsForm(instance=instance)

        if request.method == 'POST':
            form = SettingsForm(request.POST, instance=instance)

            if form.is_valid():
                form.save()
                messages.success(request, 'Changes Saved Successfully')
                return redirect('posts:homePage')
        
        context = {'form':form}
        return render(request, 'authsystem/settings.html', context)
    else:
        return redirect('posts:homePage')
