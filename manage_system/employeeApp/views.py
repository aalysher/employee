from django.shortcuts import render, redirect
from .forms import EmployeeForm, ProjectForm, PositionForm, SalaryForm, CharacteristicForm
from .models import Employee


# Create your views here.

def index(request):
    return render(request,
                  template_name='employeeApp/index.html')


def add_employee(request):
    emp_add = EmployeeForm(request.POST)
    if request.method == 'POST':
        if emp_add.is_valid():
            emp_add.save()
            return redirect('emp_add')
    else:
        emp_add = EmployeeForm
    return render(
        request,
        'employeeApp/add.html',
        context={'emp_add': emp_add}
    )


def add_project(request):
    project_add = ProjectForm(request.POST)
    if request.method == 'POST':
        if project_add.is_valid():
            project_add.save()
            return redirect('project_add')
    else:
        project_add = ProjectForm
    return render(
        request,
        'employeeApp/add.html',
        context={'project_add': project_add}
    )


def position_add(request):
    pos_add = PositionForm(request.POST)
    if request.method == 'POST':
        if pos_add.is_valid():
            pos_add.save()
            return redirect('pos_add')
    else:
        pos_add = PositionForm
    return render(
        request,
        'employeeApp/add.html',
        context={'pos_add': pos_add}
    )


def salary_add(request):
    sal_add = SalaryForm(request.POST)
    if request.method == 'POST':
        if sal_add.is_valid():
            sal_add.save()
            return redirect('sal_add')
    else:
        sal_add = SalaryForm
    return render(
        request,
        'employeeApp/add.html',
        context={'sal_add': sal_add}
    )


def Characteristic_add(request):
    char_add = CharacteristicForm(request.POST)
    if request.method == 'POST':
        if char_add.is_valid():
            char_add.save()
            return redirect('char_add')
    else:
        char_add = CharacteristicForm
    return render(
        request,
        'employeeApp/add.html',
        context={'char_add': char_add}
    )


def show_employee(request):
    emp = Employee.objects.all()

    return render(request,
                  'employeeApp/show.html',
                  context={'emp': emp})
