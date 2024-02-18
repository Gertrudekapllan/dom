from django.urls import path

from pages import views

urlpatterns = [
    path('services/silkscreen/', views.silkscreen, name='silkscreen'),
    path('services/dtf-printing/', views.dtf_printing, name='dtf_printing'),
    path('services/embroidery/', views.embroidery, name='embroidery'),
    path('services/printing-special-effects/', views.printing_special_effects, name='printing_special_effects'),
    path('services/individual-print/', views.individual_print, name='individual_print'),
]