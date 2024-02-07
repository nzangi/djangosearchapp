from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.urls import reverse
from .models import UploadFileModel
from django.http import FileResponse, Http404



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
    return render(request, 'base/view_pdfs.html',{
        'uploaded_pdfs':uploaded_pdfs,
    })

