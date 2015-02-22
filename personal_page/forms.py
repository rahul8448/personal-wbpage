from django import forms
from models import Message

class MessageForm(forms.ModelForm):

    class Meta:
        model=Message
        exclude = ['create_time','update_time']