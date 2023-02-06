from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from datetime import date
from rest_framework.views import APIView
from rest_framework import filters, response, status
from .models import JmlPengeluaranKerbau
from django.db import connection
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# from .permissions import IsOwner

# Create your views here.
class GetDataLulusanPeserta(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def custom_sql(self):

        p_kategori  = self.request.query_params.get("p_kategori")
        p_tahun     = self.request.query_params.get("p_tahun")

        if p_kategori:
            var_kategori = p_kategori
        else:
            var_kategori = 'nama_kegiatan'

        if p_tahun:
            var_tahun = """ where tahun = '"""+p_tahun+"""'"""
        else:
            var_tahun = ''

        with connection.cursor() as cursor:
            sql = """ select """ +var_kategori+ """,
                    sum(jumlah_lulusan) as jml_lulusan,
                    tahun
                    from jml_lulusan_peserta_pelatihan
                    """ +var_tahun+ """
                    GROUP BY """ +var_kategori+ """,tahun
                    ORDER BY tahun asc """ 
            cursor.execute(sql)
            print(sql)
            row = self.dictfetchall(cursor)
        return row

    # query jumlah total lulus peserta pelatihan 
    def sum_lulusan(self):

        p_tahun2     = self.request.query_params.get("p_tahun")

        if p_tahun2:
            var_tahun2 = """ where tahun = '"""+p_tahun2+"""'"""
        else:
            var_tahun2 = ''

        with connection.cursor() as cursor:
            sql2 = """  select sum(jumlah_lulusan) as jumlah_lulusan 
                        from jml_lulusan_peserta_pelatihan 
                    """+var_tahun2
            cursor.execute(sql2)
            row = self.dictfetchall(cursor)
        return row

    token_param_config = openapi.Parameter(
        'p_kategori',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    token_param_config2 = openapi.Parameter(
        'p_tahun',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    @swagger_auto_schema(manual_parameters=[token_param_config,token_param_config2])

    def get(self, request):
        data = self.custom_sql()
        jml_lulusan = self.sum_lulusan()
        return response.Response({"data": data,"total": jml_lulusan}, status=status.HTTP_200_OK)

class GetDataJumlahPegawaiPppk(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def custom_sql(self):

        p_kategori  = self.request.query_params.get("p_kategori")
        p_tahun     = self.request.query_params.get("p_tahun")

        if p_kategori:
            var_kategori = p_kategori
        else:
            var_kategori = 'tingkat_pendidikan'

        if p_tahun:
            var_tahun = """ where tahun = '"""+p_tahun+"""'"""
        else:
            var_tahun = ''

        with connection.cursor() as cursor:
            sql = """ select """ +var_kategori+ """,
                    sum(jumlah_pppk) as jml_pppk,
                    tahun
                    from jml_pegawai_pppk
                    """ +var_tahun+ """
                    GROUP BY """ +var_kategori+ """,tahun
                    ORDER BY tahun asc """ 
            cursor.execute(sql)
            print(sql)
            row = self.dictfetchall(cursor)
        return row

    # query jumlah total pegawai p3k 
    def sum_pppk(self):

        p_tahun2     = self.request.query_params.get("p_tahun")

        if p_tahun2:
            var_tahun2 = """ where tahun = '"""+p_tahun2+"""'"""
        else:
            var_tahun2 = ''

        with connection.cursor() as cursor:
            sql2 = """  select sum(jumlah_pppk) as jumlah_pppk 
                        from jml_pegawai_pppk
                        """+var_tahun2
            cursor.execute(sql2)
            row = self.dictfetchall(cursor)
        return row

    token_param_config = openapi.Parameter(
        'p_kategori',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    token_param_config2 = openapi.Parameter(
        'p_tahun',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    @swagger_auto_schema(manual_parameters=[token_param_config,token_param_config2])

    def get(self, request):
        data = self.custom_sql()
        jml_p3k = self.sum_pppk()
        return response.Response({"data": data,"total": jml_p3k}, status=status.HTTP_200_OK)

class GetDataJumlahPengeluaranKerbau(views.APIView):

    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def custom_sql(self):
        p_kategori  = self.request.query_params.get("p_kategori")
        p_tahun     = self.request.query_params.get("p_tahun")

        if p_kategori:
            var_kategori = p_kategori
        else:
            var_kategori = 'kategori_pengeluaran'

        if p_tahun:
            var_tahun = """ where tahun = '"""+p_tahun+"""'"""
        else:
            var_tahun = ''

        with connection.cursor() as cursor:
            sql = """  select """ +var_kategori+ """,
                            sum(jumlah_pengeluaran) as jml_pengeluaran,
                            tahun
                        from jml_pengeluaran_kerbau
                        """ +var_tahun+ """
                        GROUP BY """ +var_kategori+ """,tahun
                        ORDER BY tahun asc """ 
            cursor.execute(sql)
            row = self.dictfetchall(cursor)
        return row

    # query jumlah total kerbau 
    def sum_kerbau(self):
        p_tahun2     = self.request.query_params.get("p_tahun")

        if p_tahun2:
            var_tahun2 = """ where tahun = '"""+p_tahun2+"""'"""
        else:
            var_tahun2 = ''

        with connection.cursor() as cursor:
            sql2 = """  select sum(jumlah_pengeluaran) as jumlah_pengeluaran 
                        from jml_pengeluaran_kerbau
                        """ +var_tahun2
            cursor.execute(sql2)
            row = self.dictfetchall(cursor)
        return row
    
    token_param_config = openapi.Parameter(
        'p_kategori',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    token_param_config2 = openapi.Parameter(
        'p_tahun',in_=openapi.IN_QUERY,description='Value',type=openapi.TYPE_STRING
        )
    @swagger_auto_schema(manual_parameters=[token_param_config,token_param_config2])

    def get(self, request):
        data = self.custom_sql()
        jml_kerbau = self.sum_kerbau()
        return response.Response({"data": data,"total": jml_kerbau}, status=status.HTTP_200_OK)