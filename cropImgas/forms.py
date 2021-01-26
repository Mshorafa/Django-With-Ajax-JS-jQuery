from django import forms
from .models import CroopImag


class CroopImagForm(forms.ModelForm):
    class Meta():
        model = CroopImag
        fields = ['file', ]
