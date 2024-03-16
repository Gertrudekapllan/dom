from django.urls import path

from pages import views as pages_views
from post import views as post_views

urlpatterns = [
    path('', pages_views.home_page, name='home_page'),
    path('services/silkscreen/', pages_views.silkscreen, name='silkscreen'),
    path('services/dtf-printing/', pages_views.dtf_printing, name='dtf_printing'),
    path('services/embroidery/', pages_views.embroidery, name='embroidery'),
    path('services/printing-special-effects/', pages_views.printing_special_effects, name='printing_special_effects'),
    path('services/individual-print/', pages_views.individual_print, name='individual_print'),
    path('services/sublimation_printing/', pages_views.sublimation_printing, name='sublimation_printing'),
    path('post/<int:pk>', post_views.post_page),
]