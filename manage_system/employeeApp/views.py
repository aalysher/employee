from django.shortcuts import render
from .forms import EmployeeForm

from .models import Employee


# Create your views here.

def index(request):
    return render(request, template_name='employeeApp/index.html')


def add_employee(request):
    emp_add = EmployeeForm
    return render(
        request,
        'employeeApp/add_employee.html',
        context={'emp_add': emp_add}
    )


def show_employee(request):
    emp = Employee.objects.all()

    return render(request,
                  'employeeApp/show_employee.html',
                  context={'emp': emp})
