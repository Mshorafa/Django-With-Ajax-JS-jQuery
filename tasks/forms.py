from django import forms
from .models import DoTask


class TaskForm(forms.ModelForm):
    class Meta:
        model=DoTask
        fields = ['title']

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }
