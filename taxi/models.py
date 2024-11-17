from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=225, unique=True)
    country = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=225, unique=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=225)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name='cars')

    def __str__(self):
        return self.model
