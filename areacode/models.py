from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile = models.ImageField(upload_to="profile")


    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']




class Food(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="food")


    def __str__(self):
        return self.name + " " + str(self.price)
    

class Cart(models.Model):
     
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     food = models.ForeignKey(Food, on_delete=models.CASCADE)
     qty = models.IntegerField(default=1)
     dateCreated = models.DateField(auto_now_add=True)
     total = models.IntegerField(default=1)

     def __str__(self):
          return self.user.first_name + ' - ' + self.food.name + ' - ' + str(self.qty)
     
