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


class Ainsecticida(models.Model):
    idainsecticida = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    insecticidas_idinsecticida = models.ForeignKey('Insecticidas', models.DO_NOTHING, db_column='insecticidas_idinsecticida')

    class Meta:
        managed = False
        db_table = 'ainsecticida'


class Categoriaforo(models.Model):
    idcategoriaforo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    descripcion = models.TextField()
    foro_idforo = models.ForeignKey('Foro', models.DO_NOTHING, db_column='foro_idforo')
    
    def __str__(self):
        return f'Categoria: {self.nombre}'

    class Meta:
        managed = False
        db_table = 'categoriaforo'


class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    comentario = models.TextField()
    fechahoracoment = models.DateTimeField(default=timezone.now)
    postforo_idpostforo = models.ForeignKey('Postforo', models.DO_NOTHING, db_column='postforo_idpostforo')
    registrarseforo_idregistroforo = models.ForeignKey('Registrarseforo', models.DO_NOTHING, db_column='registrarseforo_idregistroforo')
    imagen_idimagen = models.ForeignKey('Imagen', models.DO_NOTHING, db_column='imagen_idimagen')
    perfilforo_idperfilforo = models.ForeignKey('Perfilforo', models.DO_NOTHING, db_column='perfilforo_idperfilforo', related_name='comentarios')
    
    def __str__(self):
        return f'{self.perfilforo_idperfilforo} {self.registrarseforo_idregistroforo} -> {self.comentario}'

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
    
    def __str__(self):
        return f'Hilo: {self.hilo}'

    class Meta:
        managed = False
        db_table = 'crearhiloforo'


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
    imagen = models.CharField(max_length=120, blank=True, null=True)
    postforo_idpostforo = models.ForeignKey('Postforo', models.DO_NOTHING, db_column='postforo_idpostforo')
    registrarseforo_idregistroforo = models.ForeignKey('Registrarseforo', models.DO_NOTHING, db_column='registrarseforo_idregistroforo')
    
    def __str__(self):
        return f'Id: {self.idimagen} Encabezado: {self.encabezado}'

    class Meta:
        # ordering nos ayuda a tener un orden ascedente
        ordering = ['-fechahoraimg']
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
    nombre_imagen = 'usuario/{0}/perfil.png'.format(instance.registrarseforo_idregistroforo.nombre)
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
    registrarseforo_idregistroforo = models.ForeignKey('Registrarseforo', models.DO_NOTHING, db_column='registrarseforo_idregistroforo')
    
    def __str__(self):
        return f'{self.fotoperfil} Perfil de {self.registrarseforo_idregistroforo}'
    

    class Meta:
        ordering = ['-registrarseforo_idregistroforo']
        managed = False
        db_table = 'perfilforo'


class Perfilforopostforo(models.Model):
    idperfilforopostforo = models.AutoField(primary_key=True)
    postforo_idpostforo = models.ForeignKey('Postforo', models.DO_NOTHING, db_column='postforo_idpostforo')
    perfilforo_idperfilforo = models.ForeignKey(Perfilforo, models.DO_NOTHING, db_column='perfilforo_idperfilforo')

    class Meta:
        managed = False
        db_table = 'perfilforopostforo'


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


class Postforo(models.Model):
    idpostforo = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.idpostforo}: {self.descripcion}'

    class Meta:
        managed = False
        db_table = 'postforo'


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
    postforo_idpostforo = models.ForeignKey(Postforo, models.DO_NOTHING, db_column='postforo_idpostforo')
    perfilforo_idperfilforo = models.ForeignKey(Perfilforo, models.DO_NOTHING, db_column='perfilforo_idperfilforo')

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


class Registrarseforo(models.Model):
    idregistroforo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45,  unique= True)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    foro_idforo = models.ForeignKey(Foro, models.DO_NOTHING, db_column='foro_idforo')
    
    # se sobreescribe la funcion "save" para encriptar la contraseña antes de que sea guardada en la base de datos
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Registrarseforo, self).save(*args, **kwargs)
        
        
    #Este metodo es para validar que la contraseña sea igual a la contrasea almab+cenada en la base de datos
    def check_password(self, raw_password):
        return auth_check_password(raw_password, self.password)
    
    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        managed = False
        db_table = 'registrarseforo'


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


class Temaforo(models.Model):
    idtemaforo = models.AutoField(primary_key=True)
    nombre = models.TextField()
    foro_idforo = models.ForeignKey(Foro, models.DO_NOTHING, db_column='foro_idforo')
    categoriaforo_idcategoriaforo = models.ForeignKey(Categoriaforo, models.DO_NOTHING, db_column='categoriaforo_idcategoriaforo')

    class Meta:
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
