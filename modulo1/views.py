#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#from django.contrib.auth.views import Loginview
from django.shortcuts import render, redirect
from django.contrib.auth import   login, logout, authenticate
from django.db.models import Q, F, Value
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import request
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import ContactoForm, RegistrarseforoForm, MyAuthenticationForm





# Create your views here.
def Home(request):
    return render(request, "principal.html")

def Login(request):
    return render (request, "login.html")

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
                data["form"] = formulario

    return render(request, 'app/contacto.html', data)
#-----------------------------------------------------------------------------------------------------------------------------------------------#
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('principal.html') # Si el usuario ya ha iniciado sesión, redirige a la nueva página personalizada

    # Si el usuario no ha iniciado sesión, muestra la página de inicio de sesión predeterminada de Django
    else:
        return LoginView.as_view(template_name='registration/login.html', extra_context={'next': '/principal.html/'})(request)


def principal(request):
    if request.user.is_authenticated:
        return render(request, 'principal.html')
    else:
        return redirect('login')

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------REGISTRO-------------------------------------------------#

def registro_usuario(request):

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentiar el usuario y regresar al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/register.html')    

#-----------------------------------------------------------------------------------------------------#

def foro_login(request):
    if request.method == "POST":
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            #vamos a guardar en una varible usuario lo que el usuario ingrese en el campo "username"
            usuario = form.cleaned_data.get('Enter_username')
            contraseña = form.cleaned_data.get('Enter_password')
            
            try:
                registrado = Registrarseforo.objects.get(nombre=usuario)
            except Registrarseforo.DoesNotExist:
                registrado = None
                
            user = authenticate(request, usuario=registrado.nombre, password=contraseña)
            #si tiene algun valor
            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {usuario}")
                 # Agregue un registro para depurar
                Logger.debug(f"Usuario {usuario} autenticado y logueado")
                return redirect('modulo1:leercf')
            else:
                messages.error(request, "usuario o contraseña equivocada")
        else:
            messages.error(request, "usuario o contraseña equivocada")         
    
    form = MyAuthenticationForm
    return render (request, "login_foro.html", {"form": form})



def foro_logout(request):
    logout(request)
    #return render (request, "logout_foro.html")
    messages.info(request, "Saliste exitosamente")
    return redirect("modulo1:leercf")

 

     
    # librerias del crud

    #----------------------------ainseticida---------------------------------------------------------------------------------------------------------#
class ListadoAinsecticida(ListView):
    model = Ainsecticida
    
    
class AinsecticidaCrear(SuccessMessageMixin, CreateView):
    model =Ainsecticida
    form = Ainsecticida
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer'

class AinsecticidaDetalle (DetailView):
    model =Ainsecticida

class  AinsecticidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Ainsecticida
    form = Ainsecticida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer'
    
class AinsecticidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Ainsecticida
    form = Ainsecticida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer'

 
 
       

        #--------------------------------------------------CategoriaForo-------------------------------------------#
        
class ListadoCategoriaforo(ListView):
    model = Categoriaforo
    template_name = "crud\categoriaforo\index.html"
    context_object_name = 'categoria'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = queryset.filter(Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar))
        return queryset
        

class CategoriaforoCrear(SuccessMessageMixin, CreateView):
    model =Categoriaforo
    form = Categoriaforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leercf') # Redireccionamos a la vista principal 'leer'

class CategoriaforoDetalle (DetailView):
    model =Categoriaforo

class  CategoriaforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Categoriaforo
    form = Categoriaforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leercf') # Redireccionamos a la vista principal 'leer'
class CategoriaforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriaforo
    form = Categoriaforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leercf') # Redireccionamos a la vista principal 'leer'
    
    
    #------------------------------------------COMENTARIO-----------------------------------------------------------------------------------#
class ListadoComentario(ListView):
    model = Comentario
    context_object_name = 'comentarios'
    
    #funciones para traer la foto de perfil de acuerdo al comentario
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(perfilforo_idperfilforo__fotoperfil__isnull=False)        
        return qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    #--------------------------funcion para hacer una busqueda------------------------------------------
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = queryset.filter(Q (comentario__icontains=buscar))
        return queryset

    
    
    
class ComentarioCrear(SuccessMessageMixin, CreateView):
    model = Comentario
    form = Comentario
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'

class ComentarioDetalle (DetailView):
    model = Comentario

class ComentarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Comentario
    form = Comentario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'
class ComentarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Comentario
    form = Comentario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'



        #----------------------------------Crearhiloforo------------------------------------------------------------------------------------------------------------------#

class ListadoChiloF(ListView):
    model = Crearhiloforo
    
    
class ChiloFCrear(SuccessMessageMixin, CreateView):
    model =Crearhiloforo
    form = Crearhiloforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerchf') # Redireccionamos a la vista principal 'leer'

class ChiloFDetalle (DetailView):
    model =Crearhiloforo

class  ChiloFActualizar(SuccessMessageMixin,UpdateView):
    model =  Crearhiloforo
    form = Crearhiloforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerchf') # Redireccionamos a la vista principal 'leer'
class ChiloFEliminar(SuccessMessageMixin, DeleteView): 
    model = Crearhiloforo
    form = Crearhiloforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerchf') # Redireccionamos a la vista principal 'leer'

#--------------------------------------------ENFERMEDADES-------------------------------------------------------------------------------------------------------------------#
class ListadoEnfermedades(ListView):
    model = Enfermedades
    
    
class EnfermedadesCrear(SuccessMessageMixin, CreateView):
    model = Enfermedades
    form = Enfermedades
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leeref') # Redireccionamos a la vista principal 'leer'

class EnfermedadesDetalle (DetailView):
    model = Enfermedades

class EnfermedadesActualizar(SuccessMessageMixin,UpdateView):
    model =  Enfermedades
    form = Enfermedades
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leeref') # Redireccionamos a la vista principal 'leer'
class EnfermedadesEliminar(SuccessMessageMixin, DeleteView): 
    model = Enfermedades
    form = Enfermedades
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leeref') # Redireccionamos a la vista principal 'leer'
    
    
     #----------------------------------Foro------------------------------------------------------------------------------------------------------------------#

class ListadoForo(ListView):
    model = Foro
    
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = queryset.filter(Q(nombre__icontains=buscar))
        return queryset
    
    
    
    
class ForoCrear(SuccessMessageMixin, CreateView):
    model =Foro
    form = Foro
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerfr') # Redireccionamos a la vista principal 'leer'

class ForoDetalle (DetailView):
    model =Foro

class  ForoActualizar(SuccessMessageMixin,UpdateView):
    model =  Foro
    form = Foro
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerfr') # Redireccionamos a la vista principal 'leer'
class ForoEliminar(SuccessMessageMixin, DeleteView): 
    model = Foro
    form = Foro
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerfr') # Redireccionamos a la vista principal 'leer'



        #----------------------------------Gastos------------------------------------------------------------------------------------------------------------------#

class ListadoGastos(ListView):
    model = Gastos
    
    
class GastosCrear(SuccessMessageMixin, CreateView):
    model =Gastos
    form = Gastos
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leer7') # Redireccionamos a la vista principal 'leer'

class GastosDetalle (DetailView):
    model =Gastos

class  GastosActualizar(SuccessMessageMixin,UpdateView):
    model =  Gastos
    form = Gastos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leer7') # Redireccionamos a la vista principal 'leer'
class GastosEliminar(SuccessMessageMixin, DeleteView): 
    model = Gastos
    form = Gastos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leer7') # Redireccionamos a la vista principal 'leer'

#------------------------------------------------Historial-----------------------------------------------------------------------#

class ListadoHistorial(ListView):
    model = Historial
    
    
class HistorialCrear(SuccessMessageMixin, CreateView):
    model = Historial
    form = Historial
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerh') # Redireccionamos a la vista principal 'leer'

class HistorialDetalle (DetailView):
    model = Historial

class HistorialActualizar(SuccessMessageMixin,UpdateView):
    model =  Historial
    form = Historial
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerh') # Redireccionamos a la vista principal 'leer'
class HistorialEliminar(SuccessMessageMixin, DeleteView): 
    model = Historial
    form = Historial
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerh') # Redireccionamos a la vista principal 'leer'
    
    
    
    #--------------------------------------------Imagen--------------------------------------------------------------------------------------------------------#

class ListadoImagen(ListView):
    model = Imagen
    
    
class ImagenCrear(SuccessMessageMixin, CreateView):
    model =Imagen
    form = Imagen
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerimg') # Redireccionamos a la vista principal 'leer'

class ImagenDetalle (DetailView):
    model =Imagen

class  ImagenActualizar(SuccessMessageMixin,UpdateView):
    model =  Imagen
    form = Imagen
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerimg') # Redireccionamos a la vista principal 'leer'
class ImagenEliminar(SuccessMessageMixin, DeleteView): 
    model = Imagen
    form = Imagen
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerimg') # Redireccionamos a la vista principal 'leer'
    
    
    #--------------------------------------------Informacion del café--------------------------------------------------------------------------------------------------------#

class ListadoInformacioncafe(ListView):
    model = Informacioncafe
    
    
class InformacioncafeCrear(SuccessMessageMixin, CreateView):
    model =Informacioncafe
    form = Informacioncafe
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerinfo') # Redireccionamos a la vista principal 'leer'

class InformacioncafeDetalle (DetailView):
    model =Informacioncafe

class  InformacioncafeActualizar(SuccessMessageMixin,UpdateView):
    model =  Informacioncafe
    form = Informacioncafe
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerinfo') # Redireccionamos a la vista principal 'leer'
    
class InformacioncafeEliminar(SuccessMessageMixin, DeleteView): 
    model = Informacioncafe
    form = Informacioncafe
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerinfo') # Redireccionamos a la vista principal 'leer'
    
    
    
    #--------------------------------------------Insecticidas--------------------------------------------------------------------------------------------------------#

class ListadoInsecticidas(ListView):
    model = Insecticidas
    
    
class InsecticidasCrear(SuccessMessageMixin, CreateView):
    model =Insecticidas
    form = Insecticidas
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerinsec') # Redireccionamos a la vista principal 'leer'

class InsecticidasDetalle (DetailView):
    model =Insecticidas

class  InsecticidasActualizar(SuccessMessageMixin,UpdateView):
    model =  Insecticidas
    form = Insecticidas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerinsec') # Redireccionamos a la vista principal 'leer'
    
class InsecticidasEliminar(SuccessMessageMixin, DeleteView): 
    model = Insecticidas
    form = Insecticidas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerinsec') # Redireccionamos a la vista principal 'leer'
    
    
     #--------------------------------------------Inversion--------------------------------------------------------------------------------------------------------#

class ListadoInversion(ListView):
    model = Inversion
    
    
class InversionCrear(SuccessMessageMixin, CreateView):
    model =Inversion
    form = Inversion
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerinv') # Redireccionamos a la vista principal 'leer'

class InversionDetalle (DetailView):
    model =Inversion

class  InversionActualizar(SuccessMessageMixin,UpdateView):
    model =  Inversion
    form = Inversion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerinv') # Redireccionamos a la vista principal 'leer'
    
class InversionEliminar(SuccessMessageMixin, DeleteView): 
    model = Inversion
    form = Inversion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerinv') # Redireccionamos a la vista principal 'leer'
    
    
    
    #--------------------------------------------Lote--------------------------------------------------------------------------------------------------------#

class ListadoLote(ListView):
    model = Lote
    
    
class LoteCrear(SuccessMessageMixin, CreateView):
    model =Lote
    form = Lote
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerlot') # Redireccionamos a la vista principal 'leer'

class LoteDetalle (DetailView):
    model =Lote

class  LoteActualizar(SuccessMessageMixin,UpdateView):
    model =  Lote
    form = Lote
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerlot') # Redireccionamos a la vista principal 'leer'
    
class LoteEliminar(SuccessMessageMixin, DeleteView): 
    model = Lote
    form = Lote
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerlot') # Redireccionamos a la vista principal 'leer'


#---------------------------------------MCONTROLENFERMEDADES-----------------------------------------------------------#
class ListadoMcontrolenfermedad(ListView):
    model = Mcontrolenfermedad
    
    
class McontrolenfermedadCrear(SuccessMessageMixin, CreateView):
    model = Mcontrolenfermedad
    form = Mcontrolenfermedad
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leermce') # Redireccionamos a la vista principal 'leer'

class McontrolenfermedadDetalle (DetailView):
    model = Mcontrolenfermedad

class McontrolenfermedadActualizar(SuccessMessageMixin,UpdateView):
    model =  Mcontrolenfermedad
    form = Mcontrolenfermedad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leermce') # Redireccionamos a la vista principal 'leer'
class McontrolenfermedadEliminar(SuccessMessageMixin, DeleteView): 
    model = Mcontrolenfermedad
    form = Mcontrolenfermedad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leermce') # Redireccionamos a la vista principal 'leer'

#-------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------mcontrolplagas------------------------------------------------------------------------------------------------------------------#
class ListadoMcontrolplagas(ListView):
    model = Mcontrolplagas
    
    
class McontrolplagasCrear(SuccessMessageMixin, CreateView):
    model =Mcontrolplagas
    form = Mcontrolplagas
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leermcp') # Redireccionamos a la vista principal 'leer'

class McontrolplagasDetalle (DetailView):
    model =Mcontrolplagas

class  McontrolplagasActualizar(SuccessMessageMixin,UpdateView):
    model =  Mcontrolplagas
    form = Mcontrolplagas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leermcp') # Redireccionamos a la vista principal 'leer'
class McontrolplagasEliminar(SuccessMessageMixin, DeleteView): 
    model = Mcontrolplagas
    form = Mcontrolplagas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leermcp') # Redireccionamos a la vista principal 'leer'




 #----------------------------------pcurativasEnfer------------------------------------------------------------------------------------------------------------------#

class ListadoPcurativasenfer(ListView):
    model = Pcurativasenfer
    
    
class PcurativasenferCrear(SuccessMessageMixin, CreateView):
    model = Pcurativasenfer
    form = Pcurativasenfer
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpcuraenf') # Redireccionamos a la vista principal 'leer'

class PcurativasenferDetalle (DetailView):
    model =Pcurativasplaga

class  PcurativasenferActualizar(SuccessMessageMixin,UpdateView):
    model =  Pcurativasenfer
    form = Pcurativasenfer
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpcuraenf') # Redireccionamos a la vista principal 'leer'
class PcurativasenferEliminar(SuccessMessageMixin, DeleteView): 
    model = Pcurativasenfer
    form = Pcurativasenfer
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpcuraenf') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    #----------------------------------pcurativasplaga------------------------------------------------------------------------------------------------------------------#

class ListadoPcuraP(ListView):
    model = Pcurativasplaga
    
    
class PcuraPCrear(SuccessMessageMixin, CreateView):
    model =Pcurativasplaga
    form = Pcurativasplaga
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer'

class PcuraPDetalle (DetailView):
    model =Pcurativasplaga

class  PcuraPActualizar(SuccessMessageMixin,UpdateView):
    model =  Pcurativasplaga
    form = Pcurativasplaga
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer'
class PcuraPEliminar(SuccessMessageMixin, DeleteView): 
    model = Pcurativasplaga
    form = Pcurativasplaga
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    
    
#----------------------------------perdidas------------------------------------------------------------------------------------------------------------------#

class ListadoPerdidas(ListView):
    model = Perdidas
    
    
class PerdidasCrear(SuccessMessageMixin, CreateView):
    model = Perdidas
    form = Perdidas
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerper') # Redireccionamos a la vista principal 'leer'

class PerdidasDetalle (DetailView):
    model = Perdidas

class  PerdidasActualizar(SuccessMessageMixin,UpdateView):
    model =  Perdidas
    form = Perdidas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerper') # Redireccionamos a la vista principal 'leer'
class PerdidasEliminar(SuccessMessageMixin, DeleteView): 
    model = Perdidas
    form = Perdidas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerper') # Redireccionamos a la vista principal 'leer'
    
    
 #----------------------------------perfilforo----------------------------------------------------------------------#

class ListadoPerfilforo(ListView):
    model = Perfilforo

class PerfilforoCrear(SuccessMessageMixin, CreateView):
    model = Perfilforo
    form = Perfilforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpef') # Redireccionamos a la vista principal 'leer'

class PerfilforoDetalle (DetailView):
    model = Perfilforo

class PerfilforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Perfilforo
    form = Perfilforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpef') # Redireccionamos a la vista principal 'leer'
class PerfilforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Perfilforo
    form = Perfilforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpef') # Redireccionamos a la vista principal 'leer'



#----------------------------------perfilforo postforo------------------------------------------------------------------------------------------------------------------#

class ListadoPerfilforopostforo(ListView):
    model = Perfilforopostforo
    
    
class PerfilforopostforoCrear(SuccessMessageMixin, CreateView):
    model = Perfilforopostforo
    form = Perfilforopostforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpfpf') # Redireccionamos a la vista principal 'leer'

class PerfilforopostforoDetalle (DetailView):
    model = Perfilforopostforo

class  PerfilforopostforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Perfilforopostforo
    form = Perfilforopostforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpfpf') # Redireccionamos a la vista principal 'leer'
class PerfilforopostforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Perfilforopostforo
    form = Perfilforopostforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpfpf') # Redireccionamos a la vista principal 'leer'
    
    
    
#----------------------------------Persona-----------------------------------------------------------#

class ListadoPersona(ListView):
    model = Persona
    
    
class PersonaCrear(SuccessMessageMixin, CreateView):
    model = Persona
    form = Persona
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerperso') # Redireccionamos a la vista principal 'leer'

class PersonaDetalle (DetailView):
    model = Persona

class  PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerperso') # Redireccionamos a la vista principal 'leer'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona 
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerperso') # Redireccionamos a la vista principal 'leer'
    
    


#-----------------------------------------PERFIL INFO CAFEE---------------------------------------------------#

class ListadoPersonainfocafe(ListView):
    model = Personainfocafe
    
    
class PersonainfocafeCrear(SuccessMessageMixin, CreateView):
    model = Personainfocafe
    form = Personainfocafe
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class PersonainfocafeDetalle (DetailView):
    model = Personainfocafe

class PersonainfocafeActualizar(SuccessMessageMixin,UpdateView):
    model =  Personainfocafe
    form = Personainfocafe
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class PersonainfocafeEliminar(SuccessMessageMixin, DeleteView): 
    model = Personainfocafe
    form = Personainfocafe
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    


 #----------------------------------Plagas------------------------------------------------------------------------------------------------------------------#

class ListadoPlagas(ListView):
    model = Plagas
    
    
class PlagasCrear(SuccessMessageMixin, CreateView):
    model =Plagas
    form = Plagas
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerplg') # Redireccionamos a la vista principal 'leer'

class PlagasDetalle (DetailView):
    model = Plagas

class  PlagasActualizar(SuccessMessageMixin,UpdateView):
    model =  Plagas
    form = Plagas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerplg') # Redireccionamos a la vista principal 'leer'
class PlagasEliminar(SuccessMessageMixin, DeleteView): 
    model = Plagas
    form = Plagas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerplg') # Redireccionamos a la vista principal 'leer'
    

#-------------------------------------------POST FORO-------------------------------------------------------------------#

class ListadoPostforo(ListView):
    model = Postforo
    
    
class PostforoCrear(SuccessMessageMixin, CreateView):
    model = Postforo
    form = Postforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpof') # Redireccionamos a la vista principal 'leer'

class PostforoDetalle (DetailView):
    model = Postforo

class PostforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Postforo
    form = Postforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpof') # Redireccionamos a la vista principal 'leer'
class PostforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Postforo
    form = Postforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpof') # Redireccionamos a la vista principal 'leer'
    
    
    
    
#-------------------------------------------ppreventiva enfer-------------------------------------------------------------------#

class ListadoPpreventivaenfer(ListView):
    model = Ppreventivaenfer
    
    
class PpreventivaenferCrear(SuccessMessageMixin, CreateView):
    model = Ppreventivaenfer
    form = Ppreventivaenfer
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerppenf') # Redireccionamos a la vista principal 'leer'

class PpreventivaenferDetalle (DetailView):
    model = Ppreventivaenfer

class PpreventivaenferActualizar(SuccessMessageMixin,UpdateView):
    model =  Ppreventivaenfer
    form = Ppreventivaenfer
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerppenf') # Redireccionamos a la vista principal 'leer'
class PpreventivaenferEliminar(SuccessMessageMixin, DeleteView): 
    model = Ppreventivaenfer
    form = Ppreventivaenfer
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerppenf') # Redireccionamos a la vista principal 'leer'
    
    
    
    #-------------------------------------------ppreventiva plaga-------------------------------------------------------------------#

class ListadoPpreventivasplaga(ListView):
    model = Ppreventivasplaga
    
    
class PpreventivasplagaCrear(SuccessMessageMixin, CreateView):
    model = Ppreventivasplaga
    form = Ppreventivasplaga
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpprep') # Redireccionamos a la vista principal 'leer'

class PpreventivasplagaDetalle (DetailView):
    model = Ppreventivasplaga

class PpreventivasplagaActualizar(SuccessMessageMixin,UpdateView):
    model =  Ppreventivasplaga
    form = Ppreventivasplaga
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpprep') # Redireccionamos a la vista principal 'leer'
class PpreventivasplagaEliminar(SuccessMessageMixin, DeleteView): 
    model = Ppreventivasplaga
    form = Ppreventivasplaga
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpprep') # Redireccionamos a la vista principal 'leer'
    
    
    
     #-------------------------------------------reaccion post-------------------------------------------------------------------#

class ListadoReaccionpost(ListView):
    model = Reaccionpost
    
    
class ReaccionpostCrear(SuccessMessageMixin, CreateView):
    model = Reaccionpost
    form = Reaccionpost
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerrp') # Redireccionamos a la vista principal 'leer'

class ReaccionpostDetalle (DetailView):
    model = Reaccionpost

class ReaccionpostActualizar(SuccessMessageMixin,UpdateView):
    model =  Reaccionpost
    form = Reaccionpost
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrp') # Redireccionamos a la vista principal 'leer'
class ReaccionpostEliminar(SuccessMessageMixin, DeleteView): 
    model = Reaccionpost
    form = Reaccionpost
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrp') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    
#-------------------------------------------recomendacion insect-------------------------------------------------------------------#

class ListadoRecomendacioninsect(ListView):
    model = Recomendacioninsect
    
    
class RecomendacioninsectCrear(SuccessMessageMixin, CreateView):
    model = Recomendacioninsect
    form = Recomendacioninsect
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerri') # Redireccionamos a la vista principal 'leer'

class RecomendacioninsectDetalle (DetailView):
    model = Recomendacioninsect

class RecomendacioninsectActualizar(SuccessMessageMixin,UpdateView):
    model =  Recomendacioninsect
    form = Recomendacioninsect
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerri') # Redireccionamos a la vista principal 'leer'
class RecomendacioninsectEliminar(SuccessMessageMixin, DeleteView): 
    model = Recomendacioninsect
    form = Recomendacioninsect
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerri') # Redireccionamos a la vista principal 'leer'
    
    
    
    
#-------------------------------------------recomendacion plaga-------------------------------------------------------------------#

class ListadoRecomendacionplaga(ListView):
    model = Recomendacionplaga
    
    
class RecomendacionplagaCrear(SuccessMessageMixin, CreateView):
    model = Recomendacionplaga
    form = Recomendacionplaga
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerrplg') # Redireccionamos a la vista principal 'leer'

class RecomendacionplagaDetalle (DetailView):
    model = Recomendacionplaga

class RecomendacionplagaActualizar(SuccessMessageMixin,UpdateView):
    model =  Recomendacionplaga
    form = Recomendacionplaga
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrplg') # Redireccionamos a la vista principal 'leer'
class RecomendacionplagaEliminar(SuccessMessageMixin, DeleteView): 
    model = Recomendacionplaga
    form = Recomendacionplaga
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrplg') # Redireccionamos a la vista principal 'leer'
    
    
    
#-------------------------------------------Registrarse foro-------------------------------------------------------------------#

class ListadoRegistrarseforo(ListView):
    model = Registrarseforo
    
    
class RegistrarseforoCrear(FormView):
    model = Registrarseforo
    form_class= RegistrarseforoForm
    template_name = 'crud/registrarseforo/crear.html'
    fields = "__all__"
    success_url = ('modulo1:leerco')
    
    def form_valid(self, form):
        usuario = form.save()
        nombre = form.cleaned_data['nombre']
        correo = form.cleaned_data['correo']
        password = form.cleaned_data['password']
        usuario = authenticate(self.request,nombre=nombre, correo=correo, password=password)
        if usuario is not None:
            foro_login(self.request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(self.request, 'Bienvenido!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Usuario o contraseña incorrectos.')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
    
               
             
    def get_success_url(self):        
        return redirect('modulo1:leerco') # Redireccionamos a la vista principal 'leer'
            
        
                
    
    form = Registrarseforo
    def get_success_url(self):        
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'    
                
class RegistrarseforoDetalle (DetailView):
    model = Registrarseforo

class RegistrarseforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Registrarseforo
    form = Registrarseforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrefo') # Redireccionamos a la vista principal 'leer'
class RegistrarseforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Registrarseforo
    form = Registrarseforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrefo') # Redireccionamos a la vista principal 'leer'
    
    
    
    
#-------------------------------------------Registrarseforo perfilforo-------------------------------------------------------------------#

#class ListadoRegistrarseforoperfilforo(ListView):
    #model = Registrarseforoperfilforo
    
    
#class RegistrarseforoperfilforoCrear(SuccessMessageMixin, CreateView):
    #model = Registrarseforoperfilforo
    #form = Registrarseforoperfilforo
    #fields = "__all__"
    #success_message ='Categoria creada correctamente'
     
    #def get_success_url(self):        
        #return reverse('modulo1:leerrfpf') # Redireccionamos a la vista principal 'leer'

#class RegistrarseforoperfilforoDetalle (DetailView):
    #model = Registrarseforoperfilforo

#class RegistrarseforoperfilforoActualizar(SuccessMessageMixin,UpdateView):
    #model =  Registrarseforoperfilforo
    #form = Registrarseforoperfilforo
    #fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    #success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    #def get_success_url(self):               
        #return reverse('modulo1:leerrfpf') # Redireccionamos a la vista principal 'leer'
#class RegistrarseforoperfilforoEliminar(SuccessMessageMixin, DeleteView): 
    #model = Registrarseforoperfilforo
    #form = Registrarseforoperfilforo
    #fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    #def get_success_url(self): 
        #success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        #messages.success (self.request, (success_message))       
        #return reverse('modulo1:leerrfpf') # Redireccionamos a la vista principal 'leer'
    
    
    
#-------------------------------------------rfinanciero-------------------------------------------------------------------#

class ListadoRfinanciero(ListView):
    model = Rfinanciero
    
    
class RfinancieroCrear(SuccessMessageMixin, CreateView):
    model = Rfinanciero
    form = Rfinanciero
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerrefinan') # Redireccionamos a la vista principal 'leer'

class RfinancieroDetalle (DetailView):
    model = Rfinanciero

class RfinancieroActualizar(SuccessMessageMixin,UpdateView):
    model =  Rfinanciero
    form = Rfinanciero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrefinan') # Redireccionamos a la vista principal 'leer'
class RfinancieroEliminar(SuccessMessageMixin, DeleteView): 
    model = Rfinanciero
    form = Rfinanciero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrefinan') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    #-------------------------------------------rfinanciero lote-------------------------------------------------------------------#

class ListadoRfinancierolote(ListView):
    model = Rfinancierolote
    
    
class RfinancieroloteCrear(SuccessMessageMixin, CreateView):
    model = Rfinancierolote
    form = Rfinancierolote
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerrefilo') # Redireccionamos a la vista principal 'leer'

class RfinancieroloteDetalle (DetailView):
    model = Rfinancierolote

class RfinancieroloteActualizar(SuccessMessageMixin,UpdateView):
    model =  Rfinancierolote
    form = Rfinancierolote
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrefilo') # Redireccionamos a la vista principal 'leer'
class RfinancieroloteEliminar(SuccessMessageMixin, DeleteView): 
    model = Rfinancierolote
    form = Rfinancierolote
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrefilo') # Redireccionamos a la vista principal 'leer'
    
    
    
#-------------------------------------------Tema foro-------------------------------------------------------------------#

class ListadoTemaforo(ListView):
    model = Temaforo
    
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = queryset.filter(nombre__icontains=buscar)
        return queryset
    
    
class TemaforoCrear(SuccessMessageMixin, CreateView):
    model = Temaforo
    form = Temaforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertefo') # Redireccionamos a la vista principal 'leer'

class TemaforoDetalle (DetailView):
    model = Temaforo

class TemaforoActualizar(SuccessMessageMixin,UpdateView):
    model =  Temaforo
    form = Temaforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertefo') # Redireccionamos a la vista principal 'leer'
class TemaforoEliminar(SuccessMessageMixin, DeleteView): 
    model = Temaforo
    form = Temaforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertefo') # Redireccionamos a la vista principal 'leer'
    
    
    
    
 #-------------------------------------------tenfermedad-------------------------------------------------------------------#

class ListadoTenfermedad(ListView):
    model = Tenfermedad
    
    
class TenfermedadCrear(SuccessMessageMixin, CreateView):
    model = Tenfermedad
    form = Tenfermedad
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertenfe') # Redireccionamos a la vista principal 'leer'

class TenfermedadDetalle (DetailView):
    model = Tenfermedad

class TenfermedadActualizar(SuccessMessageMixin,UpdateView):
    model =  Tenfermedad
    form = Tenfermedad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertenfe') # Redireccionamos a la vista principal 'leer'
class TenfermedadEliminar(SuccessMessageMixin, DeleteView): 
    model = Tenfermedad
    form = Tenfermedad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertenfe') # Redireccionamos a la vista principal 'leer'
    
    
    
    
 #-------------------------------------------tgastos-------------------------------------------------------------------#

class ListadoTgastos(ListView):
    model = Tgastos
    
    
class TgastosCrear(SuccessMessageMixin, CreateView):
    model = Tgastos
    form = Tgastos
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertgst') # Redireccionamos a la vista principal 'leer'

class TgastosDetalle (DetailView):
    model = Tgastos

class TgastosActualizar(SuccessMessageMixin,UpdateView):
    model =  Tgastos
    form = Tgastos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertgst') # Redireccionamos a la vista principal 'leer'
class TgastosEliminar(SuccessMessageMixin, DeleteView): 
    model = Tgastos
    form = Tgastos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertgst') # Redireccionamos a la vista principal 'leer'
    
    
    
 #-------------------------------------------tinsecticida-------------------------------------------------------------------#

class ListadoTinsecticida(ListView):
    model = Tinsecticida
    
    
class TinsecticidaCrear(SuccessMessageMixin, CreateView):
    model = Tinsecticida
    form = Tinsecticida
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertinsec') # Redireccionamos a la vista principal 'leer'

class TinsecticidaDetalle (DetailView):
    model = Tinsecticida

class TinsecticidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tinsecticida
    form = Tinsecticida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertinsec') # Redireccionamos a la vista principal 'leer'
class TinsecticidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tinsecticida
    form = Tinsecticida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertinsec') # Redireccionamos a la vista principal 'leer'
    
    
    
    
#-------------------------------------------tinversion-------------------------------------------------------------------#

class ListadoTinversion(ListView):
    model = Tinversion
    
    
class TinversionCrear(SuccessMessageMixin, CreateView):
    model = Tinversion
    form = Tinversion
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertinver') # Redireccionamos a la vista principal 'leer'

class TinversionDetalle (DetailView):
    model = Tinversion

class TinversionActualizar(SuccessMessageMixin,UpdateView):
    model =  Tinversion
    form = Tinversion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertinver') # Redireccionamos a la vista principal 'leer'
class TinversionEliminar(SuccessMessageMixin, DeleteView): 
    model = Tinversion
    form = Tinversion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertinver') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    #-------------------------------------------tperdida-------------------------------------------------------------------#

class ListadoTperdida(ListView):
    model = Tperdida
    
    
class TperdidaCrear(SuccessMessageMixin, CreateView):
    model = Tperdida
    form = Tperdida
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertperd') # Redireccionamos a la vista principal 'leer'

class TperdidaDetalle (DetailView):
    model = Tperdida

class TperdidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tperdida
    form = Tperdida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertperd') # Redireccionamos a la vista principal 'leer'
class TperdidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tperdida
    form = Tperdida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertperd') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    #-------------------------------------------tpersona-------------------------------------------------------------------#

class ListadoTpersona(ListView):
    model = Tpersona
    
    
class TpersonaCrear(SuccessMessageMixin, CreateView):
    model = Tpersona
    form = Tpersona
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertperso') # Redireccionamos a la vista principal 'leer'

class TpersonaDetalle (DetailView):
    model = Tpersona

class TpersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tpersona
    form = Tpersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertperso') # Redireccionamos a la vista principal 'leer'
class TpersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tpersona
    form = Tpersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertperso') # Redireccionamos a la vista principal 'leer'
    
    
        #----------------------------------Tratamiento------------------------------------------------------------------------------------------------------------------#

class ListadoTratamiento(ListView):
    model = Tratamiento
    
    
class TratamientoCrear(SuccessMessageMixin, CreateView):
    model =Tratamiento
    form = Tratamiento
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertrt') # Redireccionamos a la vista principal 'leer'

class TratamientoDetalle (DetailView):
    model =Tratamiento

class  TratamientoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tratamiento
    form = Tratamiento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertrt') # Redireccionamos a la vista principal 'leer'
class TratamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tratamiento
    form = Tratamiento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertrt') # Redireccionamos a la vista principal 'leer'
    
    
    #----------------------------------Tusuarioforo------------------------------------------------------------------------------------------------------------------#

class ListadoTUFo(ListView):
    model = Tusuarioforo
    
    
class TUFoCrear(SuccessMessageMixin, CreateView):
    model =Tusuarioforo
    form = Tusuarioforo
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertuf') # Redireccionamos a la vista principal 'leer'

class TUFoDetalle (DetailView):
    model =Tusuarioforo

class  TUFoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tusuarioforo
    form = Tusuarioforo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertuf') # Redireccionamos a la vista principal 'leer'
class TUFoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tusuarioforo
    form = Tusuarioforo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertuf') # Redireccionamos a la vista principal 'leer'


    #----------------------------------Tvariedad------------------------------------------------------------------------------------------------------------------#

class ListadoTvar(ListView):
    model = Tvariedad
    
    
class TvarCrear(SuccessMessageMixin, CreateView):
    model =Tvariedad
    form = Tvariedad
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leertvr') # Redireccionamos a la vista principal 'leer'

class TvarDetalle (DetailView):
    model =Tvariedad

class  TvarActualizar(SuccessMessageMixin,UpdateView):
    model =  Tvariedad
    form = Tvariedad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leertvr') # Redireccionamos a la vista principal 'leer'
class TvarEliminar(SuccessMessageMixin, DeleteView): 
    model = Tvariedad
    form = Tvariedad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertvr') # Redireccionamos a la vista principal 'leer'
    

    #----------------------------------Valorganancia------------------------------------------------------------------------------------------------------------------#

class ListadoValorg(ListView):
    model = Valorganancia
    
    
class ValorgCrear(SuccessMessageMixin, CreateView):
    model =Valorganancia
    form = Valorganancia
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervgc') # Redireccionamos a la vista principal 'leer'

class ValorgDetalle (DetailView):
    model =Valorganancia

class  ValorgActualizar(SuccessMessageMixin,UpdateView):
    model =  Valorganancia
    form = Valorganancia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervgc') # Redireccionamos a la vista principal 'leer'
class ValorgEliminar(SuccessMessageMixin, DeleteView): 
    model = Valorganancia
    form = Valorganancia
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervgc') # Redireccionamos a la vista principal 'leer'


    #----------------------------------Valorgasto------------------------------------------------------------------------------------------------------------------#

class ListadoVgasto(ListView):
    model = Valorgasto
    
    
class VgastoCrear(SuccessMessageMixin, CreateView):
    model =Valorgasto
    form = Valorgasto
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervgt') # Redireccionamos a la vista principal 'leer'

class VgastoDetalle (DetailView):
    model =Valorgasto

class  VgastoActualizar(SuccessMessageMixin,UpdateView):
    model =  Valorgasto
    form = Valorgasto
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervgt') # Redireccionamos a la vista principal 'leer'
class VgastoEliminar(SuccessMessageMixin, DeleteView): 
    model = Valorgasto
    form = Valorgasto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervgt') # Redireccionamos a la vista principal 'leer'


#----------------------------------Valorinversion------------------------------------------------------------------------------------------------------------------#

class ListadoVinver(ListView):
    model = Valorinversion
    
    
class VinverCrear(SuccessMessageMixin, CreateView):
    model =Valorinversion
    form = Valorinversion
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerviv') # Redireccionamos a la vista principal 'leer'

class VinverDetalle (DetailView):
    model =Valorinversion

class  VinverActualizar(SuccessMessageMixin,UpdateView):
    model =  Valorinversion
    form = Valorinversion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerviv') # Redireccionamos a la vista principal 'leer'
class VinverEliminar(SuccessMessageMixin, DeleteView): 
    model = Valorinversion
    form = Valorinversion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerviv') # Redireccionamos a la vista principal 'leer'
    
    
    
    #----------------------------------Valorperdida------------------------------------------------------------------------------------------------------------------#

class ListadoVperdida(ListView):
    model = Valorperdida
    
    
class VperdidaCrear(SuccessMessageMixin, CreateView):
    model =Valorperdida
    form = Valorperdida
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervpd') # Redireccionamos a la vista principal 'leer'

class VperdidaDetalle (DetailView):
    model =Valorperdida

class  VperdidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Valorperdida
    form = Valorperdida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervpd') # Redireccionamos a la vista principal 'leer'
class VperdidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Valorperdida
    form = Valorperdida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervpd') # Redireccionamos a la vista principal 'leer'
    
    
    
    
    
    #----------------------------------variedad------------------------------------------------------------------------------------------------------------------#

class ListadoVariedad(ListView):
    model = Variedad
    
    
class VariedadCrear(SuccessMessageMixin, CreateView):
    model =Variedad
    form = Variedad
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervvar') # Redireccionamos a la vista principal 'leer'

class VariedadDetalle (DetailView):
    model =Variedad

class  VariedadActualizar(SuccessMessageMixin,UpdateView):
    model =  Variedad
    form = Variedad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervvar') # Redireccionamos a la vista principal 'leer'
class VariedadEliminar(SuccessMessageMixin, DeleteView): 
    model = Variedad
    form = Variedad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervvar') # Redireccionamos a la vista principal 'leer'
    
    
    
    #----------------------------------Variedadgenetica------------------------------------------------------------------------------------------------------------------#

class ListadoVariedadgenetica(ListView):
    model = Variedadgenetica
    
    
class VariedadgeneticaCrear(SuccessMessageMixin, CreateView):
    model =Variedadgenetica
    form = Variedadgenetica
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervgen') # Redireccionamos a la vista principal 'leer'

class VariedadgeneticaDetalle (DetailView):
    model =Variedadgenetica

class  VariedadgeneticaActualizar(SuccessMessageMixin,UpdateView):
    model =  Variedadgenetica
    form = Variedadgenetica
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervgen') # Redireccionamos a la vista principal 'leer'
class VariedadgeneticaEliminar(SuccessMessageMixin, DeleteView): 
    model = Variedadgenetica
    form = Variedadgenetica
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervgen') # Redireccionamos a la vista principal 'leer'




 #----------------------------------Vistas------------------------------------------------------------------------------------------------------------------#

class ListadoVistas(ListView):
    model = Vistas
    
    
class VistasCrear(SuccessMessageMixin, CreateView):
    model =Vistas
    form = Vistas
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leervi') # Redireccionamos a la vista principal 'leer'

class VistasDetalle (DetailView):
    model =Vistas 

class  VistasActualizar(SuccessMessageMixin,UpdateView):
    model =  Vistas
    form = Vistas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leervi') # Redireccionamos a la vista principal 'leer'
class VistasEliminar(SuccessMessageMixin, DeleteView): 
    model = Vistas
    form = Vistas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leervi') # Redireccionamos a la vista principal 'leer'