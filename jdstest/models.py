from django.db import models

# Create your models here.
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
        db_table = 'jml_pengeluaran_kerbau'