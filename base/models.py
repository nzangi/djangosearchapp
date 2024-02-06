from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class UploadFileModel(models.Model):
    pdf_file=models.FileField(upload_to='media/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    pdf_user = models.ForeignKey(User,on_delete=models.CASCADE)
    # db table.

    class Meta:
            db_table = "uploadfiles"

    def __str__(self):
        return self.pdf_file.name
