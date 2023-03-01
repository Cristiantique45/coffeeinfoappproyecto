from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Contacto, Registrarseforo, Foro





class CustomUserCreationForm(UserCreationForm):
    pass


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'


class RegistrarseforoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=45)
    correo = forms.EmailField(max_length=45)
    password = forms.CharField(max_length=120)

        
    
    class Meta:
        model = Registrarseforo
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Registrarseforo.objects.filter(correo=correo).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso')
        return correo
    
    
class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('last_login', None)