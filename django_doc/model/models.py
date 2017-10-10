from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True,
    )


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
