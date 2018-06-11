from django import forms
from .models import Qna

class PostForm(forms.ModelForm):

        class Meta:
            model = Qna
            fields = ('question',)
