from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models    import department,employee,role
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')
def showemployee(request):
    emp=employee.objects.all()
    return render(request,'showemp.html',{'context':emp})
def addemployee(request):
        if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            dept=int (request.POST ['dept'])
            salary=int(request.POST['salary'])
            role=int(request.POST['role'])
            phone=int(request.POST['phone'])
            newemployee=employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,role_id=role,phone=phone,hire_date=datetime.now())
            newemployee.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'addemp.html')
def removeemployee(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponseRedirect('/showemployee/')
        except:
            return HttpResponse("enter a valid employee id")
    emp=employee.objects.all()
    return render(request,'rememp.html',{'emp':emp})
def filteremployee(request):
    
    return render(request,'filemp.html')
