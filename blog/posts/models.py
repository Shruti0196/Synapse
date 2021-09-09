from django.db import models
from datetime import datetime
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=150)
    body=models.CharField(max_length=100000)
    created_at=models.DateTimeField(default=datetime.now)
    
