from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

		
@api_view(['GET', 'POST'])
def employee_list(request):
	if request.method == 'GET':
		all_employees = Employee.objects.all()
		serializer = EmployeeSerializer(all_employees, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
	employee = get_object_or_404(Employee, id = id)
	
	if request.method == 'GET':
		serializer = EmployeeSerializer(employee)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = EmployeeSerializer(employee, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		employee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	




