from django.shortcuts import render,redirect
from .models import Employee
from django.contrib import  messages


# Create your views here.

def index(request):
    emp=Employee.objects.all()
    return render(request,'index.html',{'emp':emp})

def viewEmployee(request,pk):
    emp=Employee.objects.get(id=pk)
    return render(request,'view.html',{'emp':emp})

def deleteEmployee(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()
    messages.success(request,'Employee Deleted Successfully!')
    return redirect('/employee')

def updateEmployee(request,pk):
    emp=Employee.objects.get(id=pk)
    return render(request,'update.html',{'emp':emp})


def update(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.emp_name=request.POST.get('emp_name')
    emp.emp_email=request.POST.get('emp_email')
    emp.emp_mobile=request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Updated Successfully!")
    return redirect('/employee')
  
def CreateView(request):
    return render(request,'create.html')

def Store(request):
    emp=Employee()
    emp.emp_name=request.POST.get('emp_name')
    emp.emp_email=request.POST.get('emp_email')
    emp.emp_mobile=request.POST.get('emp_contact')
    emp.save()
    messages.success(request,"Employee Added SuccessFully!")
    return redirect('create')
    pass