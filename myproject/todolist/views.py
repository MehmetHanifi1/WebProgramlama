from django.shortcuts import render
from .models import Task
# Create your views here.

def gorev_listesi(request):
    gorevler = Task.objects.all
    return render(request,"todolist/gorev_listesi.html", {"gorevler":gorevler})