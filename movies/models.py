from django.db import models

# Create your models here.

class Actor(models.Model):
    aName = models.CharField(max_length=50)
    aAge = models.IntegerField
    aGender = models.CharField(max_length=80)


class Movies(models.Model):
    mName = models.CharField(max_length=50)
    mRdate = models.DateField()
    mLang = models.CharField(max_length=80)
    actmovie = models.ManyToManyField(Actor)

# class Actor_Movies(models.Model):
#     actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
