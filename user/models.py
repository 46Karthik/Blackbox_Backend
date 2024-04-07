from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(unique=True,max_length=255)
    apikey= models.CharField(unique=True, max_length=500)
    # def _str_(self):
    #     return name
    class Meta:
        managed = False
        db_table = 'user_user'

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'

class Storesong(models.Model):
    id = models.BigAutoField(primary_key=True)
    song = models.CharField(unique=True, max_length=255)
   
    class Meta:
        managed = False
        db_table = 'storesong'
#new
class Storefile(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    name = models.CharField(max_length=255, unique=True)
    rename = models.CharField(max_length=255, unique=True)
    endpoint = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'storefile'