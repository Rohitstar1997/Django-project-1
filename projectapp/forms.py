from django import forms
from projectapp.models import Employee_Details

class Employee_Details_Form(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
    	model = Employee_Details
    	fields=('ENAME','AGE','SALARY','PHONE_NO','CITY','EMAIL')
    