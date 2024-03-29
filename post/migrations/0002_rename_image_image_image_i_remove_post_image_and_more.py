# Generated by Django 5.0.2 on 2024-02-29 14:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_i',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image_p',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
