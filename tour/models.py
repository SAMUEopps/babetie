from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    	return self.name

class Tour(models.Model):
	name=models.CharField(max_length=200, null=True)
	days=models.CharField(max_length=200, null=True)
	price=models.FloatField(null=True)
	description=models.CharField(max_length=200, null=True, blank=True)
	image=models.ImageField(null=True, blank=True)
	date_created=models.DateTimeField(max_length=200, null=True)

	def __str__(self):
	    	return self.name

class DayTrips(models.Model):
	name=models.CharField(max_length=200, null=True)
	price=models.FloatField(null=True)
	description=models.CharField(max_length=200, null=True, blank=True)
	image=models.ImageField(null=True, blank=True)
	date_created=models.DateTimeField(max_length=200, null=True)


	def __str__(self):
	    	return self.name

class Order(models.Model):
	STATUS=(
        ('Pending','Pending'),
        ('Verified', 'Verified'),
		)
	customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	tour=models.ForeignKey(Tour, null=True, on_delete=models.SET_NULL)
	date_created=models.CharField(max_length=200, null=True)
	status=models.CharField(max_length=200, null=True, choices=STATUS)

		