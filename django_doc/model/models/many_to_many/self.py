from django.db import models


class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name
