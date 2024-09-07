from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    state12th = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    locality = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15)
    alternate_contact = models.CharField(max_length=15, blank=True)
    email = models.EmailField()

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
