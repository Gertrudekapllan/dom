from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    machine_name = models.CharField(unique=True, max_length=255)

