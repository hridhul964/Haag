from django.db import models

# Create your models here.

class Login_model(models.Model):
    username= models.CharField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)
    Type=models.CharField(max_length=100, null=True, blank=True)

class Course_model(models.Model):
    coursename= models.CharField(max_length=100, null=True, blank=True)
    duration= models.CharField( max_length=100, null=True, blank=True)
    type= models.CharField(max_length=100, null=True, blank=True)
    description= models.CharField(max_length=100, null=True, blank=True)
    startdate= models.DateField(null=True, blank=True)
    enddate= models.DateField(null=True, blank=True)

class User_model(models.Model):
    LOGIN= models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    COURSE= models.ForeignKey(Course_model, on_delete=models.CASCADE, null=True, blank=True)  
    username= models.CharField(max_length=100, null=True, blank=True)
    dob= models.CharField(max_length=100, null=True, blank=True)
    phoneno= models.IntegerField( null=True, blank=True)
    email= models.CharField(max_length=100, null=True, blank=True)

class Teacher_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    COURSE = models.ForeignKey(Course_model, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=100, null=True, blank=True)
    address= models.CharField(max_length=100, null=True, blank=True)
    phoneno =  models.BigIntegerField( null=True, blank=True)
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
    MANAGER = models.ForeignKey(Eventmanager_model, on_delete=models.CASCADE, null=True, blank=True)
    programname= models.CharField(max_length=100, null=True, blank=True)
    coordinator= models.CharField(max_length=100, null=True, blank=True)
    date= models.DateField( null=True, blank=True)
    place= models.CharField(max_length=100, null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)
    action= models.CharField(max_length=100, null=True, blank=True)


class Notification_model(models.Model):
    notification= models.CharField(max_length=100, null=True, blank=True)
    TEACHER= models.ForeignKey(Teacher_model,on_delete=models.CASCADE,null=True,blank=True)
    type=models.CharField(max_length=100, null=True, blank=True)
    date= models.DateField(auto_now_add=True,null=True, blank=True)

class Fees_model(models.Model):
    USER=models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    COURSE=models.ForeignKey(Course_model, on_delete=models.CASCADE, null=True, blank=True)
    amount= models.CharField(max_length=100, null=True, blank=True)
    teacherid=models.ForeignKey(Teacher_model, on_delete=models.CASCADE, null=True, blank=True)
    paymentstatus=models.CharField(max_length=100, null=True, blank=True)
    date= models.DateField(auto_now_add=True,null=True, blank=True)

class Feedback_model(models.Model):
    USER_ID = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    feedback=models.CharField(max_length=100, null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    
#//////////////////// event manager////////////////
class Eventrequest_model(models.Model):
    Eventid= models.ForeignKey(Eventprogram_model, on_delete=models.CASCADE, null=True, blank=True)
    USER_ID = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    date=models.DateField( null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)


class Eventmaterials_model(models.Model):
    Eventid= models.ForeignKey(Eventmanager_model, on_delete=models.CASCADE, null=True, blank=True)
    Materialsname=models.CharField(max_length=100, null=True, blank=True)
    imagematerial=models.FileField( null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)
    Amount=models.BigIntegerField( null=True, blank=True)
    date=models.DateField( null=True, blank=True)

class Materialrequestable_model(models.Model):
    USER= models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    MATERIAL= models.ForeignKey(Eventmaterials_model, on_delete=models.CASCADE, null=True, blank=True)
    Quantity=models.BigIntegerField( null=True, blank=True)
    date=models.DateField( null=True, blank=True)
    Status=models.CharField(max_length=100, null=True, blank=True)
    Description=models.CharField(max_length=300, null=True, blank=True)
    

class Video_model(models.Model):
    TEACHERID = models.ForeignKey(Teacher_model, on_delete=models.CASCADE, null=True, blank=True)
    Classvideo= models.FileField(upload_to='classvideo/',null=True, blank=True)
    date=models.DateField(auto_now_add=True, null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)
    amount=models.CharField(max_length=100, null=True, blank=True)
    