# Generated by Django 2.2.6 on 2019-11-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191109_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('authentication', models.TextField()),
            ],
        ),
    ]