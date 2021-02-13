from django.db import models

# Create your models here.
class Employee_Details(models.Model):
	ENAME = models.CharField(max_length=50)
	AGE = models.IntegerField()
	SALARY = models.IntegerField()
	PHONE_NO = models.CharField(max_length=50)
	CITY = models.CharField(max_length=50)
	EMAIL = models.EmailField()

	class Meta:
		verbose_name = "Employee_Details"
		verbose_name_plural = "Employee_Detailss"
	def __str__(self):
		return self.ENAME
    