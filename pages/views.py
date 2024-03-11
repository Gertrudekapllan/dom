from django.db.models import Subquery, OuterRef
from django.shortcuts import render

from pages.models import Page
from post.models import Post, Image


def home_page(request):
    pages = Page.objects.all()
    posts = Post.objects.all()
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'home_page.html', {'pages': pages, 'posts': posts, 'post_images': post_images})


def silkscreen(request):
    page = Page.objects.get(machine_name='silkscreen')
    posts = Post.objects.filter(category=1)
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'silkscreen.html', {'page': page, 'post_images': post_images})


def dtf_printing(request):
    page = Page.objects.get(machine_name='dtf_printing')
    posts = Post.objects.filter(category=3)
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'dtf_printing.html', {'page': page, 'post_images': post_images})


def embroidery(request):
    page = Page.objects.get(machine_name='embroidery')
    posts = Post.objects.filter(category=2)
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'embroidery.html', {'page': page, 'post_images': post_images})


def printing_special_effects(request):
    page = Page.objects.get(machine_name='printing_special_effects')
    posts = Post.objects.filter(category=5)
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'printing_special_effects.html', {'page': page, 'post_images': post_images})


def individual_print(request):
    page = Page.objects.get(machine_name='individual_print')
    return render(request, 'individual_print.html', {'page': page})


def sublimation_printing(request):
    pages = Page.objects.get(machine_name='sublimation_printing')
    posts = Post.objects.filter(category=6)
    post_images = {}
    for post in posts:
        post_images[post] = Image.objects.filter(post=post)
    return render(request, 'sublimation_printing.html', {'page': pages, 'post_images': post_images})
