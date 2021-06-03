from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employee-add/', views.add_employee, name='emp_add'),
    path('project-add/', views.add_project, name='project_add'),
    path('position-add/', views.position_add, name='pos_add'),
    path('salary-add/', views.salary_add, name='sal_add'),
    path('Characteristic-add/', views.Characteristic_add, name='char_add'),
    path('show/', views.show_employee, name='emp_show')

]
