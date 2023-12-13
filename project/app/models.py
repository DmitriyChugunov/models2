from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    age = models.PositiveIntegerField(default=1, verbose_name='Возраст')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    gender = models.BooleanField(verbose_name='Гендер')
    birthDay = models.DateTimeField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'