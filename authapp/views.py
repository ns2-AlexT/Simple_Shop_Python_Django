from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import ShopUserLoginForm, ShopUserCreationForm, ShopUserUserChangeForm
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            redirect_post = request.POST.get('redirect_post')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_post or reverse('mainapp:index'))
    else:
        form = ShopUserLoginForm()
    context = {
        'form': form,
        'page_title': 'LogIn',
        'get_back_redirect': redirect_to,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def registration(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    #     можено сделать поздравление с регистрацией ...
    else:
        form = ShopUserCreationForm()
    context = {
        'page_title': 'Registration form',
        'form': form,
        'pg_title': 'Registration',
        'btn_title': 'Register',
    }
    return render(request, 'authapp/register_update.html', context)
    # return render(request, 'authapp/_registration.html', context)


def updating(request):
    if request.method == 'POST':
        form = ShopUserUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ShopUserUserChangeForm(instance=request.user)
    context = {
        'page_title': 'Updating form',
        'form': form,
        'pg_title': 'Edit profile',
        'btn_title': 'Save',
    }
    return render(request, 'authapp/register_update.html', context)
    # return render(request, 'authapp/_updating.html', context)
