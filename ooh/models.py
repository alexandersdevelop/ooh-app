from django.db import models


class Maindatabase(models.Model):


    campaign = models.TextField(blank=True, null=True)
    number = models.PositiveIntegerField()
    region = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    side = models.TextField(blank=True, null=True)
    grp = models.TextField(blank=True, null=True)
    oohformat = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    submission = models.TextField(blank=True, null=True)
    cost = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    check = models.PositiveIntegerField()

    def __str__(self):
        return self.address

# Create your models here.
