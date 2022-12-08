from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Api.models import Employee
from django.shortcuts import render
from Api.serializers import employeeSerializer
# Create your views here.
#Here Listing All employees data (Retiving Data)
@api_view(['GET'])
def home(request):
    employee=Employee.objects.all()
    serialEmployee=employeeSerializer(employee,many=True)
    return Response(serialEmployee.data)
    # return JsonResponse("Testing json data",safe=False)



#Here Data Getting By ID
@api_view(['GET'])
def employeeView(request, pk):
    employee = Employee.objects.get(id=pk)
    serialEmployee = employeeSerializer(employee, many=False)
    return Response(serialEmployee.data)

#By using Ty catch method Employee Data Posting(Crating Data)
@api_view(['POST'])
def employeeAdd(request):
    try:
            
        serialdata = employeeSerializer(data=request.data)
        if serialdata.is_valid():
            serialdata.save()
        
        return Response({
            'status':200,
            'employee':serialdata.data,
            'message':'Employee added successfully'
        })

    except:
        return Response({'status':400})

#update Employee data
@api_view(['POST'])
def employeeUpdate(request, pk):
    try :
        employee = Employee.objects.get(id=pk)
        serialemployee = employeeSerializer(instance=employee, data=request.data)

        if serialemployee.is_valid():
            serialemployee.save()
            
        return Response({
            'status':200,
            'employee':serialemployee.data,
            'message':'Updated successfully'
        })

    except :
        return Response({'status':400})

#Delete Employee data 
@api_view(['DELETE'])
def employeeDelete(request, pk):
    try:

        employee = Employee.objects.get(id=pk)
        employee.delete()
        
        employees = Employee.objects.all()
        serialemployees = employeeSerializer(employees, many=True)
        
        return Response({
            'status':200,
            'employee':serialemployees.data,
            'message':'Employee Deleted successfully'
        })

    except:
        return Response({'status':400})

#username:admin
#password:123456
#i construted program by using App urls like api/