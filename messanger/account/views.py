from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm, ChatForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
import random
from chats.models import Chat


def index(request, pk):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            id = random.randint(1, 9999)
            x = Chat.objects.create(id=id, name=request.POST['name'])
            x = Chat.objects.get(id=id)
            x.members.add(Account.objects.get(id=request.user.id))
            x.members.add(Account.objects.get(id=pk))
            return redirect('chats')

    form = ChatForm
    acc = Account.objects.filter(id=pk)
    context = {'acc': acc, 'form': form}
    return render(request, 'account/account.html', context)


def auth(request):
    acc = Account.objects.filter(username=request.user)
    context = {'acc': acc}
    return render(request, 'account/myacc.html', context)


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy('myacc')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)