from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics",null=True,default="img-avatar2.jpg")

    def __str__(self):
        return self.user.username + "profile"

class AnonymouseCustomer(models.Model):
    mobileno = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email