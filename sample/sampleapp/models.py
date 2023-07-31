from django.db import models

# Create your models here.
class sample(models.Model):
    image=models.ImageField(upload_to='pics')
    title = models.CharField(max_length=250)
    description = models.TextField()
