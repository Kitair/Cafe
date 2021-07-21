from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username.strip(), password=password.strip())
        login(request, user)
        next_post = request.GET.get('next')
        redirect_path = next_ or next_post or '/'
        return redirect(redirect_path)
    return render(request, 'login.html', context={'form': form})


def register_view(request):
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'register_done.html', context={'new_user': new_user})

    return render(request, 'register.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

