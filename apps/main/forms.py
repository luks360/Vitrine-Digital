from django import forms
from apps.main.models import User


class RegisterStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterStoreForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ["name", "email", "password", "cnpj", "contact", "segment", "icon"]

class RegisterClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterClientForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ["name", "email", "password", "birth_date", "icon"]

class LoginClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginClientForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ["email", "password"]

class LoginStoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginStoreForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ["cnpj", "password"]