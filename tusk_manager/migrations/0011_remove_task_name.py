# Generated by Django 4.0.4 on 2022-05-21 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tusk_manager', '0010_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
    ]