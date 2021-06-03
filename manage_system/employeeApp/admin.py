from django.contrib import admin
from .models import Employee, Project, Position, Salary, Characteristic

# Register your models here.
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Position)
admin.site.register(Salary)
admin.site.register(Characteristic)
