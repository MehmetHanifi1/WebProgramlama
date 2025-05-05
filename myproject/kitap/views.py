from django.shortcuts import render, get_object_or_404, redirect
from .models import Kitap
from .forms import KitapForm, KitapFilterForm
from django.db.models import Q
from datetime import datetime

def kitap_listesi(request):
    form = KitapFilterForm(request.GET)
    kitaplar = Kitap.objects.all()

    if form.is_valid():
        fiyat_min = form.cleaned_data.get('fiyat_min')
        fiyat_max = form.cleaned_data.get('fiyat_max')
        yayin_baslangic = form.cleaned_data.get('yayin_baslangic')
        yayin_bitis = form.cleaned_data.get('yayin_bitis')
        sayfa_min = form.cleaned_data.get('sayfa_min')
        sayfa_max = form.cleaned_data.get('sayfa_max')
        title = form.cleaned_data.get('title') 

        if fiyat_min is not None:
            kitaplar = kitaplar.filter(price__gte=fiyat_min)
        if fiyat_max is not None:
            kitaplar = kitaplar.filter(price__lte=fiyat_max)
        if yayin_baslangic is not None:
            kitaplar = kitaplar.filter(published_time__gte=yayin_baslangic)
        if yayin_bitis is not None:
            kitaplar = kitaplar.filter(published_time__lte=yayin_bitis)
        if sayfa_min is not None:
            kitaplar = kitaplar.filter(content__gte=sayfa_min)
        if sayfa_max is not None:
            kitaplar = kitaplar.filter(content__lte=sayfa_max)
        if title:  # Başlık varsa, başlığa göre filtreleme yapıyoruz
            kitaplar = kitaplar.filter(title__icontains=title)

    return render(request, 'kitap/kitap_listesi.html', {'form': form, 'kitaplar': kitaplar})

def kitap_ekle(request):
    if request.method == "POST":
        form = KitapForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('kitap_listesi')  
    else:
        form = KitapForm()
    return render(request, 'kitap/kitap_ekle.html', {'form': form})

def kitap_duzenle(request, pk):
    kitap = get_object_or_404(Kitap, pk=pk)
    if request.method == "POST":
        form = KitapForm(request.POST, instance=kitap)
        if form.is_valid():
            form.save()
            return redirect('kitap_listesi')  
    else:
        form = KitapForm(instance=kitap)
    return render(request, 'kitap/kitap_duzenle.html', {'form': form})

def kitap_sil(request, pk):
    kitap = get_object_or_404(Kitap, pk=pk)
    if request.method == "POST":
        kitap.delete()
        return redirect('kitap_listesi')  
    return render(request, 'kitap/kitap_sil.html', {'kitap': kitap})
