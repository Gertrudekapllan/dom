from django.db.models import Subquery, OuterRef
from django.shortcuts import render

from pages.models import Page, PageSpecial
from post.models import Post, Image
from django.core.serializers import serialize
from collections import defaultdict


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
    page = PageSpecial.objects.get(machine_name='printing_special_effects')
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


def about_us(request):
    return render(request, 'about_us.html')


# def gallery(request):
#     images = Image.objects.all()
#     grouped_images = defaultdict(list)
#     print('asdf')
#     for image in images:
#         post_id = image.post.id
#         image_data = {
#             "pk": image.pk,
#             "image_i": image.image_i,  # assuming image_i is an ImageField
#         }
#         grouped_images[post_id].append(image_data)
#     grouped_images = dict(grouped_images)
#     print(grouped_images)
#     # for post_id, images in grouped_images.items():
#     #     print(f'Post ID: {post_id}')
#     #     for image in images:
#     #         print(f' - Image ID: {image.pk}, Image Path: {image.image_i}')
#
#     return render(request, 'gallery.html', {'images': grouped_images.items()})
def gallery(request):
    from collections import defaultdict
    images = Image.objects.all()
    grouped_images = defaultdict(list)
    for image in images:
        grouped_images[image.post_id].append(image)
    return render(request, 'gallery.html', {'grouped_images': grouped_images.items()})

def why_vector(request):
    pages = Page.objects.get(machine_name='why_vector')
    images = Image.objects.all()
    return render(request, 'why-vector.html', {'page': pages, 'images': images})


def contacts(request):
    pages = Page.objects.get(machine_name='contacts')
    return render(request, 'contacts.html', {'page': pages})
