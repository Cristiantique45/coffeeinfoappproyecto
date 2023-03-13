from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Contacto ,Comentario, Temaforo





class RegistroUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='',
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='',
    )
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        help_texts = {K:"" for K in fields}
        
        
        
        
class ComentarioForm(forms.ModelForm):
    comentario = forms.Textarea() 
    class Meta:
        model =  Comentario
        fields = ['comentario', 'imagen_idimagen', 'temaforo_idtemaforo']
        
        
        
class CrearTemaForm(forms.ModelForm):
    
    class Meta:
        model = Temaforo
        fields = ['nombre', 'foro_idforo']





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
        #model = Registrarseforo
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        #if Registrarseforo.objects.filter(correo=correo).exists():
            #raise forms.ValidationError('Este correo electrónico ya está en uso')
        #return correo
    
    
class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('last_login', None)