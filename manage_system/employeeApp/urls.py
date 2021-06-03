from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employee-add/', views.add_employee, name='emp_add'),
    path('employee-show/', views.show_employee, name='emp_show')
]
