from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Previous_Score(models.Model):
    #for user
    manager   =  models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    #for user's value like error,accuracy
    Errors    =  models.IntegerField()
    Accuracy  =  models.IntegerField()
    C_pm      =  models.IntegerField()
    W_pm      =  models.IntegerField()
    Time      =  models.IntegerField()




