from . import views
from django.urls import path
from .views import haber_sil
from .views import haber_getir

urlpatterns = [
    path('', views.index, name="index"),
    path("haberler/", views.haber_listesi, name="haber_listesi"),
    path("haberler/<int:haber_id>/", views.haber_detay, name = "haber_detay"),
    path("haberler/<int:haber_id>/haber_sil/", haber_sil, name = "haber_sil"),
    path("haberler/<int:haber_id>/haber_getir/", haber_getir, name = "haber_getir"),
]