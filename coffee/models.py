from django.db import models
from django.forms.widgets import Textarea

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=200)
    Phone_Number = models.IntegerField(default=10)
    delivery_Address = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.Phone_Number+" "+self.delivery_Address
