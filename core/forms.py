from .models import *
from django import forms

class BoxForm(forms.ModelForm):
  class Meta:
    model = Box
    fields = ['name', 'number', 'content']

class BoxLogForm(forms.ModelForm):
  class Meta:
    model = BoxLog
    fields = ['box']