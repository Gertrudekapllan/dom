from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Post(models.Model):
    text = models.TextField(verbose_name="Описание")
    # TODO remove image_p from this entity
    image_p = models.ImageField(upload_to="images/", verbose_name="Фото", null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name="Категория")
    # image_t = models.ImageField(verbose_name='Кар')

    # def __str__(self):
    #     return str(self.id)

    def get_absolute_url(self):
        return reverse('pages', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['id']


class Image(models.Model):
    image_i = models.ImageField(upload_to='image/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
