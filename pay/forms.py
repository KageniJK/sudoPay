from django import forms
from .models import Account , Profile
from django.contrib.auth.models import User

class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['qr_id','user']


class AccountForm (forms.ModelForm ):
    class Meta:
        model = Account
        exclude = [ 'owner' ]