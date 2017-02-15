from django.db import models
from django.conf import settings
from datetime import date


class NrSt(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	nr_st = models.CharField(max_length = 9, unique=True)
	name = models.CharField(max_length = 255)
	data_przyjecia = models.DateField(default=date.today)
	price = models.DecimalField(null = True, blank=True, max_digits = 20, decimal_places = 2)
	uwagi = models.TextField(null = True, blank=True)
	dzierzawca = models.CharField(max_length = 255, null = True, blank=True)
	place = models.CharField(max_length = 255, null = True, blank=True)

	def __str__(self):
		return self.name

class NrStc(models.Model):
	nr_st = models.ForeignKey(NrSt)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	nr_stc = models.CharField(max_length = 9, unique=True)
	name = models.CharField(max_length = 255)
	data_przyjecia = models.DateField(default=date.today)
	price = models.DecimalField(null = True, blank=True, max_digits = 20, decimal_places = 2)
	uwagi = models.TextField(null=True)
	dzierzawca = models.CharField(max_length = 255, null = True)
	place = models.CharField(max_length = 255, null = True, blank = True)
	photo = models.ImageField()

	def __str__(self):
		return self.name