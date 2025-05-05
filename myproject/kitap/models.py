from django.db import models

# Create your models here.

class Kitap(models.Model):
    title = models.CharField(max_length=200)
    page = models.IntegerField()
    content = models.TextField()
    published_time = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
    