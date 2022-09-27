from django.db import models

# Create your models here.

class Facility(models.Model):
	KMFL_code=models.CharField(primary_key=True,max_length=50,blank=False)
	facility_name=models.CharField(max_length=100)
	facility_county=models.CharField(max_length=50)
	facility_subcounty=models.CharField(max_length=100)
	facility_type=models.CharField(max_length=50)
	facility_owner=models.CharField(max_length=50)
	date_created_facility=models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

	def __str__(self):
		return self.KMFL_code + '(' + str(self.facility_name) + ')'


class Client(models.Model):
	id=models.CharField(primary_key=True,max_length=11,blank=False,null=False)
	client_name=models.CharField(max_length=100,blank=False,null=False)
	gender=models.CharField(max_length=10)
	DOB=models.DateField()
	phone_no=models.IntegerField()
	county=models.CharField(max_length=50)
	sub_county=models.CharField(max_length=50)
	date_created_client=models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

	def __str__(self):
		return self.id + '(' + str(self.client_name) + ')'