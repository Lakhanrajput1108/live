from django.shortcuts import render
from django.http import HttpResponse
from .import forms
# Create your views here.
def show(request):
    return HttpResponse("this is Home page")
def studentreg(request):
    global form
    form=forms.Student()
    my_dict={'form':form}
    form=forms.Student(request.POST)
    return render(request,'app2_form/register.html', context=my_dict)
