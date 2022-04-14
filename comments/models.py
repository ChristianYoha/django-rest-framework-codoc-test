from django.contrib.auth.models import User
from django.db import models
from django.db import models

# Create your models here.
from patients.models import Patient


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
