from .models import ConversationMessage
from django import forms

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        

