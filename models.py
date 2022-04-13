from django.db import models

# Create your models here.
class Expense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.item
    
class rg_signup(models.Model):
    Firstname = models.CharField(default="",max_length=20)
    Lastname = models.CharField(default="",max_length=20)
    email= models.EmailField(default="",max_length=50)
    passw = models.CharField(default="",max_length=15)
    re_pwd=models.CharField(default="",max_length=15)
    
    def __str__(self):
        return self.Firstname

class fixed_deposit(models.Model):
    amount = models.IntegerField()
    date = models.DateField()

class feedback(models.Model):
    name = models.CharField(default="",max_length=20)
    email= models.EmailField(default="",max_length=50)
    subject = models.CharField(default="",max_length=30)
    message = models.TextField(default="",max_length=60)
    
    def __str__(self):
        return self.name
