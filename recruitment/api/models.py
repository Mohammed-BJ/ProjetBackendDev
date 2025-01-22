from django.db import models

# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    resume = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Recruiter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)