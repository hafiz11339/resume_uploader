from django.db import models

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