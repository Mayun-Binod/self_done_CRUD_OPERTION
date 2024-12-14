from django.shortcuts import render,redirect
from StudentCrud.forms import StudentRegistration
from .models import User
# Create your views here.
# this function will add new item and show all items
def add_show(request):
    stud=User.objects.all()
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            store=User(name=nm,email=em,password=pw)
            store.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    return render(request,"StudentCrud/addandshow.html",{'form':fm,"stu":stud,})

# this function will Update/Edit
def update_data(request,id):
    if request.method=="POST":
        ed=User.objects.get(pk=id)
        form=StudentRegistration(request.POST,instance=ed)
        if form.is_valid():
            form.save()
    else:
         ed=User.objects.get(pk=id)
         form=StudentRegistration(instance=ed)

    return render(request,'StudentCrud/updatestudents.html',{"form1":form})

# this function will delete
def delete_data(request,id):
    if request.method=="POST":
        dele=User.objects.get(pk=id)
        dele.delete()
        return redirect('/')



