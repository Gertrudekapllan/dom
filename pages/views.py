from django.shortcuts import render

from pages.models import Page


def silkscreen(request):
    page = Page.objects.get(machine_name='silkscreen')
    print(page, '2222222')
    return render(request, 'silkscreen.html', {'page': page})


def dtf_printing(request):
    return None


def embroidery(request):
    return None


def printing_special_effects(request):
    return None


def individual_print(request):
    return None
