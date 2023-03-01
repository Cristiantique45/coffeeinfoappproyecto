from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password as auth_check_password
from .models import Registrarseforo


class RegistrarseForoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            usuario = Registrarseforo.objects.get(nombre=username)
            if usuario.check_password(password) and usuario.is_active:
                return usuario
        except Registrarseforo.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Registrarseforo.objects.get(pk=user_id)
        except Registrarseforo.DoesNotExist:
            return None