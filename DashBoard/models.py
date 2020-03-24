from django.db import models

# Create your models here.

class VulnerableLibraries(models.Model):
	Vulnerability=models.TextField()
	Package=models.TextField()
	Package_Link=models.TextField()
	Version=models.TextField()
	Overview=models.TextField()
	
