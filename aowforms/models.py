from django.db import models

# Create your models here.
class Applicant(models.Model):
    GENDER = [("M", "Male"),("F","Female")]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    image = models.ImageField()
