from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField('Должность', max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Categories(models.Model):
    name = models.CharField('Категория работ', max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория работ"
        verbose_name_plural = "Категории работ"


class Unit(models.Model):
    name = models.CharField('Единица измерения', max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class CustomUser(AbstractUser):
    name = models.CharField('ФИО', max_length=255, default='')
    description = models.TextField('Описание', default='')
    phone = models.CharField('Номер телефона', max_length=20, default='')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, verbose_name="Должность",
                                 related_name='customuser_position')
    isWorker = models.BooleanField('Отображать в приложении', default=True)
    url = models.TextField('Описание', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Material(models.Model):
    name = models.CharField('Название материала', max_length=255, default='')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, verbose_name="Единица измерения",
                             related_name='material_unit')
    expenditure = models.CharField('Расход на единицу работы', max_length=255, default='')
    price = models.CharField('Цена за единицу материала', max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Service(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    price = models.CharField('Цена за единицу работы (руб.)', max_length=255, default='')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, verbose_name="Категория",
                                 related_name='service_category')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, verbose_name="Единица измерения",
                             related_name='service_unit')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, verbose_name="Материал",
                                 related_name='service_material')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Object(models.Model):
    name = models.CharField('Название задачи', max_length=255, default='')
    description = models.TextField('Описание', default='')
    location = models.CharField('Адрес', max_length=255, default='')
    client_name = models.CharField('ФИО заказчика', max_length=255, default='')
    client_phone = models.CharField('Номер телефона заказчика', max_length=255, default='')
    client_email = models.CharField('Email заказчика', max_length=255, default='')
    worker_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='object_worker', verbose_name="Руководитель проекта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class Task(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, verbose_name="Услуга",  related_name='tusk_service')
    completeness = models.BooleanField('Статус выполнения', default=False)
    material_status = models.BooleanField('Статус закупки', default=False)
    date_start = models.DateField('Начало задачи', default=date.today)
    date_finish = models.DateField('Конец задачи', default=date.today)
    worker_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='worker', verbose_name="Исполнитель")
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, related_name='tusks', verbose_name="Объект")
    size = models.CharField('Объем задачи', max_length=255, default='')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, verbose_name="Категория", related_name='tusk_category')

    def __str__(self):
        return f"{self.object.name} {self.service.name} {self.size} {self.service.unit.name}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
