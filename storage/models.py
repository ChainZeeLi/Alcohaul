from __future__ import unicode_literals

from django.db import models

# Create your models here.




class store(models.Model):

	name =  models.CharField(max_length=250,null=True)
	location = models.CharField(max_length=250,null=True)
	address = models.CharField(max_length=250,null=True)
	max_number_of_customer_at_one_time = models.CharField(max_length=250,null=True)
	working_driver = models.CharField(max_length=250,null=True)
	date_created = models.CharField(max_length=250,null=True)
	UID = models.CharField(max_length=250,null=True)
	is_deleted = models.CharField(max_length=250,null=True)
	discription = models.CharField(max_length=250,null=True)
	contact_first = models.CharField(max_length=250,null=True)
	contact_last = models.CharField(max_length=250,null=True)
	rating = models.CharField(max_length=250,null=True)
	number = models.CharField(max_length=250,null=True)
	#picture = models.ImageField()
	#alcohols = models.ManyToManyField(alcohol)

	
	def __str__(self):
		return self.name

	def __repr__(self):
		return "name: "+ self.name+'\n'+"location: "+self.location+'\n'+"address: "+self.address+'\n'+"max number of customer: "+self.max_number_of_customer_at_one_time+'\n'+"working_driver: "+self.working_driver+'\n'+"date created: "+self.date_created+'\n'+"UID: "+self.UID
		+'\n'+"is deleted: "+self.is_deleted+'\n'+"description: "+self.description+'\n'+"contact's firstname: "+self.contact_first+'\n'+"contact's lastname"+self.contact_last+'\n'+"rating: "+self.rating+'\n'+"number: "+self.number


class alcohol(models.Model):
	name = models.CharField(max_length=250,null=True) 
	price = models.FloatField(max_length=250,null=True)
	quantity = models.IntegerField(null=True)
	volume = models.IntegerField(null=True)
	brand = models.CharField(max_length=250,null=True)
	Type = models.CharField(max_length=250,null=True)
	subtype = models.CharField(max_length=250,null=True)
	origin = models.CharField(max_length=250,null=True)
	description = models.CharField(max_length=500,null=True)
	rating = models.IntegerField(null=True)
	available = models.NullBooleanField(null=True)
	#picture = models.ImageField()
	special = models.NullBooleanField(null=True)
	UID = models.IntegerField(null=True)
	number_sold = models.IntegerField(null=True)
	quantity_left = models.IntegerField(null=True)
	stores = models.ManyToManyField(store)



	def __str__(self):
		return self.name
		
	def __repr__(self):
		return "name: "+ self.name+'\n'+"price: "+str(self.price)+'\n'+"quantity: "+str(self.quantity)+'\n'+"volume: "+str(self.volume)+'\n'+"brand: "+self.brand+'\n'+"Type: "+self.Type+'\n'+"subtype: "+self.subtype+'\n'+"origin: "+self.origin+'\n'+"description: "+self.description+'\n'+"rating: "+str(self.rating)+'\n'+"available: "+str(self.available)+'\n'+"special: "+str(self.special)+'\n'
		+'\n'+"UID: "+str(self.UID)+'\n'+"number sold: "+str(self.number_sold)+"quantity: "+str(self.quantity_left)+"stores: "+self.stores


#a = alcohol(name="Corona",price=0.99,quantity=100,volume=100,brand="Corona",Type="beer",subtype="beer",origin="US",description="Horse Piss",rating=4,available=True, special=True,UID=123,number_sold=120,quantity_left=30)



