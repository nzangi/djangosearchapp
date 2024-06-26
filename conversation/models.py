from django.db import models
from django.db import models
from base.models import UploadFileModel
from django.contrib.auth.models import User

# Create your models here.
class Conversation(models.Model):
    pdf_file = models.ForeignKey(UploadFileModel,related_name='conversations',on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return ",".join([member.username for member in self.members.all()])

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation,related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='created_messages',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Conversation from {self.created_by}"


