from django.urls import path
from . import views


urlpatterns = [
    path('getLulusanPeserta', views.GetDataLulusanPeserta.as_view(), name="getLulusanPeserta"),
    path('getJumlahPegawaiPppk', views.GetDataJumlahPegawaiPppk.as_view(), name="getJumlahPegawaiPppk"),
    path('getJumlahPengeluaranKerbau', views.GetDataJumlahPengeluaranKerbau.as_view(), name="getJumlahPengeluaranKerbau"),
]