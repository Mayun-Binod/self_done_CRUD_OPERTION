from django.shortcuts import render
from StudentCrud.forms import StudentRegistration
# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
    else:
        fm=StudentRegistration()
    return render(request,"StudentCrud/addandshow.html",{'form':fm})
