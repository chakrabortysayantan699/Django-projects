from django.db import models

# Create your models here.
# head:str
# about:str

class Portfolio(models.Model):
	head=models.CharField(max_length=200)
	about=models.TextField()
	
