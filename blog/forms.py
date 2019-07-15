from django import forms
from django.contrib.auth.models import User
from .models import Comments
from crispy_forms.helper import FormHelper
class CommentForm(forms.ModelForm):
    author=User
    post_id=''
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label=False
    class Meta:
        model=Comments
        fields=['content']
