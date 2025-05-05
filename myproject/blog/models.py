from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    published_date = models.DateTimeField(auto_now_add=True)  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) 

    def _str_(self):
        return self.title