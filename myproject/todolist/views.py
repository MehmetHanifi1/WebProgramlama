from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Gorev

def gorev_listesi(request):
    gorevler = Gorev.objects.all()
    return render(request, 'todolist/gorev_listesi.html', {'gorevler': gorevler})

def gorev_ekle(request):
    if request.method == 'POST':
        baslik = request.POST['baslik']
        Gorev.objects.create(baslik=baslik)
        return redirect('gorev_listesi')
    return redirect('gorev_listesi')

def gorev_tamamla(request, gorev_id):
    gorev = get_object_or_404(Gorev, id=gorev_id)
    gorev.tamamlandi = not gorev.tamamlandi
    gorev.save()
    return redirect('gorev_listesi')

def gorev_duzenle(request, gorev_id):
    gorev = get_object_or_404(Gorev, id=gorev_id)
    if request.method == 'POST':
        gorev.baslik = request.POST['baslik']
        gorev.save()
        return redirect('gorev_listesi')
    return render(request, 'todolist/gorev_duzenle.html', {'gorev': gorev})

def gorev_sil(request, gorev_id):
    gorev = get_object_or_404(Gorev, id=gorev_id)
    gorev.delete()
    return redirect('gorev_listesi')