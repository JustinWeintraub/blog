from django import forms
from .models import ChatMessage
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
class ChatMessageCreationForm(forms.ModelForm):
    author=User
    def __init__(self, *args, **kwargs):
        super(ChatMessageCreationForm, self).__init__(*args, **kwargs)
        self.fields['content'].label=False
    class Meta:
        model=ChatMessage
        fields=['content']
