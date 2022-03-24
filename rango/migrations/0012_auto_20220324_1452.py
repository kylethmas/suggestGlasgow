# Generated by Django 2.2.26 on 2022-03-24 14:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0011_merge_20220324_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_map',
        ),
        migrations.RemoveField(
            model_name='place',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='place',
            name='dislikes',
            field=models.ManyToManyField(related_name='place_dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
