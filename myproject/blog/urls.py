from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<str:name>/', views.category_detail, name='category_detail'),
]