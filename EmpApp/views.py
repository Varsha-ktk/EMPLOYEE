from django.shortcuts import render, redirect

from EmpApp.forms import EmpDet
from EmpApp.models import Employee


# Create your views here.
def index(request):
    return render(request,'index.html')
def create(request):
    data=EmpDet()
    if request.method=='POST':
        form=EmpDet(request.POST)
        form.is_valid()
        form.save()
        return redirect('index')

    return render(request,'create.html',{'data':data})
def table_view(request):
    data=Employee.objects.all()
    return render(request,'table_view.html',{'form':data})

def delete(request,id):
    data=Employee.objects.get(id=id)
    data.delete()
    return redirect('table_view')
def update(request,id):
    data = Employee.objects.get(id=id)
    form=EmpDet(instance=data)
    if request.method=='POST':
        new_data=EmpDet(request.POST,instance=data)
        new_data.is_valid()
        new_data.save()
        return redirect('table_view')
    return render(request,'update.html',{'form':form})
