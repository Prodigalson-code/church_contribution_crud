from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class ChurchMember(models.Model):
    """A model representing a church member"""
   
    
    first_name = models.CharField(max_length=100,)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=2)
    address = models.TextField()

    class Meta:
        """Control default odering of the model"""

        ordering = ["first_name"]

    def __str__(self) -> str:
        return str(self.first_name) + " "+ str(self.last_name) 

class Contribution(models.Model):
    """A model for representing contribution details"""

    contribution_name = models.CharField(max_length=200)
    contribution_details = models.TextField()
    contribution_targeted_amount = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        """Control default ordering of the model"""
        ordering = ["contribution_name","contribution_targeted_amount"]

    def __str__(self):
        """String for representing a model object"""
        return self.contribution_name



class Contributor(models.Model):
    """A model for representing contributors"""

    contributor_name = models.ForeignKey(ChurchMember, on_delete=models.CASCADE)
    contribution = models.ForeignKey(Contribution, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=19, decimal_places=2)
    

    class Meta:
        """Control default ordering of the model"""
        ordering = ["contributor_name","amount_paid"]

    def __str__(self):
        """String for representing a model object"""
        return self.contributor_name

   

