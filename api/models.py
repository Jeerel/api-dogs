from django.db import models
from django.core.validators import RegexValidator


class Dog(models.Model):

    # price_regex = RegexValidator(regex=r'/^[0-9]+\.?[0-9]+$/gm', message="NO SEAS PENDEJO MARIO NO HAY PRECIO NEGATIVOS.")

    name = models.CharField(max_length=30, blank=True)
    day_birth = models.DateField()
    #price = models.FloatField(validators=[price_regex])
    id_image_drive = models.CharField(max_length=60)
    price = models.FloatField()
    color = models.CharField(max_length=30)
    male = models.BooleanField()
    description = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name
