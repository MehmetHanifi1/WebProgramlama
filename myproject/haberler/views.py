from django.shortcuts import render, get_object_or_404, redirect
from .models import Haber
from .forms import HaberForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, "haberler/index.html")

def haber_listesi(request):
    hliste = Haber.objects.all()
    return render(request, "haberler/haber_listesi.html",{"haberler": hliste})

def haber_detay(request, haber_id):
        haber = get_object_or_404(Haber, pk = haber_id)
        return render(request, "haberler/haber_detay.html",{"haber":haber})

"""def haber_sil(request, haber_id):
        haber = get_object_or_404(Haber, pk = haber_id)
        haber.delete()
        return redirect("haber_sil")"""

def haber_getir(request):
    haber = None
    if request.method == 'POST':
        form = HaberForm(request.POST)
        if form.is_valid():
            haber_id = form.cleaned_data['haber_id']
            try:
                haber = Haber.objects.get(id=haber_id)
            except Haber.DoesNotExist:
                haber = None
    else:
        form = HaberForm()

    return render(request, 'haberler/haber_getir.html', {'form': form, 'haber': haber})

def haber_sil(request, haber_id):
    haber = get_object_or_404(Haber, pk=haber_id)

    if request.method == 'POST':
        form = HaberForm(request.POST, instance=haber)

        if form.is_valid():
            haber.delete()
            return redirect('haber_listesi') 
    else:
        form = HaberForm(instance=haber)

    return render(request, 'haberler/haber_sil.html', {'form': form, 'haber': haber})



