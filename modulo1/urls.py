"""coffeeinfoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[ 
    #--------------------------------------------------------------------Ainsecticida--------------------------------------------------------------------------------------#
     
    path('Ainsecticida/', ListadoAinsecticida.as_view(template_name = "crud/ainsecticida/index.html"), name='leera'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Ainsecticida/detalle/<int:pk>',AinsecticidaDetalle.as_view(template_name = "crud/ainsecticida/detalle.html"), name='detallesa'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Ainsecticida/crear/', AinsecticidaCrear.as_view(template_name = "crud/ainsecticida/crear.html"), name='creara'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Ainsecticida/editar/<int:pk>', AinsecticidaActualizar.as_view(template_name = "crud/ainsecticida/actualizar.html"), name='actualizara'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Ainsecticida/eliminar/<int:pk>', AinsecticidaEliminar.as_view(), name='crud/ainsecticida/eliminar.html'),    


    #--------------------------------------------------------Categoriaforo--------------------------------------------------------------------------------------#
    
    path('Categoriaforo/', ListadoCategoriaforo.as_view(template_name = "crud\categoriaforo\index.html"), name='leercf'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Categoriaforo/detalle/<int:pk>',CategoriaforoDetalle.as_view(template_name = "crud\categoriaforo\detalle.html"), name='detallescf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Categoriaforo/crear/', CategoriaforoCrear.as_view(template_name = "crud\categoriaforo\crear.html"), name='crearcf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Categoriaforo/editar/<int:pk>', CategoriaforoActualizar.as_view(template_name = "crud/categoriaforo/actualizar.html"), name='actualizarcf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Categoriaforo/eliminar/<int:pk>', CategoriaforoEliminar.as_view(), name='crud/categoriaforo/eliminar.html'),   

#------------------------------------------------------------------COMENTARIO------------------------------------------------------------------------------------------

    path('Comentario/',ListadoComentario.as_view(template_name = "crud/comentario/index.html"), name='leerco'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Comentario/detalle/<int:pk>',ComentarioDetalle.as_view(template_name = "crud/comentario/detalle.html"), name='detallesco'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Comentario/crear/', ComentarioCrear.as_view(template_name = "crud/comentario/crear.html"), name='crearco'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Comentario/editar/<int:pk>', ComentarioActualizar.as_view(template_name = "crud/comentario/actualizar.html"), name='actualizarco'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Comentario/eliminar/<int:pk>', ComentarioEliminar.as_view(), name='crud/comentario/eliminar.html'),   

    #--------------------------------------------------------Crearhiloforo--------------------------------------------------------------------------------------#
    
    path('ChiloF/', ListadoChiloF.as_view(template_name = "crud\crearhiloforo\index.html"), name='leerchf'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('ChiloF/detalle/<int:pk>',ChiloFDetalle.as_view(template_name = "crud\crearhiloforo\detalle.html"), name='detalleschf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('ChiloF/crear/', ChiloFCrear.as_view(template_name = "crud\crearhiloforo\crear.html"), name='crearchf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('ChiloF/editar/<int:pk>', ChiloFActualizar.as_view(template_name = "crud/crearhiloforo/actualizar.html"), name='actualizarchf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('ChiloF/eliminar/<int:pk>', ChiloFEliminar.as_view(), name='crud\crearhiloforo\eliminar.html'),   
    

    #----------------------------------------------------------------ENFERMEDADES-------------------------------------------------------------------------------------------------
     path('Enfermedades/', ListadoEnfermedades.as_view(template_name = "crud\enfermedades\index.html"), name='leeref'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Enfermedades/detalle/<int:pk>',EnfermedadesDetalle.as_view(template_name = "crud\enfermedades\detalle.html"), name='detallesef'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Enfermedades/crear/', EnfermedadesCrear.as_view(template_name = "crud\enfermedades\crear.html"), name='crearef'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Enfermedades/editar/<int:pk>', EnfermedadesActualizar.as_view(template_name = "crud/enfermedades/actualizar.html"), name='actualizaref'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Enfermedades/eliminar/<int:pk>', EnfermedadesEliminar.as_view(), name='crud\enfermedades\eliminar.html'),  
    
    
    
    
    #--------------------------------------------------------Foro--------------------------------------------------------------------------------------#

    path('LoginForo', foro_login, name='loginforo'),
    path('logoutforo', foro_logout, name='logoutforo'),

    path('Foro/', ListadoForo.as_view(template_name = "crud/foro/index.html"), name='leerfr'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Foro/detalle/<int:pk>',ForoDetalle.as_view(template_name = "crud/foro/detalle.html"), name='detallesfr'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Foro/crear/', ForoCrear.as_view(template_name = "crud/foro/crear.html"), name='crearfr'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Foro/editar/<int:pk>', ForoActualizar.as_view(template_name = "crud/foro/actualizar.html"), name='actualizarfr'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Foro/eliminar/<int:pk>', ForoEliminar.as_view(), name='crud/foro/eliminar.html'), 
        

    #--------------------------------------------------------Gastos--------------------------------------------------------------------------------------#
    
    path('Gastos/', ListadoGastos.as_view(template_name = "crud\gastos\index.html"), name='leer7'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Gastos/detalle/<int:pk>',GastosDetalle.as_view(template_name = "crud\gastos\detalle.html"), name='detalles7'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Gastos/crear/', GastosCrear.as_view(template_name = "crud\gastos\crear.html"), name='crear7'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Gastos/editar/<int:pk>', GastosActualizar.as_view(template_name = "crud/gastos/actualizar.html"), name='actualizar7'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Gastos/eliminar/<int:pk>', GastosEliminar.as_view(), name='crud\gastos\eliminar.html'), 


    #--------------------------------------------------------------Historial----------------------------------------------------------------------------#

    path('historial/', ListadoHistorial.as_view(template_name = "crud/historial/index.html"), name='leerh'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('historial/detalle/<int:pk>',HistorialDetalle.as_view(template_name = "crud\historial\detalle.html"), name='detallesh'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('historial/crear/', HistorialCrear.as_view(template_name = "crud\historial\crear.html"), name='crearh'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('historial/editar/<int:pk>', HistorialActualizar.as_view(template_name = "crud/historial/actualizar.html"), name='actualizarh'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('historial/eliminar/<int:pk>', HistorialEliminar.as_view(), name='crud\historial\eliminar.html'), 
    
    
    #--------------------------------------------------------------Imagen----------------------------------------------------------------------------#

    path('Imagen/', ListadoImagen.as_view(template_name = "crud/imagen/index.html"), name='leerimg'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Imagen/detalle/<int:pk>',ImagenDetalle.as_view(template_name = "crud\imagen\detalle.html"), name='detallesimg'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Imagen/crear/', ImagenCrear.as_view(template_name = "crud\imagen\crear.html"), name='crearimg'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Imagen/editar/<int:pk>', ImagenActualizar.as_view(template_name = "crud/imagen/actualizar.html"), name='actualizarimg'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Imagen/eliminar/<int:pk>', ImagenEliminar.as_view(), name='crud\imagen\eliminar.html'),
    
    
    
    #--------------------------------------------------------------Informacion cafe----------------------------------------------------------------------------#

    path('Informacion cafe/', ListadoInformacioncafe.as_view(template_name = "crud/informacioncafe/index.html"), name='leerinfo'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Informacion cafe/detalle/<int:pk>',InformacioncafeDetalle.as_view(template_name = "crud\informacioncafe\detalle.html"), name='detallesinfo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Informacion cafe/crear/', InformacioncafeCrear.as_view(template_name = "crud\informacioncafe\crear.html"), name='crearinfo'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Informacion cafe/editar/<int:pk>', InformacioncafeActualizar.as_view(template_name = "crud/informacioncafe/actualizar.html"), name='actualizarinfo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Informacion cafe/eliminar/<int:pk>', InformacioncafeEliminar.as_view(), name='crud\informacioncafe\eliminar.html'),
    
    
    #--------------------------------------------------------------Insecticidas----------------------------------------------------------------------------#

    path('Insecticida/', ListadoInsecticidas.as_view(template_name = "crud/insecticidas/index.html"), name='leerinsec'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Insecticida/detalle/<int:pk>',InsecticidasDetalle.as_view(template_name = "crud\insecticidas\detalle.html"), name='detallesinsec'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Insecticida/crear/', InsecticidasCrear.as_view(template_name = "crud\insecticidas\crear.html"), name='crearinsec'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Insecticida/editar/<int:pk>', InsecticidasActualizar.as_view(template_name = "crud/insecticidas/actualizar.html"), name='actualizarinsec'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Insecticida/eliminar/<int:pk>', InsecticidasEliminar.as_view(), name='crud\insecticidas\eliminar.html'),
    
    
    #--------------------------------------------------------------Inversión----------------------------------------------------------------------------#

    path('Inversion/', ListadoInversion.as_view(template_name = "crud/inversion/index.html"), name='leerinv'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Inversion/detalle/<int:pk>',InversionDetalle.as_view(template_name = "crud\inversion\detalle.html"), name='detallesinv'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Inversion/crear/', InversionCrear.as_view(template_name = "crud\inversion\crear.html"), name='crearinv'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Inversion/editar/<int:pk>', InversionActualizar.as_view(template_name = "crud/inversion/actualizar.html"), name='actualizarinv'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Inversion/eliminar/<int:pk>', InversionEliminar.as_view(), name='crud\inversion\eliminar.html'),
    
    
    #--------------------------------------------------------------Lote----------------------------------------------------------------------------#

    path('Lote/', ListadoLote.as_view(template_name = "crud/lote/index.html"), name='leerlot'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Lote/detalle/<int:pk>',LoteDetalle.as_view(template_name = "crud\lote\detalle.html"), name='detalleslot'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Lote/crear/', LoteCrear.as_view(template_name = "crud\lote\crear.html"), name='crearlot'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Lote/editar/<int:pk>', LoteActualizar.as_view(template_name = "crud/lote/actualizar.html"), name='actualizarlot'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Lote/eliminar/<int:pk>', LoteEliminar.as_view(), name='crud\lote\eliminar.html'),

    #---------------------------------------------------------MCONTROLENFERMEDADES---------------------------------------------------#
    
    path('Mcontrolenfermedad/', ListadoMcontrolenfermedad.as_view(template_name = "crud/mcontrolenfermedades/index.html"), name='leermce'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Mcontrolenfermedad/detalle/<int:pk>',McontrolenfermedadDetalle.as_view(template_name = "crud\mcontrolenfermedades\detalle.html"), name='detallesmce'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Mcontrolenfermedad/crear/', McontrolenfermedadCrear.as_view(template_name = "crud\mcontrolenfermedades\crear.html"), name='crearmce'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Mcontrolenfermedad/editar/<int:pk>', McontrolenfermedadActualizar.as_view(template_name = "crud/mcontrolenfermedades/actualizar.html"), name='actualizarmce'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Mcontrolenfermedad/eliminar/<int:pk>', McontrolenfermedadEliminar.as_view(), name='crud\mcontrolenfermedades\eliminar.html'),
    
    
         #--------------------------------------------------------mcontrolplagas--------------------------------------------------------------------------------------#
    
    
    path('McontrolP/', ListadoMcontrolplagas.as_view(template_name = "crud\mcontrolplagas\index.html"), name='leermcp'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('McontrolP/detalle/<int:pk>',McontrolplagasDetalle.as_view(template_name = "crud\mcontrolplagas\detalle.html"), name='detallemcp'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('McontrolP/crear/', McontrolplagasCrear.as_view(template_name = "crud\mcontrolplagas\crear.html"), name='crearmcp'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('McontrolP/editar/<int:pk>', McontrolplagasActualizar.as_view(template_name = "crud/mcontrolplagas/actualizar.html"), name='actualizarmcp'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('McontrolP/eliminar/<int:pk>', McontrolplagasEliminar.as_view(), name='crud\mcontrolplagas\eliminar.html'),   

    
    
    
    
     #--------------------------------------------------------Pcurativasenfer--------------------------------------------------------------------------------------#

    path('Pcuraenfermedad/', ListadoPcurativasenfer.as_view(template_name = "crud\pcurativasenfer\index.html"), name='leerpcuraenf'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Pcuraenfermedad/detalle/<int:pk>',PcurativasenferDetalle.as_view(template_name = "crud\pcurativasenfer\detalle.html"), name='detallespcuraenf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path(' (curaenfermedad/crear/', PcurativasenferCrear.as_view(template_name = "crud\pcurativasenfer\crear.html"), name='crearpcuraenf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Pcuraenfermedad/editar/<int:pk>', PcurativasenferActualizar.as_view(template_name = "crud/pcurativasenfer/actualizar.html"), name='actualizarpcuraenf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Pcuraenfermedad/eliminar/<int:pk>', PcurativasenferEliminar.as_view(), name='crud\pcurativasenfer\eliminar.html'), 
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
     #--------------------#------------------------------------Pcurativasplaga--------------------------------------------------------------------------------------#

    path('PcuraP/', ListadoPcuraP.as_view(template_name = "crud\pcurativasplaga\index.html"), name='leerp'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('PcuraP/detalle/<int:pk>',PcuraPDetalle.as_view(template_name = "crud\pcurativasplaga\detalle.html"), name='detallesp'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('PcuraP/crear/', PcuraPCrear.as_view(template_name = "crud\pcurativasplaga\crear.html"), name='crearp'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('PcuraP/editar/<int:pk>', PcuraPActualizar.as_view(template_name = "crud/pcurativasplaga/actualizar.html"), name='actualizarp'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('PcuraP/eliminar/<int:pk>', PcuraPEliminar.as_view(), name='crud\pcurativasplaga\eliminar.html'),    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
#--------------------------------------------------------perdidas--------------------------------------------------------------------------------------#

    path('Perdida/', ListadoPerdidas.as_view(template_name = "crud\perdidas\index.html"), name='leerper'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Perdida/detalle/<int:pk>',PerdidasDetalle.as_view(template_name = "crud\perdidas\detalle.html"), name='detallesper'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Perdida/crear/', PerdidasCrear.as_view(template_name = "crud\perdidas\crear.html"), name='crearper'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Perdida/editar/<int:pk>', PerdidasActualizar.as_view(template_name = "crud/perdidas/actualizar.html"), name='actualizarper'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Perdida/eliminar/<int:pk>', PerdidasEliminar.as_view(), name='crud\perdidas\eliminar.html'),    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
#--------------------------------------------------------PERFIL FORO--------------------------------------------------------------------------------------#

    path('Perfilforo/', ListadoPerfilforo.as_view(template_name = "crud/perfilforo/index.html"), name='leerpef'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Perfilforo/detalle/<int:pk>',PerfilforoDetalle.as_view(template_name = "crud\perfilforo\detalle.html"), name='detallespef'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Perfilforo/crear/', PerfilforoCrear.as_view(template_name = "crud\perfilforo\crear.html"), name='crearpef'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Perfilforo/editar/<int:pk>', PerfilforoActualizar.as_view(template_name = "crud/perfilforo/actualizar.html"), name='actualizarpef'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Perfilforo/eliminar/<int:pk>', PerfilforoEliminar.as_view(), name='crud\perfilforo\eliminar.html'),



#--------------------------------------------------------Perfilforo postforo--------------------------------------------------------------------------------------#

    path('Postperfil/', ListadoPerfilforopostforo.as_view(template_name = "crud\perfilpostforo\index.html"), name='leerpfpf'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Postperfil/detalle/<int:pk>',PerfilforopostforoDetalle.as_view(template_name = "crud\perfilpostforo\detalle.html"), name='detallespfpf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Postperfil/crear/', PerfilforopostforoCrear.as_view(template_name = "crud\perfilpostforo\crear.html"), name='crearpfpf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Postperfil/editar/<int:pk>', PerfilforopostforoActualizar.as_view(template_name = "crud/perfilpostforo/actualizar.html"), name='actualizarpfpf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Postperfil/eliminar/<int:pk>', PerfilforopostforoEliminar.as_view(), name='crud\perfilpostforo\eliminar.html'),
    
    
    
    
    #--------------------------------------------------------Persona--------------------------------------------------------------------------------------#

    path('Persona/', ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerperso'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Persona/detalle/<int:pk>',PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallesperso'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Persona/crear/', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crearpfpf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud/persona/actualizar.html"), name='actualizarperso'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='crud\persona\eliminar.html'),
    
    
    
    
    

    #-----------------------------------PERSONA INFO CAFE-------------------------------------------------------------#

    path('Personainfocafe/', ListadoPersonainfocafe.as_view(template_name = "crud/personainfocafe/index.html"), name='leermpic'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Personainfocafe/detalle/<int:pk>',PersonainfocafeDetalle.as_view(template_name = "crud\personainfocafe\detalle.html"), name='detallespic'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Personainfocafe/crear/', PersonainfocafeCrear.as_view(template_name = "crud\personainfocafe\crear.html"), name='crearpic'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Personainfocafe/editar/<int:pk>', PersonainfocafeActualizar.as_view(template_name = "crud/personainfocafe/actualizar.html"), name='actualizarpic'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Personainfocafe/eliminar/<int:pk>', PersonainfocafeEliminar.as_view(), name='crud\personainfocafe\eliminar.html'),
    
    


 #--------------------------------------------------------Plagas--------------------------------------------------------------------------------------#

    path('Plagas/', ListadoPlagas.as_view(template_name = "crud\plagas\index.html"), name='leerplg'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Plagas/detalle/<int:pk>', PlagasDetalle.as_view(template_name = "crud\plagas\detalle.html"), name='detallesplg'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Plagas/crear/', PlagasCrear.as_view(template_name = "crud\plagas\crear.html"), name='crearplg'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Plagas/editar/<int:pk>', PlagasActualizar.as_view(template_name = "crud/plagas/actualizar.html"), name='actualizarplg'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Plagas/eliminar/<int:pk>', PlagasEliminar.as_view(), name='crud\plagas\eliminar.html'), 


    #---------------------------------------------------------POST FORO---------------------------------------------------#
    
    path('Postforo/', ListadoPostforo.as_view(template_name = "crud/postforo/index.html"), name='leerpof'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Postforo/detalle/<int:pk>',PostforoDetalle.as_view(template_name = "crud\postforo\detalle.html"), name='detallespof'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Postforo/crear/', PostforoCrear.as_view(template_name = "crud\postforo\crear.html"), name='crearpof'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Postforo/editar/<int:pk>', PostforoActualizar.as_view(template_name = "crud/postforo/actualizar.html"), name='actualizarpof'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Postforo/eliminar/<int:pk>', PostforoEliminar.as_view(), name='crud\postforo\eliminar.html'),
    
    
    
    #---------------------------------------------------------ppreventiva enfer---------------------------------------------------#
    
    path('Pprevenenfer/', ListadoPpreventivaenfer.as_view(template_name = "crud/ppreventivaenfer/index.html"), name='leerppenf'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Pprevenenfer/detalle/<int:pk>',PpreventivaenferDetalle.as_view(template_name = "crud\ppreventivaenfer\detalle.html"), name='detallesppenf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Pprevenenfer/crear/', PpreventivaenferCrear.as_view(template_name = "crud\ppreventivaenfer\crear.html"), name='crearppenf'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Pprevenenfer/editar/<int:pk>', PpreventivaenferActualizar.as_view(template_name = "crud/ppreventivaenfer/actualizar.html"), name='actualizarppenf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Pprevenenfer/eliminar/<int:pk>', PpreventivaenferEliminar.as_view(), name='crud\ppreventivaenfer\eliminar.html'),
    
    
    
    #---------------------------------------------------------ppreventiva plaga---------------------------------------------------#
    
    path('Pprevenplaga/', ListadoPpreventivasplaga.as_view(template_name = "crud/ppreventivasplaga/index.html"), name='leerpprep'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Pprevenplaga/detalle/<int:pk>',PpreventivasplagaDetalle.as_view(template_name = "crud\ppreventivasplaga\detalle.html"), name='detallespprep'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Pprevenplaga/crear/', PpreventivasplagaCrear.as_view(template_name = "crud\ppreventivasplaga\crear.html"), name='crearpprep'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Pprevenplaga/editar/<int:pk>', PpreventivasplagaActualizar.as_view(template_name = "crud/ppreventivasplaga/actualizar.html"), name='actualizarpprep'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Pprevenplaga/eliminar/<int:pk>', PpreventivasplagaEliminar.as_view(), name='crud\ppreventivasplaga\eliminar.html'),
    
    
    
    #---------------------------------------------------------reaccion post---------------------------------------------------#
    
    path('Reaccionpost/', ListadoReaccionpost.as_view(template_name = "crud/reaccionpost/index.html"), name='leerrp'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Reaccionpost/detalle/<int:pk>',ReaccionpostDetalle.as_view(template_name = "crud/reaccionpost/detalle.html"), name='detallesrp'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Reaccionpost/crear/', ReaccionpostCrear.as_view(template_name = "crud/reaccionpost/crear.html"), name='crearrp'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Reaccionpost/editar/<int:pk>', ReaccionpostActualizar.as_view(template_name = "crud/reaccionpost/actualizar.html"), name='actualizarrp'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Reaccionpost/eliminar/<int:pk>', ReaccionpostEliminar.as_view(), name='crud/reaccionpost/eliminar.html'),
    
    
    
    #---------------------------------------------------------recomendacion insect---------------------------------------------------#
    
    path('Recomeninsect/', ListadoRecomendacioninsect.as_view(template_name = "crud/recomendacioninsect/index.html"), name='leerri'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Recomeninsect/detalle/<int:pk>',RecomendacioninsectDetalle.as_view(template_name = "crud/recomendacioninsect/detalle.html"), name='detallesri'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Recomeninsect/crear/', RecomendacioninsectCrear.as_view(template_name = "crud/recomendacioninsect/crear.html"), name='crearri'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Recomeninsect/editar/<int:pk>', RecomendacioninsectActualizar.as_view(template_name = "crud/recomendacioninsect/actualizar.html"), name='actualizarri'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Recomeninsect/eliminar/<int:pk>', RecomendacioninsectEliminar.as_view(), name='crud/recomendacioninsect/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------recomendacion plaga---------------------------------------------------#
    
    path('Recomenplaga/', ListadoRecomendacionplaga.as_view(template_name = "crud/recomendacionplaga/index.html"), name='leerrplg'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Recomenplaga/detalle/<int:pk>',RecomendacionplagaDetalle.as_view(template_name = "crud/recomendacionplaga/detalle.html"), name='detallesrplg'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Recomenplaga/crear/', RecomendacionplagaCrear.as_view(template_name = "crud/recomendacionplaga/crear.html"), name='crearrplg'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Recomenplaga/editar/<int:pk>', RecomendacionplagaActualizar.as_view(template_name = "crud/recomendacionplaga/actualizar.html"), name='actualizarrplg'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Recomenplaga/eliminar/<int:pk>', RecomendacionplagaEliminar.as_view(), name='crud/recomendacionplaga/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------Registrarse foro---------------------------------------------------#
    
    #path('Registroforo/', ListadoRegistrarseforo.as_view(template_name = "crud/registrarseforo/index.html"), name='leerrefo'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    #path('Registroforo/detalle/<int:pk>',RegistrarseforoDetalle.as_view(template_name = "crud/registrarseforo/detalle.html"), name='detallesrefo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Registroforo/crear/', RegistrarseforoCrear.as_view(template_name = "crud/registrarseforo/crear.html"), name='crearrefo'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Registroforo/editar/<int:pk>', RegistrarseforoActualizar.as_view(template_name = "crud/registrarseforo/actualizar.html"), name='actualizarrefo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Registroforo/eliminar/<int:pk>', RegistrarseforoEliminar.as_view(), name='crud/registrarseforo/eliminar.html'),
    
    
    
     #---------------------------------------------------------Registrarseforo perfilforo---------------------------------------------------#
    
    #path('Regfperff/', ListadoRegistrarseforoperfilforo.as_view(template_name = "crud/registrarseforoperfilforo/index.html"), name='leerrfpf'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    #path('Regfperff/detalle/<int:pk>',RegistrarseforoperfilforoDetalle.as_view(template_name = "crud/registrarseforoperfilforo/detalle.html"), name='detallesrfpf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('Regfperff/crear/', RegistrarseforoperfilforoCrear.as_view(template_name = "crud/registrarseforoperfilforo/crear.html"), name='crearrfpf'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    #path('Regfperff/editar/<int:pk>', RegistrarseforoperfilforoActualizar.as_view(template_name = "crud/registrarseforoperfilforo/actualizar.html"), name='actualizarrfpf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    #path('Regfperff/eliminar/<int:pk>', RegistrarseforoperfilforoEliminar.as_view(), name='crud/registrarseforoperfilforo/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------rfinanciero---------------------------------------------------#
    
    path('Reporfinan/', ListadoRfinanciero.as_view(template_name = "crud/rfinanciero/index.html"), name='leerrefinan'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Reporfinan/detalle/<int:pk>',RfinancieroDetalle.as_view(template_name = "crud/rfinanciero/detalle.html"), name='detallesrefinan'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Reporfinan/crear/', RfinancieroCrear.as_view(template_name = "crud/rfinanciero/crear.html"), name='crearrefinan'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Reporfinan/editar/<int:pk>', RfinancieroActualizar.as_view(template_name = "crud/rfinanciero/actualizar.html"), name='actualizarrefinan'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Reporfinan/eliminar/<int:pk>', RfinancieroEliminar.as_view(), name='crud/rfinanciero/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------rfinanciero lote---------------------------------------------------#
    
    path('Repofinanlote/', ListadoRfinancierolote.as_view(template_name = "crud/rfinancierolote/index.html"), name='leerrefilo'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Repofinanlote/detalle/<int:pk>',RfinancieroloteDetalle.as_view(template_name = "crud/rfinancierolote/detalle.html"), name='detallesrefilo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Repofinanlote/crear/', RfinancieroloteCrear.as_view(template_name = "crud/rfinancierolote/crear.html"), name='crearrefilo'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Repofinanlote/editar/<int:pk>', RfinancieroloteActualizar.as_view(template_name = "crud/rfinancierolote/actualizar.html"), name='actualizarrefilo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Repofinanlote/eliminar/<int:pk>', RfinancieroloteEliminar.as_view(), name='crud/rfinancierolote/eliminar.html'),
    
    
    
    
    
    #---------------------------------------------------------Tema foro---------------------------------------------------#
    
    path('Tema/', ListadoTemaforo.as_view(template_name = "crud/temaforo/index.html"), name='leertefo'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tema/detalle/<int:pk>',TemaforoDetalle.as_view(template_name = "crud/temaforo/detalle.html"), name='detallestefo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tema/crear/', TemaforoCrear.as_view(template_name = "crud/temaforo/crear.html"), name='creartefo'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tema/editar/<int:pk>', TemaforoActualizar.as_view(template_name = "crud/temaforo/actualizar.html"), name='actualizartefo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tema/eliminar/<int:pk>', TemaforoEliminar.as_view(), name='crud/temaforo/eliminar.html'),
    
    
    
    #---------------------------------------------------------tenfermedad---------------------------------------------------#
    
    path('Tenfermedad/', ListadoTenfermedad.as_view(template_name = "crud/tenfermedad/index.html"), name='leertenfe'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tenfermedad/detalle/<int:pk>',TenfermedadDetalle.as_view(template_name = "crud/tenfermedad/detalle.html"), name='detallestenfe'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tenfermedad/crear/', TenfermedadCrear.as_view(template_name = "crud/tenfermedad/crear.html"), name='creartenfe'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tenfermedad/editar/<int:pk>', TenfermedadActualizar.as_view(template_name = "crud/tenfermedad/actualizar.html"), name='actualizartenfe'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tenfermedad/eliminar/<int:pk>', TenfermedadEliminar.as_view(), name='crud/tenfermedad/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------tgastos---------------------------------------------------#
    
    path('Tgasto/', ListadoTgastos.as_view(template_name = "crud/tgastos/index.html"), name='leertgst'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tgasto/detalle/<int:pk>',TgastosDetalle.as_view(template_name = "crud/tgastos/detalle.html"), name='detallestgst'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tgasto/crear/', TgastosCrear.as_view(template_name = "crud/tgastos/crear.html"), name='creartgst'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tgasto/editar/<int:pk>', TgastosActualizar.as_view(template_name = "crud/tgastos/actualizar.html"), name='actualizartgst'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tgasto/eliminar/<int:pk>', TgastosEliminar.as_view(), name='crud/tgastos/eliminar.html'),
    
    
    
    
    
    #---------------------------------------------------------tinsecticida---------------------------------------------------#
    
    path('Tinsec/', ListadoTinsecticida.as_view(template_name = "crud/tinsecticida/index.html"), name='leertinsec'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tinsec/detalle/<int:pk>',TinsecticidaDetalle.as_view(template_name = "crud/tinsecticida/detalle.html"), name='detallestinsec'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tinsec/crear/', TinsecticidaCrear.as_view(template_name = "crud/tinsecticida/crear.html"), name='creartinsec'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tinsec/editar/<int:pk>', TinsecticidaActualizar.as_view(template_name = "crud/tinsecticida/actualizar.html"), name='actualizartinsec'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tinsec/eliminar/<int:pk>', TinsecticidaEliminar.as_view(), name='crud/tinsecticida/eliminar.html'),


#---------------------------------------------------------tinversion---------------------------------------------------#
    
    path('Tinversion/', ListadoTinversion.as_view(template_name = "crud/tinversion/index.html"), name='leertinver'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tinversion/detalle/<int:pk>',TinversionDetalle.as_view(template_name = "crud/tinversion/detalle.html"), name='detallestinver'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tinversion/crear/', TinversionCrear.as_view(template_name = "crud/tinversion/crear.html"), name='creartinver'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tinversion/editar/<int:pk>', TinversionActualizar.as_view(template_name = "crud/tinversion/actualizar.html"), name='actualizartinver'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tinversion/eliminar/<int:pk>', TinversionEliminar.as_view(), name='crud/tinversion/eliminar.html'),
    
    
    
    
    #---------------------------------------------------------tperdida---------------------------------------------------#
    
    path('Tperdida/', ListadoTperdida.as_view(template_name = "crud/tperdida/index.html"), name='leertperd'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tperdida/detalle/<int:pk>',TperdidaDetalle.as_view(template_name = "crud/tperdida/detalle.html"), name='detallestperd'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tperdida/crear/', TperdidaCrear.as_view(template_name = "crud/tperdida/crear.html"), name='creartperd'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tperdida/editar/<int:pk>', TperdidaActualizar.as_view(template_name = "crud/tperdida/actualizar.html"), name='actualizartperd'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tperdida/eliminar/<int:pk>', TperdidaEliminar.as_view(), name='crud/tperdida/eliminar.html'),
    
    
    
    
    
    
    #---------------------------------------------------------tpersona---------------------------------------------------#
    
    path('Tpersona/', ListadoTpersona.as_view(template_name = "crud/tipopersona/index.html"), name='leertperso'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tpersona/detalle/<int:pk>',TpersonaDetalle.as_view(template_name = "crud/tipopersona/detalle.html"), name='detallestperso'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tpersona/crear/', TpersonaCrear.as_view(template_name = "crud/tipopersona/crear.html"), name='creartperso'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tpersona/editar/<int:pk>', TpersonaActualizar.as_view(template_name = "crud/tipopersona/actualizar.html"), name='actualizartperso'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tpersona/eliminar/<int:pk>', TpersonaEliminar.as_view(), name='crud/tipopersona/eliminar.html'),


    #--------------------------------------------------------Tratamiento--------------------------------------------------------------------------------------#
    
    path('Tratamiento/', ListadoTratamiento.as_view(template_name = "crud/tratamiento/index.html"), name='leertrt'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tratamiento/detalle/<int:pk>',TratamientoDetalle.as_view(template_name = "crud/tratamiento/detalle.html"), name='detalletrt'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tratamiento/crear/', TratamientoCrear.as_view(template_name = "crud/tratamiento/crear.html"), name='creartrt'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tratamiento/editar/<int:pk>', TratamientoActualizar.as_view(template_name = "crud/tratamiento/actualizar.html"), name='actualizartrt'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tratamiento/eliminar/<int:pk>', TratamientoEliminar.as_view(), name='crud/tratamiento/eliminar.html'),   
    
    
    #--------------------------------------------------------tusuarioforo--------------------------------------------------------------------------------------#
    
    path('TUFo/', ListadoTUFo.as_view(template_name = "crud/tusuarioforo/index.html"), name='leertuf'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('TUFo/detalle/<int:pk>',TUFoDetalle.as_view(template_name = "crud/tusuarioforo/detalle.html"), name='detalletuf'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('TUFo/crear/', TUFoCrear.as_view(template_name = "crud/tusuarioforo/crear.html"), name='creartuf'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('TUFo/editar/<int:pk>', TUFoActualizar.as_view(template_name = "crud/tusuarioforo/actualizar.html"), name='actualizartuf'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('TUFo/eliminar/<int:pk>', TUFoEliminar.as_view(), name='crud/tusuarioforo/eliminar.html'), 


    #--------------------------------------------------------Tvariedad--------------------------------------------------------------------------------------#
    
    path('Tvar/', ListadoTvar.as_view(template_name = "crud/tvariedad/index.html"), name='leertvr'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Tvar/detalle/<int:pk>',TvarDetalle.as_view(template_name = "crud/tvariedad/detalle.html"), name='detalletvr'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Tvar/crear/', TvarCrear.as_view(template_name = "crud/tvariedad/crear.html"), name='creartvr'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Tvar/editar/<int:pk>', TvarActualizar.as_view(template_name = "crud/tvariedad/actualizar.html"), name='actualizartvr'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Tvar/eliminar/<int:pk>', TvarEliminar.as_view(), name='crud/tvariedad/eliminar.html'), 


    #--------------------------------------------------------Valorganancia--------------------------------------------------------------------------------------#
    
    path('Valorg/', ListadoValorg.as_view(template_name = "crud/valorganancia/index.html"), name='leervgc'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Valorg/detalle/<int:pk>',ValorgDetalle.as_view(template_name = "crud/valorganancia/detalle.html"), name='detallevgc'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Valorg/crear/', ValorgCrear.as_view(template_name = "crud/valorganancia/crear.html"), name='crearvgc'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Valorg/editar/<int:pk>', ValorgActualizar.as_view(template_name = "crud/valorganancia/actualizar.html"), name='actualizarvgc'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Valorg/eliminar/<int:pk>', ValorgEliminar.as_view(), name='crud/valorganancia/eliminar.html'), 

    
        #--------------------------------------------------------Valorgasto--------------------------------------------------------------------------------------#
    
    path('Vgasto/', ListadoVgasto.as_view(template_name = "crud/valorgasto/index.html"), name='leervgt'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Vgasto/detalle/<int:pk>',VgastoDetalle.as_view(template_name = "crud/valorgasto/detalle.html"), name='detallevgt'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Vgasto/crear/', VgastoCrear.as_view(template_name = "crud/valorgasto/crear.html"), name='crearvgt'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Vgasto/editar/<int:pk>', VgastoActualizar.as_view(template_name = "crud/valorgasto/actualizar.html"), name='actualizarvgt'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Vgasto/eliminar/<int:pk>', VgastoEliminar.as_view(), name='crud/valorgasto/eliminar.html'), 
    
    
        #--------------------------------------------------------Valorinversion--------------------------------------------------------------------------------------#
    
    path('Vinver/', ListadoVinver.as_view(template_name = "crud/valorinversion/index.html"), name='leerviv'),
    
    # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
    path('Vinver/detalle/<int:pk>',VinverDetalle.as_view(template_name = "crud/valorinversion/detalle.html"), name='detalleviv'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Vinver/crear/', VinverCrear.as_view(template_name = "crud/valorinversion/crear.html"), name='crearviv'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Vinver/editar/<int:pk>', VinverActualizar.as_view(template_name = "crud/valorinversion/actualizar.html"), name='actualizarviv'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Vinver/eliminar/<int:pk>', VinverEliminar.as_view(), name='crud/valorinversion/eliminar.html'), 
    
    
    
    #--------------------#------------------------------------valorperdida--------------------------------------------------------------------------------------#

    path('Vperdida/', ListadoVperdida.as_view(template_name = "crud/valorperdida/index.html"), name='leervpd'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Vperdida/detalle/<int:pk>',VperdidaDetalle.as_view(template_name = "crud/valorperdida/detalle.html"), name='detallevpd'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Vperdida/crear/', VperdidaCrear.as_view(template_name = "crud/valorperdida/crear.html"), name='crearvpd'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Vperdida/editar/<int:pk>', VperdidaActualizar.as_view(template_name = "crud/valorperdida/actualizar.html"), name='actualizarvpd'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Vperdida/eliminar/<int:pk>', VperdidaEliminar.as_view(), name='crud/valorperdida/eliminar.html'),
    
    
    
    
    #--------------------#------------------------------------Variedad--------------------------------------------------------------------------------------#

    path('Variedad/', ListadoVariedad.as_view(template_name = "crud/variedad/index.html"), name='leervvar'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Variedad/detalle/<int:pk>',VariedadDetalle.as_view(template_name = "crud/variedad/detalle.html"), name='detallesvvar'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Variedad/crear/', VariedadCrear.as_view(template_name = "crud/variedad/crear.html"), name='crearvvar'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Variedad/editar/<int:pk>', VariedadActualizar.as_view(template_name = "crud/variedad/actualizar.html"), name='actualizarvvar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Variedad/eliminar/<int:pk>', VariedadEliminar.as_view(), name='crud/variedad/eliminar.html'),
    
    
    
    #--------------------#------------------------------------Variedadgenetica--------------------------------------------------------------------------------------#

    path('Vgenet/', ListadoVariedadgenetica.as_view(template_name = "crud/variedadgenetica/index.html"), name='leervgen'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Vgenet/detalle/<int:pk>',VariedadgeneticaDetalle.as_view(template_name = "crud/variedadgenetica/detalle.html"), name='detallesvgen'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Vgenet/crear/', VariedadgeneticaCrear.as_view(template_name = "crud/variedadgenetica/crear.html"), name='crearvgen'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Vgenet/editar/<int:pk>', VariedadgeneticaActualizar.as_view(template_name = "crud/variedadgenetica/actualizar.html"), name='actualizarvgen'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Vgenet/eliminar/<int:pk>', VariedadgeneticaEliminar.as_view(), name='crud/variedadgenetica/eliminar.html'),
    
    
    
    
    
    #--------------------------------------------------------Vistas--------------------------------------------------------------------------------------#

    path('Vistas/', ListadoVistas.as_view(template_name = "crud/vistas/index.html"), name='leervi'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('Vistas/detalle/<int:pk>',VistasDetalle.as_view(template_name = "crud/vistas/detalle.html"), name='detallesvi'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Vistas/crear/', VistasCrear.as_view(template_name = "crud/vistas/crear.html"), name='crearvi'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Vistas/editar/<int:pk>', VistasActualizar.as_view(template_name = "crud/vistas/actualizar.html"), name='actualizarvi'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Vistas/eliminar/<int:pk>', VistasEliminar.as_view(), name='crud\vistas\eliminar.html'),   

]
