from django import forms
from .models import EmpRegistration
class EmpRegForms(forms.ModelForm):
    class Meta:
        model=EmpRegistration
        fields='__all__'
