from django import forms
from apps.main.models import Stores, Clients


class RegisterStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterStoreForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Stores
        fields = '__all__'

class RegisterClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterClientForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Clients
        fields = '__all__'

class LoginClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginClientForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Clients
        fields = ["email", "password"]

class LoginStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginStoreForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Stores
        fields = ["cnpj", "password"]