# Generated by Django 3.2.4 on 2021-06-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Имя:')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия:')),
                ('last_name', models.CharField(max_length=50, verbose_name='Отчество:')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес:')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название позиции:')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название проекта:')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='employeeApp.employee')),
                ('value', models.CharField(max_length=50, verbose_name='Характеристика:')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Зарплата:')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default='31.12.2999')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employeeApp.employee', verbose_name='Сотрудник:')),
            ],
            options={
                'verbose_name_plural': 'Salaries',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.ManyToManyField(to='employeeApp.Project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='positions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employeeApp.position', verbose_name='Позиция'),
        ),
    ]
