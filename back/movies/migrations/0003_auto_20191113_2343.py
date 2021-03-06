# Generated by Django 2.2.6 on 2019-11-13 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20191113_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='good_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='isReport',
        ),
        migrations.AddField(
            model_name='comment',
            name='goods',
            field=models.ManyToManyField(blank=True, related_name='comment_goods', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='report',
            field=models.ManyToManyField(blank=True, related_name='comment_report', to=settings.AUTH_USER_MODEL),
        ),
    ]
