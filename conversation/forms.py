from .models import ConversationMessage
from django import forms

class ConversationMessageForm(forms.ModelForm):
    # content = forms.Textarea()
    class Meta:
        model = ConversationMessage
        fields = ('content',)
    
    #     widget=forms.Textarea(attrs={
    #     'placeholder': 'Start Conversation...',
    #     'class':'form-control w-100',
    # })