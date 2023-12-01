from django.http import HttpResponse
from django.shortcuts import render

from First_blog.models import Post, Category


# Create your views here.

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    print(cats)
    data = {
        'posts': posts,
        'cats': cats
    }

    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'post.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)

    return render(request, 'category.html', {'cat': cat, 'posts': posts})
