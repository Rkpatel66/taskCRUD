from django.urls import path

from Api import views
urlpatterns = [
 path('', views.home, name='home'),
 path('employee-view/<str:pk>/', views.employeeView, name="employeeview"),
 path('add-employee/', views.employeeAdd, name="employeeadd"),
 path('update-employee/<str:pk>/', views.employeeUpdate, name="employeeupdate"),
 path('delete-employee/<str:pk>/', views.employeeDelete, name="employeedelete"),


]
