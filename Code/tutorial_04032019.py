#  Django Tutorial
'''References
	https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04

	https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server


'''



# IMPORT MODULES
import django

# DATABASE-----------------------------------------------------
'''Django comes with an object_relational mapper'''
from django.db import models


# Define class objects
class Reporter(models.Model):
	full_name = models.CharField(max_length=70)
	def __str__(self):
		return self.full_name

class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	report = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline



