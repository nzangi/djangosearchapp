from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import UploadFileForm
from django.urls import reverse
from .models import UploadFileModel
from django.http import FileResponse, Http404
from PyPDF2 import PdfReader
import os
from spire.pdf import *
from spire.pdf.common import*
import re




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
    uploaded_pdfs = UploadFileModel.objects.all()
    # print(uploaded_pdfs)
    return render(request, 'base/view_pdfs.html',{
        'uploaded_pdfs':uploaded_pdfs,
    })

def view_pdf_at_time(request,pk):
    pdf = UploadFileModel.objects.get(pk=pk)
    # pdf = get_object_or_404(UploadFileModel,pk=pk,pdf_user=request.user)
    return render(request,'base/view_pdf_at_time.html',{
        'pdf':pdf,
    })

@login_required
def update_pdf(request,pk):
    # if request.method=="POST":
    pdf_to_update = get_object_or_404(UploadFileModel,pk=pk,pdf_user=request.user)
    if request.method=="POST":
        form = UploadFileForm(request.POST,request.FILES,instance=pdf_to_update)
        if form.is_valid():
            # form.instance.pdf_user=request.user
            form.save()
            return redirect('base:view_pdf_at_time',pk=pdf_to_update.id)
    else:
        form = UploadFileForm(instance=pdf_to_update)
    return render(request,'base/update_pdf.html',{
        'form':form,
    })

@login_required
def delete_pdf(request,pk):
    # pdf_to_delete = get_object_or_404(UploadFileModel,pk=pk,pdf_user=request.user)
    pdf_to_delete = UploadFileModel.objects.get(pk=pk,pdf_user=request.user)
    print(pdf_to_delete)
    print("Going To Method Post")

    if request.method =="POST":
        pdf_to_delete.delete()
        return redirect('base:view_pdf')
    else:
        print("Could not sent post request!")
    
    return render(request,'base/delete_pdf.html',{
            'pdf_to_delete':pdf_to_delete,
        })


def browser_pdf(request,pk):
    pdf_to_search_word = UploadFileModel.objects.get(pk=pk)
    query = request.GET.get('query','')
    matches = 0

    # Convert PDF to text and highlight occurrences of the query
    with open(pdf_to_search_word.pdf_file.path,'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        highlighted_content = ""
        text = ""

        for page_number in range(len(reader.pages)):
            # page = reader.pages[page_number]
            # text= page.extract_text()
            text += reader.pages[page_number].extract_text()


            if query.lower() in text.lower():
                matches += text.lower().count(query.lower())
                # Highlight matching occurrences using regex
                highlighted_text = re.sub(r'(?i)' + re.escape(query), r'<span style="background-color: yellow;">\g<0></span>', text)
                highlighted_content += highlighted_text

    return render(request,'base/browser_pdf.html',{
        'query':query,
        'pdf_to_search_word':pdf_to_search_word,
        'matches':matches,
        'highlighted_content':highlighted_content,
    })





