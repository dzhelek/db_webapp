# Generated by Django 3.0.8 on 2020-07-10 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]