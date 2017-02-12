from django.db import models
from django.conf import settings
from datetime import date


class NrSt(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	nr_st = models.CharField(max_length = 9, unique=True)
	name = models.CharField(max_length = 255)


	def __str__(self):
		return self.name

class NrStc(models.Model):
	nr_st = models.ForeignKey(NrSt)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	nr_stc = models.CharField(max_length = 9, unique=True)
	name = models.CharField(max_length = 255)
	data_przyjecia = models.DateField(default=date.today)

	def __str__(self):
		return self.name