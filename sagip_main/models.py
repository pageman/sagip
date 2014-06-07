from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Disaster (models.Model):
	name = models.CharField(max_length=128)
	lat_coord = models.DecimalField(max_digits=10, decimal_places=4)
	long_coord = models.DecimalField(max_digits=10, decimal_places=4)
	def __unicode__(self,):
		return self.name
	
	class Meta:
		verbose_name = 'Disaster'
		verbose_name_plural = 'Disasters'


class TabInfo (models.Model):
	
	def __unicode__(self,):
		return self.name
	
	class Meta:
		verbose_name = 'Tab Info Panel'
		verbose_name_plural = 'Tab Info Panels'
	
	name = models.CharField(max_length=150,
							help_text='For reference only.')
	title = models.CharField(max_length=150,
							help_text='This will appear on the site.')
	date_edited = models.DateField('Date Edited', blank=False, null=True)
	text = models.TextField(max_length=500, verbose_name="text info", blank=False)
#	img_file = models.CharField(max_length=150,
#							help_text='eg. wife.png')
	
class DataBits (models.Model):
	
	def __unicode__(self,):
		return self.name
	
	class Meta:
		verbose_name = 'geo data'
		verbose_name_plural = 'geo data'
	
	category = models.CharField(max_length=150,
							)
	name = models.CharField(max_length=150,
							)
	value = models.DecimalField(max_digits=10,decimal_places=2
							)
	unit = models.CharField(max_length=150,
							blank=True)						
	geo_lat = models.DecimalField(max_digits=10, decimal_places=4)
	geo_long = models.DecimalField(max_digits=10, decimal_places=4)
	contrib_user = models.ForeignKey(User)
#	time_added = models.DateField('Date Added', blank=False, null=False)
	
	def get_map_label(self):
		if value:
			return self.value
		else:
			return self.name

class Provinces (models.Model):

	def __unicode__(self,):
		return self.name
	
	class Meta:
		verbose_name = 'province'
		verbose_name_plural = 'provinces'
	
	name = models.CharField(max_length=150,
							)
	province = models.CharField(max_length=150,
							)
	region = models.CharField(max_length=150,
							)
	area = models.DecimalField(max_digits=10, decimal_places=6)	
	perimeter = models.DecimalField(max_digits=10, decimal_places=6)		
	geo_lat = models.DecimalField(max_digits=10, decimal_places=6)
	geo_long = models.DecimalField(max_digits=10, decimal_places=6)
#	contrib_user = models.ForeignKey(User)

