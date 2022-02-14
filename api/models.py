# This file instantiates models (tables) and their attributes and initialises object-relational database 
from django.db import models;
from django.db.models.fields.related import ManyToManyField;

# Define vase class
class Vase(models.Model):
    vaseRef = models.CharField(max_length=255, primary_key=True)
    collectionName = models.CharField(max_length=600,blank=True,null=True)
    previousColl = models.CharField(max_length=600,blank=True, null=True)
    provenanceName = models.CharField(max_length=600,blank=True,null=True)
    height = models.CharField(max_length=50,blank=True,null=True)
    diameter = models.CharField(max_length=50,blank=True,null=True)
    publications = models.CharField(max_length=700,blank=True,null=True)
    subject = models.CharField(max_length=1000,blank=True,null=True)
    fabric = models.CharField(max_length=50, blank=True,null=True)
    technique = models.CharField(max_length=50,blank=True,null=True)
    shapeName = models.CharField(max_length=50,blank=True,null=True)

    def _str_(self):
        return self.vaseRef
    
# Define plate class. A plate can contain multiple images from difference vases, and a vase can
# have multiple images. Many to many relationship through vase. 
class Plate(models.Model): 
    vase = models.ManyToManyField(Vase)
    plateRef = models.CharField(max_length=100, primary_key=True)

    def _str_(self):
        return self.plateRef
