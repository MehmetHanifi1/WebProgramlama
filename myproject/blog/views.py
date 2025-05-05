from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})
