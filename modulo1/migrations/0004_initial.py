# Generated by Django 4.1.3 on 2023-02-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo1', '0003_delete_ainsecticida_delete_categoriaforo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ainsecticida',
            fields=[
                ('idainsecticida', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'ainsecticida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoriaforo',
            fields=[
                ('idcategoriaforo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=65)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'categoriaforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idcomentario', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('fechahoracoment', models.DateTimeField()),
            ],
            options={
                'db_table': 'comentario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Crearhiloforo',
            fields=[
                ('idcrearhilo', models.AutoField(primary_key=True, serialize=False)),
                ('hilo', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'crearhiloforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enfermedades',
            fields=[
                ('idenfermedades', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('imagen', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('sintomas', models.TextField()),
                ('danios', models.TextField()),
                ('cfavorecen', models.TextField()),
                ('deconomicos', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'enfermedades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('idforo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'foro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('idgastos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('unidad', models.IntegerField(blank=True, null=True)),
                ('periodo', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'gastos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('idhistorial', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'db_table': 'historial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idimagen', models.AutoField(primary_key=True, serialize=False)),
                ('fechahoraimg', models.DateTimeField()),
                ('encabezado', models.CharField(blank=True, max_length=55, null=True)),
                ('imagen', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'imagen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Informacioncafe',
            fields=[
                ('idinformacioncafe', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'informacioncafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Insecticidas',
            fields=[
                ('idinsecticida', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('imagen', models.TextField()),
                ('ingredientes', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('beneficios', models.TextField()),
                ('dosis', models.CharField(blank=True, max_length=45, null=True)),
                ('rnacional', models.TextField()),
                ('tformulacion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'insecticidas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('idinversion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55)),
                ('vidautil', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'inversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('idlote', models.AutoField(primary_key=True, serialize=False)),
                ('nombrelote', models.CharField(max_length=45)),
                ('hectarea', models.IntegerField()),
            ],
            options={
                'db_table': 'lote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mcontrolenfermedad',
            fields=[
                ('idmetodosenfer', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'mcontrolenfermedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mcontrolplagas',
            fields=[
                ('idmetodosplagas', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'mcontrolplagas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pcurativasenfer',
            fields=[
                ('idpcurativasenfer', models.AutoField(primary_key=True, serialize=False)),
                ('controlquimico', models.TextField()),
            ],
            options={
                'db_table': 'pcurativasenfer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pcurativasplaga',
            fields=[
                ('idpcurativasplaga', models.AutoField(primary_key=True, serialize=False)),
                ('controlquimico', models.TextField()),
            ],
            options={
                'db_table': 'pcurativasplaga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perdidas',
            fields=[
                ('idperdidas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('unidad', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'perdidas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfilforo',
            fields=[
                ('idperfilforo', models.AutoField(primary_key=True, serialize=False)),
                ('fnacimiento', models.DateField(blank=True, null=True)),
                ('intereses', models.TextField(blank=True, null=True)),
                ('fotoperfil', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perfilforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfilforopostforo',
            fields=[
                ('idperfilforopostforo', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'perfilforopostforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=45)),
                ('nombre2', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido1', models.CharField(max_length=45)),
                ('apellido2', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=45)),
                ('fechanacimiento', models.DateField()),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personainfocafe',
            fields=[
                ('idpersonainfocafe', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'personainfocafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plagas',
            fields=[
                ('idplagas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('danios', models.TextField()),
                ('imagen', models.TextField()),
                ('deconomicos', models.TextField()),
                ('cfavorecen', models.TextField()),
            ],
            options={
                'db_table': 'plagas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Postforo',
            fields=[
                ('idpostforo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'postforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ppreventivaenfer',
            fields=[
                ('idppreventivaenfer', models.AutoField(primary_key=True, serialize=False)),
                ('controlcultural', models.TextField()),
                ('controlbiologico', models.TextField()),
                ('controlfisico', models.TextField()),
            ],
            options={
                'db_table': 'ppreventivaenfer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ppreventivasplaga',
            fields=[
                ('idppreventivasplaga', models.AutoField(primary_key=True, serialize=False)),
                ('controlcultural', models.TextField()),
                ('controlbiologico', models.TextField()),
                ('controlfisico', models.TextField()),
            ],
            options={
                'db_table': 'ppreventivasplaga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reaccionpost',
            fields=[
                ('idreaccionpost', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'reaccionpost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recomendacioninsect',
            fields=[
                ('idrecomendainsect', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'recomendacioninsect',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recomendacionplaga',
            fields=[
                ('idrecomendaplaga', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'recomendacionplaga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registrarseforo',
            fields=[
                ('idregistroforo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'registrarseforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rfinanciero',
            fields=[
                ('idrfinanciero', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rfinanciero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rfinancierolote',
            fields=[
                ('idfinancierolote', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rfinancierolote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Temaforo',
            fields=[
                ('idtemaforo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'temaforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tenfermedad',
            fields=[
                ('idtenfermedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tenfermedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tgastos',
            fields=[
                ('idtgastos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tgastos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timestamps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'timestamps',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timestamps1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'timestamps_1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tinsecticida',
            fields=[
                ('idtinsecticida', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tinsecticida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tinversion',
            fields=[
                ('idtinversion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tinversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tperdida',
            fields=[
                ('idtperdida', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tperdida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tpersona',
            fields=[
                ('idtpersona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tpersona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('idtratamiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('imagen', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tratamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tusuarioforo',
            fields=[
                ('idtusuarioforo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tusuarioforo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tvariedad',
            fields=[
                ('idtvariedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('tamaniofruto', models.CharField(max_length=50)),
                ('aniosprimeracosecha', models.CharField(max_length=45)),
                ('alturaplanta', models.CharField(max_length=45)),
                ('colorbrote', models.CharField(max_length=45)),
                ('colorfruto', models.CharField(max_length=45)),
                ('calidadtaza', models.CharField(max_length=45)),
                ('adaptabilidad', models.TextField()),
            ],
            options={
                'db_table': 'tvariedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Valorganancia',
            fields=[
                ('idvalorganancia', models.AutoField(primary_key=True, serialize=False)),
                ('ganancia', models.IntegerField()),
            ],
            options={
                'db_table': 'valorganancia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Valorgasto',
            fields=[
                ('idvalorgasto', models.AutoField(primary_key=True, serialize=False)),
                ('gasto', models.IntegerField()),
            ],
            options={
                'db_table': 'valorgasto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Valorinversion',
            fields=[
                ('idvalorinversion', models.AutoField(primary_key=True, serialize=False)),
                ('inversion', models.IntegerField()),
            ],
            options={
                'db_table': 'valorinversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Valorperdida',
            fields=[
                ('idvalorperdida', models.AutoField(primary_key=True, serialize=False)),
                ('perdida', models.IntegerField()),
            ],
            options={
                'db_table': 'valorperdida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variedad',
            fields=[
                ('idvariedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('imagen', models.TextField()),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'variedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variedadgenetica',
            fields=[
                ('idvariedadgenetica', models.AutoField(primary_key=True, serialize=False)),
                ('familia', models.TextField()),
                ('grupogenetico', models.TextField()),
            ],
            options={
                'db_table': 'variedadgenetica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vistas',
            fields=[
                ('idvistas', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'vistas',
                'managed': False,
            },
        ),
    ]
