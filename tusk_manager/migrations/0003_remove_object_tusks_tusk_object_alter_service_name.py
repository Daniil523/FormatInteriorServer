# Generated by Django 4.0.4 on 2022-05-15 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tusk_manager', '0002_alter_tusk_date_finish_alter_tusk_date_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='tusks',
        ),
        migrations.AddField(
            model_name='tusk',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object', to='tusk_manager.object'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
    ]
