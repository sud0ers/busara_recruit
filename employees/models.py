from django.db import models
from django.contrib.auth.models import User



# Employee/Job Applicant.
class Employee(models.Model):
	# user = models.OneToOneField(User, null=True)
	first_name  = models.CharField(blank=False, max_length=30,default="")
	last_name = models.CharField(blank=False, max_length=30,default="")
	username = models.CharField(blank=False, max_length=30,default="")
	password = models.CharField(blank=False, max_length=200,default="")
	email = models.CharField(blank=False, max_length=35,default="")
	phone_number = models.CharField(blank=True, max_length=12)
	profile_photo = models.ImageField(upload_to='employees/%Y/%m/%d/', blank=True)
	created_on = models.DateTimeField(auto_now=True)
	
	def __str__(self): # __unicode__ on Python 2
		return self.first_name+' '+self.last_name
	

			
	 