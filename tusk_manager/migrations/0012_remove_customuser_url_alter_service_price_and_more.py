# Generated by Django 4.0.4 on 2022-05-25 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tusk_manager', '0011_remove_task_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='url',
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(default='', max_length=255, verbose_name='Цена за единицу работы (руб.)'),
        ),
        migrations.AlterField(
            model_name='task',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tusks', to='tusk_manager.object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='task',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tusk_service', to='tusk_manager.service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
