from django.urls import path
from . import views

urlpatterns = [
    path('', views.gorev_listesi, name='gorev_listesi'),
    path('ekle/', views.gorev_ekle, name='gorev_ekle'),
    path('tamamla/<int:gorev_id>/', views.gorev_tamamla, name='gorev_tamamla'),
    path('duzenle/<int:gorev_id>/', views.gorev_duzenle, name='gorev_duzenle'),
    path('sil/<int:gorev_id>/', views.gorev_sil, name='gorev_sil'),
]
