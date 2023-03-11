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
from django.urls import path, include
from modulo1.views import *
from django.contrib.auth.views import LoginView, LogoutView #password_reset, password_reset_done, password_reset_cofirm, password_reset_complete
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    #------------------------------login---------------------------------#
    
    path('accounts/', include('django.contrib.auth.urls')),

    path('', Login_request, name="login"),
    path('logout/', logout_request, name="logout"),


    path('admin/', admin.site.urls),
    path('modulo1/',include(('modulo1.urls','modulo1'))),
    
    path('home/', Home, name= 'index'),

    path('contacto/', contacto, name= 'contacto'),
     
    #----------------------------------registro-----------------------------------------------

    
    path('Registro/', registro, name='registrarse'),
    
    #----------------------------------------recuperar contraseña--------------------------------
    #path(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html',
        #'email_template_name':'registration/password_reset_email.html'}, 
        #name='password_reset'),
    #path(r'^reset/password_reset_done', password_reset_done, {'template_name':'registration/password_reset_done.html'},
        #name='password_reset_done'),
    #path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_cofirm, {'template_name':'registration/password_reset_confirm.html'},
        #name=password_reset_cofirm
        #),
    #path(r'^reset/done', password_reset_complete, {'template_name':'registration/password_reset_complete.html'},
        #name='password_reset_complete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
