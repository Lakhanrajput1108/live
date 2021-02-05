from django.shortcuts import render
from .import forms
# Create your views here.
def empregview(request):
    form=forms.EmpRegForms()
    if request.method=='POST':
        form=forms.EmpRegForms(request.POST)
        if form.is_valid():
            print("**********\nOk Done")
            form.save()
            print("**************\nData Inserted Successfully")
    return render(request,'modelapp3/empregister.html',{'form':form})
