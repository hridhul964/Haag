from django.db import models

# Create your models here.

class Login_model(models.Model):
    username= models.CharField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)
    Type=models.CharField(max_length=100, null=True, blank=True)

class Course_model(models.Model):
    name= models.CharField(max_length=100, null=True, blank=True)
    phoneno= models.IntegerField( null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)
    gender= models.CharField(max_length=100, null=True, blank=True)
    password= models.CharField(max_length=100, null=True, blank=True)

class User_model(models.Model):
    LOGIN= models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    username= models.CharField(max_length=100, null=True, blank=True)
    dob= models.CharField(max_length=100, null=True, blank=True)
    phoneno= models.IntegerField( null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)

class Teacher_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    COURSE = models.ForeignKey(Course_model, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=100, null=True, blank=True)
    phoneno= models.BigIntegerField( null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)
    dob= models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=100, null=True, blank=True)
    qualification= models.CharField(max_length=100, null=True, blank=True)
    
class Eventmanager_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=100, null=True, blank=True)
    phoneno= models.BigIntegerField(null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)
    place= models.CharField(max_length=100, null=True, blank=True)
    gender= models.CharField(max_length=100, null=True, blank=True)

class Eventprogram_model(models.Model):
    programname= models.CharField(max_length=100, null=True, blank=True)
    coordinator= models.CharField(max_length=100, null=True, blank=True)
    date= models.DateField(max_length=100, null=True, blank=True)
    place= models.CharField(max_length=100, null=True, blank=True)
    action= models.CharField(max_length=100, null=True, blank=True)

class Notification_model(models.Model):
    notification= models.CharField(max_length=100, null=True, blank=True)
    type= models.CharField(max_length=100, null=True, blank=True)
    date= models.DateField(max_length=100, null=True, blank=True)

class Fees_model(models.Model):
    USER=models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    COURSE=models.ForeignKey(Course_model, on_delete=models.CASCADE, null=True, blank=True)
    amount= models.CharField(max_length=100, null=True, blank=True)

class Feedback_model(models.Model):
    USER_ID = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    feedback=models.CharField(max_length=100, null=True, blank=True)
    date=models.DateField(max_length=100, null=True, blank=True)
    

