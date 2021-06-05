from django import forms
from .models import Employee, Project, Position, Salary, Characteristic


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'


class CharacteristicForm(forms.ModelForm):
    class Meta:
        model = Characteristic
        fields = '__all__'
