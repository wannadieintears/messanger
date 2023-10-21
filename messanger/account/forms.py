from .models import Account
from chats.models import Chat
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields + ('email', 'age', 'phone', )


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['name']