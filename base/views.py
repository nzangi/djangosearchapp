from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import UploadFileForm
from django.urls import reverse
from .models import UploadFileModel
from django.http import FileResponse, Http404
from PyPDF2 import PdfReader
import os




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


# def pdf_view(request, pdf_id):
#     # Get the PDF file from the database based on the id
#     pdf_file = UploadFileModel.objects.get(id=pdf_id).pdf_file
#     try:
#         # Return the PDF file as a response
#         return FileResponse(open(pdf_file.path, 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         # Handle the file not found error
#         raise Http404('PDF file not found')

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
        print("Method Post")
        pdf_to_delete.delete()
        print("Item deleted")
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
        # Convert PDF to text
    file_path = pdf_to_search_word.pdf_file.path
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as file:
            pdf = PdfReader(file)
            text=''
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text()
            if query:
                matches = text.count(query)
            # print(matches)
    else:
        print(f"File does not exist at {file_path}")


    return render(request,'base/browser_pdf.html',{
        'query':query,
        'pdf_to_search_word':pdf_to_search_word,
        'matches':matches,
    })





