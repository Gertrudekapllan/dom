# Generated by Django 5.0.2 on 2024-04-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_pagespecial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagespecial',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото5'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='name_1',
            field=models.CharField(max_length=255, null=True, verbose_name='Название спецэффекта'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='name_2',
            field=models.CharField(max_length=255, null=True, verbose_name='Название спецэффекта'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='name_3',
            field=models.CharField(max_length=255, null=True, verbose_name='Название спецэффекта'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='name_4',
            field=models.CharField(max_length=255, null=True, verbose_name='Название спецэффекта'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='name_5',
            field=models.CharField(max_length=255, null=True, verbose_name='Название спецэффекта'),
        ),
        migrations.AddField(
            model_name='pagespecial',
            name='text_5',
            field=models.TextField(blank=True, null=True, verbose_name='Текст 5'),
        ),
    ]
