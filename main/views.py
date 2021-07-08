from django.shortcuts import render
from django.db import connection

def home(request):
    response = {}
    stmt = '''
    SELECT * FROM MODUL;
    '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(stmt)
            listModul = cursor.fetchall()
        # listKelasGratis = []
        # listKelasBaru = []
        # listKelasExpert = []
        # listModulUnggulan = []
        # listTalksUnggulan = []
        # listPetaUnggulan = []
        # listKelasBisnis = []
        # listKelasPemasaran = []
        # listKelasMO = []

        # for modul in listModul:
        #     if (modul[3] == 'kelas gratis'):
        #         listKelasGratis.append(modul)
        #     if (modul[3] == 'kelas baru'):
        #         listKelasBaru.append(modul)
        #     if (modul[3] == 'kelas expert'):
        #         listKelasExpert.append(modul)
        #     if (modul[3] == 'modul unggulan'):
        #         listModulUnggulan.append(modul)
        #     if (modul[3] == 'talks unggulan'):
        #         listTalksUnggulan.append(modul)
        #     if (modul[3] == 'peta unggulan'):
        #         listPetaUnggulan.append(modul)
        #     if (modul[3] == 'kelas bisnis'):
        #         listKelasBisnis.append(modul)
        #     if (modul[3] == 'kelas pemasaran'):
        #         listKelasPemasaran.append(modul)
        #     if (modul[3] == 'kelas managemen operasional'):
        #         listKelasMO.append(modul)
        
        response['listModul'] = listModul
    except:
        response['error'] = 'Ada suatu kesalahan, silahkan coba lagi'
    return render(request, 'main/home.html', response)
