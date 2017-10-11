from django.db import models

__all__ = (
    'Fruit',
)


class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True,
    )
