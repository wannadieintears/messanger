from django.shortcuts import render
from .models import Chat
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    chats = Chat.objects.filter(members=request.user.id)
    context = {'chats': chats}
    return render(request, 'chats/chats.html', context)
