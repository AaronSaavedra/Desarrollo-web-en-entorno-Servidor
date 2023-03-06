# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencia(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=True, max_length=20)
    contrasena = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    tiktok = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Agencia'


class Clientes(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(max_length=20)
    usuario = models.CharField(unique=True, max_length=20)
    contrasena = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=500, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clientes'


class Comentarioagencia(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idusuario = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idagencia = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='idAgencia')  # Field name made lowercase.
    comentario = models.CharField(max_length=500)
    valoracion = models.IntegerField()
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ComentarioAgencia'


class Comentariofotografo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idusuario = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idfotografo = models.ForeignKey('Fotografo', models.DO_NOTHING, db_column='idFotografo')  # Field name made lowercase.
    comentario = models.CharField(max_length=500)
    valoracion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ComentarioFotografo'


class Fotografo(models.Model):
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    tiktok = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fotografo'


class Fotosagencia(models.Model):
    idagencia = models.ForeignKey(Agencia, models.DO_NOTHING, db_column='idAgencia')  # Field name made lowercase.
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosAgencia'


class Fotosfotografo(models.Model):
    idfotografo = models.ForeignKey(Fotografo, models.DO_NOTHING, db_column='idFotografo')  # Field name made lowercase.
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosFotografo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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
