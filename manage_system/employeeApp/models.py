from django.db import models


# Create your models here.
class Employee(models.Model):
    project = models.ManyToManyField('Project')
    name = models.CharField('Имя:',
                            max_length=50)

    surname = models.CharField('Фамилия:',
                               max_length=50)

    last_name = models.CharField('Отчество:',
                                 max_length=50)

    address = models.CharField('Адрес:',
                               max_length=50)

    positions = models.ForeignKey("Position",
                                  on_delete=models.DO_NOTHING,
                                  verbose_name='Позиция')

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Employees'


class Position(models.Model):
    name = models.CharField('Название позиции:',
                            max_length=50)

    def __str__(self):
        return self.name


class Salary(models.Model):
    value = models.FloatField('Зарплата:')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    employees = models.ForeignKey(Employee,
                                  on_delete=models.DO_NOTHING,
                                  verbose_name='Сотрудник:')

    class Meta:
        verbose_name_plural = 'Salaries'


class Characteristic(models.Model):
    id = models.OneToOneField(Employee, on_delete=models.DO_NOTHING, primary_key=True)
    value = models.CharField('Характеристика:',
                             max_length=50)


class Project(models.Model):
    name = models.CharField('Название проекта:',
                            max_length=50)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
