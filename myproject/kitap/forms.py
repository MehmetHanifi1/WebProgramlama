from django import forms
from .models import Kitap

class KitapForm(forms.ModelForm):
    class Meta:
        model = Kitap
        fields = ['title', 'page', 'content', 'published_time', 'price']
from django import forms

class KitapFilterForm(forms.Form):
    fiyat_min = forms.DecimalField(label="Fiyat Min", required=False, widget=forms.NumberInput(attrs={'type': 'number'}))
    fiyat_max = forms.DecimalField(label="Fiyat Max", required=False, widget=forms.NumberInput(attrs={'type': 'number'}))
    yayin_baslangic = forms.DateField(label="Yayın Başlangıcı", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    yayin_bitis = forms.DateField(label="Yayın Bitişi", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    sayfa_min = forms.IntegerField(label="Sayfa Sayısı Min", required=False)
    sayfa_max = forms.IntegerField(label="Sayfa Sayısı Max", required=False)
    title = forms.CharField(required=False) 