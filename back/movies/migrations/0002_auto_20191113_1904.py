# Generated by Django 2.2.6 on 2019-11-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='good_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='isReport',
            field=models.IntegerField(choices=[(0, 'FINE'), (1, 'REPORT'), (2, 'BLOCK')], default=0),
        ),
    ]
