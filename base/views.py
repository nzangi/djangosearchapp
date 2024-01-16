from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

# def home(request):
#     return render(request, 'base/base.html')
@login_required
def upload_pdf(request):
    return render(request, 'base/upload_pdf.html')
