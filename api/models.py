from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    class Meta:
        managed: False
