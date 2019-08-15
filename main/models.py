from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=256)
    path=models.FileField()
    
    def __str__(self):
        return self.name