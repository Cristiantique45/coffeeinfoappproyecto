# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
import os
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password as auth_check_password
from django.contrib.auth.models import User


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Ainsecticida(models.Model):
    idainsecticida = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    insecticidas_idinsecticida = models.ForeignKey('Insecticidas', models.DO_NOTHING, db_column='insecticidas_idinsecticida')

    class Meta:
        managed = False
        db_table = 'ainsecticida'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoriaforo(models.Model):
    idcategoriaforo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'Categoria: {self.nombre}'

    class Meta:
        managed = False
        db_table = 'categoriaforo'


class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    comentario = models.TextField()
    fechahoracoment = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    imagen_idimagen = models.ForeignKey('Imagen', models.DO_NOTHING, db_column='imagen_idimagen')
    perfilforo_idperfilforo = models.ForeignKey('Perfilforo', models.DO_NOTHING, db_column='perfilforo_idperfilforo')
    temaforo_idtemaforo = models.ForeignKey('Temaforo', models.DO_NOTHING, db_column='temaforo_idtemaforo')
    
    def __str__(self):
        return f'{self.usuario} -> {self.comentario}'

#la clase meta nos dice como se va comportar esa clase
    class Meta:
        #ordering nos ayuda a tener un orden ascedente
        ordering = ['-fechahoracoment']
        managed = False
        db_table = 'comentario'


class Crearhiloforo(models.Model):
    idcrearhilo = models.AutoField(primary_key=True)
    hilo = models.CharField(max_length=60)
    perfilforo_idperfilforo = models.ForeignKey('Perfilforo', models.DO_NOTHING, db_column='perfilforo_idperfilforo')

    class Meta:
        managed = False
        db_table = 'crearhiloforo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Enfermedades(models.Model):
    idenfermedades = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=120, blank=True, null=True)
    descripcion = models.TextField()
    sintomas = models.TextField()
    danios = models.TextField()
    cfavorecen = models.TextField()
    deconomicos = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermedades'


class Foro(models.Model):
    idforo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    categoriaforo_idcategoriaforo = models.ForeignKey(Categoriaforo, models.DO_NOTHING, db_column='categoriaforo_idcategoriaforo')
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        managed = False
        db_table = 'foro'


class Gastos(models.Model):
    idgastos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    unidad = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastos'


class Historial(models.Model):
    idhistorial = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = False
        db_table = 'historial'


class Imagen(models.Model):
    idimagen = models.AutoField(primary_key=True)
    fechahoraimg = models.DateTimeField(default=timezone.now)
    encabezado = models.CharField(max_length=55, blank=True, null=True)
    imagen = models.ImageField(max_length=120, blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    
    def __str__(self):
        return f'Encabezado: {self.encabezado}'

    class Meta:
        managed = False
        db_table = 'imagen'


class Informacioncafe(models.Model):
    idinformacioncafe = models.AutoField(primary_key=True)
    tratamiento_idtratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='tratamiento_idtratamiento')
    plagas_idplagas = models.ForeignKey('Plagas', models.DO_NOTHING, db_column='plagas_idplagas')
    enfermedades_idenfermedades = models.ForeignKey(Enfermedades, models.DO_NOTHING, db_column='enfermedades_idenfermedades')
    insecticidas_idinsecticida = models.ForeignKey('Insecticidas', models.DO_NOTHING, db_column='insecticidas_idinsecticida')
    variedad_idvariedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='variedad_idvariedad')

    class Meta:
        managed = False
        db_table = 'informacioncafe'


class Insecticidas(models.Model):
    idinsecticida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=120)
    ingredientes = models.TextField(blank=True, null=True)
    descripcion = models.TextField()
    beneficios = models.TextField()
    dosis = models.CharField(max_length=45, blank=True, null=True)
    rnacional = models.TextField()
    tformulacion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'insecticidas'


class Inversion(models.Model):
    idinversion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=55)
    vidautil = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inversion'


class Lote(models.Model):
    idlote = models.AutoField(primary_key=True)
    nombrelote = models.CharField(max_length=45)
    hectarea = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lote'


class Mcontrolenfermedad(models.Model):
    idmetodosenfer = models.AutoField(primary_key=True)
    enfermedades_idenfermedades = models.ForeignKey(Enfermedades, models.DO_NOTHING, db_column='enfermedades_idenfermedades')

    class Meta:
        managed = False
        db_table = 'mcontrolenfermedad'


class Mcontrolplagas(models.Model):
    idmetodosplagas = models.AutoField(primary_key=True)
    plagas_idplagas = models.ForeignKey('Plagas', models.DO_NOTHING, db_column='plagas_idplagas')

    class Meta:
        managed = False
        db_table = 'mcontrolplagas'


class Pcurativasenfer(models.Model):
    idpcurativasenfer = models.AutoField(primary_key=True)
    controlquimico = models.TextField()
    mcontrolenfermedad_idmetodosenfer = models.ForeignKey(Mcontrolenfermedad, models.DO_NOTHING, db_column='mcontrolenfermedad_idmetodosenfer')

    class Meta:
        managed = False
        db_table = 'pcurativasenfer'


class Pcurativasplaga(models.Model):
    idpcurativasplaga = models.AutoField(primary_key=True)
    controlquimico = models.TextField()
    mcontrolplagas_idmetodosplagas = models.ForeignKey(Mcontrolplagas, models.DO_NOTHING, db_column='mcontrolplagas_idmetodosplagas')

    class Meta:
        managed = False
        db_table = 'pcurativasplaga'


class Perdidas(models.Model):
    idperdidas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    unidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perdidas'
        
#esto guarda la imagen que subimos, en la carpeta usuario, crea una carpeta con el nombre del usuario
#y dentro la imagen que subio de su perfil

def directorio_user_path_perfil(instance, filename):
    nombre_imagen = 'usuario/{0}/perfil.png'.format(instance.usuario.username)
    #donde vamos a guardar ese archivo
    full_path = os.path.join(settings.MEDIA_ROOT, nombre_imagen)
        
    if os.path.exists(full_path):
        os.remove(full_path)
            
    return nombre_imagen
#upload_to=directorio_user_path_perfil,


class Perfilforo(models.Model):
    idperfilforo = models.AutoField(primary_key=True)
    fnacimiento = models.DateField(blank=True, null=True)
    intereses = models.TextField(blank=True, null=True)
    fotoperfil = models.ImageField(default='logocoffee.png', upload_to=directorio_user_path_perfil)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    
    def __str__(self):
        return f'Perfil de {self.usuario}'

    class Meta:
        managed = False
        db_table = 'perfilforo'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombre1 = models.CharField(max_length=45)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=45)
    fechanacimiento = models.DateField()
    foro_idforo = models.ForeignKey(Foro, models.DO_NOTHING, db_column='foro_idforo')

    class Meta:
        managed = False
        db_table = 'persona'


class Personainfocafe(models.Model):
    idpersonainfocafe = models.AutoField(primary_key=True)
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_idpersona')
    informacioncafe_idinformacioncafe = models.ForeignKey(Informacioncafe, models.DO_NOTHING, db_column='informacioncafe_idinformacioncafe')

    class Meta:
        managed = False
        db_table = 'personainfocafe'


class Plagas(models.Model):
    idplagas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    danios = models.TextField()
    imagen = models.TextField()
    deconomicos = models.TextField()
    cfavorecen = models.TextField()

    class Meta:
        managed = False
        db_table = 'plagas'


class Ppreventivaenfer(models.Model):
    idppreventivaenfer = models.AutoField(primary_key=True)
    controlcultural = models.TextField()
    controlbiologico = models.TextField()
    controlfisico = models.TextField()
    mcontrolenfermedad_idmetodosenfer = models.ForeignKey(Mcontrolenfermedad, models.DO_NOTHING, db_column='mcontrolenfermedad_idmetodosenfer')

    class Meta:
        managed = False
        db_table = 'ppreventivaenfer'


class Ppreventivasplaga(models.Model):
    idppreventivasplaga = models.AutoField(primary_key=True)
    controlcultural = models.TextField()
    controlbiologico = models.TextField()
    controlfisico = models.TextField()
    mcontrolplagas_idmetodosplagas = models.ForeignKey(Mcontrolplagas, models.DO_NOTHING, db_column='mcontrolplagas_idmetodosplagas')

    class Meta:
        managed = False
        db_table = 'ppreventivasplaga'


class Reaccionpost(models.Model):
    idreaccionpost = models.AutoField(primary_key=True)
    tiporeaccion = models.CharField(max_length=4, blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    comentario_idcomentario = models.ForeignKey(Comentario, models.DO_NOTHING, db_column='comentario_idcomentario')

    class Meta:
        managed = False
        db_table = 'reaccionpost'


class Recomendacioninsect(models.Model):
    idrecomendainsect = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    insecticidas_idinsecticida = models.ForeignKey(Insecticidas, models.DO_NOTHING, db_column='insecticidas_idinsecticida')

    class Meta:
        managed = False
        db_table = 'recomendacioninsect'


class Recomendacionplaga(models.Model):
    idrecomendaplaga = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    plagas_idplagas = models.ForeignKey(Plagas, models.DO_NOTHING, db_column='plagas_idplagas')

    class Meta:
        managed = False
        db_table = 'recomendacionplaga'


class Rfinanciero(models.Model):
    idrfinanciero = models.AutoField(primary_key=True)
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_idpersona')
    gastos_idgastos = models.ForeignKey(Gastos, models.DO_NOTHING, db_column='gastos_idgastos')
    inversion_idinversion = models.ForeignKey(Inversion, models.DO_NOTHING, db_column='inversion_idinversion')
    perdidas_idperdidas = models.ForeignKey(Perdidas, models.DO_NOTHING, db_column='perdidas_idperdidas')
    valorganancia_idvalorganancia = models.ForeignKey('Valorganancia', models.DO_NOTHING, db_column='valorganancia_idvalorganancia')

    class Meta:
        managed = False
        db_table = 'rfinanciero'


class Rfinancierolote(models.Model):
    idfinancierolote = models.AutoField(primary_key=True)
    rfinanciero_idrfinanciero = models.ForeignKey(Rfinanciero, models.DO_NOTHING, db_column='rfinanciero_idrfinanciero')
    lote_idlote = models.ForeignKey(Lote, models.DO_NOTHING, db_column='lote_idlote')

    class Meta:
        managed = False
        db_table = 'rfinancierolote'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Temaforo(models.Model):
    idtemaforo = models.AutoField(primary_key=True)
    nombre = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    foro_idforo = models.ForeignKey(Foro, models.DO_NOTHING, db_column='foro_idforo')
    def __str__(self):
        return f'Tema de: {self.usuario} : {self.nombre}'

    class Meta:
        ordering = ['-idtemaforo']
        managed = False
        db_table = 'temaforo'


class Tenfermedad(models.Model):
    idtenfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    enfermedades_idenfermedades = models.ForeignKey(Enfermedades, models.DO_NOTHING, db_column='enfermedades_idenfermedades')

    class Meta:
        managed = False
        db_table = 'tenfermedad'


class Tgastos(models.Model):
    idtgastos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    gastos_idgastos = models.ForeignKey(Gastos, models.DO_NOTHING, db_column='gastos_idgastos')

    class Meta:
        managed = False
        db_table = 'tgastos'


class Timestamps(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timestamps'


class Timestamps1(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timestamps_1'


class Tinsecticida(models.Model):
    idtinsecticida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    insecticidas_idinsecticida = models.ForeignKey(Insecticidas, models.DO_NOTHING, db_column='insecticidas_idinsecticida')

    class Meta:
        managed = False
        db_table = 'tinsecticida'


class Tinversion(models.Model):
    idtinversion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    inversion_idinversion = models.ForeignKey(Inversion, models.DO_NOTHING, db_column='inversion_idinversion')

    class Meta:
        managed = False
        db_table = 'tinversion'


class Tperdida(models.Model):
    idtperdida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    perdidas_idperdidas = models.ForeignKey(Perdidas, models.DO_NOTHING, db_column='perdidas_idperdidas')

    class Meta:
        managed = False
        db_table = 'tperdida'


class Tpersona(models.Model):
    idtpersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = False
        db_table = 'tpersona'


class Tratamiento(models.Model):
    idtratamiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    imagen = models.TextField(blank=True, null=True)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'tratamiento'


class Tusuarioforo(models.Model):
    idtusuarioforo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    foro_idforo = models.ForeignKey(Foro, models.DO_NOTHING, db_column='foro_idforo')

    class Meta:
        managed = False
        db_table = 'tusuarioforo'


class Tvariedad(models.Model):
    idtvariedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tamaniofruto = models.CharField(max_length=50)
    aniosprimeracosecha = models.CharField(max_length=45)
    alturaplanta = models.CharField(max_length=45)
    colorbrote = models.CharField(max_length=45)
    colorfruto = models.CharField(max_length=45)
    calidadtaza = models.CharField(max_length=45)
    adaptabilidad = models.TextField()
    variedad_idvariedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='variedad_idvariedad')
    variedadgenetica_idvariedadgenetica = models.ForeignKey('Variedadgenetica', models.DO_NOTHING, db_column='variedadgenetica_idvariedadgenetica')

    class Meta:
        managed = False
        db_table = 'tvariedad'


class Valorganancia(models.Model):
    idvalorganancia = models.AutoField(primary_key=True)
    ganancia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'valorganancia'


class Valorgasto(models.Model):
    idvalorgasto = models.AutoField(primary_key=True)
    gasto = models.IntegerField()
    gastos_idgastos = models.ForeignKey(Gastos, models.DO_NOTHING, db_column='gastos_idgastos')

    class Meta:
        managed = False
        db_table = 'valorgasto'


class Valorinversion(models.Model):
    idvalorinversion = models.AutoField(primary_key=True)
    inversion = models.IntegerField()
    inversion_idinversion = models.ForeignKey(Inversion, models.DO_NOTHING, db_column='inversion_idinversion')

    class Meta:
        managed = False
        db_table = 'valorinversion'


class Valorperdida(models.Model):
    idvalorperdida = models.AutoField(primary_key=True)
    perdida = models.IntegerField()
    perdidas_idperdidas = models.ForeignKey(Perdidas, models.DO_NOTHING, db_column='perdidas_idperdidas')

    class Meta:
        managed = False
        db_table = 'valorperdida'


class Variedad(models.Model):
    idvariedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variedad'


class Variedadgenetica(models.Model):
    idvariedadgenetica = models.AutoField(primary_key=True)
    familia = models.TextField()
    grupogenetico = models.TextField()

    class Meta:
        managed = False
        db_table = 'variedadgenetica'


class Vistas(models.Model):
    idvistas = models.AutoField(primary_key=True)
    fechahoravista = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario')
    temaforo_idtemaforo = models.ForeignKey(Temaforo, models.DO_NOTHING, db_column='temaforo_idtemaforo')

    class Meta:
        managed = False
        db_table = 'vistas'


opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    aviso = models.BooleanField()


    def __str__(self):
        return self.nombre