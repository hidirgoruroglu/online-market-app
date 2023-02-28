from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation
# Create your views here.

@login_required(login_url="core:login_view")
def new_conversation(request,id):
    form = ConversationMessageForm()
    item = get_object_or_404(Item,id = id)
    if item.created_by == request.user:
        return redirect("dashboard:index")
    conversations = Conversation.objects.filter(item = item).filter(members__in = [request.user.id])
    
    if conversations:
        return redirect("conversation:detail", id = conversations.first().id)
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item = item)
            conversation.members.add(request.user) 
            conversation.members.add(item.created_by) 
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect("item:detail_view",id = id)
    context = dict(item = item,form = form)
    return render(request,"conversation/new.html",context)

@login_required(login_url="core:login_view")
def inbox(request):
    conversations = Conversation.objects.filter(members__in = [request.user.id])
    context = dict(conversations = conversations)
    return render(request,"conversation/inbox.html",context)

@login_required(login_url="core:login_view")
def detail(request,id):
    form = ConversationMessageForm()
    conversation = Conversation.objects.filter(members__in = [request.user.id]).get(id = id)
    if request.method =="POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()
            return redirect("conversation:detail",id = id)
    context = dict(conversation = conversation,form = form)
    return render(request,"conversation/detail.html",context)
