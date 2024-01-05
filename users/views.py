from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'users/signup.html')

def signin(request):
    return render(request,'users/signin.html')
