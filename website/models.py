
from django.db import models




class Infocounter(models.Model):
    projects=models.CharField(max_length=50,default="21")
    workers=models.IntegerField(null=True)
    support=models.IntegerField(null=True)
    clients=models.IntegerField(null=True)


    def __str__(self):
        return self.projects


class ServiceDes(models.Model):

    headDiscription=models.CharField( max_length=100)
    webdev=models.CharField( max_length=100)
    Mlearning=models.CharField( max_length=100)
    dataA=models.CharField( max_length=100)

    def __str__(self):
        return self.headDiscription 
    

    
# Create your models here.
