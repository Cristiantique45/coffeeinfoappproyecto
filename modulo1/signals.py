#atravez de señales podemos crear perfiles del foro cuando se registra un usuario

from django.db.models.signals import post_save
from .models import Perfilforo, Registrarseforo
from django.dispatch import receiver


@receiver(post_save, sender=Registrarseforo)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfilforo.objects.create(registrarseforo_idregistroforo=instance)