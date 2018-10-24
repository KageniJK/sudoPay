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
    )
    card_type = models.CharField(choices=ACCEPTED_CHOICES, max_length=100 )
    card_number = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()
    password = models.TextField()



class Profile(models.Model):
    '''
    Profile of an customer . More Information .
    '''
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='static/profile', default="https://i.imgur.com/oo1xyTr.jpg", blank=True)
    phone_number = models.PositiveIntegerField( blank=True,null=True )
    email = models.EmailField()
    account = models.ForeignKey(Account)
    about = models.TextField(max_length=100, blank=True, null=True )

    def __str__(self):
        return self.user.username

    @classmethod
    def get_user_profile(cls, user):
        return cls.objects.get(user=user)

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


