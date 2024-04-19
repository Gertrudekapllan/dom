from django.db import models
from django.urls import reverse


class Page(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя страницы")
    image = models.ImageField(null=True, blank=True, verbose_name="Фото")
    text_1 = models.TextField(verbose_name="Текст 1", blank=True, null=True)
    machine_name = models.CharField(unique=True, max_length=255)
    text_2 = models.TextField(verbose_name="Текст 2", blank=True, null=True)
    text_3 = models.TextField(verbose_name="Текст 3", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pages', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'
        ordering = ['name']


class PageSpecial(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя страницы")
    machine_name = models.CharField(unique=True, max_length=255)
    image_1 = models.ImageField(null=True, blank=True, verbose_name="Фото1")
    text_1 = models.TextField(verbose_name="Текст 1", blank=True, null=True)
    image_2 = models.ImageField(null=True, blank=True, verbose_name="Фото2")
    text_2 = models.TextField(verbose_name="Текст 2", blank=True, null=True)
    image_3 = models.ImageField(null=True, blank=True, verbose_name="Фото3")
    text_3 = models.TextField(verbose_name="Текст 3", blank=True, null=True)
    image_4 = models.ImageField(null=True, blank=True, verbose_name="Фото4")
    text_4 = models.TextField(verbose_name="Текст 4", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница Спецэффектов'
        verbose_name_plural = 'Страница Спецэффектов'
