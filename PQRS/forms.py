# forms.py
from django import forms
from .models import Pqrs

class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = Pqrs
        fields = ['description', 'type']

    def _init_(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Seleccionar"

class FormResponderPqrs(forms.ModelForm):
    class Meta:
        model = Pqrs
        fields=['answer']