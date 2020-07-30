from django.db import models

class File(models.Model):
	name = models.CharField(max_length=30)
	src = models.CharField(max_length=30)
	extension = models.CharField(max_length=30)