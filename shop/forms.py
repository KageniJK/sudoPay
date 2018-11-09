from .models import Cart,Profile,Account
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']



class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['user','paid','item']
        field = []

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']


class AccountForm (forms.ModelForm ):
    class Meta:
        model = Account
        exclude = [ 'owner' ]

class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['qr_id','user']
