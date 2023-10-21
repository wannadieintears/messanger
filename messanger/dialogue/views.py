from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect
from chats.models import Chat
from account.models import Account


def index(request, pk):
    chat = Chat.objects.filter(id=pk)
    messages = Message.objects.filter(where_id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.where = Chat.objects.get(id=pk)
            message.sender = Account.objects.get(id=request.user.id)
            message.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = MessageForm()
    context = {'messages': messages, 'form': form, 'chat': chat}
    return render(request, 'dialogue/dialogue.html', context)