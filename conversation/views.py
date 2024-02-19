from django.shortcuts import render,get_object_or_404,redirect
from base.models import UploadFileModel
from conversation.forms import ConversationMessageForm
from conversation.models import Conversation


# Create your views here.
def new_conversation(request,pdf_pk):
    pdf_file = get_object_or_404(UploadFileModel,pk=pdf_pk)
    if pdf_file.pdf_user == request.user:
        return redirect('base:view_pdf')
    
    conversations = Conversation.objects.filter(pdf_file=pdf_file).filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(pdf_file=pdf_file)
            conversation.members.add(request.user)
            conversation.members.add(pdf_file.pdf_user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('base:view_pdf_at_time',pk=pdf_pk)
    else:
        form = ConversationMessageForm()

    return render (request,'conversation/')
        





