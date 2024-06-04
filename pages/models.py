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
    name_1 = models.CharField(max_length=255, verbose_name="Название спецэффекта 1", null=True)
    image_1 = models.ImageField(null=True, blank=True, verbose_name="Фото 1")
    text_1 = models.TextField(verbose_name="Текст 1", blank=True, null=True)
    name_2 = models.CharField(max_length=255, verbose_name="Название спецэффекта 2", null=True)
    image_2 = models.ImageField(null=True, blank=True, verbose_name="Фото 2")
    text_2 = models.TextField(verbose_name="Текст 2", blank=True, null=True)
    name_3 = models.CharField(max_length=255, verbose_name="Название спецэффекта 3", null=True)
    image_3 = models.ImageField(null=True, blank=True, verbose_name="Фото 3")
    text_3 = models.TextField(verbose_name="Текст 3", blank=True, null=True)
    name_4 = models.CharField(max_length=255, verbose_name="Название спецэффекта 4", null=True)
    image_4 = models.ImageField(null=True, blank=True, verbose_name="Фото 4")
    text_4 = models.TextField(verbose_name="Текст 4", blank=True, null=True)
    name_5 = models.CharField(max_length=255, verbose_name="Название спецэффекта 5", null=True)
    image_5 = models.ImageField(null=True, blank=True, verbose_name="Фото 5")
    text_5 = models.TextField(verbose_name="Текст 5", blank=True, null=True)
    name_6 = models.CharField(max_length=255, verbose_name="Название спецэффекта 6", null=True)
    image_6 = models.ImageField(null=True, blank=True, verbose_name="Фото 6")
    text_6 = models.TextField(verbose_name="Текст 6", blank=True, null=True)
    name_7 = models.CharField(max_length=255, verbose_name="Название спецэффекта 7", null=True)
    image_7 = models.ImageField(null=True, blank=True, verbose_name="Фото 7")
    text_7 = models.TextField(verbose_name="Текст 7", blank=True, null=True)
    name_8 = models.CharField(max_length=255, verbose_name="Название спецэффекта 8", null=True)
    image_8 = models.ImageField(null=True, blank=True, verbose_name="Фото 8")
    text_8 = models.TextField(verbose_name="Текст 8", blank=True, null=True)
    name_9 = models.CharField(max_length=255, verbose_name="Название спецэффекта 9", null=True)
    image_9 = models.ImageField(null=True, blank=True, verbose_name="Фото 9")
    text_9 = models.TextField(verbose_name="Текст 9", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница Спецэффектов'
        verbose_name_plural = 'Страница Спецэффектов'
