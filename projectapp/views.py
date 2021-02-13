from django.shortcuts import render
from projectapp.models import Employee_Details
from projectapp import forms
import datetime

# Create your views here.
def table_display(request):
	emp_list=Employee_Details.objects.all()#this is used to fetch the data from database
	date=datetime.datetime.now();
	hour=int(date.strftime('%H'))
	msg=None
	if hour<12:
		msg="GOOD MORNING"
	elif hour<16:
		msg="GOOD AFTERNOON"
	elif hour<20:
		msg="GOOD EVENING"
	else:
		msg="GOOD NIGHT"

	form_page=forms.Employee_Details_Form
	if request.method=='POST':
		form_data=forms.Employee_Details_Form(request.POST)
		if form_data.is_valid():
			print('EMPLOYEE INFO')
			print('THE EMPLOYEE NAME IS :',form_data.cleaned_data['ENAME'])
			print('THE EMPLOYEE AGE IS :',form_data.cleaned_data['AGE'])
			print('THE EMPLOYEE SALARY IS :',form_data.cleaned_data['SALARY'])
			print('THE EMPLOYEE PHONE_NO IS :',form_data.cleaned_data['PHONE_NO'])
			print('THE EMPLOYEE CITY IS :',form_data.cleaned_data['CITY'])
			print('THE EMPLOYEE EMAIL IS :',form_data.cleaned_data['EMAIL'])
			form_data.save(commit=True)

	my_dict={'msg':msg,'date':date,'emp_list':emp_list,'forms':form_page}
	return render(request,'projectapp/display.html',context=my_dict)