from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

#
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         field = '__all__'
#
#
# class PositionForm(forms.ModelForm):
#     class Meta:
#         model = Position
#         field = '__all__'
#
#
# class SalaryForm(forms.ModelForm):
#     class Meta:
#         model = Salary
#         field = '__all__'
#
#
# class CharacteristicForm(forms.ModelForm):
#     class Meta:
#         model = Characteristic
#         field = '__all__'
