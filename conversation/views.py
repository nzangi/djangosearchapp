from django.shortcuts import render,get_object_or_404,redirect
from base.models import UploadFileModel
from conversation.forms import ConversationMessageForm
from conversation.models import Conversation
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def new_conversation(request,pdf_pk):
    pdf_file = get_object_or_404(UploadFileModel,pk=pdf_pk)
    if pdf_file.pdf_user == request.user:
        return redirect('base:view_pdf')
    
    conversations = Conversation.objects.filter(pdf_file=pdf_file).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:conversation_detail',pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['content'])
            conversation = Conversation.objects.create(pdf_file=pdf_file)
            conversation.members.add(request.user)
            conversation.members.add(pdf_file.pdf_user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('base:view_pdf_at_time',pk=pdf_pk)
        # else:
        #     print(form.errors)
    else:
        form = ConversationMessageForm()


    return render (request,'conversation/new.html',{'form':form})
        
@login_required
def inbox(request):
    conversations  = Conversation.objects.filter(members__in=[request.user.id])
    print(conversations)
    for conversation in conversations:
        print(conversation.pdf_file.pdf_file.url)
    return render(request,'conversation/inbox.html',{'conversations':conversations})


@login_required
def conversation_detail(request,pk):
    conversation  = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:conversation_detail',pk=pk)
    else:
        form = ConversationMessageForm()
    
    for message in conversation.messages.all():
        print(message.id)

    return render(request,'conversation/conversation_detail.html',{
        'form':form,
        'conversation':conversation,
    })


