# Generated by Django 4.0.4 on 2022-05-15 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusk_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tusk',
            name='date_finish',
            field=models.DateField(default=datetime.date.today, verbose_name='Конец задачи'),
        ),
        migrations.AlterField(
            model_name='tusk',
            name='date_start',
            field=models.DateField(default=datetime.date.today, verbose_name='Начало задачи'),
        ),
    ]