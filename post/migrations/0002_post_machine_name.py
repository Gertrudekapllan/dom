# Generated by Django 5.0.2 on 2024-02-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='machine_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
