from random import random

from django.db import models



# Models.

SUB_COUNTY_CHOICES = (
    ('Ikolomani','IKOLOMANI'),
    ('Lurambi', 'LURAMBI'),
    ('Wareng','WARENG'),
    ('Kapsaret','KAPSARET'),
    ('Kimilili','KIMILILI'),
    ('Naitiri','NAITIRI'),

)
COUNTY_CHOICES = (
	('Kakamega', 'KAKAMEGA'),
	('Uasin Gishu', 'UASIN GISHU'),
	('Bungoma', 'BUNGOMA'),

)
SEX_CHOICES = (
	('Female', 'FEMALE'),
	('Male', 'Male'),


)
FACILITY_TYPE_CHOICES = (

	('Dispensary', 'DISPENSARY'),
	('Hospital', 'HOSPITAL'),
    ('Nursing Home', 'NURSING HOME'),
	('Health Centre', 'HEALTH CENTRE'),
	('Dental Clinic', 'DENTAL CLINIC'),


)
OWNER_CHOICES = (
	('MOH', 'MINISTRY OF HEALTH'),
	('NGO', 'NGO'),
	('Kenya Police', 'KENYA POLICE'),


)



class Client(models.Model):


	id=models.IntegerField(primary_key=True,auto_created = True, max_length=11,default=0)
	client_name=models.CharField(max_length=100,blank=False,null=False)
	gender=models.CharField(max_length=10,choices=SEX_CHOICES)
	DOB=models.DateField()
	phone_no=models.IntegerField()
	county=models.CharField(max_length=50,choices=COUNTY_CHOICES)
	sub_county=models.CharField(max_length=50,choices=SUB_COUNTY_CHOICES)
	date_created_client=models.DateTimeField(auto_now_add=True, auto_now=False, null=True)


	def __str__(self):

		return self.id + '(' + str(self.client_name) + ')'




class Facility(models.Model):
	KMFL_code=models.CharField(primary_key=True,max_length=50,blank=False)
	facility_name=models.CharField(max_length=100)
	facility_county=models.CharField(max_length=50,choices=COUNTY_CHOICES)
	facility_subcounty=models.CharField(max_length=100,choices=SUB_COUNTY_CHOICES)
	facility_type=models.CharField(max_length=50,choices=FACILITY_TYPE_CHOICES)
	facility_owner=models.CharField(max_length=50,choices=OWNER_CHOICES)
	date_created_facility=models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

	def __str__(self):
		return self.KMFL_code + '(' + str(self.facility_name) + ')'