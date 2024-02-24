from django.shortcuts import render

from pages.models import Page


def silkscreen(request):
    page = Page.objects.get(machine_name='silkscreen')
    return render(request, 'silkscreen.html', {'page': page})


def dtf_printing(request):
    page = Page.objects.get(machine_name='dtf_printing')
    return render(request, 'dtf_printing.html', {'page': page})


def embroidery(request):
    page = Page.objects.get(machine_name='embroidery')
    return render(request, 'embroidery.html', {'page': page})


def printing_special_effects(request):
    page = Page.objects.get(machine_name='printing_special_effects')
    return render(request, 'printing_special_effects.html', {'page': page})


def individual_print(request):
    page = Page.objects.get(machine_name='individual_print')
    return render(request, 'individual_print.html', {'page': page})