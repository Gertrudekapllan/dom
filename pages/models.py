from django.db import models
from django.urls import reverse


class Page(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя страницы")
    image = models.ImageField(null=True, blank=True, verbose_name="Фото")
    text = models.TextField(verbose_name="Описание")
    machine_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pages', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'
        ordering = ['name']

