from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    fm = Employee.objects.all
    return render(request, 'all_emp.html', {'ash': fm})


def add_emp(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dept = int(request.POST.get('dept'))
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        role = int(request.POST.get('role'))
        phone = int(request.POST.get('phone'))
        emp = Employee(firstname=firstname, lastname=lastname, salary=salary, bonus=bonus,phone=phone, dept_id=dept, role_id=role, hire_date=datetime.today())
        emp.save()
        return HttpResponse('Details Saved')
    return render(request, 'add_emp.html')


def remove_emp(request, i_id=0):
    if i_id:
        try:
            d = Employee.objects.get(id=i_id)
            d.delete()
            return HttpResponse("Employee Remove Successfully")
        except:
            return HttpResponse("Please Enter valid emp id")
    fm1 = Employee.objects.all
    return render(request, 'remove_emp.html', {'ash': fm1})


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
         emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
        if dept:
         emps = emps.filter(dept__name__icontains = dept)
        if role:
         emps = emps.filter(role__name__icontains = role)
        return render(request, 'all_emp.html',{'ash':emps})
    
    elif request.method == "GET":
         return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exception Occurred')
