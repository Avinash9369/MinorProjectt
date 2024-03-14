from django.db import models
from django.utils import timezone

# Create your models here.

#Model 1
class Query(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
#Model 2
class Feedback(models.Model):
    name=models.CharField(max_length=45) 
    email=models.EmailField(max_length=45)
    date=models.DateField(default=timezone.now)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6)

    def __str__(self):
        return self.name
    
#Model 3
class User(models.Model): 
    user_id=models.CharField(max_length=45)
    user_pass=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
#Model 4
class Employee_Type(models.Model):
    employee_type=models.CharField(max_length=45,primary_key=True)
    charge_permonth=models.IntegerField()
    other_details=models.TextField()

    def __str__(self):
        return self.employee_type
    
#Model 5
gender=[
    ("M","Male"),
    ("F","Female")
]
class Employee(models.Model):
    employee_type=models.ForeignKey(Employee_Type,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=45)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField(max_length=45)
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=gender)
    experience=models.CharField(max_length=20)
    employee_pic=models.FileField(max_length=100,upload_to="solutionapp/employee_pic",default="")
    about_employee=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
#Model 6
class Offers_Scheme(models.Model):
    offer_contents=models.CharField(max_length=100)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.offer_contents
    




