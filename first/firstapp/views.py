from django.shortcuts import render
from firstapp.models import Employee
# Create your views here.
def dataset(r):
    data=Employee.objects.all()
    dic={'data':data}
    return render(r,'employee.html',dic)
