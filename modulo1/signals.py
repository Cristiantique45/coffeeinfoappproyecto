#atravez de señales podemos crear perfiles del foro cuando se registra un usuario

from django.db.models.signals import post_save
from .models import Perfilforo, Imagen
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfilforo.objects.create(usuario=instance)
        
        
@receiver(post_save, sender=User)
def crear_imagen(sender, instance, created, **kwargs):
    if created:
        Imagen.objects.create(usuario=instance)