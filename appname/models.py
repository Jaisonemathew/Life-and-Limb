from django.db import models

# Create your models here.
class UserDetail(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    location = models.CharField(max_length=50)
    # photo = 
    email = models.CharField(max_length=50)
    description = models.CharField( max_length=100)
    no_year = models.IntegerField()

class SponserDetail(models.Model):
        sponserid = models.IntegerField()
        name = models.CharField(max_length=50)
        mobile_no = models.BigIntegerField()
        email = models.CharField(max_length=50)

class SponserShip(models.Model):
    userid = models.IntegerField()
    sponserid = models.IntegerField()
    amount = models.BigIntegerField()

class MedicalTeam(models.Model):
    Medicalid = models.IntegerField()
    member1name = models.CharField( max_length=50)
    member2name = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

class Feedback(models.Model):
    name = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)
    message = models.CharField( max_length=50)
    


