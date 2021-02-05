from django.db import models

# Create your models here.
class EmpRegistration(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    esal=models.IntegerField()
