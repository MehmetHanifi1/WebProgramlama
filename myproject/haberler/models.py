from django.db import models

# Create your models here.
class Haber(models.Model):

    baslik = models.CharField(max_length=50, default="")
    icerik = models.TextField(max_length=155, default="")

    kategori_teknoloji = "Teknoloji"
    kategori_spor = "Spor"
    kategori_ekonomi="Ekonomi"
    kategori_magazin="Magazin"

    kategori_secenekler = [
        (kategori_teknoloji, "Teknoloji"),
        (kategori_spor, "Spor"),
        (kategori_ekonomi, "Ekonomi"),
        (kategori_magazin, "Magazin"),
    ]

    #kategori = models.CharField(max_length=20, choices=kategori_secenekler)
    #yayinTarihi = models.DateTimeField(auto_now_add=True)
    #yazar = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.baslik
