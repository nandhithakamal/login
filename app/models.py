from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

India = 'India'
USA = 'USA'
China = 'China'

countries = [(India, "India"), (USA, "USA"), (China, "China")]
# Create your models here.
class User(models.Model) :
	firstName = models.CharField(max_length = 20, null = False)
	middleName = models.CharField(max_length = 20, null = True, blank = True)
	lastName = models.CharField(max_length = 20, null = False)
	country = models.CharField(max_length = 50, choices = countries, default = India)
	emailID = models.CharField(max_length = 50, validators =[EmailValidator()], null = False, default = "example@example.com")
	username = models.CharField(max_length = 50, primary_key = True)
	password = models.CharField(max_length = 32, validators = [MinLengthValidator(8)], )
	
	def __str__(self) :
		return self.firstName + ' ' + self.lastName