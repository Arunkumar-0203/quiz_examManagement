from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=True)
    status= models.CharField(max_length=100,null=True)

class division(models.Model):
    division = models.CharField(max_length=100,null=True)
    status =models.CharField(max_length=100,null=True)

class staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    division =models.ForeignKey(division,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=True)
    status= models.CharField(max_length=100,null=True)


class Questions(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Staff = models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    Division = models.ForeignKey(division,on_delete=models.CASCADE,null=True)
    Question1 =  models.CharField(max_length=400,null=True)
    answer1= models.CharField(max_length=400,null=True)
    options1 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question2 =  models.CharField(max_length=400,null=True)
    answer2= models.CharField(max_length=400,null=True)
    options2 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question3 =  models.CharField(max_length=400,null=True)
    answer3= models.CharField(max_length=400,null=True)
    options3 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question4 =  models.CharField(max_length=400,null=True)
    answer4= models.CharField(max_length=400,null=True)
    options4 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question5 =  models.CharField(max_length=400,null=True)
    answer5= models.CharField(max_length=400,null=True)
    options5 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    status = models.CharField(max_length=30,null=True)
    expire = models.CharField(max_length=30,null=True)

class Answers(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Division = models.ForeignKey(division,on_delete=models.CASCADE,null=True)
    Staff = models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    Student = models.ForeignKey(users,on_delete=models.CASCADE,null=True)
    Question1 =  models.CharField(max_length=400,null=True)
    answer1= models.CharField(max_length=400,null=True)
    Question2 =  models.CharField(max_length=400,null=True)
    answer2= models.CharField(max_length=400,null=True)
    Question3 =  models.CharField(max_length=400,null=True)
    answer3= models.CharField(max_length=400,null=True)
    Question4 =  models.CharField(max_length=400,null=True)
    answer4= models.CharField(max_length=400,null=True)
    Question5 =  models.CharField(max_length=400,null=True)
    answer5= models.CharField(max_length=400,null=True)
    status = models.CharField(max_length=30,null=True)
    expire = models.CharField(max_length=30,null=True)

class payments(models.Model):
    Users = models.ForeignKey(users,on_delete=models.CASCADE,null=True)
    user_name= models.CharField(max_length=400,null=True)
    card_number = models.CharField(max_length=400,null=True)
    expire = models.CharField(max_length=400,null=True)
    csv = models.CharField(max_length=400,null=True)
    amount = models.CharField(max_length=400,null=True)
