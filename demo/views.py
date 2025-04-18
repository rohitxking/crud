from django.shortcuts import render,redirect
from .models import StudentModel


def home(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        cls=request.POST.get('cls')
        city=request.POST.get('city')

        data=StudentModel(name=nm,cls=cls,city=city)
        data.save()
    record=StudentModel.objects.all()

    return render(request,'index.html',{'record':record})


def delete(request,id):
    data = StudentModel.objects.get(pk=id)
    data.delete()
    return redirect('/')


def update(request,id):
    if request.method=="POST":
        nm=request.POST.get('name')
        cls=request.POST.get('cls')
        city=request.POST.get('city')

        data=StudentModel(id=id,name=nm,cls=cls,city=city)
        data.save()

    record=StudentModel.objects.get(id=id)

    return render(request,'update.html',{'record':record})
