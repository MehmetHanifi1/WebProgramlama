from django.urls import path
from . import views

urlpatterns = [
    path('', views.gorev_listesi, name = 'gorev_listesi'),  
]
