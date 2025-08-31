from django import forms
from .models import User

class FormEntrega(forms.ModelForm):
    class Meta:
        model = User
        fields = ['address', 'zip_code', 'locality']
        exclude = ['number_document',
                    'phone',
                    'type_document_id', 
                    'date_joined', 
                    'email', 
                    'first_name', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'last_login',
                    'last_name',
                    'password',
                    'username']
        
    def __init__(self, *args, **kwargs):
        super(FormEntrega, self).__init__(*args, **kwargs)
        self.fields['locality'].empty_label = "Seleccionar localidad"
        
class FormEditarEntrega(forms.ModelForm):
    class Meta:
        model = User
        fields = ['address', 'zip_code', 'locality']
        exclude = [ 'number_document', 
                    'phone', 
                    'type_document_id', 
                    'date_joined', 
                    'email', 
                    'first_name', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'last_login',
                    'last_name',
                    'password',
                    'username']
        
    def __init__(self, *args, **kwargs):
        super(FormEditarEntrega, self).__init__(*args, **kwargs)
        self.fields['locality'].empty_label = "Seleccionar localidad"
