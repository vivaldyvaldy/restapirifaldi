# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthenticationUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    is_verified = models.BooleanField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    auth_provider = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'authentication_user'


class AuthenticationUserGroups(models.Model):
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authentication_user_groups'
        unique_together = (('user', 'group'),)


class AuthenticationUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authentication_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)

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


class ExpensesExpense(models.Model):
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    owner = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'expenses_expense'


class IncomeIncome(models.Model):
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    owner = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'income_income'


class JmlLulusanPesertaPelatihan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kode_provinsi = models.IntegerField(blank=True, null=True)
    nama_provinsi = models.CharField(max_length=255, blank=True, null=True)
    nama_bidang = models.CharField(max_length=255, blank=True, null=True)
    nama_kegiatan = models.CharField(max_length=255, blank=True, null=True)
    jumlah_lulusan = models.BigIntegerField(blank=True, null=True)
    satuan = models.CharField(max_length=30, blank=True, null=True)
    tahun = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jml_lulusan_peserta_pelatihan'


class JmlPegawaiPppk(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kode_provinsi = models.IntegerField(blank=True, null=True)
    nama_provinsi = models.CharField(max_length=255, blank=True, null=True)
    perangkat_daerah = models.CharField(max_length=255, blank=True, null=True)
    tingkat_pendidikan = models.CharField(max_length=30, blank=True, null=True)
    jumlah_pppk = models.BigIntegerField(blank=True, null=True)
    satuan = models.CharField(max_length=30, blank=True, null=True)
    tahun = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jml_pegawai_pppk'


class JmlPengeluaranKerbau(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kode_provinsi = models.IntegerField(blank=True, null=True)
    nama_provinsi = models.CharField(max_length=255, blank=True, null=True)
    kode_kabupaten_kota = models.IntegerField(blank=True, null=True)
    nama_kabupaten_kota = models.CharField(max_length=255, blank=True, null=True)
    kategori_pengeluaran = models.CharField(max_length=100, blank=True, null=True)
    jumlah_pengeluaran = models.BigIntegerField(blank=True, null=True)
    satuan = models.CharField(max_length=30, blank=True, null=True)
    tahun = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jml_pengeluaran_kerbau'


class SequencesSequence(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    last = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sequences_sequence'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'
