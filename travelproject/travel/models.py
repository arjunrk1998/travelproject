from django.db import models

# Create your models here.
from django.db import models


class arjun(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='mypics')
    dis=models.TextField()

    def __str__(self):
        return self.name
class datas(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    disc=models.TextField()

