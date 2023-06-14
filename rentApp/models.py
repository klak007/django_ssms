# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Klient(models.Model):
    id_klienta = models.AutoField(db_column='ID_klienta', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    miasto = models.CharField(db_column='Miasto', max_length=80, db_collation='Polish_CI_AS')  # Field name made lowercase.
    mail = models.EmailField(db_column='Mail', max_length=40, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefon = models.IntegerField(db_column='Telefon', unique=True, blank=True, null=True)  # Field name made lowercase.
    wzrost = models.IntegerField(db_column='Wzrost', blank=True, null=True)  # Field name made lowercase.
    waga = models.IntegerField(db_column='Waga', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Klient'



class Oplata(models.Model):
    id_oplaty = models.AutoField(db_column='ID_oplaty', primary_key=True)  # Field name made lowercase.
    kwota = models.IntegerField(db_column='Kwota')  # Field name made lowercase.
    waluta = models.CharField(db_column='Waluta', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    rodzaj_paragonu = models.CharField(db_column='Rodzaj_paragonu', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Oplata'


class Pracownicy(models.Model):
    id_pracownika = models.AutoField(db_column='ID_pracownika', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    data_zatrudnienia = models.DateTimeField(db_column='Data_zatrudnienia')  # Field name made lowercase.
    id_salonu = models.ForeignKey('Salon', models.DO_NOTHING, db_column='ID_salonu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pracownicy'


class Rower(models.Model):
    id_roweru = models.AutoField(db_column='ID_roweru', primary_key=True)  # Field name made lowercase.
    id_salonu = models.ForeignKey('Salon', models.DO_NOTHING, db_column='ID_salonu')  # Field name made lowercase.
    marka = models.CharField(db_column='Marka', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    koszt = models.IntegerField(db_column='Koszt')  # Field name made lowercase.
    wysokosc = models.CharField(db_column='Wysokosc', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    kolor = models.CharField(db_column='Kolor', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    przeznaczenie_plciowe = models.CharField(db_column='Przeznaczenie_plciowe', max_length=6, db_collation='Polish_CI_AS')  # Field name made lowercase.
    material_ramy = models.CharField(db_column='Material_ramy', max_length=40, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rodzaj_roweru = models.CharField(db_column='Rodzaj_roweru', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rower'


class Salon(models.Model):
    id_salonu = models.AutoField(db_column='ID_salonu', primary_key=True)  # Field name made lowercase.
    miasto = models.CharField(db_column='Miasto', max_length=40, db_collation='Polish_CI_AS')  # Field name made lowercase.
    ulica = models.CharField(db_column='Ulica', max_length=80, db_collation='Polish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salon'


class Wypozyczenia(models.Model):
    id_wypozyczenia = models.AutoField(db_column='ID_wypozyczenia', primary_key=True)  # Field name made lowercase.
    data_wypozyczenia = models.DateTimeField(db_column='Data_wypozyczenia')  # Field name made lowercase.
    data_zwrotu = models.DateTimeField(db_column='Data_zwrotu')  # Field name made lowercase.
    id_pracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='ID_pracownika')  # Field name made lowercase.
    id_roweru = models.ForeignKey(Rower, models.DO_NOTHING, db_column='ID_roweru')  # Field name made lowercase.
    id_klienta = models.ForeignKey(Klient, models.DO_NOTHING, db_column='ID_klienta')  # Field name made lowercase.
    id_oplaty = models.ForeignKey(Oplata, models.DO_NOTHING, db_column='ID_oplaty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wypozyczenia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Polish_CI_AS')

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
    name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Polish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Polish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Polish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Polish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Polish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    object_id = models.TextField(db_collation='Polish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Polish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Polish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Polish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Polish_CI_AS')
    session_data = models.TextField(db_collation='Polish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


