from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=40)
	position = models.CharField(max_length=20)
	department = models.CharField(max_length=20)
		
	def __str__ (self):
		return (str(self.id) + ': ' + self.name)