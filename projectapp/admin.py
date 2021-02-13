from django.contrib import admin
from projectapp.models import Employee_Details

# Register your models here.
class Employee_DetailsAdmin(admin.ModelAdmin):
    '''
        Admin View for employee_details
    '''
    list_display = ('ENAME','AGE','SALARY','PHONE_NO', 'CITY', 'EMAIL')

admin.site.register(Employee_Details, Employee_DetailsAdmin)
