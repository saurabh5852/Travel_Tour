from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django import forms





class Employee(models.Model):
    empId=models.AutoField(primary_key=True)
    eName=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
    salary=models.IntegerField()

    def __str__(self):
        return self.eName +' | '+self.email + ' | '+str(self.salary)


class Sign(models.Model):
    empId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
    Confirmpassword=models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName +' | '+self.LastName+' | '+self.email +' | '+self.password +' | '+self.Confirmpassword 

Country_CHOICES = (
    ('select','SELECT'),
    ('dubai','DUBAI'),
    ('seychelles', 'SEYCHELLES'),
    ('singapore','SINGAPORE'),
   
)
class contact_me(models.Model):
    name=models.CharField(max_length=265)
    phone_number = PhoneNumberField(blank=True)
    email=models.EmailField(max_length=100, null=False,error_messages={'invalid_choice':"you custom error message"})    
    Country = models.CharField(max_length=15,choices=Country_CHOICES , default='None')   
    message=models.TextField(max_length=1500)

    def __str__(self):

        return self.name+"|"+str(self.email)+"|"+str(self.phone_number)+"|"+ self.Country+"|"+ self.message  