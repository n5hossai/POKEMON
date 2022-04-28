from django.db import models
from django.core.validators import *
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    hp = models.IntegerField(default=30, validators=[MaxValueValidator(100), MinValueValidator(10)])

    def __str__(self):
        return self.name + '-' + self.description + ' type'