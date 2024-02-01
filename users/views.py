from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm,SignInForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:signin")
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {
        'form': form,
    })


def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
    else:
        form = SignInForm()

    return render(request,'users/signin.html',{
        'form':form,
    })


# @login_required
# def logout_view(request):
#     logout(request)
#     render(request,'users/logout.html')

#     return HttpResponseRedirect(("users:login"))
