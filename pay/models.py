from django.db import models
from django.contrib.auth.models import User


from django.dispatch import receiver
from django.db.models.signals import post_save



class Account(models.Model):
    '''
    Model that define user's account 
    '''
    ACCEPTED_CHOICES = (
        ("VISA", "VISA"),
        ("MasterCard", "MasterCard"),
        ("American Express", "American Express"),
        ("MEAL Card", "MEAL Card"),
        ("M-Pesa", "M-Pesa"),
    )
    card_type = models.CharField(choices=ACCEPTED_CHOICES, max_length=100 )
    card_number = models.BigIntegerField()
    cvv = models.PositiveIntegerField()
    expiry_date = models.DateField(blank=True , null=True)
    owner = models.OneToOneField(User ,null=True ,blank=True)

    def __str__(self):
        return f"{self.owner.username}'s Acc"
