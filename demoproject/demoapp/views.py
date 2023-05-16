from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from . forms import Employee


# Create your views here.
def home(request):
    
    ss = Todo()
    if request.method=='POST':
        if True:
            ss.Name=request.POST.get('Name')
            ss.Date_Of_Birth=request.POST.get('Date_Of_Birth')
            ss.email=request.POST.get('email')
            ss.Designation=request.POST.get('Designation')
            ss.Salary=request.POST.get('Salary')      
            ss.save()
            return redirect('/data/')
    return render(request,'home.html')
     

def data(request):
    kk=Todo.objects.all()
    return render(request,'data.html',locals())

def data_list(request,id):
    ss=Todo.objects.get(pk=id)
    return render (request,'data_list.html',{'aa':ss})


def update(request,id):
    dd={}
    obj=get_object_or_404(Todo,pk=id)
    ss=Employee(request.POST , instance=obj)
    if ss.is_valid():
        ss.save()
        return redirect('/data/')
    dd['o']=ss
    return render(request,'update.html',dd)

def delete(request,id):
    
    obj=get_object_or_404(Todo,pk=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/data/')
    return render (request,'delete.html')