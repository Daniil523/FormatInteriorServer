# Generated by Django 4.0.4 on 2022-05-15 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tusk_manager', '0005_rename_tusk_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tusk_category', to='tusk_manager.servicecategories', verbose_name='Категория'),
        ),
    ]
