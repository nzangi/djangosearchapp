from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.urls import reverse


# Create your views here.

# def home(request):
#     return render(request, 'base/base.html')
@login_required
def upload_pdf(request):
    if request.method=="POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.pdf_user=request.user
            form.save()
            return redirect(reverse('base:view_pdf'))
        else:
            form = UploadFileForm()
    else:
        form = UploadFileForm()

    return render(request, 'base/upload_pdf.html',{'form':form})

def view_pdf(request):
    return render(request, 'base/view_pdfs.html')

