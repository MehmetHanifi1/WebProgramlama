from django.contrib import admin
from .models import Gorev

@admin.register(Gorev)
class GorevAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'tamamlandi', 'olusturulma_tarihi')
    list_filter = ('tamamlandi',)
    search_fields = ('baslik',)