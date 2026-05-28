from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE = (
        ('admin', 'Admin'), 
        ('manager', 'Manager'), 
        ('teachrer', 'Teacher'),
        ('Student', 'student'),
    )
    city = models.CharField()
    role = models.CharField(choices=ROLE)
    

class Product(models.Model):
    title = models.CharField()
    description = models.TextField()
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_img/", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class College(models.Model):
    name = models.CharField()
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    mobile = models.CharField()
    email = models.EmailField() 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    