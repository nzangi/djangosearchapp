from django import forms
from .models import UploadFileModel
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('pdf_file',)
        widgets = {
            'pdf_file': forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        }