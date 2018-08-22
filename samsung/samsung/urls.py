# samsung URL Configuration
from django.contrib import admin
from django.urls import path, re_path, include
from employees import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('employees/', views.employee_list, name='employee_list'),
	re_path(r'^employees/(?P<id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
]