from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save

STATE_CHOICES =(
    ("Lahore","Lahore"),
    ("Multan","Multan"),
    ("Karachi","Karachi"),
    ("Quetta","Quetta"),
    ("Islamabad","Islamabad"),
    ("Faisalabad","Faisalabad")
)

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    profile_img = models.ImageField(upload_to='profileimg',blank=True,null=True)
    my_file = models.FileField(upload_to='doc',blank=True,null=True)


    def __str__(self):
        return self.email

class Profile(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self) -> str:
        return self.email