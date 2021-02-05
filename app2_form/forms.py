from django import forms
class Student(forms.Form):
    sid=forms.IntegerField()
    spass=forms.CharField(widget=forms.PasswordInput)
    sname=forms.CharField(label="Enter name", max_length=20, help_text="Enter your name")
    saddr=forms.CharField()
