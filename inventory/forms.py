from django import forms
from .models import *


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ('tipo', 'preco', 'status', 'issues')


class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = ('tipo', 'preco', 'status', 'issues')


class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = ('tipo', 'preco', 'status', 'issues')