from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class BoundaryDetails(models.Model):
    First_Name = models.CharField(max_length=100)
    Middle_Name=models.CharField(max_length=100,null =True,blank=True)
    Surname = models.CharField(max_length=100)
    Point = models. PointField(null=True,blank=True)
    # objects_custom = GeoManager()
    Northing1 = models.FloatField()
    Easting1 = models.FloatField()
    Northing2 = models.FloatField()
    Easting2 = models.FloatField()
    Northing3 = models.FloatField()
    Easting3 = models.FloatField()
    Northing4 = models.FloatField()
    Easting4 = models.FloatField()
    def __str__(self):
        self.Surname

class Registration(models.Model):
    Username= models.CharField(max_length=100)
    password = models.SlugField()
    def __str__(self):
        self.Username
    


